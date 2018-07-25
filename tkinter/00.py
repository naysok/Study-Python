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
root.title("ここにタイトルいれる")

# Window Size
root.geometry("480x480")




#Label : text
label2 = tk.Label(root, text='\nHello tkinter!, Hello python!!\n\n', font=('Times', '18'))
label2.pack()


button_exit = tk.Button(root, text = "exit", command = win_exit)
button_exit.pack()





root.mainloop()