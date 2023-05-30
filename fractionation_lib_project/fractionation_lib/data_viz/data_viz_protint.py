def data_viz_protint(
        str_data='',
        str_save=''
):
    """ data_viz_protint creates a plot from the df. Returns Log10 protein intensity plot per run/fraction.
    REQUIRES PROTEINGROUPS FILE.

    Requires:
    data_formate
    import plotly.express as px
    import numpy as np
    import pandas as pd

    Parameters
    ----------
    str_data: link to get primary data, in formate r'ful_path'
    str_save: link to save images, in formate r'ful_path'

    Returns
    -------
    :  plots

    """

    today = datetime.today()
    today = today.strftime("date_%d%m%Y_time_%H%M%S")

    # troubleshooting
    if type(str_data) != str:
        raise ValueError('address should be string')
    if str_data == '':
        raise ValueError('Please, get the path to the primary file properly and try again')
    if str_save == '':
        os.mkdir('Plots_' + str(today))
        str_save = r'Plots_' + str(today)

    # reading the file
    if str_data[-3:] == 'csv':
        df = pd.read_csv(str_data)
    elif str_data[-3:] == 'tsv':
        df = pd.read_csv(str_data, sep='\t')
    elif str_data[-3:] == 'txt':
        df = pd.read_csv(str_data, sep='\t')
    else:
        print(str_data[-3:])
        raise ValueError('file should be .csv/.tsv/.txt')

    # creating the directory
    today = datetime.today()
    today = today.strftime("date_%d%m%Y_time_%H%M%S")
    long_link_save = str_save + '\ProteinIntensity_plot_' + str(today)
    directory = os.path.join(long_link_save)
    os.mkdir(directory)

    # formatting the DataFrame
    df = df[df['Potential contaminant'] != '+']
    df_filt = df.filter(regex=r'Intensity')
    df_filt['Protein names'] = df['Protein names']
    df_filt = df_filt.melt(['Protein names']).rename(
        columns={'Protein name': 'Proteins', 'variable': 'Fraction', 'value': 'Intensity_value'})
    df_filt = df_filt[df_filt['Intensity_value'] != 0]
    df_filt['Log_intensity'] = np.log10(df_filt['Intensity_value'])

    # Plotting the DataFrame
    fig = px.box(df_filt, x='Fraction', y='Log_intensity', title='Protein intensities per run', width=1000, height=1000)
    fig.show()

    # Saving the plot to the directory
    fig.write_image(long_link_save + r'\ProteinIntensity_per_run.png')
    fig.write_image(long_link_save + r'\ProteinIntensity_per_run.pdf')
