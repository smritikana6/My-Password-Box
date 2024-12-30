from tkinter import *
from tkinter import messagebox
#import pyperclip
from generate_password import generate
import json


#setting up the window
mywindow=Tk()
mywindow.title("Password Manager")
mywindow.config(padx=50 ,pady=50,bg="white")

# setting up the image
canvas=Canvas(width=200, height=200)
image=PhotoImage(file="lockkey.png")
canvas.create_image(100,100,image=image)
canvas.config(bg="white",highlightthickness=0)
canvas.grid(row=0,column=1)

#saving the password into a json file
def save():
    website=e1_website.get().title()
    email=e2_email.get()
    password=e3_password.get()
    new_data={
        website:{
            "email": email,
            "password": password
            }
        }
    if website =="" or email =="" or password=="":
       messagebox.showerror(title="Error",message="Don't let fields empty.")
    else:
        response=messagebox.askokcancel(title="Confirmation",message=f"Website: {website}\nUsername: {email}\nPassword:{password}") 
        if response == True:
          try:
            with open("Mypasswords.json",'r') as file1:  
                data=json.load(file1) #reading the old data

          except FileNotFoundError:
                with open("Mypasswords.json",'w') as file1:  
                    json.dump(new_data, file1, indent=4)
          else:
                data.update(new_data) #updating the new data
                with open("Mypasswords.json",'w') as file1:     
                    json.dump(data, file1, indent=4) #adding the updated data
          finally:      
              e1_website.delete(0,END)
              e3_password.delete(0,END)
              messagebox.showinfo(message="Information Saved Successfully")

#for creating a new password
def create_password():
    mypassword=generate()
    e3_password.insert(0,f"{mypassword}")

#for searching password    
def searchPassword():
    website=e1_website.get().title()
    try:
        with open("Mypasswords.json",'r') as file1:  
            myData=json.load(file1) #reading the old data
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No DataFile Exists")
    else:    
        for key in myData:
            if key == website:
                messagebox.showinfo(title=f"{key}",message=f"Email: {myData[key]['email']}\nPassword:{myData[key]['password']}") 
                break
        else:
            messagebox.showinfo(title=f"{website}",message="No Details found. Please create new password.") 


#labels
l1_website=Label(text="Website:")
l1_website.grid(row=1,column=0)
l2_email=Label(text="Email/Username:")
l2_email.grid(row=2,column=0)
l3_password=Label(text="Password:")
l3_password.grid(row=3,column=0)

#enties
e1_website=Entry(width=50)
e1_website.grid(row=1,column=1,columnspan=2)
e1_website.focus()

e2_email=Entry(width=50)
e2_email.grid(row=2,column=1,columnspan=2)
e2_email.insert(0,"myemail@gmail.com")

e3_password=Entry(width=32)
e3_password.grid(row=3,column=1)

#buttons
but1=Button(text="Initiate Password",width=13,command=create_password)
but2=Button(text="Add",width=42,command=save)
but3=Button(text="Search",width=13,command=searchPassword)
but1.grid(row=3,column=2)
but2.grid(row=4,column=1,columnspan=2)
but3.grid(row=1,column=2)

mywindow.mainloop()