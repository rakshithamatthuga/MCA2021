
import tkinter as tk
from tkinter import Label,Entry,Button,Listbox,Scrollbar,Frame,VERTICAL,END,Toplevel,StringVar
from PIL import ImageTk, Image
import mysql.connector
import sys
con = mysql.connector.Connect(
        host="chatbot.ch85slfsmcjw.ap-south-1.rds.amazonaws.com",
        user="admin",
        password="hello123",
        db="rakshitha"
    )
cur=con.cursor()
class Chatbot(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        self.master=master
        self.load_gui()
        self.e1=StringVar()
        with con:
            print(con)
            cur.execute("CREATE TABLE IF NOT EXISTS chatbot(chat varchar(256))")
           
    def load_gui(self):
        self.label2=Label(self.master, text ='Hi! I am your Covid-19 info chatbot.',font=("Georgia",35),bg='#050A30',fg='#5670C2' )
        self.label2.grid(row=2,column=5)
        self.label1=Label(self.master, text ='How can I help you?',font=("Georgia",35),bg='#050A30',fg='#5670C2' )
        self.label1.grid(row=3,column=5)
        self.button1=Button(self.master,text='Lets chat',highlightbackground='#5670C2',width= 12,height=2,command = lambda: self.Letchat())
        self.button_quit = Button(self.master, text="No,Chat Later",width=12,height=2,highlightbackground='#5670C2',command = lambda: self.close())
        self.my_image=Image.open("C:\\Users\\Dell\\Downloads\\download23.jpg")
        self.my_image = self.my_image.resize((400, 400), Image.ANTIALIAS)
        self.my_image = ImageTk.PhotoImage(self.my_image)
        self.my_label = Label(root, image=self.my_image,background="#5cd9db").grid(row=0,column=5)
        #self.my_label.grid(row=1,column=5,sticky='nsew')
        #self.my_label.Label(root, image=self.my_image).grid(row=1,column=3)
        self.button_quit.grid(row=6,column=5)
        self.button1.grid(row=5,column=5)

    def close(self):
        self.master.destroy()
        
    def Letchat(self):
        x1=Toplevel(root)
        
        self.chat1 = Entry(x1,width=53, text = '')
        self.chat1.grid(row = 14,column = 1, sticky = 's')
        x1.geometry('1013x700')
        self.button = Button(x1,highlightbackground='#f0d8ef', width = 10,height = 2, text="Chat",command = lambda: self.add())
        self.button.grid(row = 15, column = 1, sticky = 'w')
        self.scrollbar1 = Scrollbar(x1, orient = VERTICAL)
        self.lstList1 = Listbox(x1, background="#b1b3b8", fg="white",selectbackground="#b9cced",highlightcolor="Red", width=54,height=31,exportselection = 0, yscrollcommand = self.scrollbar1.set)
        self.lstList1.place(relx = 0.5, rely = 0.5, anchor="e")
        self.lstList1.grid(row=0,column=1)
        self.scrollbar1.config(command = self.lstList1.yview)
        self.scrollbar1.grid(row = 1, column =13,rowspan = 7,columnspan=12 ,sticky = 'nes')
        self.lstList1.grid( row=0,column=1,rowspan = 5, columnspan = 10,sticky = 'nw')
        self.greetings={'hello':'hey','hi':'hey','hola':'hello','namaste':'Namaste','kaise ho':'mast','aur kya haal':'bole to jhakaaaaas','Hi Sita':'Namaste','How you doing':'Well, I am just trying to stay positive in this Lockdown','Whats up':'Just Corona going around','What are you upto these days':' GOOOO CORONA!!!','Aur kya haal':'Trying to upgrade myself in this 21 days lockdown period','Where am I':'You are in Green City','What is my location':'You are in Basavanagudi','What is this place':'You are in the City of IT hub','What does Modiji say':'Jaha Ho Wahi Raho','What does doctor advice for COVID-19':'Wash your hands every hour for 20 seconds','Corona':'GOOOOO','Whats the latest news':'Dont you know, COVID-19 has been declared as Pandemic by WHO','What is COVID-19':'COVID-19 is a new illness that affects your lungs and airways. It\'s caused by a virus called coronavirus.','What are the precuations can we take for COVID-19':'Regularly and thoroughly clean your hands with an alcohol-based hand rub or wash them with soap and water. If you\'re the one feeling sick, cover your entire mouth and nose when you cough or sneeze.Stay informed on the latest developments about COVID-19. Follow advice given by your healthcare provider, your national and local public health authority or your employer on how to protect yourself and others from COVID-19.','What are the symptoms':'Early symptoms include fever, dry cough,and fatique.','How can we defeat Coronavirus':'Most important, practice social distancing.Avoid touching eyes, nose and mouth. And until the situations becomes better, STAY HOME!','Aur kya haal?':
'Trying to upgrade myself in this  lockdown period','Where am I?':'You are in  Banglore karnataka','What is my location':'You are in basavangudi','how many cases in India today?':'60000','How many cases in banglore today':'','what is the total number of deaths in the country?':'1lakh 60k','what is the optimum oxygen levels?':'Above 90spo2','what is the recovery rate of covid patients?':'98','what is the ideal food for corona positive patients?':'home cooked food with lots of vitamin C and Zinc','how to stay positive?':'by doing what you like ,hobbies,painting,reading','which is the best vaccine?':'Cowaxin and Covishield','For which age can we get vaccine?':'from 18 and above to 60 age','Can we get vaccine today?':'Yes','Vaccinnation Centres near me?':'Shekar hospital,Bms Trust hospital','What are the side Effects of vaccine?':'Pain or tenderness at the injection siteHeadache,Tiredness,Muscle,joint aches,Fever,Chills,Nausea','Are COVID-19 Vaccines Safe?':'Yes','Are COVID-19 Vaccines Effective?':'Covishield-76% and Covaxin-82%','how many shots vaccine should i get??':'2','symptoms':'cold,cough,headache'}
        self.image = Image.open('C:\\Users\\Dell\\Downloads\\dp1.jpg')
        self.image = self.image.resize((550, 500), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.image)
        self.label = Label(x1,bg='white', image = self.photo)
        self.label.image = self.photo
        self.label.grid(row=0)
        self.image = Image.open('C:\\Users\\Dell\\Downloads\\dp2.jpg')
        self.image = self.image.resize((500, 500), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.image)
        self.label = Label(x1,bg='white', image = self.photo)
        self.label.image = self.photo
        self.label.grid(row=0,column=2)
        x1.configure(background='white')
        
    def add(self):

        for item in [self.chat1.get()]:
            if item=='hola'or item=='hello' or item=='hi' or item=='namaste' or item=='How you doing' or item=='Whats up' or item=='kaise ho' or item=='aur kya haal' or item=='Where am I?' or item=='What is my location' or item=='what is this place' or item=='Hi Sita' or item=='Whats up' or item=='What are you upto these days' or item=='Aur kya haal' or item=='Where am I?' or item=='What is my location' or item=='What is this place' or item=='Where am I' or item=='What is this place' or item=='What does Modiji say' or item=='What does doctor advise' or item=='What precuations can we take' or item=='How can we defeat Coronavirus' or item=='Aur kya haal?' or item=='Where am I' or item=='how many cases in India today?' or item=='How many cases in banglore today' or item=='what is the total number of deaths in the country?' or item=='what is the optimum oxygen levels?' or item=='what is the recovery rate of covid patients?' or item=='what is the ideal food for corona positive patients?' or item=='how to stay positive?' or item=='which is the best vaccine?' or item=='For which age can we get vaccine?' or item=='symptoms' or item=='Can we get vaccine today?' or item=='Vaccinnation Centres near me?' or item=='What are the side Effects of vaccine?' or item=='Are COVID-19 Vaccines Safe?' or item=='Are COVID-19 Vaccines Effective?' or item=='how many shots vaccine should i get??':
                self.lstList1.insert(END,str('User:'),str(self.chat1.get()),str('Covid:'),str(self.greetings.get(str(self.chat1.get()))))
            else:
                return 0

        con = mysql.connector.Connect(
            host="chatbot.ch85slfsmcjw.ap-south-1.rds.amazonaws.com",
            user="admin",
            password="hello123",
            database="rakshitha"
        )
        cur = con.cursor()
        cur.execute("INSERT INTO chatbot(chat) VALUES(%s)" , (str(self.chat1.get()),))
        con.commit()
        cur.execute("INSERT INTO chatbot(chat) VALUES(%s)" , (str(self.greetings.get(self.chat1.get())),))
        con.commit()
        cur.execute("SELECT * FROM chatbot")
        rows=cur.fetchall()
        print(rows)

           
if __name__=="__main__":
    root = tk.Tk()
    c=Chatbot(root)
    root.configure(background="#7EC8E3")
    root.geometry('640x700')
    root.title("COVID- The ChatBot")
    root.mainloop()
