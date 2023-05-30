def data_format_max(
        df
):
    """ data_format_max creates the DataFrame of the typical formate from MaxQuant file.

    Requires:
    import numpy as np
    import pandas as pd

    Parameters
    ----------
    df: DataFrame from data_formate()

    Returns
    -------
    : pandas dataframe
        DataFrame ready to plot
    """

    # cutting the name
    df["Fraction"] = [df["Raw file"][index].split("_")[-1] for index in range(len(df))]
    df['Fraction'] = df['Fraction'].astype(int)
    df = df.sort_values('Fraction')
    df['Fraction'] = df['Fraction'].astype(str)
    df['Precursor'] = df['Sequence'] + '_' + df['Charge'].apply(str)
    df['Potential_contaminant'] = df['Potential contaminant']
    df['Length'] = df['Sequence'].str.len()

    # looking for the NaN, creating the list of missing proteins
    if df['Intensity'].isna().sum() != 0:
        df = df.dropna(axis=0)

    # filtering the dataframe
    df_filtered = df.loc[df.Reverse != '+'].loc[df.Potential_contaminant != '+']

    # changing the shape
    df_filtered['RT_round'] = df_filtered['Retention time'].round()
    # df_filtered['Ion_mobility'] = df_filtered['1/K0'].round(3)
    df_filtered['Log_intensity'] = np.log10(df_filtered['Intensity'])
    df_filtered['Rank'] = df_filtered['Intensity'].rank(ascending=False)
    df_filtered['m/z'] = df_filtered['m/z'].round(-1)
    # df_filtered = df_filtered[['Proteins', 'Precursor', 'Fraction', 'Intensity',
    # 'Log_intensity', 'RT_round', 'm/z', 'Ion_mobility', 'Rank']]
    df_filtered = df_filtered[[
        'Proteins',
        'Precursor',
        'Fraction',
        'Intensity',
        'Log_intensity',
        'RT_round',
        'm/z',
        'Rank',
        'Length']]

    return df_filtered

