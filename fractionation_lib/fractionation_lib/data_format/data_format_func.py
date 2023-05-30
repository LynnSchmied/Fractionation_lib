def data_format_func(
        data_address: str
):
    """ data_format_func creates the DataFrame of the typical formate. It can process two types of files: Spectranaut file
    and MaxQuant file.


    Requires:
    import numpy as np
    import pandas as pd
    import pingouin as pg

    Parameters
    ----------
    data_address: string with the address of the local file to import df. data_address = r'link_to_data'

    Returns
    -------
    : pandas dataframe
        DataFrame ready to plot
    """
    if type(data_address) != str:
        raise ValueError('address should be string')

    # reading the file TEST
    # if data_address[0]!='r':
    #  raise ValueError('file address should be in formate r'address')

    if type(data_address) != str:
        raise ValueError('address should be string')

    # reading the file
    if data_address[-3:] == 'csv':
        df = pd.read_csv(data_address)
    elif data_address[-3:] == 'tsv':
        df = pd.read_csv(data_address, sep='\t')
    elif data_address[-3:] == 'txt':
        df = pd.read_csv(data_address, sep='\t')
    else:
        print(data_address[-3:])
        raise ValueError('file should be .csv/.tsv')

    # TEST
    # print(list(df.columns))

    if 'PG.Genes' in list(df.columns):
        df = data_format_spec(df)
    elif 'PG.Genes' not in list(df.columns):
        df = data_format_max(df)

    return df

