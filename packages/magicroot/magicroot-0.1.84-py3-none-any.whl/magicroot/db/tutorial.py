import pandas as pd

from .build_sequence import Table as CompleteTable
import inspect


class TableName(CompleteTable):
    """
    Below are the attributes (ex: i, rename_columns or f) and methods (create or validate)
        The attributes will always run in order by which they are defined below
        (changing them below has no effect on the order they run in)
    """

    name = 'some_table'

    """
    Recomended use
    """

    i = {  # i means inputs, it also allowed using table_inputs, inputs_dicionary or inputs_dictionary
        'table_input_1': 'table_name_1',
        'table_input_2': 'table_name_2',
        'table_input_3': 'table_name_3'
    }
    """
    Used to define inputs 
    
    :Allowed definitions:
       as a ordered list : list
           define \'i\' as a list in order to receive the inputs the create function by the same order 
           
           .. tip::
    
                For most tables this is the recomended way of setting the inputs.
        
       columns : list
           Columns to pull forward or backwards
       to_the_begin: Bool, default True
    
    :Returns:
       pandas.Dataframe
           'df' with the columns reordered
    """

    rename_columns = {
        'New_Name': ['Previous_name_1', 'Previous_name_2']
    }

    f = {

    }

    def create(self, table_input_1, table_input_2, table_input_3):
        return table_input_1

    def set_assumptions(self, df,  *args, **kwargs):
        return df

    # the attributes below are filled automatically (only necessary to uncomment if needed to change)
    # default_extension = '.ftr' # used to set the output format in folder output
    # release_extension = '.csv' # used to set the output format in folder release_to

    def validate(self, df):
        return df

    """
    Alternatives for speciallized applications
    """

    def load_inputs(self):  # alternative to i
        table_1 = pd.DataFrame()
        return {
            'table_input_1': table_1
        }


class SomeTable(CompleteTable):
    i = {  # i means inputs, it also allowed using table_inputs, inputs_dicionary or inputs_dictionary
        'table_input_1': 'table_name_1',
        'table_input_2': 'table_name_2',
        'table_input_3': 'table_name_3'
    }

    rename_columns = {
        'New_Name': ['Previous_name_1', 'Previous_name_2']
    }

    f = {

    }

    def create(self, table_input_1, table_input_2, table_input_3):
        return table_input_1

    def set_assumptions(self, df,  *args, **kwargs):
        return df

    def validate(self, df):
        return df


def get_table_tutorial():
    return inspect.getsource(TableName).replace('CompleteTable', 'mr.CompleteTable')


def get_table_template():
    return inspect.getsource(SomeTable).replace('CompleteTable', 'mr.CompleteTable')




