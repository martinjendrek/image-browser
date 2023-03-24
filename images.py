import os
import tkinter as tk
from PIL import ImageTk, Image
import glob

# setting relative file directory 
filenames = glob.glob('images\*.jpg')
print (filenames)

dirname = os.path.dirname(__file__)
print(dirname)

# creating toplevel widget
root = tk.Tk()
root.title('Images app')
root.iconbitmap(os.path.join(dirname,'Icon.ico'))


mainimage = ImageTk.PhotoImage(Image.open(os.path.join(dirname,'images/Logopng.png')))
photosize = [800,600]



cat_image_list = []
for i in filenames:
    cat_image_list.append(ImageTk.PhotoImage(Image.open(i).resize(photosize)))

img_index = 0
def forward():
    global cat_label
    global img_index
    global index_label
    cat_label.grid_forget()
    index_label.grid_forget()
    if img_index == (len(cat_image_list)-1):
        img_index = 0
    else:
        img_index +=1
    cat_label = tk.Label(image=cat_image_list[img_index],width=photosize[0], height=photosize[1])
    cat_label.grid(row=1, column=0, columnspan=3)
    index_label = tk.Label(text=img_index)
    index_label.grid(row=3,columnspan=3)

def back():
    
    global cat_label
    global img_index
    global index_label
    cat_label.grid_forget()
    index_label.grid_forget()
    if img_index == 0:
        img_index = (len(cat_image_list)-1)
    else:
        img_index -= 1
    cat_label = tk.Label(image=cat_image_list[img_index],width=photosize[0], height=photosize[1])
    cat_label.grid(row=1, column=0, columnspan=3)
    index_label = tk.Label(text=img_index)
    index_label.grid(row=3,columnspan=3)


my_label = tk.Label(image=mainimage)
my_label.grid(row=0, column=0, columnspan=3)

cat_label = tk.Label(image=cat_image_list[img_index],width=photosize[0], height=photosize[1])
cat_label.grid(row=1, column=0, columnspan=3)


button_back = tk.Button(root, text='<<<', command=lambda:back())
button_quit = tk.Button(root, text='Exit Program', command= root.quit)
button_forward = tk.Button(root, text='>>>', command=lambda:forward())

button_back.grid(row=2, column=0)
button_quit.grid(row=2, column=1)
button_forward.grid(row=2, column=2)

index_label = tk.Label(text=img_index)
index_label.grid(row=3,columnspan=3)

root.mainloop()