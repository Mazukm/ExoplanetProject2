import pandas as pd
import numpy as np



if __name__ == "__main__":
    data_frame1 = pd.read_csv("PS_2022.05.23_16.34.26.csv", skiprows=99)
    data_frame2 = pd.read_csv("PS_2022.05.23_16.36.33.csv", skiprows=96)


    full_data_frame = data_frame1.append(data_frame2, ignore_index=True)
  #  planet_number = full_data_frame.groupby(["hostname",])
    full_data_frame = full_data_frame[(full_data_frame["pl_controv_flag"] == 0 ) | (full_data_frame["pl_controv_flag"] == "0")]
    full_data_frame.to_csv("full.csv")
 #   planet_number.to_csv("planet_number.csv")