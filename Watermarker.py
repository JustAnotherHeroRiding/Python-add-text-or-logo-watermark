from PIL import Image,ImageTk,ImageDraw,ImageFont
import tkinter as tk
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


window = tk.Tk()
window.title("Pomodoro")
#Lowered padding
window.geometry("900x600")
window.config(bg="#0F3D3E")


title_label = tk.Label(text="WaterMarker", fg=GREEN, bg="#0F3D3E", font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)


#canvas = tk.Canvas(width=800, height=480, bg= "#0F3D3E", highlightthickness=0)
#cog= tk.PhotoImage(file="watermark.png")
#cogimage= canvas.create_image(96, 96,anchor='center', image=cog)
#canvas.grid(column=1, row=1)



def add_text_watermark():
    f_types = [('Image Files',['.jpeg', '.jpg', '.png', '.gif','.tiff', '.tif', '.bmp'])]
    filename = askopenfilename(filetypes=f_types)
    #img = ImageTk.PhotoImage(file=filename)
    #b2 =tk.Label(window,image=img)
    #b2.grid(row=1,column=1)
    add_watermark(filename, "Kiko's")
    
    

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
    filename = askopenfilename(filetypes=f_types)
    #Dont show the image inside the window
    #img = ImageTk.PhotoImage(file=filename)
    #b2 =tk.Label(window,image=img)
    #b2.grid(row=1,column=1)
    watermark = "watermark.png"
    add_watermark_image(filename, watermark)
    
    
def add_watermark_image(image, wm_image):
    # Open the original image and the watermark image
    opened_image = Image.open(image)
    watermark = Image.open(wm_image)

    # Get the size of the original image
    image_width, image_height = opened_image.size


    # Convert both images to the RGBA mode
    opened_image = opened_image.convert("RGBA")
    watermark = watermark.convert("RGBA")

    # Calculate the position for the watermark
    x = int(image_width * 0.9)
    y = int(image_height  - 50)

    opened_image.paste(watermark,(x,y))

    # Show the new image
    opened_image.show()


        

upload_text_button = tk.Button(text="Add a text Watermark", highlightthickness=0, command=add_text_watermark)
upload_text_button.grid(column=0, row=1)


upload_image_button = tk.Button(text="Add a logo Watermark", highlightthickness=0, command=add_image_watermark)
upload_image_button.grid(column=1, row=1)


window.mainloop()