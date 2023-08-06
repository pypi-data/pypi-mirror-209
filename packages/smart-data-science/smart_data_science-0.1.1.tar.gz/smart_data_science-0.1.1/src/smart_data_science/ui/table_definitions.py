"""
- Title:            Table Definitions. Smart Regressor for tabular data
- Project/Topic:    Smart Data Science. Practical functions for Data Science  (side project)
- Author/s:         Angel Martinez-Tenor
- Dev Date:         2020 - 2023

- Status:           In progress.

"""

from pathlib import Path

import pandas as pd

from smart_data_science import logger
from smart_data_science.ui import ui_io

# # Data & Output paths
# DATA_PATH = "../data/"
# OUTPUT_PATH = "../output/"

PATH_NORMALIZED = Path("data/normalized")
FILEPATH_DATA_FOR_ML = PATH_NORMALIZED / "data.parquet"

log = logger.get_logger(__name__)

# UPDATE TO  @dataclass


class DataTable:
    """Data Table Definition. Abstract Parent Class with common variables & methods for all the Tables"""

    def __init__(self, df=None):
        self.NAME = None
        self.VARIABLES = None
        self.FILEPATH_SOURCE = None
        self.FILEPATH = None  # parquet file
        # self.INDEX = None
        self.REFERENCE_DATE_VARIABLE = None  # optional
        self.link_zip = None  # link to zip of last uploaded excel file (Streamlit download solution)
        self.df = df

    def process(self, df: pd.DataFrame, check=False, matrix_type=False):
        """
        Parse & Process the input dataframe
        """
        df = df.copy()
        # if df.index.name == self.INDEX:
        #     df = df.reset_index()
        if check:
            check_variables(df.reset_index(), self.VARIABLES)
            df = df[self.VARIABLES]
        df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)  # Remove Tailing spaces found excel files

        if not matrix_type:  # valid index
            df = df.drop_duplicates()
        # to improve: check for unique indexes in matrix type
        # df = df.dropna(subset=[self.INDEX])  # Reject samples with null index
        # df.set_index(self.INDEX, inplace=True)
        return df

    def etl(self, filepath=None):
        """
        Load the source File, parse, process & save the normalized data to parquet
        """
        if not filepath:
            filepath = self.FILEPATH_SOURCE
        df = self.load_excel(filepath)
        df = self.process(df)
        self.df = df
        df.to_parquet(self.FILEPATH)

    def load(self):
        """
        Load the normalized parquet file
        """
        df = pd.read_parquet(self.FILEPATH)

        check_variables(df.reset_index(), self.VARIABLES)
        self.df = df.copy()
        return df

    def check_datafile(self):
        """
        Generate  a normalized parquet datafile if it nor exists.
        Future Improvement: To be used for a Recovery
        """
        if not Path(self.FILEPATH).exists():
            self.etl()

    def load_excel(self, filepath=None):
        """
        Abstract method: Load the  excel file into a dataframe
        The abc library can be used here: https://pymotw.com/3/abc/
        """
        raise ValueError("ERROR - Abstract Method: Override this function in its subclass")

    def update_excel_and_zip(self, file_uploaded):
        """
        Save uploaded excel & zip files.
        """
        ui_io.save_file_and_zip(file_uploaded, self.FILEPATH_SOURCE)

    def generate_download_link(self, update=False):
        """
        Generate a downloadable link of a zipped file with the last excel file uploaded
        Changes & Incidences Tables also generates a downloadable link of a zipped excel file with all the historical
        data normalized
        """
        if update:
            self.link_zip = ui_io.generate_download_link(self.FILEPATH_SOURCE, caption="**Download**")

    def save_and_generate_download_link(self, filepath: str | Path):  # New - fast demo
        """
        Generate a downloadable link of a zipped file with the last excel file uploaded
        Changes & Incidences Tables also generates a downloadable link of a zipped excel file with all the historical
        data normalized
        """
        # pathlib generate parent  folder if not exists of filepath
        filepath = Path(filepath)
        filepath.parent.mkdir(parents=True, exist_ok=True)
        self.df.to_parquet(filepath)
        self.link_zip = ui_io.generate_download_link(filepath, caption="**Download**")


class DataForML(DataTable):
    """Table Products Definition"""

    def __init__(self, df):
        super().__init__()
        self.NAME = "DATA FOR ML"
        self.FILEPATH = FILEPATH_DATA_FOR_ML
        self.FILEPATH_source = FILEPATH_DATA_FOR_ML
        self.df = df
        self.save_and_generate_download_link(self.FILEPATH)

        # self.df = df
        # TO IMPROVE check rest of variables, Add numerical_features, etc.. .


def check_variables(df, needed_variables):
    """
    Check if all the variables from the list or set 'needed_variables' are columns of the input dataframe 'df.
    Generate an assertion error showing the missing the variables if any
    """
    missing_variables = set(needed_variables).difference(set(df))
    assert not missing_variables, f"ERROR: MISSING VARIABLES: {missing_variables}"
