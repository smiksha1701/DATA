"""Prepered by Sakevich Michael K-11"""
def ini_error():#Prints if ini file is missing
    print("init file is missing")
def error_text(error_type,errors):#Stores all errors (which I found) and prints if some occures
    error_list={
    "Unknown Error":{
        1:'Unknown Error'
    },
    "OK":{
        1:'Everything is ok'
    },
    "ini_error":{
        1:'input is missing',
        2:'csv is missing',
        3:'input encoding is missing',
        4:'json is missing',
        5:'output is missing',
        6:'output encoding is missing',
        7:'output file name is missing',
        10:'Json file is broken'
    },
    "Csv_row":{
        1:"Wrong number of keys"
    },
    "keys_error":{
        1:'ID of meteostation contains more/less symbols',
    },
    "data_error":{
        1:'Year of invalid length',
        2:'Invalid month',
        3:'Invalid day',
    },
    "fits_error":{
        1:"CSV and JSON doesn`t fit"
    }
    }
    for b in errors:
        print ("*****",error_list[error_type][b],"*****",sep=" ",end="\n ")