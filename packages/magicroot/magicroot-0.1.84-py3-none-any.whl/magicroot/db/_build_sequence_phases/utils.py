from ...attach import attachment
from ..utils import TableAttachmentProtocol, TableImplementationError
from .. import df
import pandas as pd
from matplotlib.patches import Patch
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
from datetime import timedelta
from ...errors import TableFormmatingValueError
import matplotlib.colors as mcolors


class Format:

    @staticmethod
    def table(table, format_dic):
        for ty, cols in format_dic.items():
            if ty == float:
                table = Format().as_float(table, cols)
            if ty == int:
                table = Format().as_int(table, cols, errors='ignore')
            if ty == str:
                table = Format().as_string(table, cols)
            if isinstance(ty, int):
                table = Format().as_code(table, cols, ty)
            if isinstance(ty, str):
                table = Format().as_date(table, cols, ty, errors='coerce')
            if isinstance(ty, tuple):
                for strg in ty:
                    table = Format().as_date(table, cols, strg, errors='coerce')

        return table

    @staticmethod
    def with_func(df, columns, func):
        """
        Tranforms the given columns based on the given function
        :param df: Table to be transformed
        :param columns: columns to be transformed
        :param func: function that receives the dataframe and the name of the column to be formated
        :return:
        """
        columns = columns if columns is not None else df.columns
        for column in columns:
            if column in df.columns:
                try:
                    df = df.assign(**{column: func(df, column)})
                except ValueError as e:
                    raise TableFormmatingValueError(f'Column: {column} could not be formatted')
        # return df.assign(**{column: lambda x: func(x, column) for column in columns if column in df.columns})
        return df

    @staticmethod
    def as_date(df, columns=None, format=None, *args, **kwargs):
        """
        Tranforms the given columns into european dates in the given table
        :param df: Table to be transformed
        :param columns: columns to be transformed
        :return:
        """
        if format == 'excel':
            return Format()._from_excel_date(df, columns, *args, **kwargs)
        return Format()._as_date(df, columns, format=format, *args, **kwargs)

    @staticmethod
    def _from_excel_date(df, columns=None, *args, **kwargs):
        """
        Formats from an excel date (which is really a number of days since the origin day)
        :param df:
        :param columns:
        :param args:
        :param kwargs:
        :return:
        """
        return Format().with_func(
            df, columns, lambda x, column: pd.to_datetime(
                df[column], *args, unit='d', origin=Format()._excel_origin, **kwargs
            )
        )

    _excel_origin = pd.to_datetime('1899-12-30', format='%Y-%m-%d')

    @staticmethod
    def _as_date(df, columns=None, *args, **kwargs):
        """
        Tranforms the given columns into european dates in the given table
        :param df: Table to be transformed
        :param columns: columns to be transformed
        :return:
        """
        return Format().with_func(df, columns, lambda x, column: pd.to_datetime(df[column], *args, **kwargs))

    @staticmethod
    def as_date_excel(df, columns=None, *args, **kwargs):
        """
        Tranforms the given columns into european dates in the given table
        :param df: Table to be transformed
        :param columns: columns to be transformed
        :return:
        """
        return Format().with_func(df, columns, lambda x, column: (x[column] - Format()._excel_origin).dt.days.astype(float))

    @staticmethod
    def as_code(df, columns, lenght, fillna='0', fillchar='0', side='left'):
        """
        Tranforms the given columns into set lenght codes (ex. '001')
        :param df: Table to be transformed
        :param columns: dict
        columns to be transformed as keys, lenght of expected results as values
        :param lenght: columns to be transformed
        :return:
        """
        columns = columns if isinstance(columns, list) else [columns]
        return Format().with_func(
            df, columns,
            lambda x, col: x[col].astype(float).fillna(fillna).astype(int).abs().astype(str).str.pad(
                width=lenght, fillchar=fillchar, side=side
            )
        )

    @staticmethod
    def as_float(df, columns=None, errors='coerce', fill=0.0):
        """
        Tranforms the given columns into floats
        :param df: Table to be transformed
        :param columns: dict
        columns to be transformed as keys, lenght of expected results as values
        :param lenght: columns to be transformed
        :return:
        """
        return Format().with_func(df, columns, lambda x, column: pd.to_numeric(x[column], errors=errors).fillna(fill))

    @staticmethod
    def as_int(df, columns=None, *args, **kwargs):
        """
        Tranforms the given columns into integers
        :param df:
        :param columns:
        :param args:
        :param kwargs:
        :return:
        """
        return Format().with_func(df, columns, lambda x, column: df[column].astype(float).fillna(0).astype(int, *args, **kwargs))

    @staticmethod
    def as_string(df, columns=None):
        """
        Tranforms the given columns into strings
        :param df: Table to be transformed
        :param columns: dict
        columns to be transformed as keys, lenght of expected results as values
        :param lenght: columns to be transformed
        :return:
        """
        return Format().with_func(df, columns, lambda x, column: df[column].astype(str))


class Plot:
    def gantt(
            self, df, legend, title='', background='#53565A',
            start_dt_col='Start', end_dt_col='End', color_by='Department', tasks='Task',
            sort_by=None
    ):
        font_color = '#000000'
        rail_color = '#D0D0CE'

        df = df[
            df[[tasks, color_by, start_dt_col, end_dt_col]].notnull().all(axis=1) &
            ((df[end_dt_col] - df[start_dt_col]).dt.days > 0)
        ].groupby(
            [tasks, color_by]).agg({start_dt_col: 'min', end_dt_col: 'max'}).reset_index()

        # updates legend to only include given color bys
        df['color'] = df[color_by].replace(legend)

        # project start date
        proj_start = np.minimum(df[start_dt_col].min(), pd.to_datetime(dt.datetime.today()) - pd.to_timedelta(3, 'D'))

        # number of days from project start to task start
        today_day = (pd.to_datetime(dt.datetime.today()) - proj_start).days

        df['gantt_dep_start'] = mr.df.group.min([start_dt_col], [tasks])(df)
        df['gantt_dep_end'] = mr.df.group.max([end_dt_col], [tasks])(df)

        df['gantt_rail_start'] = (df['gantt_dep_start'] - proj_start).dt.days
        df['gantt_rail_end'] = (df['gantt_dep_end'] - proj_start).dt.days
        df['gantt_rail_width'] = np.maximum(df['gantt_rail_end'] - df['gantt_rail_start'], 0)

        df['gantt_past_start'] = (df[start_dt_col] - proj_start).dt.days
        df['gantt_fut_end'] = (df[end_dt_col] - proj_start).dt.days

        df['gantt_fut_start'] = np.maximum(today_day, df['gantt_past_start'])
        df['gantt_past_end'] = np.minimum(today_day, df['gantt_fut_end'])

        df['gantt_past_width'] = np.maximum(df['gantt_past_end'] - df['gantt_past_start'], 0)
        df['gantt_fut_width'] = np.maximum(df['gantt_fut_end'] - df['gantt_fut_start'], 0)

        fig, ax = plt.subplots(2, 1, figsize=(16, 6), facecolor=background)
        # fig = fig[0]
        ax = ax[0]

        # TICKS
        xticks_labels = pd.date_range(proj_start, end=df[end_dt_col].max() + pd.to_timedelta(7, 'D'), freq='W').strftime(
            "%d %b")
        xticks = np.arange(0, len(xticks_labels)) * 7

        def mondays(start_dt, end_dt):  # January 1st
            d = start_dt + timedelta(days=6 - start_dt.weekday())  # First Sunday
            d += timedelta(days=1)  # make it monday
            while d < end_dt:
                yield d
                d += timedelta(days=7)

        xticks_labels = [d.strftime("%d %b") for d in mondays(proj_start, df[end_dt_col].max() + pd.to_timedelta(7, 'D'))]
        xticks = [(d - proj_start).days for d in mondays(proj_start, df[end_dt_col].max() + pd.to_timedelta(7, 'D'))]

        ax.set_xticks(xticks)
        ax.set_xticklabels(xticks_labels, color=font_color)
        ax.grid(True, which='major', axis='x', color=font_color, ls="--", lw=0.1)
        plt.minorticks_on()
        ax.set_xticks([(x - proj_start).days for x in pd.date_range(proj_start, df[end_dt_col].max() + pd.to_timedelta(7, 'D'))], minor=True)
        ax.grid(True, which='minor', axis='x', color=font_color, ls='--', lw=0.05)
        ax.set_axisbelow(True)

        ax.tick_params(axis='y', colors=font_color)

        plt.axvline(x=today_day, color='red', label='axvline - full height', lw=0.5)

        # leave_day = (pd.to_datetime('30-06-2023', format='%d-%m-%Y') - proj_start).days
        # plt.axvline(x=leave_day, color=Colors().green, label='axvline - full height', lw=0.5)

        if sort_by:
            df = df.sort_values(sort_by)

        deps = [dep for dep in legend.keys() if dep in df[color_by].drop_duplicates().to_list()]
        locs = {t: len(deps) - i - 1 for i, t in enumerate(deps)}
        leng = 0.8/len(locs.keys())
        df['Depar_Locs'] = df[color_by].replace(locs) * leng - 0.4

        df_locs = df[tasks].drop_duplicates().sort_values()
        locs = {t: len(df_locs) - i for i, t in enumerate(df_locs)}
        df['Task_Locs'] = df[tasks].replace(locs)

        ticks_labels = list(locs.keys())
        ticks = list(locs.values())

        ax.set_yticks(ticks)
        ax.set_yticklabels(ticks_labels, color=font_color)

        df['Locs'] = df['Task_Locs'] + df['Depar_Locs']

        # bars
        # ax.barh(df.Task, df.gantt_rail_width, left=df.gantt_rail_start, color='grey', alpha=0.5, hatch='//')
        ax.barh(df['Task_Locs'], df.gantt_rail_width, left=df.gantt_rail_start, color=rail_color, alpha=0.5)

        for dep in legend.keys():
            df_dep = df[df[color_by] == dep]
            # loc = [i for i, _ in enumerate(df_dep.Task)]
            ax.barh(y=df_dep['Locs'], width=df_dep.gantt_past_width, left=df_dep.gantt_past_start, color=df_dep.color, height=leng, align='edge', alpha=0.6)
            ax.barh(y=df_dep['Locs'], width=df_dep.gantt_fut_width, left=df_dep.gantt_fut_start, color=df_dep.color, height=leng, align='edge')

        # ax.set_title(title, color='white', family='Arial')
        ax.set_yticks(list(locs.values()), list(locs.keys()))

        # LEGENDS
        c_dict = legend

        legend_elements = [Patch(facecolor=c_dict[i], label=i) for i in c_dict if i in df[color_by].to_list()]

        # Shrink current axis's height by 10% on the bottom
        # box = ax.get_position()
        # ax.set_position([box.x0, box.y0 + box.height * 0.1,
        #                  box.width, box.height * 0.9])

        # Put a legend below current axis
        print(mcolors.BASE_COLORS)
        legend = ax.legend(
            handles=legend_elements, loc='lower right', bbox_to_anchor=(1.0, 1.01), fancybox=False, shadow=False,
            ncol=len(legend_elements), labelcolor=font_color, fontsize=6
        )
        # legend = ax.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(0.5, -0.05),
        #                    fancybox=False, shadow=False, ncol=len(legend_elements), labelcolor=font_color)
        frame = legend.get_frame()
        frame.set_color(background)

        # Setting the background color of the plot
        ax.set_facecolor(background)
        plt.text(
            0.0, -0.1, 'Copyright © 2023', horizontalalignment='left',
            verticalalignment='center', transform=ax.transAxes, fontsize=8, fontfamily='Calibri'
        )
        plt.text(
            1.0, -0.1, 'Project' + '    ' + '4', horizontalalignment='right',
            verticalalignment='center', transform=ax.transAxes, fontsize=8, fontfamily='Calibri'
        )
        plt.text(
            0.0, 1.1, 'Ponto de Situação', horizontalalignment='left',
            verticalalignment='center', transform=ax.transAxes, fontsize=21, fontfamily='Calibri'
        )
        plt.text(
            0.0, 1.0, title, horizontalalignment='left',
            verticalalignment='bottom', transform=ax.transAxes, fontsize=18, fontfamily='Calibri',
            color='#575757'
        )
        return fig



class Colors:
    red = '#E64646'

    orange = '#E69646'
    orange_dark = '#B74919'

    yellow_functional = '#FFCD00'

    green = '#86BC25'
    green_accessible = '#26890D'

    black = '#000000'

    teal = '#34D0C3'
    blue = '#3475D0'
    blue_night = '#36454F'

    gray_cool = '#53565A'

    white = '#FFFFFF'

    purple_deep = '#3C1361'
    purple = '#663A82'


@attachment
class Utils(TableAttachmentProtocol):

    @staticmethod
    def sort_custom(df, column, order, sufix='SortAuxCol', *args, **kwargs):
        df[column + sufix] = df[column].replace({val: i for i, val in enumerate(order)})
        return df.sort_values(column + sufix, *args, **kwargs).drop(columns=[column + sufix])

    def rename_columns_inputs(self, inputs, rename_dic):
        self._rename_msg(rename_dic)
        for arg_name, table in inputs.items():
            inputs[arg_name] = mr.cp.rename_cols(self.rename_columns, table)
        return inputs

    def _rename_msg(self, rename_dic):
        if len(rename_dic) > 0:
            msg = f'\t\tRenaming columns: '
            for key, value in rename_dic.items():
                msg += f'\n\t\t\t{value} -> \'{key}\''
            self._instance.log.debug(msg)
            print(msg)

    format = Format()
    colors = Colors()
    plot = Plot()







