"""Prepared by Orgunova Polina K-10"""
import sys 
import json

from Exceptions import CommandLError,Ini_FileError,Add_FileError
import Checks
import File_upload
import Error_list as er
import Diagnosis as D
def print_performer_info():
    print("Orgunova Polina K-10. ", end='')

def print_lab_info():
    print("Lab 5 Variant 21\n",
    "At the entrance of the program we receive weather data\n",
    "We have to find the dates on which the average daily temperature\n"
    " was recorded higher than the average for all observations")
def process(ini):#The function reads the configuration file and processes the information
    try:
        input_settings, output_settings=load_ini(ini)
        Information=File_upload.load(input_settings["encoding"], input_settings["csv"], input_settings["json"])
        Information.output(output_settings["encoding"],output_settings["fname"])
    except:
        raise

def load_ini(fname):#The function loads ini file and checks it
    a={}
    input_params,output_params={},{}
    print("ini {}:".format(fname),end=" ")
    try:
        with open(fname, 'r')  as f:
            a=json.load(f)
        ErrorID=Checks.ini_reference(a)
        if any(ErrorID):
            raise Ini_FileError
        input_params=a['input']
        output_params=a["output"]
    except Ini_FileError as IFE:
        D.diagnosis.append(IFE)
        D.errors=("ini",ErrorID)
        raise
    except Add_FileError as e:
        D.diagnosis.append(e)
        raise
    else:
        print("OK")
    return input_params,output_params
if __name__ == "__main__":#starts program to respons if called from CommandLine
    print_performer_info()
    print_lab_info()
    
    try:
        print("*****")

        programArgs = sys.argv
        if len(programArgs) != 2:
            raise CommandLError
        
        process(programArgs[1])
    except CommandLError as e:
        print("***** program aborted *****")
        print(e)
        er.ini_error()
    except:
        print("\n***** program aborted *****")
        D.diagnosis.append("***** Unknown Error *****")
    finally:
        D.Diagnostics()