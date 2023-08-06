"""
- Title:            Utils load Data Samples
- Project/Topic:    Smart Data Science. Practical functions for Data Science
- Author/s:         Angel Martinez-Tenor
- Dev Date:         2017 - 2023

- Status:           Planning

- Acknowledgements. Partially Based on:
    - Personal Repo: https://github.com/angelmtenor/data-science-keras/blob/master/helper_ds.py
"""
from __future__ import annotations

from importlib import resources
from pathlib import Path

import pandas as pd

from smart_data_science.core import logger

log = logger.get_logger(__name__)

PUBLIC_DATASETS = {
    "Churn Banking": "churn_bank.csv",
    "Sales Supermarkets": "sales_supermarkets.parquet",
    "Shipping Logs": "shipping_logs.csv",
}

public_data_names = list(PUBLIC_DATASETS.keys())
public_datafiles = [Path(f) for f in PUBLIC_DATASETS.values()]


def load_sample(filename: str = "churn_bank") -> pd.DataFrame:
    """Load a Sample Dataset
    args:
        sample_data (str): Name of the sample data to load. Extension can be omitted.
    returns:
        pd.DataFrame: Sample Log Dataset Selected
    """
    datafile = Path(filename)

    if datafile.suffix:
        assert datafile.suffix in [".csv", ".parquet"], "Only .csv and .parquet files are supported"
        assert datafile in public_datafiles, f"Sample datafile {datafile} not available. Available: {public_datafiles}"
    else:
        for suffix in [".parquet", ".csv"]:
            if datafile.with_suffix(suffix) in public_datafiles:
                datafile = datafile.with_suffix(suffix)
                break
        assert datafile.suffix, f"Sample datafile {datafile} not available. Available: {public_datafiles}"

    with resources.path("smart_data_science.core.data_samples", f"{datafile}") as f:
        data_file_path = Path(f)
        if datafile.suffix == ".parquet":
            return pd.read_parquet(data_file_path)
        return pd.read_csv(data_file_path)
