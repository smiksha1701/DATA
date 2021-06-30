"""Prepered by Sakevich Michael K-11"""
def check_Data(year,month,day):#Checks data validnes
    Data_Errors=[]
    if (len(str(year))!=4):
        Data_Errors.append(1)
    if(month<1 or month>12):
        Data_Errors.append(2)
    if(day<1 or day>31):
        Data_Errors.append(3)
    return Data_Errors
def check_keys(id):#Checks keys validness
    Keys_Errors=[]
    if (len(id)<5 or len(id)>15):
        Keys_Errors.append(1)
    return Keys_Errors
def ini_reference(a):#Checks ini filling 
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
def add_reference(a):#Checks aditional json and return keys
    Error=False
    keys=0
    keys_list=[]
    for i in a.keys():
        keys+=1
        keys_list.append(i)
    if keys<2:
        Error=True
    return Error, keys_list
def Csv_row(row):#Checks row of csv validness
    Row_errors=[]
    if (len(row)!=10):
        Row_errors.append(1)
    return Row_errors