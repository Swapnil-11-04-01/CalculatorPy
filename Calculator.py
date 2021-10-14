from tkinter import *

# Action when power button is pressd
def power():
    scvalue.set(scvalue.get() + "**")
    screen.update()

# Events to happen when respective buttons are pressed
def click(event):
    # Takes the text printed on widget as input and stores in text variable
    text = event.widget.cget("text")
    print(text)

    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                scvalue.set(eval(scvalue.get()))
                screen.update()
            except Exception as e:
                print(e)
                scvalue.set("Error : wait 2 sec")
                screen.update()
                import time
                time.sleep(2)
                scvalue.set("Continue")
                screen.update()
                time.sleep(0.2)
                screen.delete(0, END)
    elif text == "x²":
        try:
            scvalue.set(float(scvalue.get()) ** 2)
            screen.update()
        except Exception as e:
            print(e)
            scvalue.set("Error : wait 2 sec")
            screen.update()
            import time
            time.sleep(2)
            scvalue.set("Continue")
            screen.update()
            time.sleep(0.2)
            screen.delete(0, END)
    elif text == "1/x":
        try:
            scvalue.set(float(scvalue.get()) ** -1)
            screen.update()
        except Exception as e:
            print(e)
            scvalue.set("Error : wait 2 sec")
            screen.update()
            import time
            time.sleep(2)
            scvalue.set("Continue")
            screen.update()
            time.sleep(0.2)
            screen.delete(0, END)
    elif text == "root(x)":
        try:
            scvalue.set(float(scvalue.get()) ** 0.5)
            screen.update()
        except Exception as e:
            print(e)
            scvalue.set("Error : wait 2 sec")
            screen.update()
            import time
            time.sleep(2)
            scvalue.set("Continue")
            screen.update()
            time.sleep(0.2)
            screen.delete(0, END)
    elif text == "+/-":
        try:
            scvalue.set(float(scvalue.get()) * -1)
            screen.update()
        except Exception as e:
            print(e)
            scvalue.set("Error : wait 2 sec")
            screen.update()
            import time
            time.sleep(2)
            scvalue.set("Continue")
            screen.update()
            time.sleep(0.2)
            screen.delete(0, END)
    elif text == "C":
        screen.delete(0, END)

    elif text == "<<":
        string = scvalue.get()
        scvalue.set(string[:-1])
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


root = Tk()
root.title("CALCY - Swapnil Sharma")
root.wm_iconbitmap("icon.ico")
root.geometry("550x580")
root.configure(background="#1E1E1E")

f = Frame(root)
f.pack()
scvalue = StringVar()
scvalue.set("")
scrollbar = Scrollbar(f, orient=HORIZONTAL, width=13, troughcolor="red", highlightthickness=3,
                      activebackground="#101010")
scrollbar.pack(side=BOTTOM, fill=X)
screen = Entry(f, textvar=scvalue, font="lucida 40 bold", background="#1E1E1E", foreground="white",
               xscrollcommand=scrollbar.set)
screen.pack(fill=X, ipadx=7, ipady=20)
scrollbar.config(command=screen.xview)

f = Frame(root, background="#1E1E1E")
f.pack()

b = Button(f, text="%", font="lucida 20 bold", padx=45, pady=10, background="#101010", foreground="white")
b.pack(side=LEFT, padx=1, pady=1)
b.bind("<Button-1>", click)

b = Button(f, text="1/x", font="lucida 20 bold", padx=38, pady=10, background="#101010", foreground="white")
b.pack(side=LEFT, padx=1, pady=1)
b.bind("<Button-1>", click)

b = Button(f, text="C", font="lucida 20 bold", padx=43, pady=10, background="#101010", foreground="white")
b.pack(side=LEFT, padx=1, pady=1)
b.bind("<Button-1>", click)

b = Button(f, text="<<", font="lucida 20 bold", padx=42, pady=10, background="#101010", foreground="white")
b.pack(side=LEFT, padx=1, pady=1)
b.bind("<Button-1>", click)

f = Frame(root, background="#1E1E1E")
f.pack()

b = Button(f, text="^", font="lucida 20 bold", padx=48, pady=10, background="#101010", foreground="white",
           command=power)
b.pack(side=LEFT, padx=1, pady=1)

b = Button(f, text="x²", font="lucida 20 bold", padx=45, pady=10, background="#101010", foreground="white")
b.pack(side=LEFT, padx=1, pady=1)
b.bind("<Button-1>", click)

b = Button(f, text="root(x)", font="lucida 20 bold", padx=10, pady=10, background="#101010", foreground="white")
b.pack(side=LEFT, padx=1, pady=1)
b.bind("<Button-1>", click)

b = Button(f, text="/", font="lucida 20 bold", padx=50, pady=10, background="#101010", foreground="white")
b.pack(side=LEFT, padx=1, pady=1)
b.bind("<Button-1>", click)

f = Frame(root, background="#1E1E1E")
f.pack()

b = Button(f, text="7", font="lucida 20 bold", padx=48, pady=10, background="black", foreground="white")
b.pack(side=LEFT, padx=1, pady=1)
b.bind("<Button-1>", click)

b = Button(f, text="8", font="lucida 20 bold", padx=50, pady=10, background="black", foreground="white")
b.pack(side=LEFT, padx=1, pady=1)
b.bind("<Button-1>", click)

b = Button(f, text="9", font="lucida 20 bold", padx=46, pady=10, background="black", foreground="white")
b.pack(side=LEFT, padx=1, pady=1)
b.bind("<Button-1>", click)

b = Button(f, text="*", font="lucida 20 bold", padx=49, pady=10, background="#101010", foreground="white")
b.pack(side=LEFT, padx=1, pady=1)
b.bind("<Button-1>", click)

f = Frame(root, background="#1E1E1E")
f.pack()

b = Button(f, text="4", font="lucida 20 bold", padx=48, pady=10, background="black", foreground="white")
b.pack(side=LEFT, padx=1, pady=1)
b.bind("<Button-1>", click)

b = Button(f, text="5", font="lucida 20 bold", padx=51, pady=10, background="black", foreground="white")
b.pack(side=LEFT, padx=1, pady=1)
b.bind("<Button-1>", click)

b = Button(f, text="6", font="lucida 20 bold", padx=46, pady=10, background="black", foreground="white")
b.pack(side=LEFT, padx=1, pady=1)
b.bind("<Button-1>", click)

b = Button(f, text="-", font="lucida 20 bold", padx=50.5, pady=10, background="#101010", foreground="white")
b.pack(side=LEFT, padx=1, pady=1)
b.bind("<Button-1>", click)

f = Frame(root, background="#1E1E1E")
f.pack()

b = Button(f, text="1", font="lucida 20 bold", padx=48, pady=10, background="black", foreground="white")
b.pack(side=LEFT, padx=1, pady=1)
b.bind("<Button-1>", click)

b = Button(f, text="2", font="lucida 20 bold", padx=51, pady=10, background="black", foreground="white")
b.pack(side=LEFT, padx=1, pady=1)
b.bind("<Button-1>", click)

b = Button(f, text="3", font="lucida 20 bold", padx=46, pady=10, background="black", foreground="white")
b.pack(side=LEFT, padx=1, pady=1)
b.bind("<Button-1>", click)

b = Button(f, text="+", font="lucida 20 bold", padx=50, pady=10, background="#101010", foreground="white")
b.pack(side=LEFT, padx=1, pady=1)
b.bind("<Button-1>", click)

f = Frame(root, background="#1E1E1E")
f.pack()

b = Button(f, text="+/-", font="lucida 20 bold", padx=39, pady=10, background="black", foreground="white")
b.pack(side=LEFT, padx=1, pady=1)
b.bind("<Button-1>", click)

b = Button(f, text="0", font="lucida 20 bold", padx=51, pady=10, background="black", foreground="white")
b.pack(side=LEFT, padx=1, pady=1)
b.bind("<Button-1>", click)

b = Button(f, text=".", font="lucida 20 bold", padx=49, pady=10, background="black", foreground="white")
b.pack(side=LEFT, padx=1, pady=1)
b.bind("<Button-1>", click)

b = Button(f, text="=", font="lucida 20 bold", padx=51, pady=10, background="red", foreground="white")
b.pack(side=LEFT, padx=1, pady=1)
b.bind("<Button-1>", click)

root.resizable(False, False)
root.mainloop()
