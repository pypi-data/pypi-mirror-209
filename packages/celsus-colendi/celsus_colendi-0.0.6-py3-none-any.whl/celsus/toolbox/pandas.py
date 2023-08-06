import pandas as pd
from datetime import timedelta

# convert date type of selecte column
def convert_column_type(df, columns, type):
    """_summary_

    Parameters
    ----------
    df : _type_
        _description_
    columns : _type_
        _description_
    type : _type_
        _description_
    """    
    for column in columns:
        if type == "datetime":
            df[column] = pd.to_datetime(df[column])
        if type == "int":
            df[column] = df[column].astype("int64")
            
def drop_columns(list_df, columns):
    """_summary_

    Parameters
    ----------
    list_df : list
        dataframe list
    columns : list
        column list
    """    
    for df in list_df:
        df.drop(columns=columns, inplace=True)

def utc_to_turkey(df, columns):
    """
    convert tc datetime to Türkiye time

    Parameters
    ----------
    df : dataframe
        dataframe
    columns : str
        date columns name
    """    
    for column in columns:
        df[column] = df[column] + timedelta(hours=3)