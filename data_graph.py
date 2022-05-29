import pandas as pd
import numpy as np
import seaborn as sb

class DataGraph():
    def plot_counts_spectrutm(df):
        plot = sb.catplot(x="st_metratio", y="sy_pnum", data=df) 
        plot.figure.savefig("spectrum_mass.png")

    def plot_counts_mass(df):
        plot = sb.scatterplot(x="st_logg", y="sy_pnum", data=df) 
        plot.figure.savefig("amount_mass.png")
    
    def plot_counts_temp(df):
        plot = sb.scatterplot(x="st_teff", y="sy_pnum", data=df) 
        plot.figure.savefig("amount_temp.png")
    
    def plot_counts_rad(df):
        plot = sb.scatterplot(x="st_rad", y="sy_pnum", data=df)
        plot.figure.savefig("amount_radius.png")