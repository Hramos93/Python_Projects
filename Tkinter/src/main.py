from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Codemy.com Image Viewer')
root.iconbitmap('images/python.ico')

my_img = ImageTk.PhotoImage(Image.open("images/me.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("images/me2.jpg"))


image_list = [my_img, my_img2]


my_label = Label(image=my_img)
my_label.grid(row=0, column=0, columnspan=3)

button_back = Button(root, text ="<<")
button_exit = Button(root, text ="EXIT PROGRAM", command=root.quit)
button_foward = Button(root, text=">>")

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_foward.grid(row=1, column=2)

root.mainloop()