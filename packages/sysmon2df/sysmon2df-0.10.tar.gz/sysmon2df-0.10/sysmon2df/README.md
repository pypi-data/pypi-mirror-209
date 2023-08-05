# Captures Sysmon events and converts the output into a pandas DataFrames / CSV

## pip install sysmon2df

### Tested against Windows 10 / Python 3.10 / Anaconda


The function start_observing prepares for the observation by uninstalling any existing Sysmon installation and removing the old event log file (if specified).
It installs Sysmon using the provided or default configuration XML (capture every event).
It starts an infinite loop where it sleeps for 1 second until a keyboard interrupt is received.
After the observation is stopped, it copies the Sysmon event log (EVTX file) to the specified or temporary output path.
It uninstalls Sysmon again to clean up.
It generates a pandas DataFrame from the Sysmon event log using the dataframe_from_evtx function.
If specified, it saves the DataFrame as a CSV file at the specified path.
Finally, it returns the DataFrame.


### How to use it:

```python
start_observing(
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
        

from sysmon2df import start_observing  
df = start_observing(
    uninstall=True,
    uninstall_force=True,
    evtx_path=None,
    remove_old_evtx=True,
    configxml=None,
    evtx_output_path="c:\\backupsysmon2.evtx",
    csv_output_path="c:\\backupsysmon2.csv",
)
        
```



