import os
import pandas as pd
import numpy as np
import re
import pingouin as pg


def spec(df: pd.DataFrame) -> pd.DataFrame:
    """
    Formats the DataFrame from a Spectranaut file.

    Parameters:
    ----------
    df : pd.DataFrame
        A DataFrame from data_formate()

    Returns:
    -------
    pd.DataFrame
        A formatted DataFrame ready for plotting
    """
    import re

    df = df.copy()

    # Dropping decoys and renaming columns
    df = df[df['EG.IsDecoy'] == False].rename(columns={'PG.ProteinGroups': 'Proteins',
                                                       'EG.PrecursorId': 'Precursor',
                                                       'EG.TotalQuantity (Settings)': 'Intensity',
                                                       'FG.ApexIonMobility': 'Ion_mobility',
                                                       'EG.ApexRT': 'Retention_time',
                                                       'FG.PrecMzCalibrated': 'm/z',
                                                       'PEP.GroupingKey': 'Sequences',
                                                       'R.FileName': 'R.FileName'})

    # Removing rows with NaN in 'Intensity' column
    df.dropna(subset=['Intensity'], inplace=True)

    # Adding log_intensity , rank, fraction
    df['Log_intensity'] = np.log10(df['Intensity'])
    df['Rank'] = df['Intensity'].rank(ascending=False)
    df['Fraction'] = [re.search(r'Fr\d+', file_name).group() for file_name in df['R.FileName']]
    df.sort_values('Fraction', inplace=True)
    df['RT_round'] = df['Retention_time'].round()
    df['Ion_mobility'] = df['Ion_mobility'].round(3)
    df['Length'] = df['Sequences'].str.len()

    # Selecting the necessary columns
    df = df[['Proteins',
             'Precursor',
             'Fraction',
             'Intensity',
             'Log_intensity',
             'RT_round',
             'm/z',
             'Ion_mobility',
             'Rank',
             'Sequences',
             'Length']]

    return df
