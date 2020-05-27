from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
w=Tk()
w.geometry("1400x1000+0+0")

def message():
    messagebox.showinfo("Verified", "Logging you in")
    w.destroy()
aa=[]
def hey(i):
    aa.append(i)
    c=sum(aa)
    if c==12:
        messagebox.showinfo("Verified", "Logging you in")
        print("done")
        w.destroy()
        
bb=[]
def notthis(j):
    bb.append(j)
    cc=sum(bb)

    if cc==1:
        messagebox.showinfo("Error", "Please try another captcha")

def sai3():
    web.pack()
    main.pack_forget()


c=[]
def sai(k):
    b.append(k)
    z=sum(c)
    if z==9:
        B3=Button(f3,text="Submit",command=lambda:sai3()).place(x=900,y=650)
a=[]
def fun1(i):
    a.append(i)
    c=sum(a)
    if c==12:
        B1=Button(f1,text="Submit",command=lambda:message()).place(x=800,y=650)
        print("done")
def fun2(i):
    messagebox.showinfo("Error", "Please select other option")
        

def second():
    f2.pack()
    f1.pack_forget()
#_______________________________________________________________________________
main=Frame(w)

f1=Frame(main,height=1300,width=1400)
Label(f1,text='SELECT STREET SIGNS',font='timesroman 20',).place(x=550,y=50)

mmi=ImageTk.PhotoImage(Image.open("street4.gif"))
b1=Checkbutton(f1,image=mmi,command=lambda:fun1(i=3)).place(x=190,y=100)
mmi1=ImageTk.PhotoImage(Image.open("stfgfhkj.gif"))
b2=Checkbutton(f1,image=mmi1,command=lambda:fun2(i=14)).place(x=490,y=100)
mmi2=ImageTk.PhotoImage(Image.open("C:\\Users\\Prateek\\Desktop\\5.gif"))
b3=Checkbutton(f1,image=mmi2,command=lambda:fun2(i=14)).place(x=800,y=100)
mmi3=ImageTk.PhotoImage(Image.open("street1.gif"))
b4=Checkbutton(f1,image=mmi3,command=lambda:fun1(i=3)).place(x=190,y=350)
mmi4=ImageTk.PhotoImage(Image.open("street5.gif"))
b5=Checkbutton(f1,image=mmi4,command=lambda:fun1(i=3)).place(x=490,y=350)
mmi5=ImageTk.PhotoImage(Image.open("street2.gif"))
b6=Checkbutton(f1,image=mmi5,command=lambda:fun1(i=3)).place(x=800,y=350)


b=Button(f1,text="REFRESH ",command=lambda:second()).place(x=1200,y=100)

f1.pack()
#___________________________________________________________________________________


f2=Frame(main,height=1300,width=1400)
l1=Label(f2,text="        CLICK ALL THE IMAGES WITH CAKE          ",bg="Black",fg="white")
l1.place(x=60,y=0)

b1=Button(f2,command=lambda:hey(i=3))
b2=Button(f2,command=lambda:notthis(j=1))
b3=Button(f2,command=lambda:notthis(j=1))
b4=Button(f2,command=lambda:hey(i=3))
b5=Button(f2,command=lambda:notthis(j=1))
b6=Button(f2,command=lambda:hey(i=3))
b7=Button(f2,command=lambda:notthis(j=1))
b8=Button(f2,command=lambda:notthis(j=1))
b9=Button(f2,command=lambda:hey(i=3))

b1.place(x=0,y=30)
b2.place(x=120,y=30)
b3.place(x=240,y=30)
b4.place(x=0,y=150)
b5.place(x=120,y=150)
b6.place(x=240,y=150)
b7.place(x=0,y=270)
b8.place(x=120,y=270)
b9.place(x=240,y=270)
mi1=PhotoImage(file="C:\\Users\\Prateek\\Desktop\\img.gif")
mi2=PhotoImage(file="C:\\Users\\Prateek\\Desktop\\3.gif")
mi3=PhotoImage(file="C:\\Users\\Prateek\\Desktop\\4.gif")
mi4=PhotoImage(file="C:\\Users\\Prateek\\Desktop\\5.gif")
mi5=PhotoImage(file="C:\\Users\\Prateek\\Desktop\\6.gif")
mi6=PhotoImage(file="C:\\Users\\Prateek\\Desktop\\7.gif")
mi7=PhotoImage(file="C:\\Users\\Prateek\\Desktop\\8.gif")
mi8=PhotoImage(file="C:\\Users\\Prateek\\Desktop\\9.gif")
mi9=PhotoImage(file="C:\\Users\\Prateek\\Desktop\\img.gif")
tm1=mi1.subsample(2,2)
tm2=mi2.subsample(2,2)
tm3=mi3.subsample(2,2)
tm4=mi4.subsample(2,2)
tm5=mi5.subsample(2,2)
tm6=mi6.subsample(2,2)
tm7=mi7.subsample(2,2)
tm8=mi8.subsample(2,2)
tm9=mi9.subsample(2,2)
b1.config(image=tm1)
b2.config(image=tm2)
b3.config(image=tm3)
b4.config(image=tm4)
b5.config(image=tm5)
b6.config(image=tm6)
b7.config(image=tm7)
b8.config(image=tm8)
b9.config(image=tm9)


f1.pack()

web=Frame(w)
main.pack()

