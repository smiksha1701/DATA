"""Prepared by Orgunova Polina K-10"""
def check_id_keys(id):#The function checks the validness of the received code of the meteostation
    Keys_Errors=[]
    if (len(id)<5 or len(id)>15):
        Keys_Errors.append(1)
    return Keys_Errors
def ini_reference(a):#The function checks ini file filling
    ErrorID=[]
    if ('input'not in a):
        ErrorID.append(1)
    else:
        if ('csv'not in a["input"]):
            ErrorID.append(2)
        if ('encoding'not in a['input']):
            ErrorID.append(3)
        if ('json'not in a['input']):
            ErrorID.append(4)
    if ('output'not in a):
        ErrorID.append(5)
    else:
        if ('encoding'not in a['output']):
            ErrorID.append(6)
        if ('fname'not in a['output']):
            ErrorID.append(7)
    return ErrorID
def check_Date(year,month,day):#The function checks the received date (year, month, day) for errors
    Data_Errors=[]
    if (len(str(year))!=4):
        Data_Errors.append(1)
    if(month<1 or month>12):
        Data_Errors.append(2)
    if(day<1 or day>31):
        Data_Errors.append(3)
    return Data_Errors
def add_keys(a):#The function checks the number of keys in the additional file and returns them
    Error=False
    keys=0
    keys_list=[]
    for i in a.keys():
        keys+=1
        keys_list.append(i)
    if keys<2:
        Error=True
    return Error, keys_list
def main_file(row):#The function checks main file validness
    Row_errors=[]
    if (len(row)!=10):
        Row_errors.append(1)
    return Row_errors