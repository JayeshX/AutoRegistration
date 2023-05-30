from tkinter import *
import formfiller
root = Tk()
sport=""
nos=0
year ="2021-2022"
idver = "y"
idpr = "ID-Card"
def dbox():
    global sport,nos,irol,ipd,ilab1,ilab2,data1
    try:
        sport = st.get()
        nos= int(ns.get())
        b=True
    except ValueError:
        b=False
    if b:
        data1 = [[0 for i in range(2)] for j in range(nos)]
        irol = [Entry(root, width=50) for i in range(nos)]
        ipd = [Entry(root, width=50) for j in range(nos)]
        ilab1 = [Label(root, text="student" + str(i + 1)) for i in range(nos)]
        ilab2 = [Label(root, text="paid status") for i in range(nos)]
        for i in range(nos):
            ilab1[i].grid(row=i + 3, column=0)
            irol[i].grid(row=i + 3, column=1)
            ilab2[i].grid(row=i + 3, column=2)
            ipd[i].grid(row=i + 3, column=3)
        b2 = Button(root, text="submit", command=auto)
        b2.grid(row=nos + 3, column=1)
    else:
        alert =Tk()
        l = Label(alert,text="a field is empty: ")
        l.grid(row=0,column=0)

def auto():
    b=True
    for k in range(nos):
        try:
            data1[k][0] = int(irol[k].get())
            data1[k][1] = int(ipd[k].get())
            b=True
        except ValueError as e:
            b =False
    if b:
        f = formfiller.FormAutomation()
        f.automation(year,idpr,idver,nos,data1,sport)
    else:
        alert =Tk()
        l = Label(alert,text="a field is empty: ")
        l.grid(row=0,column=0)



l1 = Label(root, text="sport: ")
l2 = Label(root, text="Number of student")
l1.grid(row=0, column=0)
l2.grid(row=1, column=0)
st = Entry(root, width=50)
st.grid(row=0, column=1)
ns = Entry(root, width=50)
ns.grid(row=1, column=1)
b1 = Button(root, text="submit", command=dbox)
b1.grid(row=2, column=1)
root.mainloop()


# import os
# from dotenv import load_dotenv
#
# load_dotenv()
#
# GCP_PROJECT_ID = os.getenv('gcp')
# print(GCP_PROJECT_ID)