import pandas as pd
import numpy as np
import data_import as di
import data_graph as dg


if __name__ == "__main__":
    """
    Imports and does high level filtering of the dataset
    """
    df = di.DataImport.read_in_data()
    df = di.DataImport.filter_columns(df)
 #   print(df)
    df.to_csv("full2.csv")
    df = di.DataImport.get_count_spectrum(df)
  #  print(df)
    df.to_csv("full3.csv")
    dg.DataGraph.plot_counts_spectrutm(df)