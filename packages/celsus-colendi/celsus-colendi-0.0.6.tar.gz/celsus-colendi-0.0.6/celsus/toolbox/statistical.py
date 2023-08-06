import pandas as pd

def get_statistical_info(data, column, average=True, minimum=True, maximum=True, deviation=True):
    """_summary_

    Parameters
    ----------
    data : _type_
        _description_
    column : _type_
        _description_
    average : bool, optional
        _description_, by default True
    minimum : bool, optional
        _description_, by default True
    maximum : bool, optional
        _description_, by default True
    deviation : bool, optional
        _description_, by default True

    Returns
    -------
    _type_
        _description_
    """    
    statistical = {}
    if average==True:
        avg = data[column].mean()
        if pd.isna(avg) == True:
            stdev=0
        statistical["mean"] = avg
    if minimum==True:
        mini =data[column].min()
        if pd.isna(mini) == True:
            stdev=0
        statistical["min"] = mini
    if maximum==True:
        maxi = data[column].max()
        if pd.isna(maxi) == True:
            stdev=0
        statistical["max"] = maxi
    if deviation==True:
        stdev = data[column].std()
        if pd.isna(stdev) == True:
            stdev=0
        statistical["stdev"] = stdev
        # return all values
    return statistical