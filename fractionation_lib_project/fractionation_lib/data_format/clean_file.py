# NOT READY!!!!!!!!!


import pandas as pd

def clean_data(link: str):
    """
    This function cleans the data file at the given link and prepares a pandas DataFrame for visualization.

    It reads the data from a .tsv file, selects specific columns, filters out potential contaminants,
    and aggregates unique sequences and proteins by experiment.

    Parameters
    ----------
    link: str
        The path to the .tsv data file.

    Returns
    -------
    df_count: pandas.DataFrame
        A DataFrame ready for further visualization.
        Each row corresponds to a unique experiment from the original data, with aggregated information
        about sequences and proteins.
    """
    try:
        sample = pd.read_csv(link, sep='\t')[[
            'Sequence',
            'Proteins',
            'm/z',
            'Retention time',
            'Intensity',
            'Experiment',
            'Potential contaminant'
        ]]
    except FileNotFoundError:
        raise ValueError(f"File at {link} not found.")
    except Exception as e:
        raise ValueError(f"An error occurred while reading the file: {e}")

    sample['Potential_contaminant'] = sample['Potential contaminant']
    sample = sample.loc[sample.Potential_contaminant != '+']

    experiment_list = sample.Experiment.unique()
    df_count = pd.DataFrame([
        [
            experiment,
            sample.loc[sample['Experiment'] == experiment]['Sequence'].nunique(),
            set(sample.loc[sample['Experiment'] == experiment]['Sequence']),
            sample.loc[sample['Experiment'] == experiment]['Proteins'].nunique(),
            set(sample.loc[sample['Experiment'] == experiment]['Proteins'])
        ] for experiment in experiment_list
    ]).rename(columns={0: 'Sample', 1: 'Sequences', 2: 'Sequences_set', 3: 'Proteins', 4: 'Prot_set'})

    df_count['Type'] = df_count['Sample'].apply(lambda x: x.split('_')[0])

    return df_count

