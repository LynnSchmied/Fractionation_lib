# NOT READY!!!!!!!!!


def data_format_clean(
        link: str
):
    """ data_format_clean creates the DataFrame of the typical formate from any??? file for the further going
    visualization. Returns DataFrame.

    Requires:
    import numpy as np
    import pandas as pd

    Parameters
    ----------
    link: str

    Returns
    -------
    : pandas dataframe
        DataFrame ready to plot
    """
    sample = pd.read_csv(link, sep='\t')[[
        'Sequence',
        'Proteins',
        'm/z',
        'Retention time',
        'Intensity',
        'Experiment',
        'Potential contaminant'
    ]]
    sample['Potential_contaminant'] = sample['Potential contaminant']
    sample = sample.loc[sample.Potential_contaminant != '+']
    exp_l = list(sample.Experiment.unique())
    df_count = pd.DataFrame([
        [i,
        sample.loc[sample['Experiment']==i]['Sequence'].nunique(),
        set(sample.loc[sample['Experiment']==i]['Sequence']),
        sample.loc[sample['Experiment']==i]['Proteins'].nunique(),
        set(sample.loc[sample['Experiment']==i]['Proteins'])] for i in exp_l]).rename(columns={0: 'Sample', 1: 'Sequences', 2: 'Sequences_set', 3: 'Proteins',
                      4: 'Prot_set'})
    df_count['Type'] = [df_count['Sample'][index].split('_')[0] for index in range(len(df_count))]
    return df_count
