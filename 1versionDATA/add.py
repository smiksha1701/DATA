"""Prepered by Sakevich Michael K-11"""
import json
import checker
import Diagnosis as D
from exceptions import AddError
import error as er
def read_add(fname,coding):#Reads additional Json
    Keys=[]
    try:
        with open(fname, 'r',encoding=coding)  as f:
            a=json.load(f)
            Error,Keys=checker.add_reference(a)
            if (Error):
                raise AddError
    except AddError as AE:
        D.diagnosis.append(AE)
        raise
    except Exception as e:
        D.diagnosis.append(e)
        raise
    return (a[Keys[0]],a[Keys[1]])
    