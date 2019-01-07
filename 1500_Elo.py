from tkinter import *
#import tkinter as tk
from PIL import Image, ImageTk

class Mon:
    def __init__(self,name,ability,item,m1,m2,m3,m4):
        self.name = name
        self.ability = ability
        self.item = item
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.m4 = m4
        self.moveset = [m1,m2,m3,m4]

    #writing/printing
    def printMon(self):
        #movesetString = "Move 1: " +self.m1 +" Move 2: " + self.m2+" Move 3: " + self.m3+" Move 4: " +self.m4
        #print("Name: " +self.name)# +self.name)# +" Ability " +self.ability+" Item: " +self.item) #+"Moves: " +moveset
        2+2
    def writeMon(self):
        #opens dex file
        text = open("dex.txt", "a+")

        #writing stuff
        text.write("This is working")
        text.write(str(self.name))
        text.write(str(self.ability))

        #saves it
        text.flush()

        #closes dex file
        text.close()



'''UI Stuff '''

'''Main Window'''

class MainWindow(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.title("Path to 1500")
        self.geometry('500x500') # Size 200, 200

        #this container contains all of the pages
        container = Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0,weight = 1) #make the cell in grid cover whole page
        container.grid_columnconfigure(0,weight=1)#same but with column
        self.frames = {}#pages we want to navigate stored here

        for F in (StartPage, EntryPage, LookupPage, StatsPage): #for each page
            frame = F(container, self) #create the page
            self.frames[F] = frame #store into frames
            frame.grid(row=0,column=0,sticky= "nsew")
        self.show_frame(StartPage) #let first page be StartPage

    def show_frame(self,name):
        frame = self.frames[name]
        frame.tkraise()

class StartPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.photo = PhotoImage(file = "Pokedex2.png").subsample(8)
        icon = Label(self, image = self.photo, bg = "white")#.grid(row = 0, column = 1, sticky = W + N )
        icon.pack()



        button1 = Button(self, text='Visit Page 1',  # when click on this button, call the show_frame method to make PageOne appear
                            command=lambda : controller.show_frame(EntryPage))
        button1.pack() # pack it in





        #create label
        entryLabel =Label(self, text= "Entry: ", font = "none 12 bold")
        entryLabel.pack()#.grid(row = 1, column = 0, sticky = W)
        #entryLabel.pack()


        # name label

        #callback function for the button


        #Create Button
        entryButton = Button(self, text = "Create Entries", bg = "white", command = lambda : controller.show_frame(EntryPage))#.grid(row = 1, column = 1, sticky =  N + E)
        entryButton.pack()
        #end entry

        '''Lookup'''
        #Lookup label
        lookupLabel = Label(self, text= "Lookup: ", font =" none 12 bold")#.grid(row = 2, column = 0, sticky = W)
        lookupLabel.pack()
        #lookup Button
        def lookup():
            print("callback 2")
        lookupbutton = Button(self, text = "Lookup Entry", bg = "white", command = lambda : controller.show_frame(LookupPage))#.grid(row = 2, column = 1, sticky = N + E)
        lookupbutton.pack()

        #end lookup


        #stats label
        statsLabel = Label(self, text= "Stats: ", font =" none 12 bold")#.grid(row = 3, column = 0, sticky = W)
        statsLabel.pack();

        #stats button
        statsbutton = Button(self, text = "Stats: ", bg = "white", command = lambda : controller.show_frame(StatsPage))#.grid(row = 3, column = 1, sticky = N + E)
        statsbutton.pack()

class EntryPage(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        label = Label(self, text = "works", font = " none 12 bold")
        label.pack(pady=10,padx=10)

        button1 = Button(self, text = "back", command = lambda: controller.show_frame(StartPage))
        button1.pack()


class LookupPage(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        label = Label(self, text = "lookup", font = "none 12 bold")
        label.pack(pady= 10,padx = 10)

        backButton = Button(self, text = "Back", font = "none 12 bold", command = lambda : controller.show_frame(StartPage))
        backButton.pack()
class StatsPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self,parent)
        label = Label(self, text = "Stats", font = "none 12 bold")
        label.pack(pady = 10, padx = 10)

        backButton = Button(self, text = "Back", font = "none 12 bold", command = lambda : controller.show_frame(StartPage))
        backButton.pack(side = "left")



if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
