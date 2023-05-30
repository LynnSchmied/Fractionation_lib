def data_viz_upset(
        df,
        str_save=''
):
    """ data_viz_upset creates a plot from the df. Returns Log10 protein intensity plot per run/fraction.
    REQUIRES PROTEINGROUPS FILE.

    Requires:
    data_formate
    import plotly.express as px
    import os
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    Parameters
    ----------
    df: DataFrame to get primary data
    str_save: link to save images, in formate r'ful_path'

    Returns
    -------
    :  plots

    """

    today = datetime.today()
    today = today.strftime("date_%d%m%Y_time_%H%M%S")

    # troubleshooting
    if str_save == '':
        os.mkdir('Plots_' + str(today))
        str_save = r'Plots_' + str(today)

    # getting dataframe from link

    # creating the directory
    today = datetime.today()
    today = today.strftime("date_%d%m%Y_time_%H%M%S")
    long_link_save = str_save + '\ProteinUpset_plot_' + str(today)
    directory = os.path.join(long_link_save)
    os.mkdir(directory)

    # reshaping the DataFrame
    set_dict = {'set_' + i: set(list(df['Precursor'][df['Fraction'] == i])) for i in np.array(df['Fraction'].unique())}
    set_dict['all_elements'] = set(df['Precursor'].unique())
    list_dict = list(set_dict.keys())[:-1]
    bool_dict = {}
    for i in set_dict['all_elements']:
        bool_dict[i] = [i]
        for j in list_dict:
            bool_dict[i].append(i in set_dict[j])
    names = [a + 1 for a in range(len(list_dict))]
    dict_names_to_switch = {names[i]: list_dict[i] for i in range(len(names))}
    df_dict = pd.DataFrame(bool_dict).transpose().drop(columns={0}).rename(columns=dict_names_to_switch)
    # Plotting
    df_up = df_dict.groupby(list_dict).size()
    plot(df_up, orientation='horizontal')

    # Saving plot to the directory
    plt.savefig(long_link_save + '\_' + 'Upset_plot', bbox_inches='tight', pad_inches=0, dpi=300)

