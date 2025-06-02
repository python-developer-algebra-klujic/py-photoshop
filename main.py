import tkinter as tk
from PIL import Image, ImageTk


#region CONSTANTS
image = Image.open(r'./algebra_ucionica.jpg')
width = 800
height = 550
image = image.resize((width, height))
image_data = f'Format slike:\t{image.format}\nVelicina slike:\t{image.size}\nMod slike:\t{image.mode}'
#endregion


#region FUNCTIONS
def flip_lr():
    global image, lbl_photo
    image = image.transpose(method=Image.Transpose.FLIP_LEFT_RIGHT)
    lbl_photo_image = ImageTk.PhotoImage(image=image)
    lbl_photo['image'] = lbl_photo_image

def flip_tb():
    global image, lbl_photo
    image = image.transpose(method=Image.Transpose.FLIP_TOP_BOTTOM)
    lbl_photo_image = ImageTk.PhotoImage(image=image)
    lbl_photo['image'] = lbl_photo_image

def blur():
    print('blur')
def set_blur_radius(value):
    print(f'set_blur_radius {value}')

def contour():
    print('contour')

def emboss():
    print('emboss')

def edges():
    print('edges')

def save():
    print('save')
def load():
    print('load')
def reset():
    print('reset')
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
