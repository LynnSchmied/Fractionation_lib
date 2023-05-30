import os
import pandas as pd
import numpy as np
import re


def diann_report(df: pd.DataFrame) -> pd.DataFrame:
    """
    Formats the DataFrame from a DIA-NN report file for further visualization. Returns DataFrame.

    Parameters:
    ----------
    df : pd.DataFrame
        A DataFrame from data_format_func

    Returns:
    -------
    pd.DataFrame
    """
    import re

    df = df.copy()

    df = df[[
        'Protein.Group',
        'Protein.Ids',
        'Stripped.Sequence',
        'RT',
        'IM',
        'File.Name'
    ]].rename(
        columns={
            'Protein.Group': 'Protein',
            'Protein.Ids': 'ProtId',
            'Stripped.Sequence': 'Peptide'
        }
    )

    df['Fraction'] = [re.search(r'Fr\d+', file_name).group() for file_name in df["File.Name"]]
    df['Sample'] = [re.search(r'X\dS\dFr\d', file_name).group() for file_name in df["File.Name"]]
    df['Fraction'] = df['Fraction'].astype(str)
    df['Sample'] = df['Sample'].astype(str)
    df.drop(columns='File.Name', inplace=True)

    print('Unique proteins in df: ' + str(df.Protein.nunique()))
    print('Unique peptides in df: ' + str(df.Peptide.nunique()))

    return df