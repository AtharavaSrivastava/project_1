#Importing required libraries
import tkinter as tk
from tkinter import StringVar
from tkinter import messagebox
import mysql.connector as sq

 
#Creating the database Movie_database and a table inside it called Movies
def create():
    mydb = sq.connect(host="localhost",user="root",password="root")
    mycursor = mydb.cursor()
    sql = "Create database Movie_database"
    mycursor.execute(sql)
    mycursor.execute("Use Movie_database")
    mydb.commit()
    mycursor.execute("Create table Movies (Movie_Name VARCHAR(500), Genre VARCHAR(100), date_of_release DATE, IMDB_id INTEGER,Director VARCHAR(500), Rating VARCHAR(500))")
    mydb.commit()


#Checking the existence of the database and creating it if the database does not exist
def check_database_existence():
    try:
        mydb = sq.connect(host="localhost",user="root",password="root",database="Movie_database")
    except sq.Error as e:
        if e.errno == 1049:  #1049 is the MySQL error code for "Unknown database"
            create()
        else:
            print(f"Error: {e}")
check_database_existence()


#Re-opening the menu window whenever the close button is clicked.
def recreate_root():
    global root
    root=tk.Tk()
    root.geometry('690x350')
    root.configure(bg='#42c8f5')
    root.title('Menu')
    lab3=tk.Label(root, text="WELCOME TO BLOCKBUSTER: A Movie Database",font=('Cascadia Mono SemiLight',16,'bold'),bg='#42c8f5')
    lab6=tk.Label(root, text="Made By: Atharava Srivastava",font=('Cascadia Mono SemiLight',16,'bold'),bg='#42c8f5')
    lab3.pack()  
    lab6.pack()    

    lin1=tk.Label(root,text="1.Insert new records",font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
    lin2=tk.Label(root,text="2.Update a record",font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
    lin3=tk.Label(root,text="3.Delete a record",font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
    lin4=tk.Label(root,text="4.Search a record",font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
    lin5=tk.Label(root,text="5.Display the data",font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
    lin6=tk.Label(root,text="6.Quit",font=('Cascadia Mono SemiLight',14),bg='#42c8f5')

    lin1.place(x=10,y=80)
    lin2.place(x=10,y=110)
    lin3.place(x=10,y=140)
    lin4.place(x=10,y=170)
    lin5.place(x=10,y=200)
    lin6.place(x=10,y=230)

    ch=StringVar()
       
    lab1=tk.Label(root,text="Which function do you want to apply?:",font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
    lab1.place(x=10,y=260)

    en1=tk.Entry(root, textvariable=ch, font=('Cascadia Mono SemiLight',14))
    en1.place(x=420,y=263)

    #Function to ask for confirmation from user if quiting
    def on_closing():
            if messagebox.askyesno(title='QUIT?',message='Are you sure you want to quit'):
                root.destroy()
            else:
                pass
            
    #Function to accept the choice from user of menu items
    def choicefunc(event=None):
        choice=ch.get()
        #To insert new records
        if choice=='1':  
            insert()        
        #To update a record
        elif choice=='2':
            update()
        #To delete a record
        elif choice=='3':
            delete()
        #To search a record
        elif choice=='4':
            search()
        #To display the data
        elif choice=='5':
            display()       
        #To exit the program
        elif choice=='6':
            exit_=tk.Tk()
            exit_.geometry('500x100')
            exit_.config(bg='#42c8f5')
            exit_.title('Exit')
            label_0=tk.Label(exit_, text="Thank You!",font=('Cascadia Mono SemiLight',16,'bold'),bg='#42c8f5')
            label_1=tk.Label(exit_, text="Hope you have a nice day!",font=('Cascadia Mono SemiLight',16,'bold'),bg='#42c8f5')
            label_0.pack()
            label_1.pack()
            root.destroy()
        #Invaild input
        else:
            lab2=tk.Label(root,text="Please Enter Valid Input!",font=('Cascadia Mono SemiLight',15),bg='#42c8f5')
            lab2.place(x=170,y=300)
            ch.set('')

    en1.bind ('<Return>',choicefunc)
    
    #Recreating the option window
    root.mainloop()
    

#Function for inserting data
def insert():
    
    #Closing menu window
    root.destroy()
    
    #Creating window to insert data
    insertk=tk.Tk()  
    insertk.geometry('850x380')
    insertk.configure(bg='#42c8f5')
    insertk.title('Insert Record')
    
    #Creating labels 
    lab0=tk.Label(insertk,text='Fill out the below information',bg='#42c8f5',font=('Cascadia Mono SemiLight',18,'bold'))
    lab1=tk.Label(insertk,text="Name of the Movie :",bg='#42c8f5',font=('Cascadia Mono SemiLight',14))
    lab2=tk.Label(insertk,text="Genre of the Movie:",bg='#42c8f5',font=('Cascadia Mono SemiLight',14))
    lab3=tk.Label(insertk,text="Date of Releae of the Movie (in YYYY-MM-DD format):",bg='#42c8f5',font=('Cascadia Mono SemiLight',14))
    lab4=tk.Label(insertk,text="IMDB ID:",bg='#42c8f5',font=('Cascadia Mono SemiLight',14))
    lab5=tk.Label(insertk,text="Movie Director:",bg='#42c8f5',font=('Cascadia Mono SemiLight',14))
    lab6=tk.Label(insertk,text="IMDB Rating:",bg='#42c8f5',font=('Cascadia Mono SemiLight',14))
    
    #Placing labels
    lab0.pack()
    lab1.place(x=10,y=60)
    lab2.place(x=10,y=100)
    lab3.place(x=10,y=140)
    lab4.place(x=10,y=180)
    lab5.place(x=10,y=220)
    lab6.place(x=10,y=260)

    #Initializing variables to read the entry box data
    nm=StringVar()
    genre=StringVar()
    dor=StringVar()
    code=StringVar()
    dr=StringVar()
    rt=StringVar()

    #Creating entry boxes
    en1=tk.Entry(insertk,textvariable=nm,font=('Cascadia Mono SemiLight',14))
    en2=tk.Entry(insertk,textvariable=genre,font=('Cascadia Mono SemiLight',14))
    en3=tk.Entry(insertk,textvariable=dor,font=('Cascadia Mono SemiLight',14))
    en4=tk.Entry(insertk,textvariable=code,font=('Cascadia Mono SemiLight',14))
    en5=tk.Entry(insertk,textvariable=dr,font=('Cascadia Mono SemiLight',14))
    en6=tk.Entry(insertk,textvariable=rt,font=('Cascadia Mono SemiLight',14))
    en7=tk.Entry(insertk)
    
    #Placing entry boxes
    en1.place(x=225,y=62)
    en2.place(x=225,y=102)
    en3.place(x=575,y=142)
    en4.place(x=105,y=182)
    en5.place(x=180,y=222)      
    en6.place(x=145,y=262)
    
    #Function to execute query for entering data in MySQL table
    def insertin(event=None):
        
        #Getting information from entry boxes
        Name=nm.get()
        Genre=genre.get()
        DOR=dor.get()
        Movie_code=code.get()
        Director=dr.get()
        Rating=rt.get()

        #Connecting to MySQL and executing the query
        mydb = sq.connect(host="localhost",user="root",password="root",database="movie_database")
        mycursor = mydb.cursor()
        sql = "INSERT INTO Movies (Movie_Name, Genre, Date_of_release, IMDB_id, Director, Rating) VALUES (%s,%s,%s,%s,%s,%s)"
        val = (Name,Genre,DOR,Movie_code,Director,Rating)
        mycursor.execute(sql, val)
        mydb.commit()
        
        #Displaying message for successful insert
        added=tk.Label(insertk,text='Record Inserted',font=('Cascadia Mono SemiLight',20),bg='#42c8f5')
        added.place(x=300,y=295)

        #Setting all entry boxes to blank so that new data can be entered
        nm.set('')
        genre.set('')
        dor.set('')
        code.set('')
        dr.set('')
        rt.set('')
        
    insertk.bind_all('<Return>', insertin)
        
    #Function to ask confirmation from user for quiting
    def on_closing():
        if messagebox.askyesno(title='QUIT?',message='Are you sure you want to quit'):
            insertk.destroy() #Closing this window
            recreate_root() #Re-opening root window
        else:
            pass
        
    insertk.protocol('WM_DELETE_WINDOW',on_closing)
    insertk.mainloop()


#Function for updating a record
def update(event=None):

    #Closing menu window
    root.destroy()

    #Creating window to update a record
    updatetk=tk.Tk()
    updatetk.geometry('1000x100')
    updatetk.configure(bg='#42c8f5')
    updatetk.title('Update Record')

    #Asking user if they want to use the movie name or IMDB ID to update the record
    #Creating labels 
    lab0=tk.Label(updatetk,text='Update Record',font=('Cascadia Mono SemiLight',18,'bold'),bg='#42c8f5')
    lab1=tk.Label(updatetk,text='Enter 1 to use movie name or 2 to use IMDB ID to update the data:',font=('Cascadia Mono SemiLight',14),bg='#42c8f5')

    #Placing labels
    lab0.pack()
    lab1.place(x=10,y=50)

    #Initializing variable to read the entry box data
    val=StringVar()

    #Creating and placing entry box
    en1=tk.Entry(updatetk,textvariable=val,font=('Cascadia Mono SemiLight',14))
    en1.place(x=740,y=50)

    #Function to ask for confirmation and close the window 
    def on_closing():
            if messagebox.askyesno(title='QUIT?',message='Are you sure you want to quit'):
                nonlocal updatetk
                updatetk.destroy() #Closing this window
                recreate_root() #Re-opening root window
            else:
                pass
    updatetk.protocol('WM_DELETE_WINDOW',on_closing)

    #Checking whether user wants to update using movie name or IMDB ID
    def updateit(event=None):
        char=val.get()
        while char!='':
            if char=='1':
                updatewithname()
                break                
            elif char=='2':
                updatewithid()
                break

    #Function to update using movie name        
    def updatewithname():

        #Closing choice window
        nonlocal updatetk
        updatetk.destroy()

        #Creating window to update using movie name
        nametk=tk.Tk()
        nametk.geometry('750x380')
        nametk.configure(bg='#42c8f5')
        nametk.title('Updating Record using name')
        
        #Creating labels 
        lab0=tk.Label(nametk,text='Update Record',font=('Cascadia Mono SemiLight',18,'bold'),bg='#42c8f5')
        lab1=tk.Label(nametk,text='--> 1. Movie name ',font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
        lab2=tk.Label(nametk,text='--> 2. Genre',font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
        lab3=tk.Label(nametk,text='--> 3. Date of Release',font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
        lab4=tk.Label(nametk,text='--> 4. IMDB Id',font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
        lab5=tk.Label(nametk,text='--> 5. Director',font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
        lab9=tk.Label(nametk,text='--> 6. IMDB Rating',font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
        lab6=tk.Label(nametk,text="Movie name whose record you want to update:",font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
        lab7=tk.Label(nametk,text="Record you want to update:",font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
        lab8=tk.Label(nametk,text="Enter the change:",font=('Cascadia Mono SemiLight',14),bg='#42c8f5')

        #Placing labels
        lab0.pack()
        lab6.place(x=10,y=50)
        lab1.place(x=10,y=80)
        lab2.place(x=10,y=110)
        lab3.place(x=10,y=140)
        lab4.place(x=10,y=170)
        lab5.place(x=10,y=200)
        lab9.place(x=10,y=230)
        lab7.place(x=10,y=260)
        lab8.place(x=10,y=290)

        #Initialising variables to read entry box
        upe=StringVar()
        fi=StringVar()
        fich=StringVar()

        #Creating entry boxes
        en1=tk.Entry(nametk,textvariable=upe,font=('Cascadia Mono SemiLight',14)) 
        en2=tk.Entry(nametk,textvariable=fi,font=('Cascadia Mono SemiLight',14)) 
        en3=tk.Entry(nametk,textvariable=fich,font=('Cascadia Mono SemiLight',14)) 

        #Placing entry boxes
        en1.place(x=490,y=52)
        en2.place(x=300,y=262)
        en3.place(x=200,y=294)
                
        #Function to execute query for updating record using movie name
        def finallyupdating(event=None):
            
            #Getting information from entry boxes
            up=upe.get()
            fields=int(fi.get())
            fieldch=fich.get()

            #Checking for which data is to be updated
            if fields==1:
                field='Movie_Name'
            elif fields==2:
                field='Genre'
            elif fields==3:
                field='Date_of_release'
            elif fields==4:
                field='IMDB_id'
            elif fields==5:
                field='Director'
            elif fields==6:
                field='Rating'

            #Connecting to MySQL and executing the query
            mydb= sq.connect(host="localhost",user="root",passwd="root",database="Movie_database")
            cursor=mydb.cursor()
            update="UPDATE Movies set {} = '{}' WHERE Movie_Name like '{}'".format(field,fieldch,up)
            cursor.execute(update)
            mydb.commit()

            #Displaying message for successful update
            lab0=tk.Label(nametk,text="Record Updated!",font=('Cascadia Mono SemiLight',24),bg='#42c8f5')
            lab0.place(x=240,y=325)

            #Setting all entry boxes to blank so that more updates can be done
            upe.set('')
            fi.set('')
            fich.set('')

        #Function to ask confirmation from user for quiting
        def on_closingname():
            if messagebox.askyesno(title='QUIT?',message='Are you sure you want to quit'):
                nonlocal nametk
                nametk.destroy() #Closing this window
                recreate_root() # Re-opening root window
            else:
                pass 
        nametk.bind_all('<Return>', finallyupdating)
        nametk.protocol('WM_DELETE_WINDOW',on_closingname)

    #Function to update using IMDB ID
    def updatewithid():

        #Closing choice window
        nonlocal updatetk
        updatetk.destroy()

        #Creating window to update using IMDB ID
        idtk=tk.Tk()
        idtk.geometry('950x380')
        idtk.configure(bg='#42c8f5')
        idtk.title('Updating Record using IMDB ID')
        
        #Creating labels 
        lab0=tk.Label(idtk,text='Update Record',font=('Cascadia Mono SemiLight',18,'bold'),bg='#42c8f5')
        lab1=tk.Label(idtk,text='--> 1. Movie name ',font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
        lab2=tk.Label(idtk,text='--> 2. Genre',font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
        lab3=tk.Label(idtk,text='--> 3. Date of Release',font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
        lab4=tk.Label(idtk,text='--> 4. IMDB Id',font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
        lab5=tk.Label(idtk,text='--> 5. Director',font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
        lab9=tk.Label(idtk,text='--> 6. IMDB Rating',font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
        lab6=tk.Label(idtk,text="IMDB ID of the movie name whose record you want to update:",font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
        lab7=tk.Label(idtk,text="Record you want to update:",font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
        lab8=tk.Label(idtk,text="Enter the change:",font=('Cascadia Mono SemiLight',14),bg='#42c8f5')

        #Placing labels
        lab0.pack()
        lab6.place(x=10,y=50)
        lab1.place(x=10,y=80)
        lab2.place(x=10,y=110)
        lab3.place(x=10,y=140)
        lab4.place(x=10,y=170)
        lab5.place(x=10,y=200)
        lab9.place(x=10,y=230)
        lab7.place(x=10,y=260)
        lab8.place(x=10,y=290)

        #Initialising variables to read entry box
        upe=StringVar()
        fi=StringVar()
        fich=StringVar()

        #Creating entry boxes
        en1=tk.Entry(idtk,textvariable=upe,font=('Cascadia Mono SemiLight',14)) 
        en2=tk.Entry(idtk,textvariable=fi,font=('Cascadia Mono SemiLight',14)) 
        en3=tk.Entry(idtk,textvariable=fich,font=('Cascadia Mono SemiLight',14)) 

        #Placing entry boxes
        en1.place(x=650,y=52)
        en2.place(x=300,y=262)
        en3.place(x=200,y=294)
                
        #Function to execute query for updating record using IMDB ID
        def finallyupdating(event=None):
            
            #Getting information from entry boxes
            up=upe.get()
            fields=int(fi.get())
            fieldch=fich.get()

            #Checking for which data is to be updated
            if fields==1:
                field='Movie_Name'
            elif fields==2:
                field='Genre'
            elif fields==3:
                field='Date_of_release'
            elif fields==4:
                field='IMDB_id'
            elif fields==5:
                field='Director'
            elif fields==6:
                field='Rating'

            #Connecting to MySQL and executing the query
            mydb= sq.connect(host="localhost",user="root",passwd="root",database="Movie_database")
            cursor=mydb.cursor()
            update="UPDATE Movies set {} = '{}' WHERE IMDB_ID= '{}'".format(field,fieldch,up)
            cursor.execute(update)
            mydb.commit()

            #Displaying message for successful update
            lab0=tk.Label(idtk,text="Record Updated!",font=('Cascadia Mono SemiLight',24),bg='#42c8f5')
            lab0.place(x=240,y=325)

            #Setting all entry boxes to blank so that more updates can be made
            upe.set('')
            fi.set('')
            fich.set('')

        #Function to ask confirmation from user for quiting
        def on_closingid():
            if messagebox.askyesno(title='QUIT?',message='Are you sure you want to quit'):
                nonlocal idtk
                idtk.destroy() #Closing this window
                recreate_root() #Re-opening root window
            else:
                pass
        idtk.bind_all('<Return>', finallyupdating)
        idtk.protocol('WM_DELETE_WINDOW',on_closingid)
        
    updatetk.bind_all('<Return>', updateit)
    updateit()    
    updatetk.protocol('WM_DELETE_WINDOW',on_closing)
    updatetk.mainloop()

#Function for deleting a record 
def delete():

    #Closing menu window
    root.destroy()

    #Creating window to delete a record
    deletetk=tk.Tk()
    deletetk.geometry('1000x100')
    deletetk.configure(bg='#42c8f5')
    deletetk.title('Delete Record')

    #Asking user if they want to use the movie name or IMDB ID to delete the record
    #Creating labels
    lab0=tk.Label(deletetk,text='Delete Record',font=('Cascadia Mono SemiLight',18,'bold'),bg='#42c8f5')
    lab1=tk.Label(deletetk,text='Enter 1 to use movie name or 2 to use IMDB ID to delete the data:',font=('Cascadia Mono SemiLight',14),bg='#42c8f5')

    #Placing labels
    lab0.pack()
    lab1.place(x=10,y=50)

    #Initializing variable to read the entry box data
    val=StringVar()

    #Creating and placing entry box
    en1=tk.Entry(deletetk,textvariable=val,font=('Cascadia Mono SemiLight',14))
    en1.place(x=730,y=53)

    #Function to ask for confirmation and close the window 
    def on_closing():
            if messagebox.askyesno(title='QUIT?',message='Are you sure you want to quit'):
                nonlocal deletetk
                deletetk.destroy() #Closing this window
                recreate_root() #Re-opening root window
            else:
                pass
    deletetk.protocol('WM_DELETE_WINDOW',on_closing)

    #Checking whether user wants to delete using movie name or IMDB ID
    def deleteit(event=None):
        char=val.get()
        while char!='':
            if char=='1':
                deletewithname()
                break                
            elif char=='2':
                deletewithid()
                break

    #Function to delete using movie name                
    def deletewithname():

        #Closing choice window
        nonlocal deletetk
        deletetk.destroy()

        #Creating window to delete using movie name
        nametk=tk.Tk()
        nametk.geometry('1060x130')
        nametk.configure(bg='#42c8f5')
        nametk.title('Deleting Record using name')
        
        #Creating labels 
        lab0=tk.Label(nametk,text='Delete Record',font=('Cascadia Mono SemiLight',18,'bold'),bg='#42c8f5')
        lab1=tk.Label(nametk,text='Enter the name of the movie whose data you want to delete: ',font=('Cascadia Mono SemiLight',18),bg='#42c8f5')

        #Placing labels
        lab0.pack()
        lab1.place(x=10,y=50)
        
        #Initialising variable to read entry box
        de=StringVar()

        #Creating and placing entry box
        en1=tk.Entry(nametk,textvariable=de,font=('Cascadia Mono SemiLight',14)) 
        en1.place(x=825,y=59)
               
        #Function to execute query for deleteing record using movie name
        def finallydeleting(event=None):
            #Getting information from entry box
            dele=de.get()

            #Connecting to MySQL and executing the query
            c=sq.connect(host="localhost",user="root",passwd="root",database="movie_database")
            cursor=c.cursor()
            sql="DELETE FROM Movies WHERE Movie_Name like '%{}%'".format(dele)
            cursor.execute(sql)
            c.commit()

            #Displaying message for successful delete
            lab2=tk.Label(nametk,text="Record Deleted!",font=('Cascadia Mono SemiLight',15,'bold'),bg='#42c8f5')
            lab2.place(x=400,y=90)
            
            #Setting all entry boxes to blank so that more updates can be done
            de.set('')

        #Function to ask confirmation from user for quiting
        def on_closingname():
            if messagebox.askyesno(title='QUIT?',message='Are you sure you want to quit'):
                nonlocal nametk
                nametk.destroy() #Closing this window
                recreate_root() #Re-opening root window
            else:
                pass 
        nametk.bind_all('<Return>', finallydeleting)
        nametk.protocol('WM_DELETE_WINDOW',on_closingname)

    #Function to delete using IMDB ID            
    def deletewithid():

        #Closing choice window
        nonlocal deletetk
        deletetk.destroy()

        #Creating window to delete using movie name       
        idtk=tk.Tk()
        idtk.geometry('1150x110')
        idtk.configure(bg='#42c8f5')
        idtk.title('Deleting Record using IMDB ID')
        
        #Creating labels 
        lab0=tk.Label(idtk,text='Delete Record',font=('Cascadia Mono SemiLight',18,'bold'),bg='#42c8f5')
        lab1=tk.Label(idtk,text='Enter the IMDB ID of the movie whose data you want to delete: ',font=('Cascadia Mono SemiLight',18),bg='#42c8f5')

        #Placing labels
        lab0.pack()
        lab1.place(x=10,y=50)
        
        #Initialising variable to read entry box
        de=StringVar()

        #Creating and placing entry boxes
        en1=tk.Entry(idtk,textvariable=de,font=('Cascadia Mono SemiLight',14)) 
        en1.place(x=870,y=59)
               
        #Function to execute query for deleteing record using IMDB ID
        def finallydeleting(event=None):
            #Getting information from entry box
            dele=de.get()
            
            #Connecting to MySQL and executing the query
            c=sq.connect(host="localhost",user="root",passwd="root",database="movie_database")
            cursor=c.cursor()
            sql="DELETE FROM Movies WHERE IMDB_id like '%{}%'".format(dele)
            cursor.execute(sql)
            c.commit()

            #Displaying message for successful delete
            lab2=tk.Label(idtk,text="Record Deleted!",font=('Cascadia Mono SemiLight',15,'bold'),bg='#42c8f5')
            lab2.place(x=320,y=80)
            
            #Setting all entry boxes to blank so that more updates can be done
            de.set('')

        #Function to ask confirmation from user for quiting
        def on_closingid():
            if messagebox.askyesno(title='QUIT?',message='Are you sure you want to quit'):
                nonlocal idtk
                idtk.destroy() #Closing this window
                recreate_root() #Re-opening root window
            else:
                pass 
        idtk.bind_all('<Return>', finallydeleting)
        idtk.protocol('WM_DELETE_WINDOW',on_closingid)
        
    deletetk.bind_all('<Return>',deleteit)
    deleteit()      
    deletetk.mainloop()
    

#Function for searching a record
def search():

    #Closing menu window
    root.destroy()

    #Creating window to search a record
    searchtk=tk.Tk()
    searchtk.geometry('1000x100')
    searchtk.configure(bg='#42c8f5')
    searchtk.title('Search Record')
    
    #Asking user if they want to use the movie name or IMDB ID to search the record
    #Creating labels
    lab0=tk.Label(searchtk,text='Search Record',font=('Cascadia Mono SemiLight',18,'bold'),bg='#42c8f5')
    lab1=tk.Label(searchtk,text='Enter 1 to use movie name or 2 to use IMDB ID to search the data:',font=('Cascadia Mono SemiLight',14),bg='#42c8f5')

    #Placing labels
    lab0.pack()
    lab1.place(x=10,y=50)

    #Initializing variable to read the entry box data
    val=StringVar()

    #Creating and placing entry box
    en1=tk.Entry(searchtk,textvariable=val,font=('Cascadia Mono SemiLight',14))
    en1.place(x=730,y=53)

    #Function to ask for confirmation and close the window     
    def on_closing():
            if messagebox.askyesno(title='QUIT?',message='Are you sure you want to quit'):
                nonlocal searchtk
                searchtk.destroy() #Closing this window
                recreate_root() #Re-opening root window
            else:
                pass
    searchtk.protocol('WM_DELETE_WINDOW',on_closing)

    #Checking whether user wants to search using movie name or IMDB ID
    def searchit(event=None):
        char=val.get()
        while char!='':
            if char=='1':
                searchwithame()
                break                
            elif char=='2':
                searchwithid()
                break

    #Function to search using movie name            
    def searchwithame():

        #Closing choice window
        nonlocal searchtk
        searchtk.destroy()

        #Creating window to search using movie name
        nametk = tk.Tk()
        nametk.geometry('950x100')
        nametk.configure(bg='#42c8f5')
        nametk.title('Searching Record using Movie Name')

        #Creating labels
        lab0 = tk.Label(nametk, text='Search Record', font=('Cascadia Mono SemiLight', 18, 'bold'), bg='#42c8f5')
        lab1 = tk.Label(nametk, text='Enter the name of the movie whose data you want to search: ', font=('Cascadia Mono SemiLight', 14), bg='#42c8f5')

        #Placing labels
        lab0.pack()
        lab1.place(x=10,y=50)

        #Initializing variable to read entry box
        search = StringVar()

        #Creating and placing entry box
        en1 = tk.Entry(nametk, textvariable=search, font=('Cascadia Mono SemiLight', 14))
        en1.place(x=650,y=53)

        #Function to execute query for searching record using movie name and displaying it
        def finallysearching(event=None):
            try:
                #Getting information from entry box
                name = search.get()

                #Connecting to MySQL and executing the query
                mydb = sq.connect(host='localhost', user='root', password='root', database='movie_database')
                cursor = mydb.cursor()
                cursor.execute("SELECT * FROM Movies WHERE Movie_Name LIKE '%{}%'".format(name))

                #Reading the output provied by MySQL
                result = cursor.fetchall()

                #Displaying output according to the result obtained from the query
                #If record exists
                if result:
                    
                    #New window to display data
                    display_window = tk.Tk()
                    display_window.geometry('600x100')
                    display_window.configure(bg='#42c8f5')
                    display_window.title('Search Results for Movie Name')

                    #Creating header labels for the table
                    header_labels = ['Movie Name', 'IMDB ID', 'Director', 'Year', 'Genre']
                    for i, header in enumerate(header_labels):
                        tk.Label(display_window, text=header, font=('Cascadia Mono SemiLight', 16), bg='#42c8f5').grid(row=0, column=i, padx=10, pady=10)

                    #Adding movie records in rows
                    for i, record in enumerate(result):
                        for j, value in enumerate(record[1:]):
                            tk.Label(display_window, text=value, font=('Cascadia Mono SemiLight', 14), bg='#42c8f5').grid(row=i + 1, column=j, padx=10, pady=5)

                    display_window.mainloop()

                #If record does not exist
                else:
                    messagebox.showinfo("No Results", "No records found for the given movie name.")

            except Exception as e:
                print(f"Error: {e}")

        #Function to ask confirmation from user for quiting
        def on_closingname():
            if messagebox.askyesno(title='QUIT?',message='Are you sure you want to quit'):
                nonlocal nametk
                nametk.destroy() #Closing this window
                recreate_root() #Re-opening root window
            else:
                pass 
        nametk.bind_all('<Return>', finallysearching)
        nametk.protocol('WM_DELETE_WINDOW', on_closingname)

    #Function to search using movie name   
    def searchwithid():

        #Closing choice window
        nonlocal searchtk
        searchtk.destroy()

        #Creating window to search using IMDB ID
        idtk = tk.Tk()
        idtk.geometry('950x100')
        idtk.configure(bg='#42c8f5')
        idtk.title('Searching Record using IMDB ID')

        #Creating labels
        lab0 = tk.Label(idtk, text='Search Record', font=('Cascadia Mono SemiLight', 18, 'bold'), bg='#42c8f5')
        lab1 = tk.Label(idtk, text='Enter the IMDB ID of the movie whose data you want to search: ', font=('Cascadia Mono SemiLight', 14), bg='#42c8f5')

        #Placing labels
        lab0.pack()
        lab1.place(x=10,y=50)

        #Initializing variable to read entry box
        search = StringVar()

        #Creating and placing entry box
        en1 = tk.Entry(idtk, textvariable=search, font=('Cascadia Mono SemiLight', 14))
        en1.place(x=690,y=53)

        #Function to execute query for searching record using movie name and displaying it
        def finallysearching(event=None):
            try:
                #Getting information from entry box
                idd = search.get()

                #Connecting to MySQL and executing the query
                mydb = sq.connect(host='localhost', user='root', password='root', database='movie_database')
                cursor = mydb.cursor()
                cursor.execute("SELECT * FROM Movies WHERE IMDB_id LIKE '%{}%'".format(idd))

                #Reading the output provied by MySQL
                result = cursor.fetchall()

                #Displaying output according to the result obtained from the query
                #If record exists
                if result:
                    
                    #New window to display data
                    display_window = tk.Tk()
                    display_window.geometry('600x100')
                    display_window.configure(bg='#42c8f5')
                    display_window.title('Search Results for Movie Name')

                    #Creating header labels for the table
                    header_labels = ['Movie Name', 'IMDB ID', 'Director', 'Year', 'Genre']
                    for i, header in enumerate(header_labels):
                        tk.Label(display_window, text=header, font=('Cascadia Mono SemiLight', 16), bg='#42c8f5').grid(row=0, column=i, padx=10, pady=10)

                    #Adding movie records in rows
                    for i, record in enumerate(result):
                        for j, value in enumerate(record[1:]):  
                            tk.Label(display_window, text=value, font=('Cascadia Mono SemiLight', 14), bg='#42c8f5').grid(row=i + 1, column=j, padx=10, pady=5)

                    display_window.mainloop()
                else:
                    messagebox.showinfo("No Results", "No records found for the given IMDB ID.")
            except Exception as e:
                print(f"Error: {e}")

        #Function to ask confirmation from user for quiting
        def on_closingid():
            if messagebox.askyesno(title='QUIT?',message='Are you sure you want to quit'):
                nonlocal idtk
                idtk.destroy() #Closing this window
                recreate_root() #Re-opening root window
            else:
                pass 
        idtk.bind_all('<Return>', finallysearching)
        idtk.protocol('WM_DELETE_WINDOW', on_closingid)

    searchtk.bind_all('<Return>',searchit)

#Function for displaying the data
def display():

    #Closing menu window
    root.destroy()

    #Creating window to search a record    
    displaytk=tk.Tk()
    displaytk.configure(bg='#42c8f5')
    displaytk.geometry('1000x550')
    displaytk.title('Display Record')

    #Connecting to MySQL and executing the query
    mydb=sq.connect(host="localhost", user="root", password="root", database="movie_database")
    cursor=mydb.cursor()
    sql="SELECT * FROM Movies ORDER BY Movie_Name"
    cursor.execute(sql)
    myresult=cursor.fetchall()

    #Creating a frame
    container=tk.Frame(displaytk, bg='#42c8f5')
    container.pack(fill='both', expand=True)

    #Creating the canvas and the scrollbar
    canvas = tk.Canvas(container, bg='#42c8f5')
    scrollbar = tk.Scrollbar(container, orient='vertical', command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg='#42c8f5')

    #Configuring the scrollable frame
    scrollable_frame.bind("<Configure>",lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    #Adding the header labels
    header_labels = ['Movie Name', 'Genre', 'Date of Release', 'IMDB Id', 'Director', 'Rating']
    for i, header in enumerate(header_labels):
        tk.Label(scrollable_frame, text=header, font=('Cascadia Mono SemiLight', 16), bg='#42c8f5').grid(row=0, column=i, padx=10, pady=10)

    #Adding movie records in rows
    for i, record in enumerate(myresult):
        for j, value in enumerate(record):
            tk.Label(scrollable_frame, text=value, font=('Cascadia Mono SemiLight', 14), bg='#42c8f5').grid(row=i+1, column=j, padx=10, pady=5)

    #Placing the canvas and the scrollbar
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    #Function to ask confirmation from user for quitting
    def on_closing():
        if messagebox.askyesno(title='QUIT?', message='Are you sure you want to quit'):
            displaytk.destroy()  #Closing this window
            recreate_root()  #Re-opening root window
        else:
            pass

    displaytk.protocol('WM_DELETE_WINDOW', on_closing)
    displaytk.mainloop()

#Root window
root=tk.Tk()
root.geometry('690x350')
root.configure(bg='#42c8f5')
root.title('Menu')
lab3=tk.Label(root, text="WELCOME TO BLOCKBUSTER: A Movie Database",font=('Cascadia Mono SemiLight',16,'bold'),bg='#42c8f5')
lab6=tk.Label(root, text="Made By: Atharava Srivastava",font=('Cascadia Mono SemiLight',16,'bold'),bg='#42c8f5')
lab3.pack()  
lab6.pack()    

lin1=tk.Label(root,text="1.Insert new data ",font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
lin2=tk.Label(root,text="2.Update the table",font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
lin3=tk.Label(root,text="3.Delete the record from the table",font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
lin4=tk.Label(root,text="4.Search a record from the table",font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
lin5=tk.Label(root,text="5.Display the table",font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
lin6=tk.Label(root,text="6.Quit",font=('Cascadia Mono SemiLight',14),bg='#42c8f5')

lin1.place(x=10,y=80)
lin2.place(x=10,y=110)
lin3.place(x=10,y=140)
lin4.place(x=10,y=170)
lin5.place(x=10,y=200)
lin6.place(x=10,y=230)

ch=StringVar()
   
lab1=tk.Label(root,text="Which function do you want to apply?:",font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
lab1.place(x=10,y=260)
en1=tk.Entry(root, textvariable=ch, font=('Cascadia Mono SemiLight',14))
en1.place(x=420,y=263)

#Function to ask confirmation from user for quiting
def on_closing():
        if messagebox.askyesno(title='QUIT?',message='Are you sure you want to quit'):
            root.destroy() #Closing root window
        else:
            pass

#Function to accept the choice user from menu items
def choicefunc(event=None):
    choice=ch.get()
    #To insert new data
    if choice=='1':  
        insert()
    #To update a record
    elif choice=='2':
        update()   
    #To delete a record
    elif choice=='3':
        delete()  
    #To search a record
    elif choice=='4':
        search()
    #To display the data
    elif choice=='5':
        display()
    #To exit the program
    elif choice=='6':
        exit_=tk.Tk()
        exit_.geometry('500x100')
        exit_.config(bg='#42c8f5')
        exit_.title('Exit')
        label_0=tk.Label(exit_, text="Thank You!",font=('Cascadia Mono SemiLight',16,'bold'),bg='#42c8f5')
        label_1=tk.Label(exit_, text="Hope you have a nice day!",font=('Cascadia Mono SemiLight',16,'bold'),bg='#42c8f5')
        label_0.pack()
        label_1.pack()
        root.destroy()
    #Invaild input
    else:
        lab2=tk.Label(root,text="Please Enter Valid Input!",font=('Cascadia Mono SemiLight',15),bg='#42c8f5')
        lab2.place(x=170,y=300)
        ch.set('')
        
en1.bind('<Return>',choicefunc)
