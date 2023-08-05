import os
import sys
import ujson
from Evtx.evtx import PyEvtxParser
import pandas as pd
from flatten_any_dict_iterable_or_whatsoever import fla_tu
import re
from a_pandas_ex_horizontal_explode import pd_add_horizontal_explode
from getfilenuitkapython import get_filepath
from uffspd import list_all_files

pd_add_horizontal_explode()
from a_pandas_ex_apply_ignore_exceptions import pd_add_apply_ignore_exceptions

pd_add_apply_ignore_exceptions()
from touchtouch import touch

cfgfile = get_filepath("uffs.com")


events = {
    1: """Process creation""",
    2: """A process changed a file creation time""",
    3: """Network connection""",
    4: """Sysmon service state changed""",
    5: """Process terminated""",
    6: """Driver loaded""",
    7: """Image loaded""",
    8: """CreateRemoteThread""",
    9: """RawAccessRead""",
    10: """ProcessAccess""",
    11: """FileCreate""",
    12: """RegistryEvent (Object create and delete)""",
    13: """RegistryEvent (Value Set)""",
    14: """RegistryEvent (Key and Value Rename)""",
    15: """FileCreateStreamHash""",
    16: """ServiceConfigurationChange""",
    17: """PipeEvent (Pipe Created)""",
    18: """PipeEvent (Pipe Connected)""",
    19: """WmiEvent (WmiEventFilter activity detected)""",
    20: """WmiEvent (WmiEventConsumer activity detected)""",
    21: """WmiEvent (WmiEventConsumerToFilter activity detected)""",
    22: """DNSEvent (DNS query)""",
    23: """FileDelete (File Delete archived)""",
    24: """ClipboardChange (New content in the clipboard)""",
    25: """ProcessTampering (Process image change)""",
    26: """FileDeleteDetected (File Delete logged)""",
    27: """FileBlockExecutable""",
    28: """FileBlockShredding""",
    255: """Error""",
}


def list_all_evtx_files_in_path(hdd:str="c:\\")->pd.DataFrame:
    """
    List all EVTX files in a given path.

    Args:
        hdd (str): Path to search for EVTX files. Defaults to "c:\\".

    Returns:
        pd.DataFrame: A DataFrame containing information about the EVTX files found.
    """
    df2 = list_all_files(
        path2search=hdd,
        file_extensions=[".evtx"],
        uffs_com_path=cfgfile,
    )
    return df2


def format_folder_drive_path_backslash(path):
    path = os.path.normpath(path.strip("'\"\\ "))
    return path




def dataframe_from_evtx(
    evtx_file_path: str, csv_save_path: str | None = None
) -> pd.DataFrame():
    """
    Generate a Pandas DataFrame from an EVTX file.

    Args:
        evtx_file_path (str): Path to the EVTX file.
        csv_save_path (str | None): Optional path to save the generated DataFrame as a CSV file.
                                    Defaults to None.

    Returns:
        pd.DataFrame: DataFrame containing the EVTX data.

    Raises:
        Exception: Any exception encountered during the processing of EVTX records.
    """

    if csv_save_path:
        csv_save_path = format_folder_drive_path_backslash(csv_save_path)

    allp = []
    parser = PyEvtxParser(evtx_file_path)
    for record in iter(parser.records_json()):
        try:
            df = (
                pd.DataFrame(fla_tu(ujson.loads(record["data"])))
                .ds_horizontal_explode(1, "aa_key")
                .assign(
                    aa_event_record_id=record["event_record_id"],
                    aa_timestamp=record["timestamp"],
                )
                .drop(columns=1)
                .rename(columns={0: "aa_value"})
            )
            df.columns = [
                f"aa_key_{x[-1]}" if re.search(r"\d_\d", str(x)) else x
                for x in df.columns
            ]
            df.aa_value = df.aa_value.astype("string")
            for co in df.columns:
                if co.startswith("aa_key_"):
                    try:
                        df[co] = df[co].astype("string")
                    except Exception:
                        pass
            df.aa_event_record_id = df.aa_event_record_id.astype("Int64")
            df.aa_timestamp = pd.to_datetime(df.aa_timestamp)
            df["aa_kind_of_event"] = pd.NA
            df.loc[(df.aa_key_2 == "EventID"), "aa_kind_of_event"] = df.loc[
                df.aa_key_2 == "EventID"
            ].aa_value.ds_apply_ignore(pd.NA, lambda x: events.get(int(x), ""))
            df.aa_kind_of_event = df.aa_kind_of_event.astype("string")
            allp.append(df)
        except Exception as fe:
            print(fe)
            continue
    dfd = pd.concat(allp, ignore_index=True)
    if csv_save_path:
        touch(csv_save_path)
        dfd.to_csv(csv_save_path)
    return dfd


if __name__ == "__main__":
    if len(sys.argv) == 3:
        dataframe_from_evtx(evtx_file_path=sys.argv[1], csv_save_path=sys.argv[2])
