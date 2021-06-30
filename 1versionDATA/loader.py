"""Prepered by Sakevich Michael K-11"""
import csv
import json
import checker as C
import Diagnosis as D
from add import read_add
from exceptions import FileExistError,FitError,CSV_Filling
from information import Information
def load(coding, fmain, fadd):
    """loads information from csv to class 
    Information reads additional json file and checks it inconsistency """
    try:
        Info=Information() 
        load_data(Info,fmain,coding)
        Data_To_Check=Info.fits_args()
        GoodData=load_stat(fadd,coding)
        print("json?=csv:",end=" ")
        fits=fit(Data_To_Check,GoodData)
        if fits:
            print("OK")
        else:
            print("UPS")
            raise FitError
    except FitError as e:
        D.diagnosis.append(e)
        D.errors=("fits_error",[1])
    return Info
def load_data(Info,filename, coding):#informs about starting of loading information from csv
    print("input-csv {}: ".format(filename), end='')
    Info.clear()
    builder = Builder(Info, filename, coding)
    try:
        Info = builder.build()
    except:
        raise
    else:
        print("OK")
def load_stat(filename, coding):
    """informs about starting of loading 
    information from json, load it and check"""
    result=0
    print("input-json {}:".format(filename),end=" ")
    try:
        result=read_add(filename,coding)
    except Exception as e:
        D.diagnosis.append(e)
        raise
    else:
        print("OK")
    return result
def fit(container, verif_data):#checking inconsistency of csv and json files
    flag=True
    for i in range(2):
        if (container[i]==verif_data[i]):
            pass
        else:
            flag=False
    return flag
class Builder():
    """Class which loads and unpacks row from csv, checks it and load in information"""
    def __init__(self,info,filename,coding):
        self.filename = filename
        self.coding = coding
        self.inf = info
        self.row_num=0
        self._row = []
        self.relative_humidity = 0
        self.meteoid = ""
        self.year = 0
        self.a_precipitation = 0
        self.adt = 0
        self.hdt = 0
        self.month = 0
        self.day = 0
        self.mdt = 0
        self.wp = 0
    def build(self):#read csv, parse, check, converts and load it to Information
        self.inf.clear()
        try:
            with open(self.filename,'r',encoding=self.coding)as f:
                reader=csv.reader(f,delimiter=';')
                for num,row in enumerate(reader):
                    self.row_num=num
                    error_list=C.Csv_row(row) 
                    if (any(error_list)):
                        raise CSV_Filling
                    else:
                        self._row=row
                        self._converter()
                        
                        self.inf.input(self.relative_humidity,self.meteoid,self.year,self.a_precipitation,
                        self.adt,self.hdt,self.month,self.day,self.mdt,self.wp)
        except CSV_Filling as es:
            D.problematic_row=self.row_num+1
            D.diagnosis.append(es)
            D.errors=('Csv_row',error_list)
            raise
        except:
            D.problematic_row=self.row_num+1
            raise
        return self.inf
    def _converter(self):#converts elements of row 
        try:
            self.relative_humidity = int(self._row[0])
            self.meteoid = str(self._row[1])
            self.year = int(self._row[2])
            self.a_precipitation = float("{:.1f}".format(float(self._row[3])))
            self.adt = float("{:.2f}".format(float(self._row[4])))
            self.hdt = float("{:.2f}".format(float(self._row[5])))
            self.month = int(self._row[6])
            self.day = int(self._row[7])
            self.mdt = float("{:.2f}".format(float(self._row[8])))
            self.wp = float("{:.1f}".format(float(self._row[9])))
        except (IndexError, TypeError, ValueError):
            raise
