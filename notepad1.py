from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename





def NewFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)

def OpenFile():
    global file
    file = askopenfilename(defaultextension =".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()

def SaveFile():

   global file
   if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            #Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
   else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()
  

def quitapp():
    root.destroy()
   


def CutFile():
    TextArea.event_generate(("<<Cut>>"))
   

def CopyFile():
    TextArea.event_generate(("<<Copy>>"))

def PasteFile():
    TextArea.event_generate(("<<Paste>>"))
   

def about():
    showinfo("Notepad", "Notepad by SUPHAL ")
    
   



if __name__ == '__main__':
   root=Tk()
   root.title(" NOTEPAD ")
   root.geometry("500x500")
   root.wm_iconbitmap("C:/Users/Tnluser/Desktop/python/Project 2/projects/1.ico")


   #add text area

   TextArea=Text(root,font="lucida  12")
   file=None
   TextArea.pack(expand=True,fill=BOTH)

   Menubar=Menu(root)

   #file menu starts here
   
   Filemenu=Menu(Menubar,tearoff=0)
   Filemenu.add_command(label="New",command=NewFile)
   Filemenu.add_command(label="Open",command=OpenFile)
   Filemenu.add_command(label="Save",command=SaveFile)
   Filemenu.add_separator()
   Filemenu.add_command(label="Exit",command=quitapp)
   Menubar.add_cascade(label="File",menu=Filemenu)


    #edit menu starts here 
    
   Editmenu=Menu(Menubar,tearoff=0)
   Editmenu.add_command(label="Cut",command=CutFile)
   Editmenu.add_command(label="Copy",command=CopyFile)
   Editmenu.add_command(label="Paste",command=PasteFile)
  
   Menubar.add_cascade(label="Edit",menu=Editmenu)


   #helpmenu starts here 

   Helpmenu=Menu(Menubar,tearoff=0)
   Helpmenu.add_command(label="About Notepad",command=about)
   Menubar.add_cascade(label="Help",menu=Helpmenu)

   root.config(menu=Menubar)
   #adding scroll bar

   scroll=Scrollbar(TextArea)
   scroll.pack(side=RIGHT, fill=Y)
   scroll.config(command=TextArea.yview)
   TextArea.config(yscrollcommand=scroll.set)







   






   root.mainloop()