import pandas as pd
import numpy as np

class DataImport():
    def read_in_data():
        """
        Imports and does high level filtering of the dataset
        """
        data_frame1 = pd.read_csv("PS_2022.05.23_16.34.26.csv", skiprows=99)
        data_frame2 = pd.read_csv("PS_2022.05.23_16.36.33.csv", skiprows=96)
        full_data_frame = data_frame1.append(data_frame2, ignore_index=True)
        full_data_frame = full_data_frame[(full_data_frame["pl_controv_flag"] == 0 )
                                          | (full_data_frame["pl_controv_flag"] == "0")]
        return full_data_frame