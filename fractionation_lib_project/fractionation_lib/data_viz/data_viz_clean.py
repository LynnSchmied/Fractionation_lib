def data_viz_clean(
        df,
        link: str,
        name: str
):
    """ data_viz_clean creates the plot from DataFrame of the typical formate from data_format_clean DataFrame

    Requires:
    import numpy as np
    import pandas as pd

    Parameters
    ----------
    df: pandas DataFrame
    link: str
    name: str

    Returns
    -------
    : plot
    """
    fig = px.bar(df,
             x='Sample',
             y='Proteins',
             color='Type',
             title='Number of unique proteins per sample',
             labels={'y': 'Number', 'x': 'Samples'},
             width=800,
             height=600)
    fig.show()
    fig.write_image(link + r'\_' + name + '_.png')
    fig.write_image(link + r'\_' + name + '_.pdf')