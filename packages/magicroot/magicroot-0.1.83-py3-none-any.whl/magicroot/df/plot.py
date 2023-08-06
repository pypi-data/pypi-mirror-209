
# from .. import df
import pandas as pd
import Modelo_de_Dados_Lusitania.src.modelo_de_dados.base._modules.magicroot as mr
from matplotlib.patches import Patch
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
from datetime import timedelta
import matplotlib.colors as mcolors
from .dt import mondays, specific_weekday, portugal_holidays


def set_x_ticks_based_on_mondays(on, from_dt, to_dt, font_color, visible_lables=True):

    xticks_labels = [d.strftime("%d %b") for d in mondays(from_dt, to_dt)]
    xticks = [(d - from_dt).days for d in mondays(from_dt, to_dt)]

    on.set_xticks(xticks)
    on.set_xticklabels(xticks_labels, color=font_color)
    on.grid(True, which='major', axis='x', color=font_color, ls="--", lw=0.1)
    plt.minorticks_on()
    on.set_xticks(
        [(x - from_dt).days for x in pd.date_range(from_dt, to_dt)],
        minor=True)
    on.grid(True, which='minor', axis='x', color=font_color, ls='--', lw=0.05)
    on.set_axisbelow(True)


def gantt(
        legend, title='', background='#53565A',
        start_dt_col='Start', end_dt='End', color_by='Department', tasks='Task',
        sort_by=None, group_by=None, page=1
):
    font_color = '#000000'
    rail_color = '#D0D0CE'
    df = pd.DataFrame({
        'start_dt': start_dt_col,
        'end_dt': end_dt,
        'color_by': color_by,
        'y_label_by': tasks,
        'sort_by': sort_by
    })
    df['group_by'] = group_by if group_by is not None else 1
    df['sort_by'] = sort_by if sort_by is not None else df['y_label_by']
    df['start_dt'] = df['start_dt'].fillna(df['start_dt'].min())
    df['color_by'] = df['color_by'].fillna(df['color_by'].min())
    df['end_dt'] = df['end_dt'].fillna(df['end_dt'].max())
    df['end_dt'] = df['end_dt'].where(df['end_dt'] > df['start_dt'], df['start_dt'] + timedelta(days=1))
    today_dt = dt.datetime.today()
    print(today_dt)
    print(type(today_dt))
    # updates legend to only include given color bys
    df['color'] = df['color_by'].replace(legend)

    df = df[df['y_label_by'].notnull()].groupby([
        'group_by', 'y_label_by', 'color_by', 'color', 'sort_by'
    ]).agg({'start_dt': 'min', 'end_dt': 'max'}).reset_index()

    # Compute grid borders
    start_grid = min(df['start_dt'].min(), today_dt) - pd.to_timedelta(3, 'D')
    end_grid = max(df['end_dt'].max(), today_dt) + pd.to_timedelta(7, 'D')

    # Turn dates into days
    today_day = (today_dt - start_grid).days
    df['start_day'] = (df['start_dt'] - start_grid).dt.days
    df['end_day'] = (df['end_dt'] - start_grid).dt.days
    df['width'] = np.maximum(df['end_day'] + 1 - df['start_day'], 0)

    n_groups = len(df['group_by'].drop_duplicates())
    groups = df['group_by'].drop_duplicates().to_list()

    fig, axs = plt.subplots(n_groups, 1, figsize=(16, 6), facecolor=background, sharex='all')
    plt.subplots_adjust(wspace=0.05, hspace=0.05)
    # fig = fig[0]
    df_ori = df

    if n_groups == 1:
        axs = [axs]

    for i, ax in enumerate(axs):
        print(i)
        df = df_ori[df_ori['group_by'] == groups[i]].reset_index(drop=True).copy()

        group_name = plt.text(
            -0.02, 0.5, groups[i], horizontalalignment='left', rotation=90,
            verticalalignment='center', transform=ax.transAxes, fontsize=12, fontfamily='Calibri',
            fontweight='light'
        )

        df['start_rail_day'] = mr.df.group.min(['start_day'], ['y_label_by'])(df)
        df['end_rail_day'] = mr.df.group.max(['end_day'], ['y_label_by'])(df)
        df['width_rail'] = np.maximum(df['end_rail_day'] + 1 - df['start_rail_day'], 0)

        # df['gantt_fut_start'] = np.maximum(df['today_day'], df['start_day'])
        # df['gantt_past_end'] = np.minimum(df['today_day'], df['end_day'])

        # df['width_start_to_today'] = df['today_day'] - df['start_day']
        # df['width_today_to_end'] = df['end_day'] - df['today_day']

        if sort_by is not None:
            df = df.sort_values('sort_by')

        deps = [dep for dep in legend.keys() if dep in df['color_by'].drop_duplicates().to_list()]
        locs = {t: len(deps) - i - 1 for i, t in enumerate(deps)}
        leng = 0.8 / len(locs.keys())
        df['color_by_locs'] = df['color_by'].replace(locs) * leng - 0.4

        df_locs = df['y_label_by'].drop_duplicates().sort_values()
        locs = {t: len(df_locs) - i for i, t in enumerate(df_locs)}
        df['y_label_by_locs'] = df['y_label_by'].replace(locs)

        ticks_labels = list(locs.keys())
        ticks = list(locs.values())

        df['locs'] = df['y_label_by_locs'] + df['color_by_locs']

        # X TICKS
        set_x_ticks_based_on_mondays(on=ax, from_dt=start_grid, to_dt=end_grid, font_color=font_color)
        ax.set_yticks(ticks)
        ax.set_yticklabels(ticks_labels, color=font_color)
        # ??
        ax.tick_params(axis='y', colors=font_color, right=True, left=False, labelright=True, labelleft=False)

        # rails
        df_rails = df.groupby('y_label_by_locs').agg({'width_rail': 'max', 'start_rail_day': 'min'}).reset_index()
        ax.barh(df_rails['y_label_by_locs'], df_rails['width_rail'], left=df_rails['start_rail_day'], color=rail_color, alpha=0.5)

        for color_by in legend.keys():
            df_dep = df[df['color_by'] == color_by]
            # loc = [i for i, _ in enumerate(df_dep.Task)]
            # ax.barh(y=df_dep['locs'], width=df_dep['width_start_to_today'], left=df_dep['start_day'], color=df_dep.color, height=leng, align='edge', alpha=0.6)
            # ax.barh(y=df_dep['locs'], width=df_dep['width_today_to_end'], left=today_day, color=df_dep.color, height=leng, align='edge')
            ax.barh(y=df_dep['locs'], width=df_dep['width'], left=df_dep['start_day'], color=df_dep.color, height=leng, align='edge')

        # ax.set_title(title, color='white', family='Arial')
        ax.set_yticks(list(locs.values()), list(locs.keys()))
        ax.set_facecolor(background)

        # Today Line
        ax.axvline(x=today_day + 0.5, color='red', label='axvline - full height', lw=0.5)

        # weekends
        print('--------------------')
        print(ax.viewLim)
        lim = ax.viewLim
        ax.bar(
            [(d - start_grid).days for d in specific_weekday(7, start_grid, end_grid)] +
            [(d - start_grid).days for d in specific_weekday(1, start_grid, end_grid)] +
            [(d[0] - start_grid).days for d in portugal_holidays(start_grid, end_grid)],
            lim.y1 + 1, width=1, color=rail_color, align='edge', zorder=0, alpha=0.2)
        ax.set_ylim([lim.y0, lim.y1])
        ax.set_xlim([lim.x0, lim.x1])

    # LEGENDS
    c_dict = legend
    legend_elements = [Patch(facecolor=c_dict[i], label=i) for i in c_dict if i in df['color_by'].to_list()]

    # Put a legend below current axis
    legend = axs[0].legend(
        handles=legend_elements, loc='lower right', bbox_to_anchor=(1.0, 1.01), fancybox=False, shadow=False,
        ncol=len(legend_elements), labelcolor=font_color, fontsize=6
    )
    frame = legend.get_frame()
    frame.set_color(background)

    # Setting the background color of the plot
    r = fig.canvas.get_renderer()
    bb = group_name.get_window_extent(renderer=r)
    width = bb.width
    height = bb.height
    pos = axs[0].get_position()

    print(f'{width=}')
    print(f'{height=}')
    fig.text(
        0.0 + pos.x0 - 0.02, 0.0, 'Deloitte Risk Advisory S.A. © 2023', horizontalalignment='left',
        verticalalignment='center', fontsize=8, fontfamily='Calibri'
    )
    fig.text(
        1.0, 0.0, 'Lusitania | IFRS 17 | Plano de Projeto' + '    ' + str(page), horizontalalignment='right',
        verticalalignment='center', fontsize=8, fontfamily='Calibri'
    )

    fig.text(
        0.0 + pos.x0 - 0.02, 1.0, 'Ponto de Situação', horizontalalignment='left',
        verticalalignment='center', fontsize=21, fontfamily='Calibri'
    )
    fig.text(
        0.0 + pos.x0 - 0.02, 0.95, title, horizontalalignment='left',
        verticalalignment='center', fontsize=18, fontfamily='Calibri',
        color='#575757'
    )

    return fig


class Colors:
    red = '#E64646'

    orange = '#E69646'
    orange_dark = '#B74919'

    yellow_functional = '#FFCD00'

    green_dtt = '#86BC25'
    green_accessible = '#26890D'

    black = '#000000'

    teal = '#34D0C3'
    blue = '#3475D0'
    blue_night = '#36454F'

    gray_cool = '#53565A'

    white = '#FFFFFF'

    purple_deep = '#3C1361'
    purple = '#663A82'






