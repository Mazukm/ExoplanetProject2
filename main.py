import pandas as pd
import numpy as np
import data_import as di


if __name__ == "__main__":
    """
    Imports and does high level filtering of the dataset
    """
    df = di.read_in_data()
    df = di.filter_columns(df)
    df.to_csv("full2.csv")
