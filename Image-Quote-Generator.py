"""
Created on Fri Mar  6 11:49:16 2020

@author: Yadnesh
"""

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import textwrap
import pandas as pd
import re
import random

number_of_img_required = 10 
Y=1  #Image number 

#--------input quotes files----------------------------------------------------
dataset = pd.read_csv("Data/quotes_motivational.csv")  #File 
rows=dataset['Quote'].head(number_of_img_required)
quotes=list(rows)

for quote in quotes:
    #------------------------ Color Cordination--------------------------------
    select_code=random.randrange(1,3)
    #----------------Random blackbackground with Shades of White color text----
    if select_code ==1:
        
        background_Black= ["Black_1.jpg","Black_2.jpg","Black_3.jpg","Black_4.jpg"]
    
        #-----------------Black background text color--------------------------
        
        white_min=230
        white_max=256
        r  = random.randrange(white_min, white_max)
        g = random.randrange(white_min, white_max)
        b = random.randrange(white_min, white_max)
        
        background_rnd=random.choice(background_Black)
    
    #------------------Random White Background with Shades of Black color Text-
    else:
        
        background_White=["White_1.jpg","White_2.jpg","White_3.jpg","White_4.jpg"]
    
        #-----------------White background text color--------------------------
        black_min=0
        black_max=26
        r  = random.randrange(black_min, black_max)
        g = random.randrange(black_min, black_max)
        b = random.randrange(black_min, black_max)
        
        #---------------------Background image---------------------------------
    
        background_rnd=random.choice(background_White)
    
    #-------------------Text Color-------------------------------
    text_color = (r, g, b)   

#------------------------------- Main Code ------------------------------------  
    img = Image.open("Base Image/"+str(background_rnd))

    quote=re.sub("[^A-Za-z0-9 '?!%]+", '', quote)
    
    msg=quote

    msg_len=len(msg)
    if msg_len<=240:
        num_of_char_in_line=22
    else:
        num_of_char_in_line=30
    
    para = textwrap.wrap(msg, width=num_of_char_in_line)
    W, H = img.size
    
    
    fnt = ImageFont.truetype('Fonts/OpenSans-Semibold.ttf', 50) #Select Font
    d = ImageDraw.Draw(img)
    w, h = d.textsize(msg, font=fnt)
    
    #------------Code for allignment of Text in the center Start --------------
    
    txt_size=int(len(msg)/num_of_char_in_line)*int(h)
    
    current_h, pad = int((H-txt_size)/2)-100, 15
    
    for line in para:
        w, h = d.textsize(line, font=fnt)
        #current_h=(H-h)/2
        d.text(((W - w) / 2,current_h ), line, font=fnt, fill=text_color)
        current_h += h + pad
    #-------------Code for allignment of Text in the center End----------------    
    #Output Images
    img.save("Image generated post/image_"+str(Y)+".png")
    Y=Y+1

#----------Delete command if processing CSV in sets 
#--------------Remove comments from below section to run the Code in Sets -----
#dataset = dataset.iloc[number_of_img_required:]
#dataset.to_csv("H:/Instagram/Quotes/Code/Data/Processed/quotes_motivational.csv", index = False)