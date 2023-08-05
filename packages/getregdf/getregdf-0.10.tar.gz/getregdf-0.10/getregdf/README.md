# reg.exe query to pandas DataFrame 

## pip install getregdf

### Tested against Windows 10 / Python 3.10 / Anaconda

This code provides a way to execute multiple registry queries using reg.exe and obtain the results in a structured DataFrame format. It abstracts the process of querying the registry and provides additional functionalities through the custom modules and functions used.

It's interesting for people who need to programmatically retrieve registry information from Windows systems because it allows them to automate the retrieval of registry data and process it in a structured manner using the powerful data manipulation capabilities of Pandas. They can analyze the retrieved registry information, perform further computations or transformations, and integrate it into their workflows or applications.

### Calling the function in Python:


```python
reg_query2df(
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
	
# HKEY_CLASSES_ROOT (HKCR): This key contains file association and COM object registration information.
# HKEY_CURRENT_USER (HKCU): This key stores configuration information for the currently logged-in user.
# HKEY_LOCAL_MACHINE (HKLM): This key contains system-wide configuration settings and information for all users.
# HKEY_USERS (HKU): This key contains user-specific configuration settings for each user profile on the computer.
# HKEY_CURRENT_CONFIG (HKCC): This key provides access to the current hardware profile being used by the computer.


from getregdf import reg_query2df

df = reg_query2df(
    regquerys=[
        "HKEY_USERS",
        r"HKEY_CLASSES_ROOT",
        r"HKEY_LOCAL_MACHINE",
        r"HKEY_USERS",
        r"HKEY_CURRENT_CONFIG",
    ],
    bufsize=2048 * 100,
    timeout=30000000,
    max_threads=5,
    timeout_check_sleep=1,
)
df.to_pickle("c:\\myregexported.pkl")	
```
