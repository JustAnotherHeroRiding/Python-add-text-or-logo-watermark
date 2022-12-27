from PIL import Image,ImageTk,ImageDraw,ImageFont
import tkinter as tk
import tkinter.ttk as ttk
from ttkthemes import ThemedTk
from tkinter.filedialog import askopenfilename



PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"


#Goal-Create a Watermarker program with a gui

#I should be able to upload an image and it should have watermark added to it 

#What do i need to make this work?

#First a window with an empty space for the the image,make it look nice with a background color

#Upload image button below the empty space for the image
#The image should fit in the predetermined empty space

#Python code to add the watermark in the lower right corner
#Some way to download the watermarker image

#Check out if there are any bugs 


window = ThemedTk()

window.title("WaterMarker")
window.set_theme('breeze')
#Lowered padding
window.geometry("900x600")
window.config(bg="#243763")





title_label = tk.Label(text="WaterMarker", fg="#E7E7DE", bg="#243763", font=(FONT_NAME, 50))
title_label.grid(column=1, row=0, padx=15,pady=20)


#canvas = tk.Canvas(width=800, height=480, bg= "#0F3D3E", highlightthickness=0)
#cog= tk.PhotoImage(file="watermark.png")
#cogimage= canvas.create_image(96, 96,anchor='center', image=cog)
#canvas.grid(column=1, row=1)



def add_text_watermark():
    text = watermark_text_entry.get()
    if len(text) == 0:
        tk.messagebox.showerror(title= "Empty field!",message= "You shouldn't leave any fields empty!")
    else:
        
        f_types = [('Image Files',['.jpeg', '.jpg', '.png', '.gif','.tiff', '.tif', '.bmp'])]
        filename = askopenfilename(filetypes=f_types)
        #img = ImageTk.PhotoImage(file=filename)
        #b2 =tk.Label(window,image=img)
        #b2.grid(row=1,column=1)
    
        add_watermark(filename, text)
    
    

def add_watermark(image, wm_text):
    # Creates the Image object
    opened_image = Image.open(image)

    # Get Image size
    image_width, image_height = opened_image.size
    

    # Draw on Image
    draw = ImageDraw.Draw(opened_image)

    # Specify a font size
    font_size = int(image_width / 15)

    # For Windows, change font type to 'arial'
    font = ImageFont.truetype("arial.ttf", font_size)
    # Coordinates for where we want the image
    x, y = int(image_width *0.9), int(image_height )

    # Add the watermark
    draw.text((x, y), wm_text, font=font, fill='#FFF', stroke_width=5, stroke_fill='#222', anchor='ms')

    # Show the new image
    opened_image.show()
    
    
def add_image_watermark():
    f_types = [('Image Files',['.jpeg', '.jpg', '.png', '.gif','.tiff', '.tif', '.bmp'])]
    tk.messagebox.showinfo(title= "Notice",message= "First select the image you want to watermark then select the watermark. It should be a transparent image but non-transparent ones will be watermarked too.")
    filename = askopenfilename(filetypes=f_types)
    #Dont show the image inside the window
    #img = ImageTk.PhotoImage(file=filename)
    #b2 =tk.Label(window,image=img)
    #b2.grid(row=1,column=1)
    watermark = askopenfilename(filetypes=f_types)
    add_watermark_image(filename, watermark)
    
    
def add_watermark_image(image, wm_image):
    # Open the original image and the watermark image
    opened_image = Image.open(image).convert("RGBA")
    watermark = Image.open(wm_image).convert("RGBA")
    layer = Image.new('RGBA', opened_image.size, (0, 0, 0, 0))
    

    # Get the size of the original image
    image_width, image_height = opened_image.size
    
    # Calculate the size of the watermark based on the size of the original image
    wm_width, wm_height = watermark.size

    # Calculate the new width of the watermark
    new_wm_width = int(image_width * 0.1)

    # Calculate the new height of the watermark based on the aspect ratio of the original image
    aspect_ratio = wm_height / wm_width
    new_wm_height = int(new_wm_width * aspect_ratio)

    # Resize the watermark to the calculated size
    watermark = watermark.resize((new_wm_width, new_wm_height))

    # Calculate the position for the watermark
    x = int(image_width * 0.9)
    y = int(image_height *0.9)
    
    layer.paste(watermark, (x, y))

    # Create a copy of the layer
    layer2 = layer.copy()

    # Put alpha on the copy
    layer2.putalpha(256)

    # merge layers with mask
    layer.paste(layer2, layer)


    result = Image.alpha_composite(opened_image, layer)

    result.show()

        
watermark_text_entry = tk.Entry(width=20)
watermark_text_entry.grid(column=0, row=1,padx=25,pady=50)

upload_text_button = tk.Button(
    text="Add a text Watermark",
    highlightthickness=0, 
    command=add_text_watermark,
    bg="#FF6E31",
    fg="#FFEBB7")
upload_text_button.grid(column=0, row=2, padx=25,pady=15)


upload_image_button = tk.Button(
    text="Add a logo Watermark", 
    highlightthickness=0, 
    command=add_image_watermark,
    bg="#FF6E31",
    fg="#FFEBB7")
upload_image_button.grid(column=2, row=2,padx=25,pady=15)


window.mainloop()