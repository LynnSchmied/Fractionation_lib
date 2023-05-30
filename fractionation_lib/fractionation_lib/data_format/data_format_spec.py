def data_format_spec(
        df
):
    """ data_format_spec creates the DataFrame of the typical formate from Spectranaut file.

    Requires:
    import numpy as np
    import pandas as pd
    import pingouin as pg

    Parameters
    ----------
    df: DataFrame from data_formate()

    Returns
    -------
    : pandas dataframe
        DataFrame ready to plot
    """

    # dropping wrong columns, filtering decoys
    df = df[df['EG.IsDecoy'] == False]
    df = df[['PG.ProteinGroups', 'EG.PrecursorId', 'EG.TotalQuantity (Settings)', 'FG.ApexIonMobility', 'EG.ApexRT',
             'FG.PrecMzCalibrated', 'R.FileName', 'PEP.GroupingKey']].rename(
        columns={'PG.ProteinGroups': 'Proteins', 'EG.PrecursorId': 'Precursor',
                 'EG.TotalQuantity (Settings)': 'Intensity', 'FG.ApexIonMobility': 'Ion_mobility',
                 'EG.ApexRT': 'Retention_time', 'FG.PrecMzCalibrated': 'm/z', 'PEP.GroupingKey': 'Sequences'})

    # looking for the NaN, creating the list of missing proteins TEST
    if df['Intensity'].isna().sum() != 0:
        df = df.dropna(axis=0)

    # adding log_intensity , rank, fraction
    df['Log_intensity'] = np.log10(df['Intensity'])
    df['Rank'] = df['Intensity'].rank(ascending=False)
    df['Fraction'] = [df['R.FileName'][index].split('_')[-1] for index in range(len(df))]
    df['Fraction'] = df['Fraction'].astype(int)
    df = df.sort_values('Fraction')
    df['Fraction'] = df['Fraction'].astype(str)
    df['RT_round'] = df['Retention_time'].round()
    df['Ion_mobility'] = df['Ion_mobility'].round(3)
    df['m/z'] = df['m/z'].round(-1)
    df['Length'] = df['Sequences'].str.len()

    # changing the shape
    df = df[
        ['Proteins',
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
