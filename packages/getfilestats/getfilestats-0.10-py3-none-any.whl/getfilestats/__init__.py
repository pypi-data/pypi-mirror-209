import os
import pandas as pd
from list_all_files_recursively import get_folder_file_complete_path
from a_pandas_ex_apply_ignore_exceptions import pd_add_apply_ignore_exceptions
from a_pandas_ex_horizontal_explode import pd_add_horizontal_explode

pd_add_apply_ignore_exceptions()

pd_add_horizontal_explode()


def get_stats_from_all_files_in_folders(
    folders: str | list | tuple,
    allowed_extensions: str | list | tuple = (),
    maxsubfolders: int = -1,
) -> pd.DataFrame:
    r"""
    Retrieve statistics from all files in the specified folders.

    Args:
    - folders: The folder path(s) to search for files. Can be a single string or a list/tuple of strings.
    - allowed_extensions: Optional. A string or a list/tuple of allowed file extensions. Default is an empty tuple (all extensions are allowed).
    - maxsubfolders: Optional. The maximum number of subfolders to search within each folder. Default is -1 (unlimited).

    Returns:
    A pandas DataFrame containing the statistics for each file found.

    Example:

    import pandas as pd
    from getfilestats import get_stats_from_all_files_in_folders
    df = get_stats_from_all_files_in_folders(
        folders=r"C:\cygwinxx",
        allowed_extensions=(".exe", ".bat"),
        maxsubfolders=-1
    )
    print(df1[:5].to_string())


    #                         filepath           st_atime          st_atime_ns           st_ctime          st_ctime_ns      st_dev  st_file_attributes  st_gid           st_ino  st_mode           st_mtime          st_mtime_ns  st_nlink  st_reparse_tag  st_size  st_uid
    # 0         C:\cygwinxx\Cygwin.bat  1680571708.307696  1680571708307696300  1680571708.306699  1680571708306699200  3067733448                  32       0  281474978447139    33279  1680571708.307696  1680571708307696300         1               0       88       0
    # 1  C:\cygwinxx\bin\addftinfo.exe  1680571700.969256  1680571700969256300  1680571700.968287  1680571700968286400  3067733448                  32       0  281474978444793    33279       1554031577.0  1554031577000000000         1               0    51219       0
    # 2  C:\cygwinxx\bin\addr2line.exe    1680571785.0613  1680571785061300100  1680571785.059305  1680571785059304700  3067733448                  32       0  281474978447991    33279       1676205497.0  1676205497000000000         1               0  1108499       0
    # 3    C:\cygwinxx\bin\apngasm.exe  1680573545.995065  1680573545995064900  1680573545.989051  1680573545989051100  3067733448                  32       0  562949955151788    33279       1423742864.0  1423742864000000000         1               0    97076       0
    # 4         C:\cygwinxx\bin\ar.exe  1680571785.064319  1680571785064319100  1680571785.062297  1680571785062296800  3067733448                  32       0  281474978447992    33279       1676205500.0  1676205500000000000         2               0  1136147       0



    """
    if isinstance(allowed_extensions, str):
        allowed_extensions = [allowed_extensions]
    if allowed_extensions:
        allowed_extensions = ["." + ex.strip(".").lower() for ex in allowed_extensions]
    allfi = get_folder_file_complete_path(folders, maxsubfolders=maxsubfolders)
    if allowed_extensions:
        allfiles = [x.path for x in allfi if x.ext.lower() in allowed_extensions]
    else:
        allfiles = [x.path for x in allfi]
    return get_stats_from_files(list_or_series=allfiles)


def get_stats_from_files(list_or_series: list | pd.Series | str) -> pd.DataFrame:
    r"""
    Retrieve statistics from a list/pandas Series, or a single file (file path[s]).

    Args:
    - list_or_series: A list, pandas Series, or a single file path as a string (file path[s]).

    Returns:
    A pandas DataFrame containing the statistics for each file.

    Example:
    import pandas as pd
    from getfilestats import get_stats_from_files
    df = get_stats_from_files([
        r"C:\cygwinxx\bin\sphinx-autogen",
        r"C:\cygwinxx\bin\apt.sh",
        r"C:\cygwinxx\bin\pip3",
        r"C:\cygwinxx\bin\pydoc3",
        r"C:\cygwinxx\bin\python",
        r"C:\cygwinxx\bin\python3",
        r"C:\cygwinxx\bin\sphinx-apidoc",
    ])

    print(df2[:5].to_string())

    #                          filepath           st_atime          st_atime_ns           st_ctime          st_ctime_ns      st_dev  st_file_attributes  st_gid            st_ino  st_mode           st_mtime          st_mtime_ns  st_nlink  st_reparse_tag  st_size  st_uid
    # 0  C:\cygwinxx\bin\sphinx-autogen  1680571840.266463  1680571840266462600  1680571840.266463  1680571840266462600  3067733448                   4       0  3659174697372682    33206  1680571840.266463  1680571840266462600         1               0       78       0
    # 1          C:\cygwinxx\bin\apt.sh  1680571842.981623  1680571842981622600  1680571842.981623  1680571842981622600  3067733448                  32       0  1970324838741762    33206  1680571842.981623  1680571842981622600         1               0    18531       0
    # 2            C:\cygwinxx\bin\pip3  1680571840.387299  1680571840387298800  1680571840.387299  1680571840387298800  3067733448                   4       0  3659174697374415    33206  1680571840.387299  1680571840387298800         1               0       58       0
    # 3          C:\cygwinxx\bin\pydoc3  1680571840.506555  1680571840506555000  1680571840.506555  1680571840506555000  3067733448                   4       0  3940649674085961    33206  1680571840.506555  1680571840506555000         1               0       62       0
    # 4          C:\cygwinxx\bin\python  1680571840.458692  1680571840458691500  1680571840.458692  1680571840458691500  3067733448                   4       0  3377699720663980    33206  1680571840.458692  1680571840458691500         1               0       62       0


    """
    if isinstance(list_or_series, str):
        list_or_series = [list_or_series]
    if isinstance(list_or_series, list):
        list_or_series = pd.Series(list_or_series)
    filtervar = ""
    statdf = list_or_series.ds_apply_ignore(
        filtervar,
        lambda f: (
            ossta := os.stat(f),
            tuple(
                (x, getattr(ossta, x))
                for x in sorted(dir(ossta))
                if str(x).startswith("st_")
            ),
        )[1:],
    )
    statdf = statdf.ds_apply_ignore(
        pd.NA, lambda q: (pd.NA, pd.NA) if isinstance(q, str) else q
    )

    statdfexploded = statdf.ds_horizontal_explode(
        0, concat=False
    ).ds_horizontal_explode("0_0", concat=False)
    statdf = pd.concat(
        [
            statdfexploded[co]
            .str[-1]
            .to_frame(
                statdfexploded[co]
                .str[0]
                .value_counts()
                .sort_values(ascending=False)
                .index[0]
            )
            for co in statdfexploded.columns
        ],
        axis=1,
    )
    dt = {
        "st_atime": "Float64",
        "st_atime_ns": "Int64",
        "st_ctime": "Float64",
        "st_ctime_ns": "Int64",
        "st_dev": "Int64",
        "st_file_attributes": "Int64",
        "st_gid": "Int64",
        "st_ino": "Int64",
        "st_mode": "Int64",
        "st_mtime": "Float64",
        "st_mtime_ns": "Int64",
        "st_nlink": "Int64",
        "st_reparse_tag": "Int64",
        "st_size": "Int64",
        "st_uid": "Int64",
    }
    for key, item in dt.items():
        if key in statdf.columns:
            try:
                statdf[key] = statdf[key].astype(item)
            except Exception as fe:
                continue
    statdf.insert(0, "filepath", list_or_series)
    statdf["filepath"] = statdf["filepath"].astype("string")
    return statdf
