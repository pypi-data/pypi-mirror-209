import re
import shutil
import pandas as pd
from a_pandas_ex_df_to_string import pd_add_to_string
from flatten_everything import flatten_everything, ProtectedTuple
from a_pandas_ex_fastloc import pd_add_fastloc
from multisubprocess import multi_subprocess

pd_add_fastloc()

pd_add_to_string()
compiledsplitregex = re.compile(Rb"[\r\n]+HKEY_")


regexe = shutil.which("reg.exe")


def reg_query2df(
    regquerys,
    bufsize=2048,
    timeout=30000000,
    max_threads=5,
    timeout_check_sleep=1.0,
    convert_to_string=True,
):
    r"""
    Executes registry queries and returns the results as a DataFrame.

    Args:
        regquerys (str or list): A single registry query string or a list of query strings.
        bufsize (int, optional): Buffer size for subprocess communication. Defaults to 2048.
        timeout (int, optional): Timeout value for the subprocess execution. Defaults to 30000000.
        max_threads (int, optional): Maximum number of threads to use for subprocess execution. Defaults to 5.
        timeout_check_sleep (int, float, optional): Sleep duration between timeout checks. Defaults to 1.0.
        convert_to_string (int, bool, optional): Convert data from bytes (stdout) to string. Defaults to True

    Returns:
        pandas.DataFrame: A DataFrame containing the results of the registry queries.

    Raises:
        None

    Example usage:
        reg_query2df(
            regquerys=[
                "HKEY_USERS",
                r"HKEY_USERS\S-1-5-18",
                r"HKEY_USERS\S-1-5-21-2954889181-1639616918-2495923365-1001\EUDC",
            ],
            bufsize=2048,
            timeout=30000000,
            max_threads=5,
            timeout_check_sleep=1,
        )

    # print(df[:10].to_string())
    #                                                                        aa_regkey     aa_key aa_type                                                  aa_value  aa_id
    # 0                                                            HKEY_USERS\.DEFAULT                                                                                   0
    # 1                                                  HKEY_USERS\.DEFAULT\AppEvents                                                                                   0
    # 2                                      HKEY_USERS\.DEFAULT\AppEvents\EventLabels                                                                                   0
    # 3                       HKEY_USERS\.DEFAULT\AppEvents\EventLabels\MirrorFinished  (Default)  REG_SZ                                           Mirror Finished      0
    # 4                                          HKEY_USERS\.DEFAULT\AppEvents\Schemes                                                                                   0
    # 5                                     HKEY_USERS\.DEFAULT\AppEvents\Schemes\Apps                                                                                   0
    # 6                          HKEY_USERS\.DEFAULT\AppEvents\Schemes\Apps\WinHTTrack  (Default)  REG_SZ                                 WinHTTrack Website Copier      0
    # 7           HKEY_USERS\.DEFAULT\AppEvents\Schemes\Apps\WinHTTrack\MirrorFinished                                                                                   0
    # 8  HKEY_USERS\.DEFAULT\AppEvents\Schemes\Apps\WinHTTrack\MirrorFinished\.Current  (Default)  REG_SZ    C:\Program Files\WinHTTrack\html\server\sfx\silent.wav      0
    # 9  HKEY_USERS\.DEFAULT\AppEvents\Schemes\Apps\WinHTTrack\MirrorFinished\.Default  (Default)  REG_SZ  C:\Program Files\WinHTTrack\html\server\sfx\finished.wav      0

    # Slower than the first one: https://github.com/hansalemaos/a_pandas_ex_reg2df
    # But key, type, and value are in separated columns
    """
    if isinstance(regquerys, str):
        regquerys = [regquerys]
    allqueries = [[regexe, "QUERY", f"{str(h).strip()}", "/s"] for h in regquerys]
    res = multi_subprocess(
        allqueries,
        byteinput=b"",
        shell=False,
        close_fds=False,
        start_new_session=True,
        bufsize=bufsize,
        invisible=True,
        timeout=timeout,
        max_threads=max_threads,
        timeout_check_sleep=timeout_check_sleep,
        kill_all_at_end=True,
        blockbatch=False,
    )
    allqueries = [x[1]["stdoutready"] for x in res.items() if x[1]["returncode"] == 0]

    dfreg = pd.DataFrame(
        flatten_everything(
            [
                [
                    ProtectedTuple(
                        (
                            b"HKEY_"
                            + u
                            + b"\r\n    NAN    NAN    NAN\r\n    NAN    NAN    NAN\r\n    NAN    NAN    NAN\r\n    "
                            b"NAN    NAN    NAN"
                        )
                        .strip()
                        .split(b"    ", maxsplit=4)[:4]
                        + [a]
                    )
                    for u in compiledsplitregex.split(allqueries[a])
                ]
                for a in range(len(allqueries))
            ]
        )
    )

    for co in dfreg.columns[:-1]:
        dfreg[co] = dfreg[co].s_str().strip().s_str().replace(b"NAN", b"", regex=True)

    dfreg = dfreg.loc[~(dfreg[0] == b"HKEY_")].reset_index(drop=True)

    if convert_to_string:
        for co in dfreg.columns[:-1]:
            dfreg[co] = dfreg[co].ds_to_string()

    dfreg.columns = ["aa_regkey", "aa_key", "aa_type", "aa_value", "aa_id"]
    return dfreg
