import os
import pandas as pd
import numpy as np
import re


def maxquant(df: pd.DataFrame) -> pd.DataFrame:
    """
    Formats the DataFrame from a MaxQuant file.

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

    df["Fraction"] = [re.search(r'Fr\d+', file_name).group() for file_name in df["Raw file"]]
    df['Fraction'] = df['Fraction'].astype(str)
    df.sort_values('Fraction', inplace=True)

    df['Precursor'] = df['Sequence'] + '_' + df['Charge'].apply(str)
    df['Potential_contaminant'] = df['Potential contaminant']
    df['Ion_mobility'] = df['1/K0']
    df['Length'] = df['Sequence'].str.len()

    # Removing rows with NaN in 'Intensity' column
    df.dropna(subset=['Intensity'], inplace=True)

    # Filtering the dataframe
    df_filtered = df.loc[df.Reverse != '+'].loc[df.Potential_contaminant != '+']

    # Adding columns
    df_filtered['RT_round'] = df_filtered['Retention time'].round()
    df_filtered['Log_intensity'] = np.log10(df_filtered['Intensity'])
    df_filtered['Rank'] = df_filtered['Intensity'].rank(ascending=False)
    df_filtered['m/z'] = df_filtered['m/z'].round(-1)

    df_filtered = df_filtered[[
        'Proteins',
        'Precursor',
        'Fraction',
        'Intensity',
        'Log_intensity',
        'Ion_mobility',
        'RT_round',
        'm/z',
        'Rank',
        'Length']]

    return df_filtered
