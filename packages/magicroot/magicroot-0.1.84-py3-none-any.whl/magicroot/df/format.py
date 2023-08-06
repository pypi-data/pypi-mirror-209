import pandas as pd
from .. import cls
from ..errors import TableFormmatingValueError


def all(df, format_dic):
    """
    Formats a ``pandas.Dataframe`` based on a template defined in ``format_dic``.

    :Parameters:
        df : pandas.Dataframe
            Dataframe to operate on
        format_dic : dic
            template to format df on.
        to_the_begin: Bool, default True

    :Returns:
        pandas.Dataframe
            ``df`` with the columns formatted.

    :Usages:
        Formatting with dictionary
            Let us consider a Dataframe ``df`` defined as below.

        .. code-block:: python
            :linenos:

            df = pd.DataFrame({
                'Date': ['2009-10-08', '2013-10-08', '2008-10-08', '2009-10-08'],
                'Name': ['Neil Caffrey', 'Reddigton', 'Pattrick Jane', 'Harvey Specter'],
                'n Packages': ['6', '10', '7', '9'],
                'Package Code': ['480', '40', '208', '64'],
                'Value': ['8.2', '8.0', '8.1', '8.4']
            })

        +----+------------+----------------+--------------+----------------+---------+
        |    | Date       | Name           |   n Packages |   Package Code |   Value |
        +====+============+================+==============+================+=========+
        |  0 | 2009-10-08 | Neil Caffrey   |            6 |            480 |     8.2 |
        +----+------------+----------------+--------------+----------------+---------+
        |  1 | 2013-10-08 | Reddigton      |           10 |             40 |     8   |
        +----+------------+----------------+--------------+----------------+---------+
        |  2 | 2008-10-08 | Pattrick Jane  |            7 |            208 |     8.1 |
        +----+------------+----------------+--------------+----------------+---------+
        |  3 | 2009-10-08 | Harvey Specter |            9 |             64 |     8.4 |
        +----+------------+----------------+--------------+----------------+---------+

        Check the types of the columns in ``df``.

        .. code-block:: python
            :linenos:

            print(mr.df.types.compared(df=df))

        +--------------+--------+
        |              | df     |
        +==============+========+
        | Date         | object |
        +--------------+--------+
        | Name         | object |
        +--------------+--------+
        | n Packages   | object |
        +--------------+--------+
        | Package Code | object |
        +--------------+--------+
        | Value        | object |
        +--------------+--------+


        As we can see the types of the columns in ``df`` are all wrong, ``Date`` is a ``date`` not an ``object``,
        ``n Packages`` is a ``int`` not an ``object``, ``Package Code`` is a 3 digit ``code`` not an ``object`` and
        ``Value`` is a ``float`` not an ``object``.

        We fix this by using the function above.

        .. code-block:: python
            :linenos:

            df = mr.df.format.all(df=df, format_dic={
                '%Y-%m-%d': 'Date',
                str: 'Name',
                int: 'n Packages',
                3: 'Package Code',
                float: 'Value'
            })


        +----+---------------------+----------------+--------------+----------------+---------+
        |    | Date                | Name           |   n Packages |   Package Code |   Value |
        +====+=====================+================+==============+================+=========+
        |  0 | 2009-10-08 00:00:00 | Neil Caffrey   |            6 |            480 |     8.2 |
        +----+---------------------+----------------+--------------+----------------+---------+
        |  1 | 2013-10-08 00:00:00 | Reddigton      |           10 |            040 |     8   |
        +----+---------------------+----------------+--------------+----------------+---------+
        |  2 | 2008-10-08 00:00:00 | Pattrick Jane  |            7 |            208 |     8.1 |
        +----+---------------------+----------------+--------------+----------------+---------+
        |  3 | 2009-10-08 00:00:00 | Harvey Specter |            9 |            064 |     8.4 |
        +----+---------------------+----------------+--------------+----------------+---------+

        Recheck the types of the columns in ``df``.

        +--------------+----------------+
        |              | df             |
        +==============+================+
        | Date         | datetime64[ns] |
        +--------------+----------------+
        | Name         | object         |
        +--------------+----------------+
        | n Packages   | int32          |
        +--------------+----------------+
        | Package Code | object         |
        +--------------+----------------+
        | Value        | float64        |
        +--------------+----------------+

    .. seealso::
        Related functions
            see :py:func:`magicroot.df.types.compared`.

        Used functions
            see :py:func:`magicroot.cls.to_list`.
    """
    for ty, cols in format_dic.items():
        cols = cls.to_list(cols)
        if ty == float:
            df = as_float(df, cols)
        if ty == int:
            df = as_int(df, cols, errors='ignore')
        if ty == str:
            df = as_string(df, cols)
        if isinstance(ty, int):
            df = as_code(df, cols, ty)
        if isinstance(ty, str):
            df = as_date(df, cols, ty, errors='coerce')
        if isinstance(ty, tuple):
            for strg in ty:
                df = as_date(df, cols, strg, errors='coerce')

    return df


def with_func(df, columns, func):
    """
    Tranforms the given columns based on the given function.

    :Parameters:
        df : pandas.Dataframe
            Dataframe to operate on
        columns : list
            columns to formatted (if they exist).
        func: callable
            function to use in formatting the columns

    :Returns:
        pandas.Dataframe
            ``df`` with the columns formatted.

    .. seealso::
        Related functions
            see :py:func:`magicroot.df.format.all`.

        Generalization of functions
            see :py:func:`magicroot.df.format.as_code`.

            see :py:func:`magicroot.df.format.as_date`.

            see :py:func:`magicroot.df.format.as_float`.

            see :py:func:`magicroot.df.format.as_int`.

            see :py:func:`magicroot.df.format.as_string`.

    """
    columns = columns if columns is not None else df.columns
    for column in columns:
        if column in df.columns:
            try:
                df = df.assign(**{column: func(df, column)})
            except ValueError as e:
                raise TableFormmatingValueError(f'Column: {column} could not be formatted')
    return df


_excel_origin = pd.to_datetime('1899-12-30', format='%Y-%m-%d')


def as_date(df, columns=None, format=None, *args, **kwargs):
    """
    Tranforms the given columns into dates in the given table

    :Parameters:
        df : pandas.Dataframe
            Dataframe to operate on
        columns : list
            columns to formatted (if they exist).
        format: str
            date format of the intput data, see Python `documentation <https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes>`__.



    :Returns:
        pandas.Dataframe
            ``df`` with the columns formatted.

    .. seealso::
        Related functions
            see :py:func:`magicroot.df.format.all`.

        Similar to
            see :py:func:`magicroot.df.format.as_code`.

            see :py:func:`magicroot.df.format.as_date`.

            see :py:func:`magicroot.df.format.as_float`.

            see :py:func:`magicroot.df.format.as_int`.

            see :py:func:`magicroot.df.format.as_string`.

    """
    if format == 'excel':
        return with_func(
            df, columns, lambda x, column: pd.to_datetime(
                df[column], *args, unit='d', origin=_excel_origin, **kwargs
            )
        )

    return with_func(df, columns, lambda x, column: pd.to_datetime(df[column], *args, **kwargs))


def as_code(df, columns, lenght, fillna='0', fillchar='0', side='left'):
    """
     Tranforms the given columns into codes (ex: '00023') in the given table

     :Parameters:
         df : pandas.Dataframe
             Dataframe to operate on
         columns : list
             columns to formatted (if they exist).
         lenght: int
             Number of digits in the code.


     :Returns:
         pandas.Dataframe
             ``df`` with the columns formatted.

     .. seealso::
         Related functions
             see :py:func:`magicroot.df.format.all`.

         Similar to
             see :py:func:`magicroot.df.format.as_code`.

             see :py:func:`magicroot.df.format.as_date`.

             see :py:func:`magicroot.df.format.as_float`.

             see :py:func:`magicroot.df.format.as_int`.

             see :py:func:`magicroot.df.format.as_string`.

     """
    columns = columns if isinstance(columns, list) else [columns]
    return with_func(
        df, columns,
        lambda x, col: x[col].astype(float).fillna(fillna).astype(int).abs().astype(str).str.pad(
            width=lenght, fillchar=fillchar, side=side
        )
    )


def as_float(df, columns=None, errors='coerce', fill=0.0):
    """
     Tranforms the given columns into floats in the given table

     :Parameters:
         df : pandas.Dataframe
             Dataframe to operate on
         columns : list
             columns to formatted (if they exist).


     :Returns:
         pandas.Dataframe
             ``df`` with the columns formatted.

     .. seealso::
         Related functions
             see :py:func:`magicroot.df.format.all`.

         Similar to
             see :py:func:`magicroot.df.format.as_code`.

             see :py:func:`magicroot.df.format.as_date`.

             see :py:func:`magicroot.df.format.as_float`.

             see :py:func:`magicroot.df.format.as_int`.

             see :py:func:`magicroot.df.format.as_string`.

     """
    return with_func(df, columns, lambda x, column: pd.to_numeric(x[column], errors=errors).fillna(fill))


def as_int(df, columns=None, *args, **kwargs):
    """
     Tranforms the given columns into ints in the given table

     :Parameters:
         df : pandas.Dataframe
             Dataframe to operate on
         columns : list
             columns to formatted (if they exist).


     :Returns:
         pandas.Dataframe
             ``df`` with the columns formatted.

     .. seealso::
         Related functions
             see :py:func:`magicroot.df.format.all`.

         Similar to
             see :py:func:`magicroot.df.format.as_code`.

             see :py:func:`magicroot.df.format.as_date`.

             see :py:func:`magicroot.df.format.as_float`.

             see :py:func:`magicroot.df.format.as_int`.

             see :py:func:`magicroot.df.format.as_string`.

     """
    return with_func(df, columns, lambda x, column: df[column].astype(float).fillna(0).astype(int, *args, **kwargs))


def as_string(df, columns=None):
    """
     Tranforms the given columns into strings in the given table

     :Parameters:
         df : pandas.Dataframe
             Dataframe to operate on
         columns : list
             columns to formatted (if they exist).


     :Returns:
         pandas.Dataframe
             ``df`` with the columns formatted.

     .. seealso::
         Related functions
             see :py:func:`magicroot.df.format.all`.

         Similar to
             see :py:func:`magicroot.df.format.as_code`.

             see :py:func:`magicroot.df.format.as_date`.

             see :py:func:`magicroot.df.format.as_float`.

             see :py:func:`magicroot.df.format.as_int`.

             see :py:func:`magicroot.df.format.as_string`.

     """
    return with_func(df, columns, lambda x, column: df[column].astype(str))


def guarantee(dates=None, ints=None, floats=None, strings=None, error=TypeError):
    """
    Raises error if any of the columns are not correctly formatted 

    :Parameters:
        kwargs : mapping, dict {str: pandas.Dataframe}
            names and dateframes to compare types.

    :Returns:
        pandas.Dataframe
            ``df`` with the index of columns names and one column 
            per dataframe with the types.

    """
    dates, ints, floats, strings = cls.to_list(dates, ints, floats, strings)
    
    tests = zip((dates, ints, floats, strings), ('datetime', 'int', 'float', 'object'))

    def test(list_of_series, type_str):
        if list_of_series:
            for s in list_of_series:
                try:
                    assert type_str in str(s.dtypes)
                except AssertionError:
                    raise error(f'Column \'{s.name}\' does not have type \'{type_str}\''
                                f' instead has type \'{str(s.dtypes)}\'')

    for list_of_series, type_str in tests:
        test(list_of_series=list_of_series, type_str=type_str)


def compared(**kwargs):
    """
    Compares types of several pandas.Dataframes

    :Parameters:
        kwargs : mapping, dict {str: pandas.Dataframe}
            names and dateframes to compare types.

    :Returns:
        pandas.Dataframe
            ``df`` with the index of columns names and one column 
            per dataframe with the types.
    """
    columns=kwargs.keys()
    df = pd.DataFrame({
        'df_' + str(i + 1): df.dtypes for i, df in enumerate(kwargs.values())
    })
    df.columns = columns if columns is not None else df.columns
    return df


