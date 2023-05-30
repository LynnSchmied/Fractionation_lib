# NOT READY!!!!!!!!!

def data_format_diann(
        df
):
    """ data_format_diann creates the DataFrame of the typical formate from Di-NN file for the further going
    visualization. Returns DataFrame.

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
    df = df[df['Decoy.Evidence'] == False]
    #df = pd.read_csv(link, sep='\t')
    df_mod = df[['PeptideSequence', 'decoy', 'ProteinGroup', 'PrecursorCharge', 'FileName']]
    if len(df_mod['FileName'][0].split('_')[-4])>4:
        df_mod['Fraction'] = df_mod['FileName'].str.split('_').str[-4]
        df_mod['Sample'] = [df_mod['Fraction'][i][2:4] for i in range(len(df_mod))]
        df_mod['Fraction'] = [df_mod['Fraction'][i][4:] for i in range(len(df_mod))]
    else:
        df_mod['Fraction'] = df_mod['FileName'].str.split('_').str[-4]
    df_mod = df_mod.drop(columns='FileName')
    df_mod = df_mod[df_mod['decoy']==0].rename(columns={'PeptideSequence':'Peptide', 'decoy':'Decoy', 'ProteinGroup':'Protein', 'PrecursorCharge':'Charge'})

    print('Unique proteins in df: ' + str(df_mod.Protein.nunique()))
    print('Unique peptides in df: ' + str(df_mod.Peptide.nunique()))

    return df_mod

