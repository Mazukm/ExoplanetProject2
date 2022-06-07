"""
main data file, that runs all
of the code needed
"""

import pickle
import data_import as di
import data_graph as dg
import machine_learning as ml


def main():
    """
    Imports and does high level filtering of the dataset
    """
    df = di.DataImport.read_in_data()
    df = di.DataImport.filter_columns(df)
    dg.DataGraph.plot_counts_rad(df)
    dg.DataGraph.plot_counts_mass(df)
    dg.DataGraph.plot_counts_temp(df)
    dg.DataGraph.plot_counts_distance(df)
    dg.DataGraph.plot_counts_spectrum(di.DataImport.avrg_num_spectrum(df))
    dg.DataGraph.plot_counts_metalicity(di.DataImport.avrg_num_metalicity(df))
    labels, features = ml.MachineLearning.prep_data(df)
    features_train, features_tst, labels_train, labels_tst = (
        ml.MachineLearning.seperate_datasets(labels, features))
    model = ml.MachineLearning.train_model(labels_train, features_train)
    pickle.dump(model, open("model.p", "wb"))
    ml.MachineLearning.test_model(labels_tst, features_tst, model)


if __name__ == "__main__":
    main()
