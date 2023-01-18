from tkinter import*

root=Tk()
root.title("Toggle Switch")
root.geometry("400x600")
root.config(bg="white")

button_mode=True

on=PhotoImage(file="light.png")
off=PhotoImage(file="dark.png")



def change():
    global button_mode

    if button_mode:
        button.config(image=off,bg="black",activebackground="black")
        root.config(bg="black")
        button_mode=False
    else:
        button.config(image=on,bg="white",activebackground="white")
        root.config(bg="white")
        button_mode=True

button=Button(root,image=on,bd=0,bg="white",activebackground="white",command=change)
button.pack(padx=50,pady=50)


root.mainloop()