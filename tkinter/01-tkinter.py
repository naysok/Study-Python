import tkinter as tk
import time


def pushed_time():

    # Print Current Time
    now = time.ctime()
    cnvtime = time.strptime(now)
    print("Current Time is", time.strftime("%Y/%m/%d %H:%M", cnvtime))



def win_exit():
    root.destroy()



# Create Window
root = tk.Tk()

# Window Name
root.title("Tkinter - Test")

# Window Size
root.geometry("480x800")




#Label : text
label2 = tk.Label(root, text='Hello tkinter!, Hello python!!', font=('Times', '18'))
label2.pack()


# button
button_time = tk.Button(root, text = "now is ...", command = pushed_time)
button_time.pack()



label3 = tk.Label(root, text='\n\nframe test ↓')
label3.pack()

label_line_1 = tk.Label(root, text='------------------------------------------------------')
label_line_1.pack()


frame_1 = tk.Frame(root, bd = 2, relief= "ridge")
frame_1.pack(fill = "x")


buttom_L = tk.Button(frame_1, text= "<----- Left ----->")
buttom_L.pack(side = "left")

buttom_R = tk.Button(frame_1, text= "Right")
buttom_R.pack(side = "right")


buttom_center = tk.Button(frame_1, text = "center")
buttom_center.pack()


label_line_2 = tk.Label(root, text='------------------------------------------------------')
label_line_2.pack()



frame_2 = tk.Frame(root, pady = 10, bd = 2, relief= "ridge")
frame_2.pack(fill = "x")

buttom_hello = tk.Button(frame_2, text= "pady = 10")
buttom_hello.pack()


label_line_3 = tk.Label(root, text='------------------------------------------------------')
label_line_3.pack()


# frame_3 = tk.Frame(root, padx = 10,pady = 10, bd = 2, relief= "ridge")
frame_3 = tk.Frame(root, padx = 10,pady = 10, relief= "ridge")
frame_3.pack()

label_text1 = tk.Label(frame_3,text= "msg ---  -")
label_text1.pack(side = "left")

entry_text1 = tk.Entry(frame_3, width = 15)
entry_text1.pack(side ="left")

enter_buttom1 = tk.Button(frame_3, text = "enter")
enter_buttom1.pack(side = "left")



label_line_4 = tk.Label(root, text='------------------------------------------------------')
label_line_4.pack()


# frame_3 = tk.Frame(root, padx = 10,pady = 10, bd = 2, relief= "ridge")
frame_4 = tk.Frame(root, padx = 10,pady = 10, relief= "ridge")
frame_4.pack()

label_text2 = tk.Label(frame_4,text= "hoge     -")
label_text2.pack(side = "left")

entry_text2 = tk.Entry(frame_4, width = 15)
entry_text2.pack(side ="left")

enter_buttom2 = tk.Button(frame_4, text = "enter")
enter_buttom2.pack(side = "left")


label_line_5 = tk.Label(root, text='------------------------------------------------------')
label_line_5.pack()




button_exit = tk.Button(root, text = "exit", command = win_exit)
button_exit.pack()





root.mainloop()