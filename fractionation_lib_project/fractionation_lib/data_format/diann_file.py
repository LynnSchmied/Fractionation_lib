import os
import pandas as pd
import numpy as np
import re

def diann(df: pd.DataFrame) -> pd.DataFrame:
    """
    Formats the DataFrame from a DIA-NN file.

    Parameters:
    ----------
    df : pd.DataFrame
        A DataFrame from data_formate()

    Returns:
    -------
    pd.DataFrame
        A formatted DataFrame ready for plotting
    """
    df = df.copy()

    # Renaming columns and selecting necessary ones
    df = df.rename(columns={'Protein.Group': 'Proteins',
                            'Precursor.Id': 'Precursor',
                            'Precursor.Quantity': 'Intensity',
                            'File.Name': 'R.FileName',
                            'RT': 'Retention_time',
                            'IM': 'Ion_mobility',
                            'Stripped.Sequence': 'Sequences'}).loc[:, ['Proteins',
                                                                        'Precursor',
                                                                        'Intensity',
                                                                        'R.FileName',
                                                                        'Retention_time',
                                                                        'Ion_mobility',
                                                                        'Sequences']]

    # Removing rows with NaN in 'Intensity' column
    df.dropna(subset=['Intensity'], inplace=True)

    # Adding log_intensity, rank, fraction
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
             'Ion_mobility',
             'Rank',
             'Sequences',
             'Length']]

    return df
