# made by Shayan Babar

from tkinter import *
from tkinter.filedialog import askopenfile
from collections import OrderedDict
import pyexcel_ods3
address=""




def compile(name):


    global address
    if name==None:
        name="new.ods"
    else:

        name = str(name) + ".ods"


    data = pyexcel_ods3.get_data(address)
    new_data = OrderedDict()
    cell=OrderedDict()
    new_data.update({"sheet1": []})
    # pyexcel_ods3.save_data("Diana - single sheet.ods",new_data)
    list1 = data.keys()
    for i in list1:
        list2 = data[i]
        cell.update({"sheet1":str(i)})
        for items in range(len(list2)):
            x = list2[items]
            if (len(x) > 0):
                new_data["sheet1"].append(x)
            else:
                print("none")
        pyexcel_ods3.write_data(name,cell)
        pyexcel_ods3.write_data(name, new_data)


def open_file():
    global address
    file = askopenfile(filetypes =[('Python Files', '*.ods')])
    address=file.name
root=Tk()
root.configure(bg='#0c1620')
root.geometry('600x150')


#Label1=Label(root,text="select file").grid(column=0,row=0)
btn = Button(root, text ='Open file', command = lambda:open_file())
btn.grid(column=3,row=0)


btn2= Button(root, text =' Compile', command = lambda:compile(file_name.get()))
btn2.grid(column=6,row=6)

Label2=Label(root,text="Save new as").grid(column=3,row=3,padx=10)

file_name=Entry(root)
file_name.grid(column=6,row=3)


root.mainloop()
