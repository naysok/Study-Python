import tkinter as tk
import time


def pushed():
    print("Hello!!")

    # Print Current Time
    now = time.ctime()
    cnvtime = time.strptime(now)
    print (time.strftime("%Y/%m/%d %H:%M", cnvtime))



# Create Window
root = tk.Tk()

# Window Name
root.title("Tkinter-Test")

# Window Size
root.geometry("480x480")


# text
# add label
label1 = tk.Label(root, text= "Hello, World!!")
# preview
label1.grid()

label2 = tk.Label(None, text='Hello Python, Hello World!!', font=('Times', '18'))
label2.grid()


# button
button1 = tk.Button(root, text="Hello", command =pushed)
button1.grid()

root.mainloop()