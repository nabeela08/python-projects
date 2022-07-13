from cgitb import text
from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

#Label
my_label = Label(text="I am a Label", font=("Comic Sans MS", 18, "bold"))
my_label.pack()
my_label["text"] = "New Text"
my_label.config(text="New Text")

#Button
def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

button = Button(text="Click Me", command=button_clicked)
button.pack()

#Entries
entry = Entry(width=30)
# add some text to begin with 
entry.insert(END, string="Some text to begin with.")
# gets text in entry    
print(entry.get())
entry.pack()  

#Text
text = Text(height=5, width=35)
#puts cursor in textbox
text.focus()
#adds some text to begin with
text.insert(END, "Example of multiline text entry")
#gets current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()

#Spinbox
def spinbox_used():
    #gets the current value in spinbox
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=100, width=5, command=spinbox_used)
spinbox.pack()

#Scale
#called with current scale values
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbutton
def checkbutton_used():
    #prints 1 if On button checked otherwise 0
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()




window.mainloop()