"""Prepared by Orgunova Polina K-10"""
import Error_list as e
diagnosis=[]
errors=('Unknown Error',[1])
problematic_row=0
def Diagnostics():#The function prints the program diagnostics according to the transmitted errors
    print("Diagnostics of session:")
    if problematic_row==0:
        print(" Problematic_row: None")
    else:
        print(" Problematic_row: {}".format(problematic_row))
    print("Problems:", end="\n")
    print(end=" ")
    if any(diagnosis):
        for i in diagnosis:
            print(i)
        print("Extended Diagnostic:",end="\n ")
        e.error_text(errors[0],errors[1])
    else:
        e.error_text("OK",[1])
    