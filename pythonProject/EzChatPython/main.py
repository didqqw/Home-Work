from tkinter import *

root = Tk()


# nazvanie okna
root.title("Chat")

# nastrojki okna
root.geometry("500x300")

# vkladki menu
main_menu = Menu(root)

# pod menju
file_menu = Menu(root, tearoff = 0)
file_menu.add_command(label = "New ..")
file_menu.add_command(label = "Save As ..")

main_menu.add_cascade(label = "File", menu = file_menu)
main_menu.add_command(label = "Quit")
root.config(menu = main_menu)

# pole soobwenij
chat_window = Text(root, bd = 1, bg = "grey", width = 50, height = 8, font =  ("Arial", 10))
chat_window.place(x=6, y=6, height = 230, width = 480)

# pole vvoda soobwenija
message_window = Text(root, bg = "grey", width = 30, height = 4, font =  ("Arial", 10))
message_window.place(x = 186, y =240, height = 50, width = 300)

# knopka dlja otpravki soobwenija
Button = Button(root, text = "Отправить", bg = "grey", activebackground = "white", width = 12, height = 5, font = ("Arial", 12, "bold"))
Button.place(x=6, y=240, height = 50, width = 170)

# scroll dlja polja soobwenij
scrollbar = Scrollbar(root, command = chat_window.yview())
scrollbar.place(x=475, y=5, height = 230)


root.mainloop()