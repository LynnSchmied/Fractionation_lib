def data_viz_heatmap(
        df,
        str_save: str
):
    """ data_viz_heatmap creates the bunch of plots from the df. Returns three heatmaps: Elution time vs Fraction
    number, m/z vs Fraction number, Ion mobility vs Fraction number

    Requires:
    data_formate
    import plotly.express as px
    import numpy as np
    import pandas as pd

    Parameters
    ----------
    df: pandas dataframe
    str_save: link to save images in formate r'ful_path'
    Return
    -------
    :  plots

    """

    df_heatmap = df.copy()

    # heatmap Elution time vs Fraction number
    new_heatmap = {}
    a = 0
    # print(df_heatmap)
    for i in np.array(df_heatmap['Fraction'].unique()):
        mask = df_heatmap.loc[df_heatmap.Fraction == i]
        for j in np.array(df_heatmap['RT_round'].unique()):
            var = mask.loc[mask.RT_round == j]
            new_heatmap[a] = [i, j, var['Precursor'].count()]
            a += 1
    new_heatmap = pd.DataFrame(new_heatmap).transpose().rename(columns={0: 'Fraction', 1: 'RT_round', 2: 'number'})
    piv = pd.pivot_table(new_heatmap, values='number', index=["RT_round"], columns=['Fraction'], fill_value=0)
    # plot pivot table as heatmap using seaborn
    fig = px.imshow(
        piv,
        title='Heatmap Retention time vs Fraction number',
        color_continuous_scale='viridis',
        width=1000,
        height=1000
    )
    fig.show()
    fig.write_image(str_save + r'\heat_rt_frac.png')
    fig.write_image(str_save + r'\heat_rt_frac.pdf')

    # heatmap m/z vs Fraction number
    new_heatmap = {}
    a = 0
    # print(df_heatmap)
    df_heatmap['m_over_z'] = df_heatmap['m/z']
    for i in np.array(df_heatmap['Fraction'].unique()):
        mask = df_heatmap.loc[df_heatmap.Fraction == i]
        for j in np.array(df_heatmap['m_over_z'].unique()):
            var = mask.loc[mask.m_over_z == j]
            new_heatmap[a] = [i, j, var['Precursor'].count()]
            a += 1
    new_heatmap = pd.DataFrame(new_heatmap).transpose().rename(columns={0: 'Fraction', 1: 'm/z', 2: 'number'})
    piv = pd.pivot_table(new_heatmap, values='number', index=["m/z"], columns=['Fraction'], fill_value=0)
    # plot pivot table as heatmap using seaborn
    fig = px.imshow(
        piv,
        title='Heatmap m/z vs Fraction number',
        zmax=new_heatmap['number'].max() * 0.6,
        color_continuous_scale='viridis',
        width=1000,
        height=1000
    )
    fig.show()
    fig.write_image(str_save + r'\mz_frac.png')
    fig.write_image(str_save + r'\mz_frac.pdf')

    # heatmap Ion mobility vs Fraction number
    new_heatmap = {}
    a = 0
    # print(df_heatmap)
    for i in np.array(df_heatmap['Fraction'].unique()):
        mask = df_heatmap.loc[df_heatmap.Fraction == i]
        for j in np.array(df_heatmap['Ion_mobility'].unique()):
            var = mask.loc[mask.Ion_mobility == j]
            new_heatmap[a] = [i, j, var['Precursor'].count()]
            a += 1
    new_heatmap = pd.DataFrame(new_heatmap).transpose().rename(columns={0: 'Fraction', 1: 'Ion_mobility', 2: 'number'})
    piv = pd.pivot_table(new_heatmap, values='number', index=["Ion_mobility"], columns=['Fraction'], fill_value=0)
    # plot pivot table as heatmap using seaborn
    fig = px.imshow(
        piv,
        title='Heatmap Ion mobility vs Fraction number',
        zmax=new_heatmap['number'].max() * 0.5,
        color_continuous_scale='viridis',
        width=1000,
        height=1000
    )
    fig.show()
    fig.write_image(str_save + r'\IM_frac.png')
    fig.write_image(str_save + r'\IM_frac.pdf')