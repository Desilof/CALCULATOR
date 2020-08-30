from tkinter import *
root = Tk()
root.title('CALCULATOR')
# FUNCTIONS


def addition():
    print('E1.get()'+E1.get())
    print('E2.get()'+E2.get())
    a = int(E1.get())
    b = int(E2.get())
    answer = a + b
    print('answer'+str(answer))
    E3.insert(0, answer)


def subtraction():
    print('E1.get()'+E1.get())
    print('E2.get()'+E2.get())
    a = int(E1.get())
    b = int(E2.get())
    answer = a - b
    print('answer'+str(answer))
    E3.insert(0, answer)


def multiplication():
    print('E1.get()'+E1.get())
    print('E2.get()'+E2.get())
    a = int(E1.get())
    b = int(E2.get())
    answer = a * b
    print('answer'+str(answer))
    E3.insert(0, answer)


def division():
    print('E1.get()'+E1.get())
    print('E2.get()'+E2.get())
    a = int(E1.get())
    b = int(E2.get())
    answer = a / b
    print('answer'+str(answer))
    E3.insert(0, answer)

# DISPLAY SETTINGS ARE HERE , width=80


E1 = Entry(root, bd=10, bg='cyan')
E1.pack(side=TOP)
E2 = Entry(root, bd=10, bg='cyan')
E2.pack(side=TOP)

Ans = Label(root, text='ANS')
Ans.pack(side=TOP)
E3 = Entry(root, bd=10, bg='cyan')
E3.pack(side=TOP)



# ALL BUTTONS CONTROL ARE HERE
# Frame settings
Topframe = Frame(root)
Topframe.pack()

# DIGITS PANEL
# Am still working on my button panel


# CONTROL BUTTONS
Botplus = Button(Topframe, text='+', command=addition)
Botplus.pack(side=LEFT)

Botminus = Button(Topframe, text='-', command=subtraction)
Botminus.pack(side=LEFT)

Botproduct = Button(Topframe, text='*', command=multiplication)
Botproduct.pack(side=LEFT)

Botdivide = Button(Topframe, text='/', command=division)
Botdivide.pack(side=LEFT)

root.mainloop()
