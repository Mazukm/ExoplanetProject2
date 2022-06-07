"""
CSE 163

using the gicen data frames
creats a seriese of graphs
"""

import seaborn as sbn
import matplotlib.pyplot as plt


class DataGraph():

    def plot_counts_metalicity(df):
        """
        makes a boxplot of the metal ratios
        to the amount of planets
        """
        sbn.catplot(x="st_metratio", kind='bar', y="sy_pnum", data=df)
        plt.xlabel("Metalicity ratio of the star")
        plt.ylabel("number of planets")
        plt.title("Metalicity of the star to the number of planets")
        plt.savefig("./graphdata/metalicit_av_count.png", bbox_inches="tight")
        plt.tight_layout()
        plt.clf()

    def plot_counts_spectrum(df):
        """
        makes a boxplot of the spectrum
        to the avrage amount of planets
        """
        sbn.catplot(x="st_spectype", kind='bar', y="sy_pnum", data=df)
        plt.xlabel("Spectrum of the star")
        plt.ylabel("number of planets")
        plt.title("Spectrum of the star to the number of planets")
        plt.savefig("./graphdata/spectrum_av_count.png", bbox_inches="tight")
        plt.tight_layout()
        plt.clf()

    def plot_counts_mass(df):
        """
        makes a scatterplot of number of planets
        to the log of the tempurature of the star
        """
        sbn.regplot(x="st_logg", y="sy_pnum", data=df)
        plt.xlabel("log mass of the star (Kg)")
        plt.ylabel("number of planets")
        plt.title("log mass of the star to the number of planets")
        plt.savefig("./graphdata/mass_planet_count.png")
        plt.clf()

    def plot_counts_temp(df):
        """
        makes a scatter plot with the tempurature
        and plots the number of planets
        """
        sbn.regplot(x="st_teff", y="sy_pnum", data=df)
        plt.xlabel("Temp of the star log(K)")
        plt.ylabel("number of planets")
        plt.title("Temputure of the star to the number of planets")
        plt.savefig("./graphdata/amount_to_tempurature.png")
        plt.clf()

    def plot_counts_distance(df):
        """
        makes a scatter plot with the tempurature
        and plots the number of planets
        """
        sbn.regplot(x="sy_dist", y="sy_pnum", data=df)
        plt.xlabel("Distance to the planet (pc)")
        plt.ylabel("number of planets")
        plt.title("Number of the planets to distance from the solar system")
        plt.savefig("./graphdata/amount_to_distance.png")
        plt.clf()

    def plot_counts_rad(df):
        """
        makes a scatterplot of radius to planet number
        """
        sbn.regplot(x="st_rad", y="sy_pnum", data=df)
        plt.xlabel("Radius of the star (Solar Radius)")
        plt.ylabel("number of planets")
        plt.title("Radius of the star to the number of planets")
        plt.savefig("./graphdata/amount_radius.png")
        plt.clf()
