

#Hier erstelle ich den Objekt pet als Klasse
class pet :
    def __init__(self, name, rasse, alter): 
        # Ich benutze __init__ Methode weil ich dabei diversen values, Attributen, properties sowie andere Operationen übertragen kann.
        #In meinem Beispiel gibt es drei grundlegende Attribute als Name, Rasse und Alter
        self.name = name
        self.rasse = rasse
        self.alter = alter
        print("name:",self.name,"rasse : ",self.rasse,"alter:",self.alter) #Diese Zeile ist um Informationen von meiner Katze in Console zu zeigen
   

#Oben musste ich diese Parametern mit self verknüpfen weil um diesen Class abzurufen sowie Objekte auf diese Klasse erstellen zu können
#self Parameter ist ein Parameter zu Instanzen von diesem Class. Ich will bei der Instanzierung Name, Rasse und Alter setzen und übergeben
#wir können auf die Eigenschaften von Objekten mit diesem Parameter als self zugreifen.



#Unten definiere ich die Methoden, womit ich meine Katze beschäftigen kann.
#Ich werde mit meiner Katze spielen, sie streicheln und sie fressen.

    def spielen(self):
        print("Ich spiele mit" + " " + self.name) #Hier bedeutet " " dass es eine leerzeichen gibt, ich will eine leerzeichen vor Duman haben. Und self.name ruft Name von meine Katze Duman
        
        
    def streicheln(self):
        print("Ich streichle meine Katze")
       

    def fressen(self):
        print ("Es ist jetzt Zeit" + " " + self.name + " " + "zu fressen")
        
        
#Unten erstelle ich meine Objekt. Sie ist mein erste Pet Cat als ich als Kind hatte, heisst Duman und ich hatte sie für 2 Jahren.
#Diese Objekt definieren gehört zu Aufgabe 1 aber ich sollte meine Objekt hier definieren weil sonst ich Probleme mit funktioneren von Methoden haben kann.
    
x = pet("Duman", "cat", 2)

#Unten benutze ich die Methoden, die ich erstellt habe. Ich muss diese Methoden mit meiner Objekt verknüpfen, sodass sie richtig funktionieren
x.spielen()
x.streicheln()
x.fressen()



#Now creating a GUI with TKinter and create a button with the function/method of a countdown from 10.
#Firstly we import from tkinter

from tkinter import *
from time import sleep

#here we define a counter
def counter():
    t= 10
    while t>-1 :  #its a loop for counting time
        l1.config(text=t)
        root.update()  #for update  root window 
        sleep(1)   # stop for 1 sec   
        t=t-1 # make new number 

root= Tk()
root.geometry("150x150") 
root.configure(bg="orange") # change background
b1 = Button(root,text="start now",command=counter)   # button for call counter function
l1 = Label(root ,text = "click to start",bg="orange") # at first show's  click to start after click button  show's count down
b1.grid(row=0,column=0,padx=20,pady=10) #position of button
l1.grid(row=1,column=0,padx=20,pady=10) # position of Label



root.mainloop()

