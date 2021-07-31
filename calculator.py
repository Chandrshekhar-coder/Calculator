from tkinter import *
from tkinter import messagebox
from math import *
import pyttsx3
from numpy import log as ln
import math
# Function body...........
'''
def speak(content):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(content)
    engine.runAndWait()
'''

def backButton(s_frame):
    # print("Back")
    s_frame.pack_forget()
    frame.pack(side=TOP)


def open_new_window():
    # print("open")
    frame.pack_forget()

    # creating new frame.........
    s_frame = Frame(window)
    s_frame.pack(side=TOP)

    backBtn = Button(s_frame, text="⇐", font=font, width=6, activebackground='red',command=lambda: backButton(s_frame))
    backBtn.grid(row=0, column=0)

    sinBtn = Button(s_frame, text="sin", font=font, width=6, activebackground='blue')
    sinBtn.grid(row=0, column=1)

    cosBtn = Button(s_frame, text="cos", font=font, width=6, activebackground='blue')
    cosBtn.grid(row=0, column=2)
    
    tanBtn = Button(s_frame, text="tan", font=font, width=7, activebackground='blue')
    tanBtn.grid(row=0, column=3)

    logBtn = Button(s_frame, text="log", font=font, width=7, activebackground='blue')
    logBtn.grid(row=1, column=3)

    obrktBtn = Button(s_frame, text="(", font=font, width=6, activebackground='blue')
    obrktBtn.grid(row=2, column=0)

    lnBtn = Button(s_frame, text="ln", font=font, width=6, activebackground='blue')
    lnBtn.grid(row=1, column=2)

    piBtn = Button(s_frame, text="∏", font=font, width=6, activebackground='blue')
    piBtn.grid(row=2, column=2)

    eBtn = Button(s_frame, text="e", font=font, width=6, activebackground='blue')
    eBtn.grid(row=3, column=0)

    

    cbrktBtn = Button(s_frame, text=")", font=font, width=6, activebackground='blue')
    cbrktBtn.grid(row=2, column=1)

    powBtn = Button(s_frame, text="pow", font=font, width=6, activebackground='blue')
    powBtn.grid(row=1, column=1)

    cBtn = Button(s_frame, text="C", relief='ridge' ,font=font, width=7, activebackground='red',activeforeground = 'white', command=c_field)
    cBtn.grid(row=3, column=3)

    sqrtBtn = Button(s_frame, relief='ridge', text="sqrt", activebackground='blue', activeforeground='white', font=font,width=6)
    sqrtBtn.grid(row=1, column=0)

    eqlBtn = Button(s_frame, relief='ridge', text="=", activebackground='green', activeforeground='white', font=font, width=6)
    eqlBtn.grid(row=3, column=2)

    camaBtn = Button(s_frame, text=",", font=font, width=6, activebackground='blue')
    camaBtn.grid(row=3, column=1)

    AcBtn = Button(s_frame, text="AC",relief = 'ridge', font=font, width=7, activebackground='red' , command = ac_field)
    AcBtn.grid(row=2, column=3)


   
    logBtn.bind('<Button-1>', set_text)
    lnBtn.bind('<Button-1>', set_text)
    cosBtn.bind('<Button-1>', set_text)
    sinBtn.bind('<Button-1>', set_text)
    cosBtn.bind('<Button-1>', set_text)
    tanBtn.bind('<Button-1>', set_text)
    obrktBtn.bind('<Button-1>', set_text)
    cbrktBtn.bind('<Button-1>', set_text)
    powBtn.bind('<Button-1>', set_text)
    piBtn.bind('<Button-1>', set_text)
    eBtn.bind('<Button-1>', set_text)
    sqrtBtn.bind('<Button-1>', set_text)
    eqlBtn.bind('<Button-1>', set_text)
    camaBtn.bind('<Button-1>', set_text)

  


f = False




def set_text(event):
    global f
    # print("button clicked")
    b = event.widget
    text = b['text']
    # speak(text)
    if text == "X":
        field.insert(END, '*')
        return
    if text == "=":
        try:
            ex = field.get()
            ans = eval(ex)
            # speak(ans)
            field.delete(0, END)
            field.insert(0, ans)
            f = True
        except Exception as e:
            messagebox.showerror("Something went wrong", e)
        return
    
    if text == "e":
        field.insert(END,"2.71828183")
        return

    if text == "∏":
        field.insert(END,"3.14159265")
        return
    # print(text)
    
    if f == True and text in ['+', '-', 'X', '÷', '%']:
        field.insert(END, text)
        f = False
    elif f == True:
        field.delete(0, END)
        field.insert(END, text)
        f = False
    else:
        field.insert(END, text)


def c_field():
    t = field.get()
    field.delete(len(t)-1, END)
    # speak(cBtn)

def ac_field():
    t = field.get()
    field.delete(0,END)


# End of function..........

font = ('Helvetica', 18, 'bold')
# creaye a window--------
window = Tk()
window.title("Calculator")
window.geometry('426x508+20+20')
# (widthxheight+x+y)
# picture lable...........
img = PhotoImage(file='PHOTO.png')
picLabel = Label(window, image=img)
picLabel.pack(side=TOP, pady=10)
# heading..........
headingLabel = Label(window, text="Calculator", font=font, underline=1)
headingLabel.pack(side=TOP)

# textfield.......:

field = Entry(window, font=font, justify=CENTER)
field.pack(side=TOP, pady=5, fill=X)

# frame...............

frame = Frame(window)
frame.pack(side=TOP)

# buttons....
# b1=Button(frame,text="1",font=font)
# b1.grid(row=0,column=0)
# b2=Button(frame,text="2",font=font)
# b2.grid(row=0,column=1)
temp = 1
for i in range(0, 3):
    for j in range(0, 3):
        button = Button(frame, relief='ridge', text=str(temp), activebackground='blue', activeforeground='white',font=font, width=5)
        temp = temp + 1

        # bind buttion
        button.bind('<Button-1>', set_text)
        button.grid(row=i, column=j)

# other button.......
plusBtn = Button(frame, relief='ridge', text="+", activebackground='blue', activeforeground='white', font=font, width=5)
plusBtn.grid(row=0, column=3)

minusBtn = Button(frame, relief='ridge', text="-", activebackground='blue', activeforeground='white', font=font, width=5)
minusBtn.grid(row=1, column=3)

multBtn = Button(frame, relief='ridge', text="X", activebackground='blue', activeforeground='white', font=font, width=5)
multBtn.grid(row=2, column=3)

zeroBtn = Button(frame, relief='ridge', text="0", activebackground='blue', activeforeground='white', font=font, width=5)
zeroBtn.grid(row=3, column=0)

pointBtn = Button(frame, relief='ridge', text=".", activebackground='blue', activeforeground='white', font=font, width=5)
pointBtn.grid(row=3, column=1)

cBtn = Button(frame, relief='ridge', text="C", activebackground='red', activeforeground='white', font=font,command=c_field, width=5)
cBtn.grid(row=3, column=4)

divBtn = Button(frame, relief='ridge', text="/", activebackground='blue', activeforeground='white', font=font, width=5)
divBtn.grid(row=3, column=3)

MoreBtn = Button(frame, relief='ridge', text="⇒", activebackground='red', activeforeground='white', font=font,width=5, command=open_new_window)
MoreBtn.grid(row=0, column=4)

rimdrBtn = Button(frame, relief='ridge', text="%", activebackground='blue', activeforeground='white', font=font, width=5)
rimdrBtn.grid(row=1, column=4)

AcBtn = Button(frame, text="AC",relief = 'ridge', font=font, width=5, activebackground='red' , command = ac_field)
AcBtn.grid(row=2, column=4)

eqlBtn = Button(frame, relief='ridge', text="=", activebackground='green', activeforeground='white', font=font, width=5)
eqlBtn.grid(row=3, column=2)

# bind the button
plusBtn.bind('<Button-1>', set_text)
minusBtn.bind('<Button-1>', set_text)
multBtn.bind('<Button-1>', set_text)
divBtn.bind('<Button-1>', set_text)
eqlBtn.bind('<Button-1>', set_text)
rimdrBtn.bind('<Button-1>', set_text)
pointBtn.bind('<Button-1>', set_text)
zeroBtn.bind('<Button-1>', set_text)

window.mainloop()
