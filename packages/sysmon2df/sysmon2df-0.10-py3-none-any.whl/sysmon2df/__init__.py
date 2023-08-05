import os
import shutil
import subprocess
import tempfile

import pandas as pd
from getfilenuitkapython import get_filepath
from kthread_sleep import sleep
from touchtouch import touch
from evtx2df import dataframe_from_evtx

startupinfo = subprocess.STARTUPINFO()
creationflags = 0 | subprocess.CREATE_NO_WINDOW
startupinfo.wShowWindow = subprocess.SW_HIDE
invisibledict = {
    "startupinfo": startupinfo,
    "creationflags": creationflags,
}


sysmonexe = get_filepath("Sysmon.exe")

# https://github.com/0xrawsec/whids/blob/44a57e6023c222572a9daa4112c55f396259576f/utilities/sysmon/v12/sysmon-v12.x-all.xml
sysmonall = r"""
<Sysmon schemaversion="4.40">
  <!-- Capture All Hashes -->
  <HashAlgorithms>*</HashAlgorithms>
  <DnsLookup>False</DnsLookup>
  <!-- <ArchiveDirectory></ArchiveDirectory> -->

  <EventFiltering>

      <!-- EventID: 1 -->
      <!-- Log all process creation -->
      <ProcessCreate onmatch="exclude"/>

      <!-- EventID: 2 -->
      <!-- Log all file creation time stamps -->
      <FileCreateTime onmatch="exclude"/>

      <!-- EventID: 3 -->
      <!-- Log all network connections -->
      <NetworkConnect onmatch="exclude"/>

      <!-- EventID: 5 -->
      <!-- Log all process termination -->
      <ProcessTerminate onmatch="exclude" />

      <!-- EventID: 6 -->
      <!-- Log all Drivers Loaded -->
      <DriverLoad onmatch="exclude" />

      <!-- EventID: 7 -->
      <!-- Log all image loaded-->
      <!-- There is way too much image loaded by Sysmon.exe in this version -->
      <!-- Mostly due to the new feature of File Information -->
      <!-- This Schema needs to be adapted with the name of the service -->
      <RuleGroup groupRelation="or">
        <ImageLoad onmatch="exclude">
          <Image condition="is">C:\Windows\Sysmon.exe</Image>
          <Image condition="is">C:\Windows\Sysmon64.exe</Image>
        </ImageLoad>
      </RuleGroup>


      <!-- EventID: 8 -->
      <!-- Log all RemoteThread created -->
      <CreateRemoteThread onmatch="exclude" />

      <!-- EventID: 9 -->
      <!-- Log all -->
      <RawAccessRead onmatch="exclude" />

      <!-- EventID: 10 -->
      <!-- Log all -->
      <ProcessAccess onmatch="exclude" />

      <!-- EventID: 11 -->
      <!-- Log all -->
      <FileCreate onmatch="exclude" />

      <!-- EventID: 12/13/14 -->
      <!-- Log all registry operations -->
      <RuleGroup groupRelation="or">
          <RegistryEvent onmatch="exclude">
            <Image condition="is">C:\Windows\Sysmon.exe</Image>
            <Image condition="is">C:\Windows\Sysmon64.exe</Image>
          </RegistryEvent>
      </RuleGroup>

      <!-- EventID: 15 -->
      <!-- Log all -->
      <FileCreateStreamHash onmatch="exclude" />

      <!-- EventID: 17/18 -->
      <!-- Log all -->
      <PipeEvent onmatch="exclude" />

      <!-- EventID: 19/20/21 -->
      <!-- Log all -->
      <WmiEvent onmatch="exclude" />

      <!-- EventID: 22 -->
      <!-- Log all -->
      <DnsQuery onmatch="exclude" />

      <!-- EventID: 23 -->
      <!-- Log all -->
      <FileDelete onmatch="exclude" />

      <!-- EventID: 24 -->
      <!-- Log all -->
      <ClipboardChange onmatch="exclude" />
      
  </EventFiltering>
</Sysmon>
 
""".strip()


def start_observing(
    uninstall: int | bool = 1,
    uninstall_force: int | bool = 1,
    evtx_path: str | None = None,
    remove_old_evtx: int | bool = 1,
    configxml: str | None = None,
    evtx_output_path: str | None = None,
    csv_output_path: str | None = None,
) -> pd.DataFrame:
    r"""
    Starts observing system events using Sysmon and returns a pandas DataFrame containing the recorded events.

    Args:
        uninstall (int | bool, optional): Flag indicating whether to uninstall Sysmon after/before observation. Defaults to 1.
        uninstall_force (int | bool, optional): Flag indicating whether to force uninstall Sysmon. Defaults to 1.
        evtx_path (str | None, optional): Path to the Sysmon event log (EVTX file). If not provided, the default path ("System32\Winevt\Logs\Microsoft-Windows-Sysmon%4Operational.evtx") will be used. Defaults to None.
        remove_old_evtx (int | bool, optional): Flag indicating whether to remove the existing Sysmon event log before starting observation. Defaults to 1.
        configxml (str | None, optional): Path to the Sysmon configuration XML file. If not provided, a temporary file will be created. Defaults to None.
        evtx_output_path (str | None, optional): Path to save the Sysmon event log (EVTX file) after observation. If not provided, a temporary file will be created. Defaults to None.
        csv_output_path (str | None, optional): Path to save the recorded events as a CSV file. If not provided, no CSV file will be created. Defaults to None.

    Returns:
        pd.DataFrame: A pandas DataFrame containing the recorded system events.

        Example of CSV output:
        ,aa_value,aa_key_0,aa_key_1,aa_key_2,aa_key_3,aa_key_4,aa_event_record_id,aa_timestamp,aa_kind_of_event
        0,http://schemas.microsoft.com/win/2004/08/events/event,Event,#attributes,xmlns,,,32,2023-05-18 14:11:16.815117+00:00,
        1,C:\Windows\SYSTEM32\ntdll.dll+9d364|C:\Windows\system32\basesrv.DLL+2fba|C:\Windows\SYSTEM32\CSRSRV.dll+5af4|C:\Windows\SYSTEM32\ntdll.dll+6d72f,Event,EventData,CallTrace,,,32,2023-05-18 14:11:16.815117+00:00,
        2,0x1fffff,Event,EventData,GrantedAccess,,,32,2023-05-18 14:11:16.815117+00:00,
        3,-,Event,EventData,RuleName,,,32,2023-05-18 14:11:16.815117+00:00,
        4,C:\Windows\system32\csrss.exe,Event,EventData,SourceImage,,,32,2023-05-18 14:11:16.815117+00:00,
    """
    print("Getting ready ...")
    uninstallsysmon(uninstall=uninstall, uninstall_force=uninstall_force)

    if not evtx_path:
        sysmonfile = os.path.normpath(
            os.path.join(
                os.environ["SYSTEMROOT"],
                r"System32\Winevt\Logs\Microsoft-Windows-Sysmon%4Operational.evtx",
            )
        )
    else:
        sysmonfile = os.path.normpath(evtx_path)
        touch(sysmonfile)
    if remove_old_evtx:
        if os.path.exists(sysmonfile):
            os.remove(sysmonfile)
    install_sysmon(configxml)
    print("Recording started ...")
    try:
        while True:
            try:
                sleep(1)
            except KeyboardInterrupt:
                print("Stopping the observation ...")
                break
    except KeyboardInterrupt:
        print("Stopping the observation ...")
        pass
    if not evtx_output_path:
        evtx_output_path = get_tmpfile(suffix=".evtx")
    else:
        evtx_output_path = os.path.normpath(evtx_output_path)
        touch(evtx_output_path)
    while True:
        try:
            if os.path.exists(evtx_output_path):
                os.remove(evtx_output_path)
            shutil.copyfile(sysmonfile, evtx_output_path)
            break
        except Exception as fe:
            print(fe)
            continue
    uninstallsysmon(uninstall=uninstall, uninstall_force=uninstall_force)
    print("Generating the DataFrame ...")
    df = dataframe_from_evtx(evtx_file_path=evtx_output_path)
    print("Done generating the DataFrame ...")

    if csv_output_path:
        csv_output_path = os.path.normpath(csv_output_path)
        touch(csv_output_path)
        df.to_csv(csv_output_path)
        print(f"CSV written to: {csv_output_path}")
    return df


def get_tmpfile(suffix=".bin"):
    tfp = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
    filename = tfp.name
    filename = os.path.normpath(filename)
    tfp.close()
    touch(filename)
    return filename


def install_sysmon(configxml=None):
    if not configxml:
        configxml = get_tmpfile(".xml")
        with open(configxml, mode="w", encoding="utf-8") as f:
            f.write(sysmonall)
    subprocess.run(
        [
            sysmonexe,
            "-accepteula",
            "-i",
            configxml,
            "-e",
            "-g",
            "-p",
            "-r",
            "-f",
            "-w",
        ],
        shell=True,
        **invisibledict,
    )


def uninstallsysmon(uninstall=True, uninstall_force=True):
    if uninstall and uninstall_force:
        subprocess.run([sysmonexe, "-u"], shell=True, **invisibledict)
        subprocess.run([sysmonexe, "-u", "force"], shell=True, **invisibledict)
    elif uninstall and not uninstall_force:
        subprocess.run([sysmonexe, "-u"], shell=True, **invisibledict)
