from tkinter import *
import tkinter . messagebox as tmsg
import webbrowser

data={"1":"u","sheryar1234":"sheryar@gmail.com","uzair":"uzairishfaq1234@gmail.com"}

#####################################################################################################################################
firstpage=Tk()
def canco():
    name113.delete(0,'end')
    pass113.delete(0,'end')


def dest():
    firstpage.destroy()
 

def help():
    
    webbrowser.open_new(r"https://bit.ly/2VMMqDK ")
##################################REGISTER BUTTON#################################33
def register():
    datapage2=Tk()
    name113.delete(0,'end')
    pass113.delete(0,'end')

    def canco():
        name1123.delete(0,'end')
        pass1213.delete(0,'end')

    def comple():

      


        if regrequirevalue.get()==0:
            if regusernamesig.get() in data.values():
                regusermis=tmsg.showwarning("ALERT!","User Name already taken /n Try something New!")
                if regpasswordsig.get() in data.keys():

                    regusermis121=tmsg.showwarning("ALERT!","Password already taken /n Try something New!")
        else:
            regreqmis221=tmsg.showwarning("ALERT!","FILL ALL DATA & AGREE WITH OUR POLICY!")
    
        if regusernamesig.get() not in data.values() and regpasswordsig.get() not in data.keys():
            data.update({regpasswordsig.get(): regusernamesig.get()})
        
            regreqmis2121=tmsg.showwarning("ACCESSED!","YOU HAVE SUCCESSUFLY SIGN UP!")
            datapage2.destroy()
            name1123.delete(0,'end')
            pass1213.delete(0,'end')
        


    def go():
        datapage2.destroy()

    






    #data.update({regpasswordsig.get(): regusernamesig.get()})


    width= datapage2.winfo_screenwidth()  
    height= datapage2.winfo_screenheight() 
#full screen 
    datapage2.geometry("%dx%d" % (width, height)) 
    datapage2.minsize(width,height)
#background icon title
    datapage2.configure(background="black")
    datapage2.title("Sign Up Form -Uzairs_designers")

    regusernamesig=StringVar()
    regpasswordsig=StringVar()
    regrequirevalue=IntVar()


    ###################sign up  label###########3
    name112=Label(datapage2,bg="black",fg="white",text="S I G N U P",font=("Helvetica",15,"bold"))
    name112.place(x=635,y=110)


    name145=Label(datapage2,bg="black",fg="white",text="Gmail",font=("Helvetica",12,"bold"))
    name145.place(x=665,y=400)
    ##################name emtry################
   
    name1123=Entry(datapage2,width=40,textvariable=regusernamesig,bg="white",borderwidth=0,relief=FLAT,font=("Helvetica",9))
    name1123.place(x=560,y=430)

    ###################password label###########3
    passo123=Label(datapage2,bg="black",fg="white",text="Password",font=("Helvetica",12,"bold"))
    passo123.place(x=655,y=450)
    ##################password emtry################
   
    pass1213=Entry(datapage2,width=40,textvariable=regpasswordsig,show="*",bg="white",borderwidth=0,relief=FLAT,font=("Helvetica",9))
    pass1213.place(x=560,y=480)
    requiry=Checkbutton(bg="black",fg="grey",text=("Have you fill all data & Agreed! with our policy."),variable=regrequirevalue)
    requiry.place(x=565,y=510)
    ################login button#############
    loin423=Button(datapage2,text="Sign Up",bg="white",font=("Helvetica",10,"bold"),fg="black",borderwidth=0,width=10,command=comple)
    loin423.place(x=594,y=550)
    ##############quite button###########
    loin523=Button(datapage2,text="Clear",bg="white",font=("Helvetica",10,"bold"),fg="black",borderwidth=0,width=10,command=canco)
    loin523.place(x=710,y=550)
    ##############Registeration button###########
    loin525=Button(datapage2,text="Login",bg="red",font=("Helvetica",10,"bold"),fg="white",borderwidth=0,width=20,command=go)
    loin525.place(x=610,y=600)







    datapage2.mainloop()





def add():
    
    if requirevalue.get()==1:
        if passwordsig.get() in data.keys():
            if usernamesig.get() in data.values():
                if data[passwordsig.get()]==usernamesig.get():
                    firstpage.destroy()
                  
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||                
                    datapage1=Tk()

                    def desto():
                        datapage1.destroy()

                    def whato():
                        webbrowser.open_new(r"https://bit.ly/2VMMqDK ")

                    def yout():
                        webbrowser.open_new(r"https://www.youtube.com/results?search_query=dark+code+by+uzair ")

                    def  insto():
                        webbrowser.open_new(r"https://www.instagram.com/uzair_cancerian/ ")


                    def cleno():
                        celerance=tmsg.askyesno("PERMISSION","ARE YOU SURE YOU WANT TO CLEAR ALL DATA")
                        if celerance==True:
                            dta1.delete(0,'end')
                            dta2.delete(0,'end')
                            dta3.delete(0,'end')
                            dta4.delete(0,'end')
                            dta5.delete(0,'end')
                            dta6.delete(0,'end')
                            dta6.delete(0,'end')
                            dta7.delete(0,'end')
                            dta8.delete(0,'end')
                            dta9.delete(0,'end')
                            mgre=tmsg.showwarning("CLEARDED!","Your data is  cleared!")
                        else:
                            mge=tmsg.showwarning("CLEARING DATA STOPED","Your data is not cleared!")
#data for gui screen
                    width= datapage1.winfo_screenwidth()  
                    height= datapage1.winfo_screenheight() 
#full screen 
                    datapage1.geometry("%dx%d" % (width, height)) 
                    datapage1.minsize(width,height)
#background icon title
                    datapage1.configure(background="black")
                    #datapage1.iconbitmap("D:\BSCS\BSCS 2 SEMESTER\LGU FILES\OOP IN PYTHON\python gui\LoginGUI\log.ico")
                    datapage1.title("Login-Uzairs_designers")

                    hed=Label(datapage1,padx=15,anchor="w",bg="white",height=2,fg="black",text="APPLICATION-DATA-FORM",borderwidth=0,relief=FLAT,font=("Helvetica",16,"bold"))
                    hed.pack(fill=X)

                    hed2=Label(datapage1,bg="white",fg="black",text="DISPLAY-DATA",borderwidth=0,relief=FLAT,font=("Helvetica",16,"bold"))
                    hed2.place(x=800,y=14)





                    def adds():
                        celerance=tmsg.askyesno("PERMISSION","DO YOU ENTERD ALL DATA")
                        if celerance==True:
                            dis1=Label(datapage1,bg="black",fg="white",text=f"NAME: {name.get()}",font=("Helvetica",13,"bold"))
                            dis1.place(x=800,y=90)

                            dis2=Label(datapage1,bg="black",fg="white",text=f"CNIC:{cnic.get()}",font=("Helvetica",13,"bold"))
                            dis2.place(x=800,y=120)

                            dis3=Label(datapage1,bg="black",fg="white",text=f"GENDER:{gen.get()}",font=("Helvetica",13,"bold"))
                            dis3.place(x=800,y=150)

                            dis4=Label(datapage1,bg="black",fg="white",text=f"DATE OF BIRTH:{birth.get()}",font=("Helvetica",13,"bold"))
                            dis4.place(x=800,y=180)

                            dis5=Label(datapage1,bg="black",fg="white",text=f"ADDRESS:{addre.get()}",font=("Helvetica",13,"bold"))
                            dis5.place(x=800,y=210)

                            dis6=Label(datapage1,bg="black",fg="white",text=f"CITY:{city.get()}",font=("Helvetica",13,"bold"))
                            dis6.place(x=800,y=240)

                            dis7=Label(datapage1,bg="black",fg="white",text=f"COUNTRY:{contry.get()}",font=("Helvetica",13,"bold"))
                            dis7.place(x=800,y=270)

                            dis8=Label(datapage1,bg="black",fg="white",text=f"PHONE-NUMBER:{phone.get()}",font=("Helvetica",13,"bold"))
                            dis8.place(x=800,y=300)

                            dis9=Label(datapage1,bg="black",fg="white",text=f"CURRENT-EDUCATION:{curtedu.get()}",font=("Helvetica",13,"bold"))
                            dis9.place(x=800,y=330)


                            f=open(f"{name.get()}.txt","w")
                            f.write(f"NAME:{name.get()}\nCNIC:{cnic.get()}\nGENDER:{gen.get()}\nDATE OF BIRTH:{birth.get()}\nADDRESS:{addre.get()}\nCITY:{city.get()}\nCOUNTRY:{contry.get()}\nPHONE NUMBER:{phone.get()}\nCURRENT-EDUCATION:{curtedu.get()}\n")
                            f.close()

                            hed3=Label(datapage1,bg="black",fg="LimeGreen",text="DATA SUBMITED..........!",borderwidth=0,relief=FLAT,font=("Helvetica",10,"bold"))
                            hed3.place(x=800,y=370)

                            

                            dta1.delete(0,'end')
                            dta2.delete(0,'end')
                            dta3.delete(0,'end')
                            dta4.delete(0,'end')
                            dta5.delete(0,'end')
                            dta6.delete(0,'end')
                            dta6.delete(0,'end')
                            dta7.delete(0,'end')
                            dta8.delete(0,'end')
                            dta9.delete(0,'end')

                        else:
                            ms1=tmsg.showinfo("ABORT!","Plz fill all the data and click check box")
                    
                    name=StringVar()
                    cnic=StringVar()
                    gen=StringVar()
                    birth=StringVar()
                    addre=StringVar()
                    city=StringVar()
                    contry=StringVar()
                    phone=StringVar()
                    curtedu=StringVar()
                    check=IntVar()

                    l1=Label(datapage1,bg="black",fg="white",text="Name",font=("Helvetica",12,"bold"))
                    l1.place(x=10,y=70)
                    dta1=Entry(datapage1,width=40,textvariable=name,bg="white",borderwidth=0,relief=FLAT,font=("Helvetica",9))
                    dta1.place(x=15,y=95)
############################################################################################################################
                    l2=Label(datapage1,bg="black",fg="white",text="Cnic",font=("Helvetica",12,"bold"))
                    l2.place(x=10,y=125)
                    dta2=Entry(datapage1,width=40,textvariable=cnic,bg="white",borderwidth=0,relief=FLAT,font=("Helvetica",9))
                    dta2.place(x=15,y=150)
############################################################################################################################
                    l3=Label(datapage1,bg="black",fg="white",text="Gender",font=("Helvetica",12,"bold"))
                    l3.place(x=10,y=180)
                    dta3=Entry(datapage1,width=40,textvariable=gen,bg="white",borderwidth=0,relief=FLAT,font=("Helvetica",9))
                    dta3.place(x=15,y=205)
############################################################################################################################
                    l4=Label(datapage1,bg="black",fg="white",text="Date Of Birth",font=("Helvetica",12,"bold"))
                    l4.place(x=10,y=235)
                    dta4=Entry(datapage1,width=40,textvariable=birth,bg="white",borderwidth=0,relief=FLAT,font=("Helvetica",9))
                    dta4.place(x=15,y=260)
############################################################################################################################
                    l5=Label(datapage1,bg="black",fg="white",text="Address",font=("Helvetica",12,"bold"))
                    l5.place(x=10,y=290)
                    dta5=Entry(datapage1,width=40,textvariable=addre,bg="white",borderwidth=0,relief=FLAT,font=("Helvetica",9))
                    dta5.place(x=15,y=315)
############################################################################################################################
                    l6=Label(datapage1,bg="black",fg="white",text="City",font=("Helvetica",12,"bold"))
                    l6.place(x=10,y=345)
                    dta6=Entry(datapage1,width=40,textvariable=city,bg="white",borderwidth=0,relief=FLAT,font=("Helvetica",9))
                    dta6.place(x=15,y=370)
############################################################################################################################
                    l7=Label(datapage1,bg="black",fg="white",text="Country",font=("Helvetica",12,"bold"))
                    l7.place(x=10,y=400)
                    dta7=Entry(datapage1,width=40,textvariable=contry,bg="white",borderwidth=0,relief=FLAT,font=("Helvetica",9))
                    dta7.place(x=15,y=425)
############################################################################################################################
                    l8=Label(datapage1,bg="black",fg="white",text="Phone Number",font=("Helvetica",12,"bold"))
                    l8.place(x=10,y=455)
                    dta8=Entry(datapage1,width=40,textvariable=phone,bg="white",borderwidth=0,relief=FLAT,font=("Helvetica",9))
                    dta8.place(x=15,y=480)
############################################################################################################################
                    l9=Label(datapage1,bg="black",fg="white",text="Current Education",font=("Helvetica",12,"bold"))
                    l9.place(x=10,y=510)
                    dta9=Entry(datapage1,width=40,textvariable=curtedu,bg="white",borderwidth=0,relief=FLAT,font=("Helvetica",9))
                    dta9.place(x=15,y=535)

############################################################################################################################


                    check2=Checkbutton(datapage1,text="Have You Filled All The Data?",bg="black",fg="grey",variable=check)
                    check2.place(x=10,y=560)


############################################################################################################################
                    dtalog1=Button(datapage1,text="SUBMIT",bg="white",font=("Helvetica",10,"bold"),fg="black",borderwidth=0,width=10,command=adds)
                    dtalog1.place(x=30,y=600)

                    dtalog2=Button(datapage1,text="CLEAR",bg="white",font=("Helvetica",10,"bold"),fg="black",borderwidth=0,width=10,command=cleno)
                    dtalog2.place(x=190,y=600)

                    lol1=Label(datapage1,bg="black",fg="white",text="FOLLOW US ON-",font=("Helvetica",10,"bold"))
                    lol1.place(x=5,y=660)

                    what=Button(datapage1,text="WHATSAPP",fg="green",bg="BLACK",font=("Helvetica",10,"bold"),borderwidth=0,width=10,command=whato)
                    what.place(x=150,y=660)

                    you=Button(datapage1,text="YOUTUBE",fg="dark red",bg="BLACK",font=("Helvetica",10,"bold"),borderwidth=0,width=10,command=yout)
                    you.place(x=250,y=660)

                    insta=Button(datapage1,text="INSTAGRAM",fg="aqua",bg="BLACK",font=("Helvetica",10,"bold"),borderwidth=0,width=10,command=insto)
                    insta.place(x=350,y=660)

############################################################################################################################
                    lol=Button(datapage1,text="LOGOUT",bg="red",font=("Helvetica",10,"bold"),fg="white",borderwidth=0,width=10,command=desto)
                    lol.place(x=1250,y=600)

                    lol1=Label(datapage1,bg="black",fg="red",text=f"Account: {usernamesig.get()} ",font=("Helvetica",10,"bold"))
                    lol1.place(x=1080,y=660)

                   

                    datapage1.mainloop()

 #|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||                
                    
                else:
                    usermis=tmsg.showwarning("ALERT!","INCORRECT USERNAME & PASSWORD")
            else:
                usermis=tmsg.showwarning("ALERT!","INCORRECT USERNAME!")


        else:
            passmis=tmsg.showwarning("ALERT!","INCORRECT PASSWORD!")
    else:
        reqmis=tmsg.showwarning("ALERT!","FILL ALL DATA & AGREE WITH OUR POLICY!")
           



    #setting tkinter window size 
width= firstpage.winfo_screenwidth()  
height= firstpage.winfo_screenheight() 
#full screen 
firstpage.geometry("%dx%d" % (width, height)) 
firstpage.minsize(width,height)
#background icon title
firstpage.configure(background="black")
#firstpage.iconbitmap("D:\BSCS\BSCS 2 SEMESTER\LGU FILES\OOP IN PYTHON\python gui\LoginGUI\log.ico")
firstpage.title("Login-Uzairs_designers")

usernamesig=StringVar()
passwordsig=StringVar()
requirevalue=IntVar()



#######################################################################################################
l1=Label(firstpage,text="D A R K   -   C O D E",bg="white",fg=("black"),height=2,font=("Helvetica",14,"bold"),borderwidth=5,relief=SOLID)
l1.pack(fill=X)
###########################DATA PROVIDE#####################################
l2=Label(firstpage,bg="black",font=("Helvetica",15),fg="red",justify=CENTER,text="\n \n Hello!\n Welcome to Graphic User Interface In python!")
l2.pack()


l3=Label(firstpage,bg="black",font=("Helvetica",12),fg="white",justify=CENTER,text="In computer security, logging in is the process by which an individual gains access to a computer system by identifying and authenticating themselves.\n The user credentials are typically some form of  and a matching  and these credentials themselves are sometimes referred to as a login.")
l3.pack()

l4=Label(firstpage,bg="black",font=("Helvetica",12),fg="white",justify=CENTER,text="Logging in is usually used to enter a specific page, website or application, which trespassers cannot see. Once the user is logged in, the login token \n may be used to track what actions the user has taken while connected to the site. Logging out may be performed explicitly by the user \ntaking some actions, such as entering the appropriate command or clicking a website link label as such. It can also be done implicitly, such as by the\n user powering off his or her workstation, closing a web browser window, leaving a website, or not refreshing a website within a defined period.")
l4.pack()

l5=Label(firstpage,bg="black",font=("Helvetica",12),fg="white",justify=CENTER,text="In the case of websites that use cookies to track sessions, when the user logs out, session-only cookies from that site will usually be deleted from the \n user's computer. In addition, the server invalidates any associations with the session, thereby making any session-handle in the user's \n cookie store useless. This feature comes in handy if the user is using a public computer or a computer that is using a public wireless connection.\n As a security precaution, one should not rely on implicit means of logging out of a system, especially not on a public computer; instead, one should explicitly log out and wait for the confirmation that this request has taken place.")
l4.pack()



########################Quite Button###############
#but4=Button(firstpage,text="Quite",bg="red",font=("Helvetica",10,"bold"),fg="white",borderwidth=0,width=10,command=quit)
#but4.place(x=1280,y=655)
########################help button###########3
but121=Button(firstpage,text="Quit!",bg="red",font=("Helvetica",10,"bold"),fg="white",borderwidth=0,width=10,command=dest)
but121.place(x=1260,y=655)

but3=Button(firstpage,text="Help!",bg="red",font=("Helvetica",10,"bold"),fg="white",borderwidth=0,width=10,command=help)
but3.place(x=2,y=655)
#########################################END OF FIRST PAGE FOR DESIGN##############################################3

    ###################name label###########3
name13=Label(firstpage,bg="black",fg="white",text="L  O  G  I  N",font=("Helvetica",15,"bold"))
name13.place(x=635,y=360)


name14=Label(firstpage,bg="black",fg="white",text="Gmail",font=("Helvetica",12,"bold"))
name14.place(x=665,y=400)
    ##################name emtry################
   
name113=Entry(firstpage,width=40,textvariable=usernamesig,bg="white",borderwidth=0,relief=FLAT,font=("Helvetica",9))
name113.place(x=560,y=430)
    #########################################################################################
    ###################password label###########3
passo13=Label(firstpage,bg="black",fg="white",text="Password",font=("Helvetica",12,"bold"))
passo13.place(x=655,y=450)
    ##################password emtry################
   
pass113=Entry(firstpage,width=40,textvariable=passwordsig,show="*",bg="white",borderwidth=0,relief=FLAT,font=("Helvetica",9))
pass113.place(x=560,y=480)
requiry=Checkbutton(bg="black",fg="grey",text=("Have you fill all data & Agreed! with our policy."),variable=requirevalue)
requiry.place(x=565,y=510)
    ################login button#############
loin43=Button(firstpage,text="Login",bg="white",font=("Helvetica",10,"bold"),fg="black",borderwidth=0,width=10,command=add)
loin43.place(x=594,y=550)
    ##############quite button###########
loin53=Button(firstpage,text="Clear",bg="white",font=("Helvetica",10,"bold"),fg="black",borderwidth=0,width=10,command=canco)
loin53.place(x=710,y=550)
    ##############Registeration button###########
loin55=Button(firstpage,text="Sign Up",bg="red",font=("Helvetica",10,"bold"),fg="white",borderwidth=0,width=20,command=register)
loin55.place(x=610,y=600)


firstpage.mainloop()

