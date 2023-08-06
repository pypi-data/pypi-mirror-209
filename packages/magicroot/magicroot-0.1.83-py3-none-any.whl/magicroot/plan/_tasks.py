import pandas as pd
import numpy as np
from ..db import CompleteTable
import datetime
import traceback
from ..df import plot as plt

# import matplotlib.pyplot as plt


# folder_mang = mr.os.home['Lus\\IFRS17\\Reunioes\\1. Ponto de Situacao\\00. Suporte']
# folder_mang = mr.os.home['Desktop']

# print(folder_mang)


class ProjectTasks(CompleteTable):
    """
    Status:
        O - Open
        C - Closed
        L - Late
        T - for today
    """
    today_str = str(datetime.datetime.today()).split(' ')[0].replace('-', '')
    today = pd.to_datetime(str(datetime.datetime.today()).split(' ')[0])
    default_extension = '.xlsx'
    xlsx_ori_dt = pd.to_datetime('1899-12-30', format='%Y-%m-%d')

    @property
    def table_inputs(self):
        return {
            # 'tasks': {'file_name': self.release_name, 'encoding_errors': 'ignore'},
            'tasks': {'file_name': self.release_name, 'sheet_name': 'Tasks'},
            'deli': {'file_name': self.release_name, 'sheet_name': 'Deliverbles'}
        }

    @staticmethod
    def dt_col(df):
        return [col for col in df.columns if col.str[-3:] == '_dt']

    f = {
        str: ['Deliverble', 'Componente do Projeto'],
        float: ['Id Del'],
        'excel_dt': ['Aux_Ref_dt', 'Aux_Prev_End_dt', 'Begin_dt', 'End_dt', 'End_Base_dt', 'R1']
    }

    # def format_input(self, df):
    #
    #     df = self.utils.format.as_string(df, ['Deliverble', 'Componente do Projeto'])
    #     df = self.utils.format.as_float(df, ['Id Del'])
    #
    #     for col in ['Aux_Ref_dt', 'Aux_Prev_End_dt', 'Begin_dt', 'End_dt', 'End_Base_dt', 'R1']:
    #         try:
    #             df = self.utils.format.as_date(df, [col], format='excel')
    #             print('formatted as excel')
    #         except ValueError:
    #             pass
    #         try:
    #             df = self.utils.format.as_date(df, [col], format='%Y-%m-%d')
    #         except ValueError:
    #             pass
    #         try:
    #             df = self.utils.format.as_date(df, [col], format='%d-%m-%Y')
    #         except ValueError:
    #             pass
    #
    #     return df

    def _update_tasks(self, tasks, clear_effort=False, *args, **kwargs):
        if clear_effort:
            tasks['TEffort'] = tasks['TEffort'].fillna(0) + tasks['Effort'].fillna(0)
            tasks['Effort'] = np.nan

        tasks['Status'] = tasks['Status'].fillna('O')
        tasks['End_Base_dt'] = tasks['End_Base_dt'].fillna(tasks['End_dt'])
        tasks['Aux_Status'] = tasks['Status'].replace({'L': 1, 'O': 2, 'S': 3, 'C': 4})
        tasks['Begin_dt'] = tasks['Begin_dt'].fillna(pd.to_datetime(self.today))
        tasks.loc[(tasks['Status'] == 'O') & (self.today > tasks['End_dt']), 'Status'] = 'L'
        tasks.loc[(tasks['Status'] == 'L') & (self.today <= tasks['End_dt']), 'Status'] = 'O'

        tasks['Aux_Prev_End_dt'] = tasks['Aux_Ref_dt'] + pd.to_timedelta(tasks['Day'], 'D') + pd.to_timedelta(tasks['Week'], 'w')

        tasks['Team'] = tasks['Team'].fillna('TBD')
        tasks['Member'] = tasks['Member'].fillna('-')
        # compute days

        tasks['Day'] = (tasks['End_dt'] - tasks['Aux_Ref_dt']).dt.days.fillna(0).abs()
        tasks['Week'] = (tasks['Day'] / 7).astype(int)
        tasks['Day'] = tasks['Day'].astype(int) % 7
        tasks.loc[tasks['Status'] == 'L', ['Day', 'Week']] *= -1

        # print(tasks)

        # update day
        tasks['Aux_Ref_dt'] = pd.to_datetime(self.today)

        # tasks['Status'] = tasks['Status'].fillna('O')

        # sort
        tasks = tasks.sort_values(['Aux_Status'] + [col for col in tasks.columns if col[:1] == 'L'])
        # return tasks.merge(deli, how='outer')

        rep_r1 = tasks.loc[
            lambda x: x['R1'].notnull(), ['R1', 'L3', 'Team', 'Begin_dt', 'End_dt']
        ].assign(Tasks=lambda x: x['Begin_dt']).groupby(
            ['R1', 'L3', 'Team']).agg({'Begin_dt': 'min', 'End_dt': 'max', 'Tasks': 'count'}).reset_index().pivot(
            index=['L3', 'R1', 'Begin_dt', 'End_dt'], columns='Team', values='Tasks'
        ).reset_index()
        return tasks

    def update_graphs(self, tasks):
        # stasks = tasks[tasks['R1'].notnull()]
        # stasks.loc[tasks['L4'] == 'Motor AT', 'Department'] = 'Motor AT'
        # stasks.loc[tasks['L4'] == 'RA', 'Department'] = 'Motor RA'
        # stasks.loc[tasks['L4'] == 'WTW', 'Department'] = 'WTW'
        # stasks.loc[tasks['L8'] == 'ResQ', 'Department'] = 'ResQ'
        # stasks.loc[tasks['L5'] == 'Legacy', 'Department'] = 'Ress Legacy'
        # stasks.loc[(tasks['L3'] == '3. Motor de Calculo') | (tasks['L4'] == 'Motor de calculo'), 'Department'] = 'SAS'
        # stasks.loc[tasks['L3'] == '4. SAP', 'Department'] = 'SAP'
        # stasks.loc[:, 'Department'] = stasks['Department'].fillna('TBD')
        # stasks['Execution'] = stasks['R1'].dt.strftime('%Y %m').astype(str)
        # stasks = stasks.sort_values(['Department', 'Task'])

        # fig = self.utils.plot.gantt(
        #     stasks, start_dt_col='Begin_dt', end_dt_col='End_dt', color_by='Department', tasks='Execution',
        #     sort_by='Execution', title='Calendário de Execuções', background=self.utils.colors.gray_cool, legend={
        #         'Motor AT': self.utils.colors.orange,
        #         'Motor RA': self.utils.colors.orange_dark,
        #         'Ress Legacy': self.utils.colors.green_dtt,
        #         'WTW': self.utils.colors.purple_deep,
        #         'ResQ': self.utils.colors.purple,
        #         'SAS': self.utils.colors.blue,
        #         'SAP': self.utils.colors.teal,
        #         'TBD': self.utils.colors.white
        #     })

        # fig.savefig(self.output.path + '\\mapa_execucoes.png')
        # for stream in tasks['L3'].drop_duplicates().to_list():
        #     try:
        #         stasks = tasks[(tasks['L3'] == stream) & (tasks['Status'] != 'C')]
        #         fig = plt.gantt(
        #             stasks, start_dt_col='Begin_dt', end_dt_col='End_dt', color_by='Team', tasks='L4',
        #             sort_by='L4', title=stream,
        #             background=self.utils.colors.gray_cool,
                    # background='#FFFFFF',
                    # legend={
                    #     'DTT': self.utils.colors.green_dtt,
                    #     'LUS': self.utils.colors.orange,
                    #     'SAS': self.utils.colors.blue,
                    #     'WTW': self.utils.colors.purple_deep,
                    #     'SAP': self.utils.colors.teal,
                    #     'TBD': self.utils.colors.red,
                    # })
                # fig.savefig(self.output.path + '\\' + stream + '.png', bbox_inches='tight', dpi=600, pad_inches=0.3)
            # except Exception as e:
            #     print(f"""
            #     ------------------------------------
            #     ERROR for {stream}
            #     """)
            #     print(traceback.format_exc())
            #     print(f"""
            #        -----------------------""")

        for page, stream in enumerate(tasks['L3'].drop_duplicates().to_list()):
            try:
                stasks = tasks[(tasks['L3'] == stream) & (tasks['Status'] != 'C')]
                fig = plt.gantt(
                    start_dt_col=stasks['Begin_dt'],
                    end_dt=stasks['End_dt'],
                    color_by=stasks['Team'],
                    tasks=stasks['L5'],
                    sort_by=stasks['L5'],
                    group_by=stasks['L4'],
                    title=stream,
                    background='#FFFFFF',
                    page=page + 1,
                    legend={
                        'DTT': self.utils.colors.green_dtt,
                        'LUS': self.utils.colors.orange,
                        'SAS': self.utils.colors.blue,
                        'WTW': self.utils.colors.purple_deep,
                        'SAP': self.utils.colors.teal,
                        'TBD': self.utils.colors.red,
                    })
                fig.savefig(self.output.path + '\\' + stream + '.png', bbox_inches='tight', dpi=600, pad_inches=0.3)
            except Exception as e:
                print(f"""
                ------------------------------------
                ERROR for {stream}
                """)
                print(traceback.format_exc())
                print(f"""
                   -----------------------""")

        # stasks = tasks[(tasks['L3'] == '9. Paralelo')]
        # stasks['L4'] = stasks['R1'].dt.strftime('%Y %m').astype(str)
        # fig = self.utils.plot.gantt(
        #     stasks, start_dt_col='Begin_dt', end_dt_col='End_dt', color_by='L5', tasks='L4',
        #     sort_by='L4', title='Paralelo', background=self.utils.colors.gray_cool, legend={
        #         'SAS': self.utils.colors.blue,
        #         'WTW': self.utils.colors.purple_deep,
        #         'SAP': self.utils.colors.teal,
        #         'Motor AT': self.utils.colors.orange,
        #         'Motor RA': self.utils.colors.orange_dark,
        #     })
        # fig.savefig(self.output.path + '\\Paralelo.png')


        # plt.show()
        # raise ValueError

    def create(self, tasks, deli, clear_effort=False, update_tasks=True, update_graphs=True, *args, **kwargs):
        dic = {'Tasks': tasks, 'Deliverbles': deli}
        if update_tasks:
            dic['Tasks'] = self._update_tasks(tasks, clear_effort=False, *args, **kwargs)

        tasks = dic['Tasks']

        self.update_graphs(tasks)

        bk = self.input.new(folder='.bk')
        bk.new(
            file=self.release_name + '_' + self.today_str + '.zip', with_obj=dic['Tasks']
        )

        # for col in ['Aux_Ref_dt', 'Aux_Prev_End_dt', 'Begin_dt', 'End_dt', 'End_Base_dt', 'R1']:
        #     tasks[col] = tasks[col].dt.strftime('%Y-%m-%d')
        cols = ['Begin_dt', 'End_dt', 'End_Base_dt', 'Aux_Ref_dt', 'Aux_Prev_End_dt']
        dic['Tasks'] = self.utils.format.as_date_excel(tasks, cols)
        raise StopIteration
        return dic


# ProjectTasks().build(input=folder_mang, output=folder_mang, clear_effort=False, update_tasks=False, update_graphs=True)


class ProjectTasksSchema(CompleteTable):
    table_inputs = {
        'tasks': ProjectTasks()
    }

    def create(self, tasks, *args, **kwargs):
        return tasks[[col for col in tasks.columns if col not in ['Ref_Date', 'Prev_Fim']]]


# ProjectTasksSchema().build(input=folder_mang, output=folder_mang, release_to=folder_mang)


class ProjectTasksManagement(CompleteTable):
    table_inputs = {
        'tasks': ProjectTasks()
    }

    def create(self, tasks, *args, **kwargs):
        return tasks[[
            'Team',
            'Member',
            'Begin_dt',
            'End_dt',
            'Estado',
            'Scrum',
            'L3',
            'L4',
            'L5',
            'L6',
            'L7',
            'L8',
            'L9',
            'Obs'
        ]]


# ProjectTasksManagement().build(input=folder_mang, output=folder_mang, release_to=folder_mang)


