import pandas as pd
import numpy as np
import seaborn as sb

class DataGraph():
    def plot_counts_spectrutm(df):
        plot = sb.catplot(x="st_metratio", y="sy_pnum", data=df) 
        plot.figure.savefig("output.png")