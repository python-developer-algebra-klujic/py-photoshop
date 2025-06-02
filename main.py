import tkinter as tk
from PIL import Image, ImageTk


#region CONSTANTS
image = Image.open(r'./algebra_ucionica.jpg')
#endregion





root = tk.Tk()
root.title('Algebra - Py Photoshop')

lbl_photo_image = ImageTk.PhotoImage(image=image)
lbl_photo = tk.Label(root, text='FOTOGRAFIJA', image=lbl_photo_image)
lbl_photo.grid(column=0, row=0)


if __name__ == '__main__':
    root.mainloop()
