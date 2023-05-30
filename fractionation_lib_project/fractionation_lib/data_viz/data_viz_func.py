def data_viz_func(
        str_data='',
        str_type='',
        str_save=''
):
    """ data_viz_func provides plots from the formatted data. It requires data_formate and other functions for the data
    formatting. data_viz get three links: link to get primary data, link to get type of the plot and link to save data.
    ALL THREE LINKS ARE CRITICAL FOR FUNCTION'S WORKFLOW. REQUIRES EVIDENCE FILE (SPECTRONAUT).
    Default: saves all created plots to the created directory Plots_date_xxxxxx_time_xxxxxx in the same directory,
    where the jupyter notebook placed.

    Requires:
    data_formate
    plotly.express as px
    os
    from datetime import datetime
    numpy as np
    pandas as pd

    Parameters
    ----------
    str_data: link to get the primary data. str_data = r'link_to_data'
    str_type: string to get the type of the plot. str_type='heatmap' to get heatmap plots, str_type='overlap'
            to get overlap plots, str_type='summarize' to get summarize plot, str_type='all' to get all types of plots
    str_save: link to save image. str_save = r'link_to_save'
    Returns
    -------
    :  plots

    """
    today = datetime.today()
    today = today.strftime("date_%d%m%Y_time_%H%M%S")
    #    if str_data[0]!='r' or str_save[0]!='r':
    #        raise ValueError('Please, get the path to the primary file in proper formate (r*full_path*) and try again')

    # troubleshooting
    if str_data == '':
        raise ValueError('Please, get the path to the primary file properly and try again')
    if str_type == '':
        str_type = 'all'
    if str_save == '':
        os.mkdir('Plots_' + str(today))
        str_save = r'Plots_' + str(today)
    # choosing the plot type and creating the folder
    project_name = input(r'Enter the project name as _Project_name, please')
    if str_type == 'heatmap':
        long_link_save = str_save + r'\heatmap' + r'_plots_' + str(today) + '''project_name'''
        os.mkdir(os.path.join(long_link_save))
        data_viz_heatmap(data_format_func(str_data), long_link_save)
    if str_type == 'overlap':
        long_link_save = str_save + r'\overlap' + r'_plots_' + str(today) + project_name
        os.mkdir(os.path.join(long_link_save))
        data_viz_overlap(data_format_func(str_data), long_link_save)
    if str_type == 'summarize':
        long_link_save = str_save + r'\summarize' + r'_plots_' + str(today) + project_name
        os.mkdir(os.path.join(long_link_save))
        data_viz_summarise(data_format_func(str_data), long_link_save)
    if str_type == 'upset':
        long_link_save = str_save + r'\upset' + r'_plots_' + str(today) + project_name
        os.mkdir(os.path.join(long_link_save))
        data_viz_heatmap(data_format_func(str_data), long_link_save)
    if str_type == 'all':
        long_link_save = str_save + r'\all' + r'_plots_' + str(today) + project_name
        os.mkdir(os.path.join(long_link_save))
        data_viz_heatmap(data_format_func(str_data), long_link_save)
        data_viz_overlap(data_format_func(str_data), long_link_save)
        data_viz_upset(data_format_func(str_data), long_link_save)
        data_viz_summarise(data_format_func(str_data), long_link_save)
    if str_type == 'all_but_upset':
        long_link_save = str_save + r'\all' + r'_plots_' + str(today) + project_name
        os.mkdir(os.path.join(long_link_save))
        data_viz_heatmap(data_format_func(str_data), long_link_save)
        data_viz_overlap(data_format_func(str_data), long_link_save)
        data_viz_summarise(data_format_func(str_data), long_link_save)
    if str_type != 'heatmap' and str_type != 'overlap' and str_type != 'summarize' and str_type != 'upset' \
            and str_type != 'all_but_upset' and str_type != 'all':
        raise ValueError('that is a wrong plot type!\n try another one')
