from tkinter import *
import mysql.connector as sq

mydb=sq.connect(host="localhost", user="root", passwd="", database="pharmacy")
mycur=mydb.cursor()

def admin():
    def window_1():
        stock=Toplevel()
        stock.title("Pharmacy Management System | Medicine in Stock")
        stock.resizable(width=False, height=False)
        stock.configure(bg="#d7f1c9")

        width=750
        height=500
        screen_width=stock.winfo_screenwidth()
        screen_height=stock.winfo_screenheight()
        x_coordinate=(screen_width/2)-(width/2)
        y_coordinate=(screen_height/2)-(height/2)
        stock.geometry("%dx%d+%d+%d" % (width,height,x_coordinate,y_coordinate))
        
        def insertdb():
            stmt="insert into medicines_info values(%s,%s,%s,%s,%s,%s,%s)"
            val=(entry_1.get(),entry_2.get(),entry_3.get(),entry_4.get(),
                 entry_5.get(),entry_6.get(),entry_7.get())
            mycur.execute(stmt,val)
            mydb.commit()

        def updatedb():
            stmt="update medicines_info set Med_name=%s,Qty=%s,MRP=%s,Mfg=%s,Exp=%s,Purpose=%swhere Med_code=%s"
            val=(entry_2.get(),entry_3.get(),entry_4.get(),entry_5.get(),
                 entry_6.get(),entry_7.get(),entry_1.get())
            mycur.execute(stmt,val)
            mydb.commit()

        def deletedb():
            stmt="delete from medicines_info where Med_code=%s"
            val=(entry_1.get(),)
            mycur.execute(stmt,val)
            mydb.commit()
            
        def selectdb():
            n3=Toplevel()
            n3.title("Medicines in Stock")
            n3.resizable(width=True, height=True)
            n3.configure(bg="white")
            
            width=1024
            height=700
            screen_width=n3.winfo_screenwidth()
            screen_height=n3.winfo_screenheight()
            x_coordinate=(screen_width/2)-(width/2)
            y_coordinate=(screen_height/2)-(height/2)
            n3.geometry("%dx%d+%d+%d" % (width,height,x_coordinate,y_coordinate))
            stmt="select * from medicines_info"
            mycur.execute(stmt)
            result=mycur.fetchall()
            s=""
            j=0
            for i in result:
                s+=" ( "+str(i[0])+" )  "+str(i[1])+" - "+str(i[2])+" -  Rs."+str(i[3])+" - "+str(i[4])+" - "+str(i[5])+" - "+str(i[6])
                l_3=Label(n3, text=s,
                              font="consolas 14",
                              bg="white")
                l_3.place(x=10,y=30+j)
                j+=40
                s=""

        label_0=Label(stock, text="Medicines  in  Stock", width=20,
                      font="stencil 36 bold",
                      fg="#21421e", bg="#d7f1c9",)
        label_0.place(x=1,y=30)

        label_1=Label(stock, text="Medicine Code :",
                      width=20, fg="#21421e",
                      font="stencil 14 underline",
                      bg="#d7f1c9")
        label_1.place(x=35,y=125)

        entry_1=Entry(stock, width=20)
        entry_1.place(x=240,y=130)

        label_2=Label(stock, text="Medicine Name :",
                      width=20, fg="#21421e",
                      font="stencil 14 underline",
                      bg="#d7f1c9")
        label_2.place(x=35,y=175)

        entry_2=Entry(stock)
        entry_2.place(x=240,y=180)

        label_3=Label(stock, text="Quantity :",
                      width=20, fg="#21421e",
                      font="stencil 14 underline",
                      bg="#d7f1c9")
        label_3.place(x=35,y=225)

        entry_3=Entry(stock)
        entry_3.place(x=240,y=230)

        label_4=Label(stock, text="MRP :",
                      width=20, fg="#21421e",
                      font="stencil 14 underline",
                      bg="#d7f1c9")
        label_4.place(x=35,y=275)

        entry_4=Entry(stock)
        entry_4.place(x=240,y=280)

        label_5=Label(stock, text="Mfg Date :",
                      width=20, fg="#21421e",
                      font="stencil 14 underline",
                      bg="#d7f1c9")
        label_5.place(x=35,y=325)

        entry_5=Entry(stock)
        entry_5.place(x=240,y=330)
        entry_5.insert(0,"YYYY-MM-DD")
        
        label_6=Label(stock, text="Exp Date :",
                      width=20, fg="#21421e",
                      font="stencil 14 underline",
                      bg="#d7f1c9")
        label_6.place(x=35,y=375)

        entry_6=Entry(stock)
        entry_6.place(x=240,y=380)
        entry_6.insert(0,"YYYY-MM-DD")

        label_7=Label(stock, text="Purpose :",
                      width=20, fg="#21421e",
                      font="stencil 14 underline",
                      bg="#d7f1c9")
        label_7.place(x=35,y=425)

        entry_7=Entry(stock)
        entry_7.place(x=240,y=430)

        button_1=Button(stock, text="Add new medicine",
                        width=20, bg="#87a96d",
                        fg="black",font="futura-bold 14",
                        command=insertdb).place(x=450,y=120)

        button_2=Button(stock, text="Update Medicine Info",
                        width=20, bg="#87a96d",
                        fg="black", font="futura-bold 14",
                        command=updatedb).place(x=450,y=180)
        
        button_3=Button(stock, text="Display all info",
                        width=20, bg="#87a96d",
                        fg="black", font="futura-bold 14",
                        command=selectdb).place(x=450,y=240)

        button_4=Button(stock, text="Delete this item",
                        width=20, bg="#f15757",
                        fg="black", font="futura-bold 14",
                        command=deletedb).place(x=450,y=300)

        button_5=Button(stock, text="Quit this window",
                        width=20, bg="#87a96d",
                        fg="black", font="futura-bold 14",
                        command=stock.destroy).place(x=450,y=360)

    project=Tk()

    width=590
    height=450
    screen_width=project.winfo_screenwidth()
    screen_height=project.winfo_screenheight()
    x_coordinate=(screen_width/2)-(width/2)
    y_coordinate=(screen_height/2)-(height/2)
    project.geometry("%dx%d+%d+%d" % (width,height,x_coordinate,y_coordinate))
    project.title("Pharmacy Management System")

    project.configure(bg="#d7f1c9")
    project.resizable(width=False,height=False)

    lab_1=Label(project, text="PHARMACY\nMANAGEMENT\nSYSTEM",
               bg="#d7f1c9", fg="#21421e",
                justify=CENTER,
               font="stencil 40")
    lab_1.place(x=110,y=10)

    bt_3=Button(project, text="QUIT",
                width=8, bg="#f15757",
                fg="white", font="futura-bold 16",
                command=project.destroy)
    bt_3.place(x=240,y=380)

    def dis():
            n1=Toplevel()
            n1.title("Medicines and Quantities")
            n1.resizable(width=True, height=True)
            n1.configure(bg="white")
            
            width=400
            height=500
            screen_width=n1.winfo_screenwidth()
            screen_height=n1.winfo_screenheight()
            x_coordinate=(screen_width/2)-(width/2)
            y_coordinate=(screen_height/2)-(height/2)
            n1.geometry("%dx%d+%d+%d" % (width,height,x_coordinate,y_coordinate))
            stmt="select Med_name,Qty from medicines_info"
            mycur.execute(stmt)
            result=mycur.fetchall()
            s=""
            j=0
            for i in result:
                s +=str(i[0])+" - "+str(i[1])

                l_1=Label(n1, text=s,
                              font="consolas 14",
                              bg="white")
                l_1.place(x=10,y=30+j)
                j+=40
                s=""
                
    bt_4=Button(project, text="Quantity\n in stock",
                width=8, bg="#87a96d",
                padx=5,pady=5,
                fg="black", font="futura-bold 16 ",
                command=dis)
    bt_4.place(x=450,y=230)

    bt_5=Button(project, text="Update\nStock",
                width=9, bg="#87a96d",
                padx=5,pady=5,
                fg="black", font="futura-bold 16",
                command=window_1)
    bt_5.place(x=10,y=230)

    def restocked():
            n2=Toplevel()
            n2.title("Medicines to be restocked")
            n2.resizable(width=False, height=False)
            n2.configure(bg="white")
            
            width=700
            height=250
            screen_width=n2.winfo_screenwidth()
            screen_height=n2.winfo_screenheight()
            x_coordinate=(screen_width/2)-(width/2)
            y_coordinate=(screen_height/2)-(height/2)
            n2.geometry("%dx%d+%d+%d" % (width,height,x_coordinate,y_coordinate))
            stmt="select* from medicines_info where Qty<20 or Exp<2022-05-24"
            mycur.execute(stmt)
            result=mycur.fetchall()
            s=""
            j=0
            for i in result:
                s+=" ( "+str(i[0])+" )  "+str(i[1])+" - "+str(i[2])+" -  Rs."+str(i[3])+" - "+str(i[4])+" - "+str(i[5])
                l_2=Label(n2, text=s,
                              font="consolas 14",
                              bg="white")
                l_2.place(x=10,y=30+j)
                j+=40
                s=""
            
    bt_6=Button(project, text="Medicines\nto be\nrestocked",
                width=8, bg="#87a96d",
                padx=5,pady=5,
                fg="black", font="futura-bold 16",
                command=restocked)
    bt_6.place(x=170,y=220)

    def selectdb():
            n3=Toplevel()
            n3.title("Medicines in Stock")
            n3.resizable(width=False, height=False)
            n3.configure(bg="white")

            width=1024
            height=700
            screen_width=n3.winfo_screenwidth()
            screen_height=n3.winfo_screenheight()
            x_coordinate=(screen_width/2)-(width/2)
            y_coordinate=(screen_height/2)-(height/2)
            n3.geometry("%dx%d+%d+%d" % (width,height,x_coordinate,y_coordinate))
            stmt="select * from medicines_info"
            mycur.execute(stmt)
            result=mycur.fetchall()
            s=""
            j=0
            for i in result:
                s+=" ( "+str(i[0])+" )  "+str(i[1])+" - "+str(i[2])+" - Rs."+str(i[3])+" - "+str(i[4])+" - "+str(i[5])
                l_3=Label(n3, text=s,
                              font="consolas 14",
                              bg="white")
                l_3.place(x=10,y=30+j)
                j+=40
                s=""
            
    bt_7=Button(project, text="Display\nall in\nstock",
                width=8, bg="#87a96d",
                padx=5,pady=5,
                fg="black", font="futura-bold 16",
                command=selectdb)
    bt_7.place(x=310,y=220)


def login():
    loginw = Toplevel(gui)  
    width=500
    height=600
    screen_width=loginw.winfo_screenwidth()
    screen_height=loginw.winfo_screenheight()
    x_coordinate=(screen_width/2)-(width/2)
    y_coordinate=(screen_height/2)-(height/2)
    loginw.geometry("%dx%d+%d+%d" % (width,height,x_coordinate,y_coordinate))
    loginw.title("Pharmacy Management System | Login")

    loginw.configure(bg="#d7f1c9")
    loginw.resizable(width=False,height=False)
    Label(loginw,text = "Login Here",
          font = "stencil 40",fg = "#21421e",
          bg = "#d7f1c9").place(x=110 ,y = 120)
    Label(loginw,text = "Username",
          font = "stencil 15",
          fg = "#21421e",bg = "#d7f1c9").place(x=210,y = 220)
    Label(loginw,text = "Password",
          font = "stencil 15",
          fg = "#21421e",bg = "#d7f1c9").place(x=210,y = 320)

    e1 = Entry(loginw, width=28)
    e1.place(x=175, y=250)
    e2 = Entry(loginw,show = "*",width = 28)
    e2.place(x=175, y=350)

    Button(loginw, text="Login", font="Futura-Bold 14",
           fg="White", bg="#87a96d", padx=6, pady=2,
           command = lambda : auth(e1,e2)).place(x=225, y=500)
    
    def auth(e1,e2):
        user = str(e1.get())
        pwd = str(e2.get())
        if user == "admin" and pwd == "admin":
            admin()
        else:
            loginw.destroy()

def main():
    
    def anti_inflammation():
        n1=Toplevel()
        n1.title("Search | Anti-Inflammation")
        n1.resizable(width=False, height=False)
        n1.configure(bg="white")
        
        width=400
        height=500
        screen_width=n1.winfo_screenwidth()
        screen_height=n1.winfo_screenheight()
        x_coordinate=(screen_width/2)-(width/2)
        y_coordinate=(screen_height/2)-(height/2)
        n1.geometry("%dx%d+%d+%d" % (width,height,x_coordinate,y_coordinate))
        stmt="select Med_name,MRP from medicines_info where Purpose like \"Anti-inflammation\""
        mycur.execute(stmt)
        result=mycur.fetchall()
        s=""
        j=0
        for i in result:
            s +=str(i[0])+" =  Rs."+str(i[1])

            l_1=Label(n1, text=s,
                      font="consolas 16", bg="white")
            l_1.place(x=10,y=30+j)
            j+=40
            s=""

    def fever():
        n1=Toplevel()
        n1.title("Search | Fever")
        n1.resizable(width=False, height=False)
        n1.configure(bg="white")
        width=400
        height=500
        
        screen_width=n1.winfo_screenwidth()
        screen_height=n1.winfo_screenheight()
        x_coordinate=(screen_width/2)-(width/2)
        y_coordinate=(screen_height/2)-(height/2)
        n1.geometry("%dx%d+%d+%d" % (width,height,x_coordinate,y_coordinate))
        stmt="select Med_name,MRP from medicines_info where Purpose like \"Fever\""
        mycur.execute(stmt)
        result=mycur.fetchall()
        s=""
        j=0
        for i in result:
            s +=str(i[0])+" =   Rs."+str(i[1])
            l_1=Label(n1, text=s,
                          font="consolas 16", bg="white")
            l_1.place(x=10,y=30+j)
            j+=40
            s=""

    def cough():
        n1=Toplevel()
        n1.title("Search | Cough")
        n1.resizable(width=False, height=False)
        n1.configure(bg="white")

        width=400
        height=500
        screen_width=n1.winfo_screenwidth()
        screen_height=n1.winfo_screenheight()
        x_coordinate=(screen_width/2)-(width/2)
        y_coordinate=(screen_height/2)-(height/2)
        n1.geometry("%dx%d+%d+%d" % (width,height,x_coordinate,y_coordinate))
        stmt="select Med_name,MRP from medicines_info where Purpose like \"Cough\""
        mycur.execute(stmt)
        result=mycur.fetchall()
        s=""
        j=0
        for i in result:
            s +=str(i[0])+" =  Rs."+str(i[1])
            l_1=Label(n1, text=s,
                          font="consolas 16", bg="white")
            l_1.place(x=10,y=30+j)
            j+=40
            s=""

    def infection():
        n1=Toplevel()
        n1.title("Search | Infection")
        n1.resizable(width=False, height=False)
        n1.configure(bg="white")

        width=400
        height=500
        screen_width=n1.winfo_screenwidth()
        screen_height=n1.winfo_screenheight()
        x_coordinate=(screen_width/2)-(width/2)
        y_coordinate=(screen_height/2)-(height/2)
        n1.geometry("%dx%d+%d+%d" % (width,height,x_coordinate,y_coordinate))
        stmt="select Med_name,MRP from medicines_info where Purpose like \"Infection\""
        mycur.execute(stmt)
        result=mycur.fetchall()
        s=""
        j=0
        for i in result:
            s +=str(i[0])+" =  Rs."+str(i[1])
            l_1=Label(n1, text=s,
                          font="consolas 16", bg="white")
            l_1.place(x=10,y=30+j)
            j+=40
            s=""

    def antiseptic():
        n1=Toplevel()
        n1.title("Search | Antiseptic")
        n1.resizable(width=False, height=False)
        n1.configure(bg="white")

        width=400
        height=500
        screen_width=n1.winfo_screenwidth()
        screen_height=n1.winfo_screenheight()
        x_coordinate=(screen_width/2)-(width/2)
        y_coordinate=(screen_height/2)-(height/2)
        n1.geometry("%dx%d+%d+%d" % (width,height,x_coordinate,y_coordinate))
        stmt="select Med_name,MRP from medicines_info where Purpose like \"Antiseptic\""
        mycur.execute(stmt)
        result=mycur.fetchall()
        s=""
        j=0
        for i in result:
            s +=str(i[0])+" =  Rs."+str(i[1])
            l_1=Label(n1, text=s,
                          font="consolas 16", bg="white")
            l_1.place(x=10,y=30+j)
            j+=40
            s=""
            
    def protection():
        n1=Toplevel()
        n1.title("Search | Protection")
        n1.resizable(width=False, height=False)
        n1.configure(bg="white")

        width=400
        height=500
        screen_width=n1.winfo_screenwidth()
        screen_height=n1.winfo_screenheight()
        x_coordinate=(screen_width/2)-(width/2)
        y_coordinate=(screen_height/2)-(height/2)
        n1.geometry("%dx%d+%d+%d" % (width,height,x_coordinate,y_coordinate))
        stmt="select Med_name,MRP from medicines_info where Purpose like \"Protection\""
        mycur.execute(stmt)
        result=mycur.fetchall()
        s=""
        j=0
        for i in result:
            s +=str(i[0])+" =  Rs."+str(i[1])
            l_1=Label(n1, text=s,
                          font="consolas 16", bg="white")
            l_1.place(x=10,y=30+j)
            j+=40
            s=""

    def baby_product():
        n1=Toplevel()
        n1.title("Search | Baby Products")
        n1.resizable(width=False, height=False)
        n1.configure(bg="white")

        width=400
        height=500
        screen_width=n1.winfo_screenwidth()
        screen_height=n1.winfo_screenheight()
        x_coordinate=(screen_width/2)-(width/2)
        y_coordinate=(screen_height/2)-(height/2)
        n1.geometry("%dx%d+%d+%d" % (width,height,x_coordinate,y_coordinate))
        stmt="select Med_name,MRP from medicines_info where Purpose like \"Baby product\""
        mycur.execute(stmt)
        result=mycur.fetchall()
        s=""
        j=0
        for i in result:
            s +=str(i[0])+" =  Rs."+str(i[1])

            l_1=Label(n1, text=s,
                      font="consolas 16", bg="white")
            l_1.place(x=10,y=30+j)
            j+=40
            s=""

    def anti_flu():
        n1=Toplevel()
        n1.title("Search | Anti-Flu")
        n1.resizable(width=False, height=False)
        n1.configure(bg="white")

        width=400
        height=500
        screen_width=n1.winfo_screenwidth()
        screen_height=n1.winfo_screenheight()
        x_coordinate=(screen_width/2)-(width/2)
        y_coordinate=(screen_height/2)-(height/2)
        n1.geometry("%dx%d+%d+%d" % (width,height,x_coordinate,y_coordinate))
        stmt="select Med_name,MRP from medicines_info where Purpose like \"Anti-flu\""
        mycur.execute(stmt)
        result=mycur.fetchall()
        s=""
        j=0
        for i in result:
            s +=str(i[0])+" =  Rs."+str(i[1])

            l_1=Label(n1, text=s,
                      font="consolas 16", bg="white")
            l_1.place(x=10,y=30+j)
            j+=40
            s=""

    def stomach_ache():
        n1=Toplevel()
        n1.title("Search | Stomach Ache")
        n1.resizable(width=False, height=False)
        n1.configure(bg="white")

        width=400
        height=500
        screen_width=n1.winfo_screenwidth()
        screen_height=n1.winfo_screenheight()
        x_coordinate=(screen_width/2)-(width/2)
        y_coordinate=(screen_height/2)-(height/2)
        n1.geometry("%dx%d+%d+%d" % (width,height,x_coordinate,y_coordinate))
        stmt="select Med_name,MRP from medicines_info where Purpose like \"Stomach ache\""
        mycur.execute(stmt)
        result=mycur.fetchall()
        s=""
        j=0
        for i in result:
            s +=str(i[0])+" =  Rs."+str(i[1])

            l_1=Label(n1, text=s,
                      font="consolas 16", bg="white")
            l_1.place(x=10,y=30+j)
            j+=40
            s=""

    main= Toplevel()
    width=800
    height=600
    screen_width=main.winfo_screenwidth()
    screen_height=main.winfo_screenheight()
    x_coordinate=(screen_width/2)-(width/2)
    y_coordinate=(screen_height/2)-(height/2)
    main.geometry("%dx%d+%d+%d" % (width,height,x_coordinate,y_coordinate))
    main.title("Pharmacy Management System | Search")

    main.configure(bg="#d7f1c9")
    main.resizable(width=False,height=False)
    Label(main,text = "Search",
          font = "stencil 50",fg = "#21421e",
          bg = "#d7f1c9").place(x=270, y=0)
    Button(main,text ="Anti-Inflammation", width=60,
               font = "futura-bold 14",
               fg = "black",bg = "#87a96d",
               command=anti_inflammation).place(x=5, y=80)
    Button(main,text ="Fever", width=60,
               font = "futura-bold 14",
               fg = "black",bg = "#87a96d",
               command=fever).place(x=5, y=130)
    Button(main,text ="Baby Products", width=60,
               font = "futura-bold 14",
               fg = "black",bg = "#87a96d",
               command=baby_product).place(x=5, y=180)
    Button(main,text ="Cough", width=60,
               font = "futura-bold 14",
               fg = "black",bg = "#87a96d",
               command=cough).place(x=5, y=230)
    Button(main,text ="Anti-Flu",  width=60,
               font = "futura-bold 14",
               fg = "black",bg = "#87a96d",
               command=anti_flu).place(x=5, y=280)
    Button(main,text ="Stomach Ache", width=60,
               font = "futura-bold 14",
               fg = "black",bg = "#87a96d",
               command=stomach_ache).place(x=5, y=330)
    Button(main,text ="Infection",width=60,
               font = "futura-bold 14",
               fg = "black",bg = "#87a96d",
               command=infection).place(x=5, y=380)
    Button(main,text ="Antiseptic", width=60,
               font = "futura-bold 14",
               fg = "black",bg = "#87a96d",
               command=antiseptic).place(x=5, y=430)
    Button(main,text ="Protection", width=60,
               font = "futura-bold 14",
               fg = "black",bg = "#87a96d",
               command=protection).place(x=5, y=480)
    Button(main, text="QUIT",
                width=8, bg="#f15757",
                fg="white", font="futura-bold 16",
                command=main.destroy).place(x=340,y=530)
    
if __name__ == "__main__":
    gui = Tk()
    width=600
    height=300
    screen_width=gui.winfo_screenwidth()
    screen_height=gui.winfo_screenheight()
    x_coordinate=(screen_width/2)-(width/2)
    y_coordinate=(screen_height/2)-(height/2)
    gui.geometry("%dx%d+%d+%d" % (width,height,x_coordinate,y_coordinate))
    gui.title("Pharmacy Management System | WELCOME")

    gui.configure(bg="#d7f1c9")
    gui.resizable(width=False,height=False)
    Label(gui,text = "WELCOME USER!",
          font = "stencil 50",fg = "#21421e",
          bg = "#d7f1c9").place(x=50, y=10)
    Button(gui,text ="Login",
           font = "futura-bold 14",fg = "White",
           bg = "#87a96d", padx=4, pady=4,
           command=login).place(x=260, y=120)
    Button(gui,text ="Search",
           font = "futura-bold 14",
           fg = "White",bg = "#87a96d",padx=4 ,pady=4,
           command=main).place(x=254, y=200)
    mainloop()
    
