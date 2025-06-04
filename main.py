import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFilter


#region CONSTANTS
image_path = r'./algebra_ucionica.jpg'
image = Image.open(image_path)
width = 800
height = 550
image = image.resize((width, height))
image_data = f'Format slike:\t{image.format}\nVelicina slike:\t{image.size}\nMod slike:\t{image.mode}'
#endregion


#region FUNCTIONS
def load_image():
    image = Image.open(image_path)
    width = 800
    height = 550
    return image.resize((width, height))

def flip_lr():
    global image, lbl_photo
    image = image.transpose(method=Image.Transpose.FLIP_LEFT_RIGHT)
    lbl_photo_image = ImageTk.PhotoImage(image=image)
    lbl_photo.configure(image=lbl_photo_image)
    lbl_photo.image = lbl_photo_image
def flip_tb():
    global image, lbl_photo
    image = image.transpose(method=Image.Transpose.FLIP_TOP_BOTTOM)
    lbl_photo_image = ImageTk.PhotoImage(image=image)
    lbl_photo.configure(image=lbl_photo_image)
    lbl_photo.image = lbl_photo_image

def blur():
    global lbl_photo

    image = load_image()
    image = image.filter(ImageFilter.GaussianBlur(radius=sc_blur_var.get()))
    lbl_photo_image = ImageTk.PhotoImage(image=image)
    lbl_photo.configure(image=lbl_photo_image)
    lbl_photo.image = lbl_photo_image
def set_blur_radius(value):
    sc_blur_var.set(value=value)
    blur()

def contour():
    global lbl_photo, image

    image = image.filter(ImageFilter.CONTOUR)
    lbl_photo_image = ImageTk.PhotoImage(image=image)
    lbl_photo.configure(image=lbl_photo_image)
    lbl_photo.image = lbl_photo_image

def emboss():
    global lbl_photo, image

    image = image.filter(ImageFilter.EMBOSS)
    lbl_photo_image = ImageTk.PhotoImage(image=image)
    lbl_photo.configure(image=lbl_photo_image)
    lbl_photo.image = lbl_photo_image

def edges():
    global lbl_photo, image

    image = image.filter(ImageFilter.FIND_EDGES)
    lbl_photo_image = ImageTk.PhotoImage(image=image)
    lbl_photo.configure(image=lbl_photo_image)
    lbl_photo.image = lbl_photo_image


def save():
    image.save(f'nova_slika.jpg', format='JPEG')
def load():
    global image_path, image

    image_path = filedialog.askopenfilename()
    image = Image.open(image_path)
    width = 800
    height = 550
    image = image.resize((width, height))
    image_data = f'Format slike:\t{image.format}\nVelicina slike:\t{image.size}\nMod slike:\t{image.mode}'
    lbl_image_data_var.set(image_data)

    lbl_photo_image = ImageTk.PhotoImage(image=image)
    lbl_photo.configure(image=lbl_photo_image)
    lbl_photo.image = lbl_photo_image
def reset():
    global lbl_photo, image

    image = load_image()

    lbl_photo_image = ImageTk.PhotoImage(image=image)
    lbl_photo.configure(image=lbl_photo_image)
    lbl_photo.image = lbl_photo_image
#endregion



root = tk.Tk()
root.title('Algebra - Py Photoshop')

lbl_photo_image = ImageTk.PhotoImage(image=image)
lbl_photo = tk.Label(root, text='FOTOGRAFIJA', image=lbl_photo_image)
lbl_photo.grid(column=0, row=0, padx=10, pady=10, rowspan=9)


#region BUTTONS
btn_flip_lr = tk.Button(root, text='Flip left-right',
                        command=flip_lr)
btn_flip_lr.grid(column=1, row=0, padx=10, pady=(10, 0), sticky='NWE')
btn_flip_tb = tk.Button(root, text='Flip top-bottom',
                        command=flip_tb)
btn_flip_tb.grid(column=1, row=1, padx=10, pady=(0, 10), sticky='NWE')


btn_blur = tk.Button(root, text='Zamuti',
                        command=blur)
btn_blur.grid(column=1, row=2, padx=10, pady=(10, 0), sticky='NWE')
sc_blur_var = tk.IntVar(value=1)
sc_blur = tk.Scale(root, from_=1, to=20, variable=sc_blur_var,
                   orient='horizontal', command=set_blur_radius)
sc_blur.grid(column=1, row=3, padx=10, pady=(0, 10), sticky='NWE')

btn_contour = tk.Button(root, text='Konture',
                        command=contour)
btn_contour.grid(column=1, row=4, padx=10, pady=10, sticky='NWE')

btn_emboss = tk.Button(root, text='Reljef',
                        command=emboss)
btn_emboss.grid(column=1, row=5, padx=10, pady=10, sticky='NWE')

btn_edges = tk.Button(root, text='Rubovi',
                        command=edges)
btn_edges.grid(column=1, row=6, padx=10, pady=10, sticky='NWE')

f_action_buttons = tk.Frame(root)
f_action_buttons.grid(column=1, row=7, padx=10, pady=10, sticky='WE')
btn_save = tk.Button(f_action_buttons, text='Snimi', command=save)
btn_save.grid(column=0, row=0, padx=10, pady=10)
btn_load = tk.Button(f_action_buttons, text='Ucitaj', command=load)
btn_load.grid(column=1, row=0, padx=10, pady=10)
btn_reset = tk.Button(f_action_buttons, text='Resetiraj', command=reset)
btn_reset.grid(column=2, row=0, padx=10, pady=10)
#endregion

lbl_image_data_var = tk.StringVar(value=image_data)
lbl_image_data = tk.Label(root, textvariable=lbl_image_data_var,
                          justify=tk.LEFT)
lbl_image_data.grid(column=1, row=8, padx=10, pady=(10, 0), sticky='WE')


if __name__ == '__main__':
    root.mainloop()
