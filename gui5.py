from tkinter import*


window=Tk()
l1= Label(window,text="이름")
l2= Label(window,text="직업")
l3= Label(window,text="국적")



l1.grid(row=0,column=0)
l2.grid(row=1,column=0)
l3.grid(row=2,column=0)



e1=Entry(window)
e2=Entry(window)
e3=Entry(window)



e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
e3.grid(row=2,column=1)



b1=Button(window,text="Show")
b2=Button(window,text="Quit")



b1.grid(row=3,column=0)
b2.grid(row=3,column=1)


window.mainloop()
