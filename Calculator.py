from tkinter import *

#main functions
def but_press(num):
    global equ_text
    equ_text = equ_text + str(num)
    equ_label.set(equ_text)

def equals():
    global equ_text
    try:
        total = str(eval(equ_text))
        equ_label.set(total)
        equ_text=total
    except ZeroDivisionError:
        equ_label.set('Arithmetic error')
        equ_text=''
    except SyntaxError:
        equ_label.set('Syntax error')
        equ_text=''
def clear():
    global equ_text
    equ_label.set('')
    equ_text=''

#creating the window
window = Tk()
window.title('Calculator')
window.geometry('600x600')
equ_label = StringVar()

equ_text=''

label = Label(window,textvariable=equ_label,font=('consolas',20),bg='white',width=20,height=2)
label.pack()

frame = Frame(window)
frame.pack()

#creating the buttons
button1 = Button(frame,text=1,height=4,width=9,font=35,command=lambda : but_press(1))
button1.grid(row=0,column=0)

button2 = Button(frame,text=2,height=4,width=9,font=35,command=lambda : but_press(2))
button2.grid(row=0,column=1)

button3 = Button(frame,text=3,height=4,width=9,font=35,command=lambda : but_press(3))
button3.grid(row=0,column=2)

button4 = Button(frame,text=4,height=4,width=9,font=35,command=lambda : but_press(4))
button4.grid(row=1,column=0)

button5 = Button(frame,text=5,height=4,width=9,font=35,command=lambda : but_press(5))
button5.grid(row=1,column=1)

button6 = Button(frame,text=6,height=4,width=9,font=35,command=lambda : but_press(6))
button6.grid(row=1,column=2)

button7 = Button(frame,text=7,height=4,width=9,font=35,command=lambda : but_press(7))
button7.grid(row=2,column=0)

button8 = Button(frame,text=8,height=4,width=9,font=35,command=lambda : but_press(8))
button8.grid(row=2,column=1)

button9 = Button(frame,text=9,height=4,width=9,font=35,command=lambda : but_press(9))
button9.grid(row=2,column=2)

button0 = Button(frame,text=0,height=4,width=9,font=35,command=lambda : but_press(0))
button0.grid(row=3,column=0)

buttonad = Button(frame,text='+',height=4,width=9,font=35,command=lambda : but_press('+'))
buttonad.grid(row=0,column=3)

buttonmin = Button(frame,text='-',height=4,width=9,font=35,command=lambda : but_press('-'))
buttonmin.grid(row=1,column=3)

buttonmul = Button(frame,text='*',height=4,width=9,font=35,command=lambda : but_press('*'))
buttonmul.grid(row=2,column=3)

buttonsub = Button(frame,text='/',height=4,width=9,font=35,command=lambda : but_press('/'))
buttonsub.grid(row=3,column=3)

buttoneq = Button(frame,text='=',height=4,width=9,font=35,command=equals)
buttoneq.grid(row=3,column=2)

buttondec = Button(frame,text='.',height=4,width=9,font=35,command=lambda : but_press('.'))
buttondec.grid(row=3,column=1)

buttoncl = Button(window,text='CLEAR',height=4,width=12,font=35,command=clear)
buttoncl.pack()

window.mainloop()
