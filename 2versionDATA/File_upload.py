"""Prepared by Orgunova Polina K-10"""
import csv
import json
import Checks as C
import Diagnosis as D
from Exceptions import FitError,CSV_Filling,AddError
from Info import Information
def load(coding, fmain, fadd):
    """The function loads information from csv to class "Information"
    reads additional json file and checks it inconsistency """
    try:
        Info=Information() 
        load_start(Info,fmain,coding)
        Data_To_Check=Info.fits_args()
        GoodData=load_stat(fadd,coding)
        print("json?=csv:",end=" ")
        fits=fit(Data_To_Check,GoodData)
        if fits:
            print("OK")
        else:
            raise FitError
    except FitError as e:
        D.diagnosis.append(e)
        D.errors=("similar_error",[1])
    return Info

class Builder():
    """Class that loads and parses data from an object"""

    def __init__(self, info, filename, coding):
        self.filename = filename
        self.coding = coding
        self.inf = info
        self.row_num = 0
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

    def load_data(self):
        """The function loads the contents of the main input file
        into an existing object of the "Information" class"""
        self.inf.clear()
        try:
            with open(self.filename, 'r', encoding=self.coding)as f:
                reader = csv.reader(f, delimiter=';')
                for num, row in enumerate(reader):
                    self.row_num = num
                    error_list = C.main_file(row)
                    if (any(error_list)):
                        raise CSV_Filling
                    else:
                        self._row = row
                        self._converter()
                        self.inf.load(self.relative_humidity, self.meteoid, self.year, self.a_precipitation,
                                       self.adt, self.hdt, self.month, self.day, self.mdt, self.wp)
        except CSV_Filling as es:
            D.problematic_row = self.row_num + 1
            D.diagnosis.append(es)
            D.errors = ('Csv_row', error_list)
            raise
        except:
            D.problematic_row = self.row_num + 1
            raise
        return self.inf

    def _converter(self):  # converts elements of row
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

def read_add_file(fname,coding):#The function reads additional file and checks it for some exceptions
    Keys=[]
    try:
        with open(fname, 'r',encoding=coding)  as f:
            a=json.load(f)
            Error,Keys=C.add_keys(a)
            if (Error):
                raise AddError
    except AddError as AE:
        D.diagnosis.append(AE)
        raise
    except Exception as e:
        D.diagnosis.append(e)
        raise
    return (a[Keys[0]],a[Keys[1]])

def load_stat(filename, coding):
    """The function informs about starting of loading
    information from additional file, load it and check"""
    result=0
    print("input-json {}:".format(filename),end=" ")
    try:
        result=read_add_file(filename,coding)
    except Exception as e:
        D.diagnosis.append(e)
        raise
    else:
        print("OK")
    return result

def fit(container, verif_data):#The function checks for inconsistency between csv and json files
    flag=True
    for i in range(2):
        if (container[i]==verif_data[i]):
            pass
        else:
            flag=False
    return flag

def load_start(Info,filename, coding):#The function informs about starting of loading information from main file
    print("input-csv {}: ".format(filename), end='')
    Info.clear()
    builder = Builder(Info, filename, coding)
    try:
        Info = builder.load_data()
    except:
        raise
    else:
        print("OK")