from tkinter import *

def gaycheck(name):
    if name == "markuss":
        print(name+" ir liels gejs!!!\n")
        print("fr!!!FR")

    elif name=="x":
         print("dirst ej\n")
    else:
        print("šis cilvēks nav gejs\n")

"""
vards =0
while vards!="x":
    vards = input("Ievadi vardu: ")
    gaycheck(vards)
"""
# create root window
root = Tk()                          
 
# frame inside root window
frame = Frame(root)        

c=Canvas(root, height=15, width=50)
 
# geometry method
frame.pack()                         
 
# button inside frame which is
# inside root
button = Button(frame, text ='Geek') 
button.pack()                        
 
# Tkinter event loop
root.mainloop()  
