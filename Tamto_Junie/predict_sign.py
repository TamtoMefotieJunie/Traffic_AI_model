import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import tensorflow as tf
from keras.models import load_model
import cv2
import os

# Load the trained model
model = load_model('best_model.h5')



classes = { 0:'Speed limit (20km/h)',
           1:'Speed limit (30km/h)',
           2:'Speed limit (50km/h)',
           3:'Speed limit (60km/h)',
           4:'Speed limit (70km/h)',
           5:'Speed limit (80km/h)',
           6:'End of speed limit (80km/h)',
           7:'Speed limit (100km/h)',
           8:'Speed limit (120km/h)',
           9:'No passing',
           10:'No passing veh over 3.5 tons',
           11:'Right-of-way at intersection',
           12:'Priority road',
           13:'Yield',
           14:'Stop',
           15:'No vehicles',
           16:'Veh > 3.5 tons prohibited',
           17:'No entry',
           18:'General caution',
           19:'Dangerous curve left',
           20:'Dangerous curve right',
           21:'Double curve',
           22:'Bumpy road',
           23:'Slippery road',
           24:'Road narrows on the right',
           25:'Road work',
           26:'Traffic signals',
           27:'Pedestrians',
           28:'Children crossing',
           29:'Bicycles crossing',
           30:'Beware of ice/snow',
           31:'Wild animals crossing',
           32:'End speed + passing limits',
           33:'Turn right ahead',
           34:'Turn left ahead',
           35:'Ahead only',
           36:'Go straight or right',
           37:'Go straight or left',
           38:'Keep right',
           39:'Keep left',
           40:'Roundabout mandatory',
           41:'End of no passing',
           42:'End no passing vehicle with a weight greater than 3.5 tons'
        }
top = tk.Tk()
top.geometry('800x700')
top.title('Traffic Sign Classification')
top.configure(background='#CDCDCD')
label = Label(top, background='#CDCDCD', font=('arial', 15, 'bold'))
sign_image = Label(top)

def predict_sign(file_path):
  
    filename = os.path.basename(file_path)
    label_index = int(filename.split('_')[0])  
    sign = classes.get(label_index, "Unknown Sign")  

    image = Image.open(file_path).convert("RGB")  
    image = image.resize((30, 30))
    image = np.array(image) / 255.0  
    image = np.expand_dims(image, axis=0)  

    print(f"Image Shape: {image.shape}")  

    # Make a prediction
    predictions = model.predict(image)
    print("Raw model predictions:", predictions)
    pred_class = np.argmax(predictions, axis=-1)[0]
    print(f"Predicted class index: {pred_class}")
    confidence = predictions[0][pred_class]  

     # Create the result text
    result_text = f"Predicted Class: {sign})"
    
   
    label.configure(text=result_text)  
    print(result_text)  


def show_classify_button(file_path):
    classify_b = Button(top, text="Classify Image", command=lambda: predict_sign(file_path), padx=10, pady=5)
    classify_b.configure(background='#364156', foreground='white', font=('arial', 10, 'bold'))
    classify_b.place(relx=0.79, rely=0.46)

def upload_image():
    try:
        file_path = filedialog.askopenfilename()
        uploaded = Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25), (top.winfo_height()/2.25)))
        im = ImageTk.PhotoImage(uploaded)
        sign_image.configure(image=im)
        sign_image.image = im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        print("Error loading image")

upload = Button(top, text="Upload an image", command=upload_image, padx=10, pady=5)
upload.configure(background='#364156', foreground='white', font=('arial', 10, 'bold'))
upload.pack(side=BOTTOM, pady=50)

sign_image.pack(side=BOTTOM, expand=True)
label.pack(side=BOTTOM, expand=True)

heading = Label(top, text="Check Traffic Sign", pady=20, font=('arial', 20, 'bold'))
heading.configure(background='#CDCDCD', foreground='#364156')
heading.pack()

top.mainloop()
