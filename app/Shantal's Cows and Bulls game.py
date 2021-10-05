import random
from tkinter import *

letters =["A", "B", "C", "D", "E"]
win = False
key = ""

for i in range (4):
    key += random.choice(letters)
    
letterdic = dict(zip(list(key),[0]*len(key)))
print(key)
bull = 0
cow = 0

def pickChoice():
    global bull, cow,letterdic
    
    guess = default.get() + default2.get() + default3.get() + default4.get()

    if guess == key:
        win = True
        bull = 4

        print ("You Win!!!")
        l = Label(scrollable_frame, text = "You Win!", bg = "beige", font =("Didact Gothic", 75))
        l.pack()
        
    else:
        dummy = list(key)
        for i in range(len(guess)):
            if(guess[i] not in key):
                continue
            #check them seperatly and check bulls then cows
            else:
                if (guess[i]==key[i]):
                    bull = bull + 1
                    dummy[i] = "*"
                
        for i in range(len(guess)):
            if(guess[i] in dummy):
                dummy[dummy.index(guess[i])] = "*"
                cow = cow + 1
                    

    l = Label(scrollable_frame, text = "Bull = " +str(bull) + ", " +"Cow = " + str(cow) + "  " +guess, bg = "beige", font =("Didact Gothic", 12))
    l.pack()
    
    bull = 0
    cow = 0
    letterdic = dict(zip(list(key),[0]*len(key)))


window = Tk()
window.geometry("2000x1000")
window.configure(bg = "beige")

#instructions
instructions = Label(window,text = """Welcome to my Cows and Bulls game. I will have a 4 digit combonation using the letters A, B, C, D, and E. Then you will guess the combonation.
Every letter that is in the correct combonation counts as a Cow.  A letter that is correct AND in the right place is a Bull. Using this information,
try to get the right combonation in 20 guesses.""", width = 130, height = 5, bg = "beige", fg = "black", font = ("Didact Gothic",20) )
instructions.pack(padx = 10, pady = 0)

#letter guess dropdown
frame1 = Frame(window)
letters = ["A", "B", "C", "D", "E"]

default = StringVar(frame1)
default.set("A")
dropdown = OptionMenu(frame1, default, *letters)
dropdown.config(bg = "black",fg = "white", width=5, height = 2)
dropdown["menu"].config(bg = "black",fg = "white", font = ("Didact Gothic", 13))

default2 = StringVar(frame1)
default2.set("A")
dropdown2 = OptionMenu(frame1, default2, *letters)
dropdown2.config(bg = "black",fg = "white", width=5, height = 2)
dropdown2["menu"].config(bg = "black",fg = "white", font = ("Didact Gothic", 13))

default3 = StringVar(frame1)
default3.set("A")
dropdown3 = OptionMenu(frame1, default3, *letters)
dropdown3.config(bg = "black",fg = "white", width=5, height = 2)
dropdown3["menu"].config(bg = "black",fg = "white", font = ("Didact Gothic", 13))

default4 = StringVar(frame1)
default4.set("A")
dropdown4 = OptionMenu(frame1, default4, *letters)
dropdown4.config(bg = "black",fg = "white", width=5, height = 2)
dropdown4["menu"].config(bg = "black",fg = "white", font = ("Didact Gothic", 13))

#where the letters go
dropdown.pack(side = LEFT)
dropdown2.pack(side = LEFT)
dropdown3.pack(side = LEFT)
dropdown4.pack(side = LEFT)

#pack frame
frame1.pack()

#submit button
submitbutton = Button(window,text = "Submit", width=15, height = 3, font = ("Didact Gothic", 16),command = pickChoice)
submitbutton.config(bg = "black",fg = "white")
submitbutton.config(bg = "black",fg = "white")

submitbutton.pack(pady = 15)

#results
container = Frame(window, borderwidth = 7, relief = "solid")
canvas = Canvas(container, bg = "beige")
scrollbar = Scrollbar(container, orient = "vertical", command = canvas.yview,bg="beige")
scrollable_frame = Frame(canvas,bg="beige")

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion = canvas.bbox("all")
    )
)

canvas.create_window((0,0), window = scrollable_frame, anchor = "nw")

canvas.configure(yscrollcommand = scrollbar.set)

    
container.pack()
canvas.pack()
canvas.pack(side = "left", fill = "both", expand = True)
scrollbar.pack(side = "right", fill = "y")





window.mainloop()

#game


##print ("""Welcome to my Cows and Bulls game. I will have a 4 digit combonation using the letters A, B, C, D, and E. Then you will guess the combonation.
##Every letter that is in the correct combonation counts as a Cow.  A letter that is correct AND in the right place is a Bull. Using this information,
##try to get the right combonation in 20 guesses. """)






