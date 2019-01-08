from tkinter import *
from PIL import Image, ImageTk
import sqlite3


'''
c.execute("""Create TABLE Pokemon (
            name,
            ability,
            item,
            firstMove,
            secondMove,
            thirdMove,
            fourthMove
            )""")


c.execute("""Create TABLE Moveset(
            name,
            moveset
            )""")
'''

class Mon:
    def __init__(self,name,ability,item,m1,m2,m3,m4):
        self.name = name
        self.ability = ability
        self.item = item
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.m4 = m4
        self.moveset = [m1,m2,m3,m4].sort()

    #writing/printing
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
        entryLabel = Label(self, text = "Entry Page", font = " none 12 bold")
        entryLabel.pack(pady=10,padx=10, side = "top")

        #enter name label
        nameLabel = Label(self, text = "Name", font = "none 12 bold")
        nameLabel.pack( padx = 20)

        #name text field
        nameEntry = Entry(self, width = 20, bg = 'white')
        nameEntry.pack()


        #ability

        abilityLabel = Label(self, text = "Ability", font = "none 12 bold")
        abilityLabel.pack( padx = 20)
        #ability text field

        abilityEntry = Entry(self, width = 20, bg = 'white')
        abilityEntry.pack()

        #item
        itemLabel = Label(self, text = "Item", font = "none 12 bold")
        itemLabel.pack( padx = 20)

        #Item text field
        itemEntry = Entry(self, width = 20, bg = 'white')
        itemEntry.pack()

        #move 1
        firstMoveLabel = Label(self, text = "First Move: ", font = "none 12 bold")
        firstMoveLabel.pack( padx = 20)

        #firstMove text field
        firstMoveEntry = Entry(self, width = 20, bg = 'white')
        firstMoveEntry.pack()

        secondMoveLabel = Label(self, text = "Second Move: ", font = "none 12 bold")
        secondMoveLabel.pack( padx = 20)

        #second move text field
        secondMoveEntry = Entry(self, width = 20, bg = 'white')
        secondMoveEntry.pack()

        #thirdMove label
        thirdMoveLabel = Label(self, text = "Third Move: ", font = "none 12 bold")
        thirdMoveLabel.pack()

        #third move text field

        thirdMoveEntry = Entry(self, width = 20, bg = 'white')
        thirdMoveEntry.pack()

        #fourth move label
        fourthMoveLabel = Label(self, text = "Fourth Move: ")
        fourthMoveLabel.pack()

        #fourth move text field
        fourthMoveEntry = Entry(self, width = 20, bg = 'white')
        fourthMoveEntry.pack()


        def callback():
            name = nameEntry.get()
            ability = abilityEntry.get()
            item = itemEntry.get()
            m1 = firstMoveEntry.get()
            m2 = secondMoveEntry.get()
            m3 = thirdMoveEntry.get()
            m4 = fourthMoveEntry.get()
            moveset = [m1,m2,m3,m4]
            moveset = moveset.sort()
            #connects to the database
            moveConn = sqlite3.connect('Moveset.db')
            moveCursor = moveConn.cursor()

            dexConn = sqlite3.connect('dex.db')
            dexCursor = dexConn.cursor()

            userMon = Mon(name, ability, item, m1, m2, m3, m4)

            dexCursor.execute("INSERT INTO Pokemon VALUES('{}','{}','{}','{}','{}','{}','{}')".format(userMon.name,userMon.ability,userMon.item,userMon.m1,userMon.m2,
                                                                                            userMon.m3, userMon.m4))
            dexConn.commit()
            moveCursor.execute("INSERT INTO Moveset VALUES('{}','{}')".format(name, moveset))
            moveConn.commit()

            moveConn.close()
            dexConn.close()

            nameEntry.delete(0,END)
            abilityEntry.delete(0,END)
            itemEntry.delete(0,END)
            firstMoveEntry.delete(0,END)
            secondMoveEntry.delete(0,END)
            thirdMoveEntry.delete(0,END)
            fourthMoveEntry.delete(0,END)



        submitButton = Button(self, text = "submit", command = callback)
        submitButton.pack(padx = 10, pady = 10)


        #back button
        button1 = Button(self, text = "back", command = lambda: controller.show_frame(StartPage))
        button1.pack(side = "bottom")


class LookupPage(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        label = Label(self, text = "lookup", font = "none 12 bold")
        label.pack(pady= 10,padx = 10)

        backButton = Button(self, text = "Back", font = "none 12 bold", command = lambda : controller.show_frame(StartPage))
        backButton.pack(side = "bottom")
class StatsPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self,parent)
        label = Label(self, text = "Stats", font = "none 12 bold")
        label.pack(pady = 10, padx = 10)

        backButton = Button(self, text = "Back", font = "none 12 bold", command = lambda : controller.show_frame(StartPage))
        backButton.pack(side = "bottom")



if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
