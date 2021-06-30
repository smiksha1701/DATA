"""Prepered by Sakevich Michael K-11"""
import csv
import sys 
import json

from exceptions import CommandLError,Ini_FileError,JSONError
import checker
import loader
import error as er
import Diagnosis as D
def print_performer_info():#Prints performers info
    print("Sakevich Michael K-11. ", end='')

def print_lab_info():#Prints lab info
    print("Lab 3 Variant 67\n",
    "We get data about students in csv file\n",
    "and have to find students, which have at least one mark\n",
    "excellent, one mark good and one mark satisfactory of all of their marks")
def main(ini):#doing everything from reading every file to outputing needed info
    try:
        input_settings, output_settings=load_ini(ini)
        Information=loader.load(input_settings["encoding"],input_settings["csv"],input_settings["json"])
        Information._output(output_settings["encoding"],output_settings["fname"])
    except:
        raise

def load_ini(fname):#loads ini file and checks it
    a={}
    input_params,output_params={},{}
    print("ini {}:".format(fname),end=" ")
    try:
        with open(fname, 'r')  as f:
            a=json.load(f)
        ErrorID=checker.ini_reference(a)
        if any(ErrorID):
            raise Ini_FileError
        input_params=a['input']
        output_params=a["output"]
    except Ini_FileError as IFE:
        D.diagnosis.append(IFE)
        D.errors=("ini_error",ErrorID)
        raise
    except JSONError as e:
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
        
        main(programArgs[1])
    except CommandLError as e:
        print("***** program aborted *****")
        print(e)
        er.ini_error()
    except:
        print("\n***** program aborted *****")
        D.diagnosis.append("***** Unknown Error *****")
    finally:
        D.Diagnostics()