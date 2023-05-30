def data_viz_summarise(
        df,
        str_save: str
):
    """ data_viz_summarise creates a bunch of plots from the df. Returns three plots: Dynamic range for all fractions,
    scatter plot of ranked log10 of intensity, Dynamic range per fraction

    Requires:
    data_formate
    import plotly.express as px
    import numpy as np
    import pandas as pd

    Parameters
    ----------
    df: pandas dataframe
    str_save: link to save images in formate r'ful_path'

    Returns
    -------
    :  plots

    """

    # dynamic range for all fractions RT
    a = 0
    df_dyn_range = {}
    for i in np.array(df['RT_round'].unique()):
        df_dyn_range[a] = [i, df[df['RT_round'] == i]['Log_intensity'].max() - df[df['RT_round'] == i][
            'Log_intensity'].min()]
        a += 1
    df_dyn_range = pd.DataFrame(df_dyn_range).transpose().rename(
        columns={0: 'RT_round', 1: 'Dynamic_range'}).sort_values('RT_round')
    fig = px.line(df_dyn_range,
                  x='RT_round',
                  y='Dynamic_range',
                  title='Dynamic range for all fractions',
                  width=1000,
                  height=1000)
    fig.show()
    fig.write_image(str_save + r'\Dyn_r_all_frac.png')
    fig.write_image(str_save + r'\Dyn_r_all_frac.pdf')

    # dynamic range per fraction RT
    a = 0
    df_max_summarize = {}
    df_max = df.copy()
    for j in np.array(df_max['Fraction'].unique()):
        df_intro_rt = df_max[df_max['Fraction'] == j]
        for i in np.array(df_intro_rt['RT_round'].unique()):
            df_max_summarize[a] = [i, j, df_intro_rt[df_intro_rt['RT_round'] == i]['Log_intensity'].max(),
                                   df_intro_rt[df_intro_rt['RT_round'] == i]['Log_intensity'].min()]
            a += 1
    df_max_summarize = pd.DataFrame(df_max_summarize).transpose().rename(
        columns={0: 'RT_round', 1: 'Fraction', 2: 'Max', 3: "Min"}).sort_values(['Fraction', 'RT_round'])
    df_max_summarize['Dynamic_range'] = df_max_summarize['Max'] - df_max_summarize['Min']
    fig = px.line(df_max_summarize,
                  x='RT_round',
                  y='Dynamic_range',
                  color='Fraction',
                  title='Dynamic range for different fractions',
                  width=1000,
                  height=1000)
    fig.show()
    fig.write_image(str_save + r'\Dyn_r_each_frac.png')
    fig.write_image(str_save + r'\Dyn_r_each_frac.pdf')

    # dynamic range for all fractions m/z
    a = 0
    df_dyn_range = {}
    for i in np.array(df['m/z'].unique()):
        df_dyn_range[a] = [i, df[df['m/z'] == i]['Log_intensity'].max() - df[df['m/z'] == i]['Log_intensity'].min()]
        a += 1
    df_dyn_range = pd.DataFrame(df_dyn_range).transpose().rename(columns={0: 'm/z', 1: 'Dynamic_range'}).sort_values(
        'm/z')
    fig = px.line(df_dyn_range, x='m/z', y='Dynamic_range', title='Dynamic range for all fractions', width=1000,
                  height=1000)
    fig.show()
    fig.write_image(str_save + r'\Dyn_r_all_frac_mz.png')
    fig.write_image(str_save + r'\Dyn_r_all_frac_mz.pdf')

    # Ranked log_intensity
    fig = px.scatter(df, x='Rank', y='Log_intensity', title='Ranked log2 of intensity', width=1000, height=1000)
    fig.show()
    fig.write_image(str_save + r'\ranked_log10_int.png')
    fig.write_image(str_save + r'\ranked_log10_int.pdf')

    # dynamic range per fraction m/z
    a = 0
    df_max_summarize = {}
    df_max = df.copy()
    for j in np.array(df_max['Fraction'].unique()):
        df_intro = df_max[df_max['Fraction'] == j]
        print(j)
        for i in np.array(df_intro['m/z'].unique()):
            df_max_summarize[a] = [i, j, df_intro[df_intro['m/z'] == i]['Log_intensity'].max(),
                                   df_intro[df_intro['m/z'] == i]['Log_intensity'].min()]
            a += 1
    df_max_summarize = pd.DataFrame(df_max_summarize).transpose().rename(
        columns={0: 'm/z', 1: 'Fraction', 2: 'Max', 3: "Min"}).sort_values(['Fraction', 'm/z'])
    df_max_summarize['Dynamic_range'] = df_max_summarize['Max'] - df_max_summarize['Min']
    print(df_max_summarize)
    fig = px.line(df_max_summarize, x='m/z', y='Dynamic_range', color='Fraction',
                  title='Dynamic range for different fractions', width=1000, height=1000)
    fig.show()
    fig.write_image(str_save + r'\Dyn_r_each_frac_mz.png')
    fig.write_image(str_save + r'\Dyn_r_each_frac_mz.pdf')