# NOT READY!!!!!!!!!

def data_format_diann_report(
        df
):
    """ data_format_diann_report creates the formated dataframe from diann report file for the further going
    visualization. Returns DataFrame.

    Requires:
    import pandas as pd

    Parameters
    ----------
    df: df from data_format_func

    Returns
    -------
    :  df

    """
    #df = pd.read_csv(link, sep='\t')[['Protein.Group', 'Protein.Ids', 'Stripped.Sequence', 'RT', 'IM', 'File.Name']].rename(columns={'Protein.Group': 'Protein', 'Protein.Ids': 'ProtId', 'Stripped.Sequence': 'Peptide'})
    df = df[[
        'Protein.Group', 'Protein.Ids', 'Stripped.Sequence', 'RT', 'IM', 'File.Name'
    ]].rename(
        columns={'Protein.Group': 'Protein', 'Protein.Ids': 'ProtId', 'Stripped.Sequence': 'Peptide'}
    )

    df_mod = df
    if len(df_mod['File.Name'][0].split('_')[-4])>4:
        #S1['Fraction_2'] = S1.loc[:,'File.Name'].str.split('_').str[-4]
        df_mod['Fraction'] = df_mod.loc[:,'File.Name'].str.split('_').str[-4].astype(str)
        df_mod['Sample'] = [df_mod['Fraction'][i][2:4] for i in range(len(df_mod))]
        df_mod['Fraction'] = [df_mod['Fraction'][i][4:] for i in range(len(df_mod))]
    else:
        df_mod['Fraction'] = df_mod.loc[:, 'File.Name'].str.split('_').str[-4].astype(str)
    df_mod = df_mod.drop(columns='File.Name')
    print('Unique proteins in df: ' + str(df_mod.Protein.nunique()))
    print('Unique peptides in df: ' + str(df_mod.Peptide.nunique()))
    return df_mod