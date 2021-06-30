"""Prepared by Orgunova Polina K-10"""
class CommandLError(BaseException):#class of error
    def __str__(self):
        return "***** command line error *****"
class Add_FileError(BaseException):#class of error
    def __str__(self):
        return "***** json decoder error *****"
class Ini_FileError(BaseException):#class of error
    def __str__(self):
        return "***** init file error *****"
class CSV_Filling(BaseException):#class of error
    def __str__(self):
        return "***** Invalid data *****"
class KeysError(BaseException):#class of error
    def __str__(self):
        return "***** Invalid keys *****"
class DateFError(BaseException):#class of error
    def __str__(self):
        return "***** Wrong format of date *****"
class FileExistError(BaseException):#class of error
    def __str__(self):
        return "***** No such file *****"
class AddError(BaseException):#class of error
    def __str__(self):
        return "***** can not read input json-file *****"
class DateError(BaseException):#class of error
    def __str__(self):
        return "***** One date have two marks *****"
class FitError(BaseException):#class of error
    def __str__(self):
        return "***** inconsistent information *****"
class WriteError(BaseException):#class of error
    def __str__(self):
        return "***** can not write output file *****"
class CsvFileReadingError(BaseException):#class of error
    def __str__(self):
        return "***** can not read input csv file *****"
class UnknownError(BaseException):#class of error
    def __str__(self):
        return "***** can not read input csv file *****"