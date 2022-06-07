"""
CSE 162
reades the given csv and processes it into a usable dataframe
"""
import pandas as pd
import os


class DataImport():

    def filter_columns(df):
        """
        filters the columns down and returns on the
        """
        df = df.loc[:, ["hostname", "st_teff", "st_rad",
                        "sy_snum", "st_metratio",
                        "st_spectype", "st_logg", "sy_pnum", "sy_dist"]]
        df = df[df["sy_snum"] == 1]
        df = df.dropna()
        return df[(df.T != 0).any()].drop_duplicates()

    def avrg_num_metalicity(df):
        """
        calculates the avrage number of planets according
        to each metalicity column
        """
        return (df[df["st_metratio"] != "[Fe/H["].groupby("st_metratio",
                as_index=False)["sy_pnum"].mean())

    def avrg_num_spectrum(df):
        """
        creates a dataset of the mean of planets per spectrum type
        """
        return df.groupby("st_spectype", as_index=False)["sy_pnum"].mean()

    def read_in_data():
        """
        Imports and does high level filtering of the dataset
        """
        current_dir = os.getcwd()
        data_frame1 = pd.read_csv(current_dir + "/" +
                                  "PS_2022.05.23_16.34.26.csv", skiprows=99)
        data_frame2 = pd.read_csv(current_dir + "/" +
                                  "PS_2022.05.23_16.36.33.csv", skiprows=96)
        full_data_frame = pd.concat([data_frame1, data_frame2])
        full_data_frame = full_data_frame[(full_data_frame
                                           ["pl_controv_flag"] == 0)
                                          | (full_data_frame
                                             ["pl_controv_flag"] == "0")]
        return full_data_frame
