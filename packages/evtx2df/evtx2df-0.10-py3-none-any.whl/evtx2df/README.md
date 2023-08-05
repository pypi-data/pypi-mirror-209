# converts Windows Event Logs (EVTX) into pandas DataFrames / CSV files

## pip install evtx2df

### Tested against Windows 10 / Python 3.10 / Anaconda


This script provides a convenient way to convert EVTX data into a structured DataFrame format using Pandas, which can facilitate further data analysis, exploration, and visualization.


### To extract strings from individual files:

```python
# Converts evtx into csv from the command line:
python path_to_the_package\__init__.py "C:\Windows\System32\winevt\Logs\Microsoft-Windows-AppReadiness%4Admin.evtx" "C:\Microsoft-Windows-AppReadinessAdmin.csv"

# as well as in a python script, and ...
from evtx2df import dataframe_from_evtx
df = dataframe_from_evtx(
    evtx_file_path=r"C:\Windows\System32\winevt\Logs\Microsoft-Windows-AppReadiness%4Admin.evtx"
)


print(df[19:25].to_string())
                                                 aa_value aa_key_0     aa_key_1     aa_key_2     aa_key_3    aa_key_4  aa_event_record_id                     aa_timestamp aa_kind_of_event
19                                                      1    Event       System         Task         <NA>        <NA>                1298 2023-03-25 03:07:30.497541+00:00             <NA>
20                            2023-03-25T03:07:30.497541Z    Event       System  TimeCreated  #attributes  SystemTime                1298 2023-03-25 03:07:30.497541+00:00             <NA>
21                                                      0    Event       System      Version         <NA>        <NA>                1298 2023-03-25 03:07:30.497541+00:00             <NA>
22  http://schemas.microsoft.com/win/2004/08/events/event    Event  #attributes        xmlns         <NA>        <NA>                1297 2023-03-25 03:07:30.497538+00:00             <NA>
23                                                     72    Event    EventData    TaskCount         <NA>        <NA>                1297 2023-03-25 03:07:30.497538+00:00             <NA>
24         install::Microsoft.MicrosoftEdge_8wekyb3d8bbwe    Event    EventData       TaskId         <NA>        <NA>                1297 2023-03-25 03:07:30.497538+00:00             <NA>

# ... finds all evtx files on your HDD

evtxdf=list_all_evtx_files_in_path(hdd='c:\\')

print(evtxdf[11:15].to_string())
                                                                       aa_path                                     aa_name                     aa_path_only   aa_size  aa_size_on_disk              aa_created         aa_last_written        aa_last_accessed  aa_descendents  aa_read_only  aa_archive  aa_system  aa_hidden  aa_offline  aa_not_content_indexed_file  aa_no_scrub_file  aa_integrity  aa_pinned  aa_unpinned  aa_directory_flag  aa_compressed  aa_encrypted  aa_sparse  aa_reparse  aa_attributes
11                          C:\Windows\System32\winevt\Logs\Visual Studio.evtx                          Visual Studio.evtx  C:\Windows\System32\winevt\Logs     69632            69632  b'2023-03-30 19:39:28'  b'2023-03-31 19:54:38'  b'2023-03-31 19:54:38'               0             0           1          0          0           0                            0                 0             0          0            0                  0              0             0          0           0             32
12                      C:\Windows\System32\winevt\Logs\Squid Service Log.evtx                      Squid Service Log.evtx  C:\Windows\System32\winevt\Logs     69632            69632  b'2023-03-25 05:52:15'  b'2023-03-25 12:53:59'  b'2023-03-25 12:53:59'               0             0           1          0          0           0                            0                 0             0          0            0                  0              0             0          0           0             32
13  C:\Windows\System32\winevt\Logs\Microsoft-Windows-Sysmon%4Operational.evtx  Microsoft-Windows-Sysmon%4Operational.evtx  C:\Windows\System32\winevt\Logs  18944000         18944000  b'2023-05-17 23:15:01'  b'2023-05-18 00:59:07'  b'2023-05-18 00:59:07'               0             0           1          0          0           0                            0                 0             0          0            0                  0              0             0          0           0             32
14                                  C:\Windows\System32\winevt\Logs\State.evtx                                  State.evtx  C:\Windows\System32\winevt\Logs     69632            69632  b'2023-03-24 23:46:26'  b'2023-03-25 00:06:45'  b'2023-03-25 00:06:45'               0             0           1          0          0           0                            0                 0             0          0            0                  0              0             0          0           0             32


```



