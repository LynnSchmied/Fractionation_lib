import os
import pandas as pd
from max_file import maxquant
from spec_file import spec
from diann_file import diann
from diann_report_file import diann_report


def data_format_func(data_address: str, file_type: str):
    """ data_format_func creates the DataFrame of the typical format. It can process three types of files: Spectranaut file,
    MaxQuant file, and DIA-NN file.

    Parameters
    ----------
    data_address: string with the address of the local file to import df. data_address = r'link_to_data'
    file_type: string specifying the file type, one of: 'spec', 'maxquant', 'diann'

    Returns
    -------
    : pandas dataframe
        DataFrame ready to plot
    """
    if not isinstance(data_address, str):
        raise ValueError('Address should be string')

    _, file_extension = os.path.splitext(data_address)

    try:
        if file_extension == '.csv':
            df = pd.read_csv(data_address)
        elif file_extension == '.tsv' or file_extension == '.txt':
            df = pd.read_csv(data_address, sep='\t')
        else:
            raise ValueError(f'File should be .csv/.tsv/.txt, but got {file_extension}')
    except FileNotFoundError:
        raise ValueError(f'File at {data_address} not found')
    except Exception as e:
        raise ValueError(f'An error occurred while reading the file: {e}')

    if file_type == 'spec':
        df = spec(df)
    elif file_type == 'maxquant':
        df = maxquant(df)
    elif file_type == 'diann':
        df = diann(df)
    elif file_type == 'diann_rep':
        df = diann_report(df)
    else:
        raise ValueError(f'Invalid file type: {file_type}. Expected one of: "spec", "maxquant", "diann"')

    return df
