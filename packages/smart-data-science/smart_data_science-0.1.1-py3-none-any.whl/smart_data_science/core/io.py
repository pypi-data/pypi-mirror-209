"""
- Title:            Utils I/O. Wrapper on top of Pandas for common I/O operations
- Project/Topic:    Utils Tabular Data. Practical functions for Data Science
- Author/s:         Angel Martinez-Tenor
- Dev Date:         2017 - 2022

- Status:           Planning
"""

from __future__ import annotations

import time
from datetime import datetime
from pathlib import Path

import pandas as pd

from smart_data_science import logger

log = logger.get_logger(__name__)


def load_datafile(filepath: str | Path, usecols: list[str] = None, cache=False) -> pd.DataFrame:
    """Read a parquet, csv or excel (first sheet) table and return it as a dataframe
    If no extension is given, it will try to get source files in this order: .parquet > .csv  > .xlsx
    Args:
        filepath (str|Path): Path of the source File (extension not needed)
        usecols (list[str], optional): List of columns to load. Defaults to None (all columns).
    Returns:
        pd.DataFrame: Loaded table
    """
    filepath = Path(filepath)
    df = pd.DataFrame()
    file_found = False
    valid_extensions = (".parquet", ".csv", ".xlsx")
    extension = filepath.suffix
    if extension == "":
        extension = ".parquet"
        filepath = filepath.parent / (filepath.stem + extension)

    if filepath.exists():
        log.info(f" {filepath.stem} found")
        file_found = True

    else:  # looking for an alternative source file
        for extension in valid_extensions:
            filepath = filepath.parent / (filepath.stem + extension)
            if filepath.exists():
                log.info(f" {filepath.stem} found instead")
                file_found = True
                break

    # valid_extensions_as_string = ", ".join(valid_extensions)

    if not file_found:
        log.error(f" {filepath.stem} not found")
        return None

    if extension == ".parquet":
        df = pd.read_parquet(filepath, columns=usecols)

    elif extension == ".csv":
        df = (
            pd.read_csv(filepath, usecols=usecols, low_memory=False, encoding="iso-8859-1")
            .drop_duplicates()
            .reset_index(drop=True)
        )

    elif extension == ".xlsx":
        df = pd.read_excel(filepath, usecols=usecols).drop_duplicates().reset_index(drop=True)

    # Save an optimized parquet file: lower size & faster loading
    if cache:
        if extension != ".parquet":
            extension = ".parquet"
            filepath = filepath.parent / (filepath.stem + extension)
            df.to_parquet(filepath, index=False)

    return df


def load_schema_excel(var_description_path: str) -> pd.DataFrame:
    """Get a dictionary with used variables & description from an excel file containing the following variables:
        - Field: Name of the variable (column name), must be unique
        - Description: Description of the variable
        - Type: Type of the variable (categorical, numerical, date, etc)
        - Source: Source of the variable (where it comes from)
        - Valuable: If the variable is valuable or not (X = valuable, empty = not valuable)
    Args:
        var_description_path (str): Path of excel file with the information of the variables
    Returns:
        dict[str, str]: Dictionary with key = variable name, and value = description of the variable
    """
    df = pd.read_excel(var_description_path)
    df = df[df["Valuable"] == "X"].copy()[["Field", "Description", "Type", "Source"]].sort_values("Type")

    return df

    # return df.set_index("Field").to_dict()["Description"]


def get_available_datafiles(folder: str | Path, match_string: str = "", show_output=False) -> dict[str, pd.DataFrame]:
    """Return a dictionary with the filename and filepath of all parquet, csv and xlsx files found in the given folder
    Args:
        target_path (str|Path): Directory to search for data files
        match_string (str, optional): if provided, the files must contain this text, . Defaults to "".
        Show_output (bool, optional): show files available. Defaults to False

    Returns:
        dict[str, pd.DataFrame]: Dictionary with key = filename, and value = filepath
    """
    dict_filepaths = {}
    target_path = Path(folder)
    for suffix in ("*.parquet", "*.csv", "*.xlsx"):
        filepath_list = target_path.glob(f"{match_string}{suffix}")
        dict_filepaths.update({Path(filepath).stem: filepath for filepath in filepath_list})
    if show_output:
        log.info(f"Data Files found in {target_path}: {dict_filepaths.keys()}")
    return dict_filepaths


def get_creation_date(filepath: str | Path) -> datetime:
    """
    Return the creation date of the file found in filepath (return None if not found)
    Args:
        filepath: The path to the file to get the creation date of
    Returns:
        pd.datetime: The creation date of the file in datetime format
    """
    if filepath is None:
        log.warning(f"File {filepath} not found. Cannot get creation date")
        return None
    f = Path(filepath)
    if f.exists():
        ctime = f.stat().st_ctime
        return pd.to_datetime(time.ctime(ctime))

    log.warning(f"File {filepath} not found. Cannot get creation date")
    return None
