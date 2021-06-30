"""Prepared by Orgunova Polina K-10"""
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
    "ini":{
        1:'input key is missing',
        2:'main(csv) file is missing',
        3:'encoding of input file is missing',
        4:'additional(json) is missing',
        5:'output key is missing',
        6:'encoding of output file is missing',
        7:'missing output file name'
    },
    "main_file":{
        1:"Wrong number of keys"
    },
    "keys":{
        1:'ID of meteostation contains wrong number of symbols',
    },
    "date_error":{
        1:'Wrong length of term "year"',
        2:'Invalid month',
        3:'Invalid day',
    },
    "similar_error":{
        1:"Main and additional files doesn`t fit"
    }
    }
    for b in errors:
        print ("*****",error_list[error_type][b],"*****",sep=" ",end="\n ")