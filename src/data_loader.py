import pandas as pd


def load_patient_data(file_path):
    """
    Load clinical patient data from a CSV file.

    Parameters
    ----------
    file_path : str
        Path to the CSV file.

    Returns
    -------
    pandas.DataFrame
        Loaded patient dataset.
    """
    data = pd.read_csv(file_path)
    return data