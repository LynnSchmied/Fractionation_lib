def data_viz_overlap(
        df,
        str_save: str
):
    """ data_viz_overlap creates the bunch of plots from the df. Returns two plots: barplot of Number of unique
    identified proteins/precursors in fractions, boxplot of Unique identified precursors per fraction

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

    # number of unique proteins/precursors in fractions
    a = 0
    df_overlap = {}
    df_max = df

    for i in np.array(df_max['Fraction'].unique()):
        df_overlap[a] = [i, df_max.loc[df_max.Fraction == i]['Precursor'].nunique(),
                         df_max.loc[df_max.Fraction == i]['Proteins'].nunique()]
        a += 1
    df_overlap[a] = ['Summary', df_max['Precursor'].nunique(), df_max['Proteins'].nunique()]
    df_overlap = pd.DataFrame(df_overlap).transpose().rename(
        columns={0: 'Fraction', 1: 'Precursor', 2: 'Proteins'}).melt('Fraction').rename(
        columns={'variable': 'Prot_Prec', 'value': 'Number'}).sort_values('Fraction')
    fig = px.bar(df_overlap,
                 y='Number',
                 x='Fraction',
                 color='Prot_Prec',
                 barmode='group',
                 title='Unique identified proteins and precursors',
                 width=1000,
                 height=1000)
    fig.show()
    fig.write_image(str_save + r'\Un_prot_frac_bar.png')
    fig.write_image(str_save + r'\Un_prot_frac_bar.pdf')

    # Unique identified precursors
    df_max = df[['Fraction', 'Precursor', 'Log_intensity']].sort_values('Fraction')
    fig = px.box(df_max,
                 y='Log_intensity',
                 x='Fraction',
                 title='Unique identified precursors',
                 width=1000,
                 height=1000)
    fig.show()
    fig.write_image(str_save + r'\Un_prot_frac_box.png')
    fig.write_image(str_save + r'\Un_prot_frac_box.pdf')