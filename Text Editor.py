from tkinter import*
from PIL import Image,ImageTk
from tkinter import messagebox
from tkinter import filedialog
class TkInterEx:

    @staticmethod


    # Main function
    def __init__(self,root):

        # Quit file
        def quit(event=None):
            root.quit()

       # Opening new file
        def newfile():
            global filename
            filename="Untitled"
            text.delete(0.0,END)

        # Opening saved file
        def openfile():
            f=filedialog.askopenfilename(defaultextension=".txt")
            f=open(f,"r")
            if f!=None:
                contents=f.read()
                text.insert(1.0,contents)
                f.close()

        # Saving file
        def savefile():
            global text
            t = text.get("1.0", "end-1c")
            savelocation=filedialog.asksaveasfilename()
            file1=open(savelocation, "w+")
            file1.write(t)
            file1.close()

        # About
        def about():
            messagebox.showinfo("About","This program is made in 2017.")

        #Menubar
        menubar=Menu(root)
        file_menu=Menu(root,tearoff=0)
        file_menu.add_command(label="New",command=newfile)
        file_menu.add_command(label="Open",command=openfile)
        file_menu.add_command(label="Save",command=savefile)
        file_menu.add_separator()
        file_menu.add_command(label="Exit",command=quit)
        menubar.add_cascade(label="File",menu=file_menu)

        help_menu=Menu(menubar)
        menubar.add_cascade(label="Help",menu=help_menu)
        help_menu.add_command(label="About",command=about)

        #Toolbar
        toolbar=Frame(root,bd=1,relief=RAISED)
        size = 20, 20
        open_img=Image.open("open.png")
        save_img=Image.open("save.png")
        exit_img=Image.open("exit.png")

        open_img.thumbnail(size, Image.ANTIALIAS)
        save_img.thumbnail(size, Image.ANTIALIAS)
        exit_img.thumbnail(size, Image.ANTIALIAS)

        open_icon=ImageTk.PhotoImage(open_img)
        save_icon=ImageTk.PhotoImage(save_img)
        exit_icon=ImageTk.PhotoImage(exit_img)

        open_button=Button(toolbar,image=open_icon,command=openfile)
        save_button=Button(toolbar,image=save_icon,command=savefile)
        exit_button=Button(toolbar,image=exit_icon,command=quit)

        open_button.image=open_icon
        save_button.image=save_icon
        exit_button.image=exit_icon

        open_button.pack(side=LEFT,padx=1,pady=1)
        save_button.pack(side=LEFT,padx=1,pady=1)
        exit_button.pack(side=LEFT,padx=1,pady=1)

        toolbar.pack(side=TOP,fill=X)
        root.config(menu=menubar)

root=Tk()

app=TkInterEx(root)
text=Text(root)
text.pack()
root.title("Notepad")
root.mainloop()
