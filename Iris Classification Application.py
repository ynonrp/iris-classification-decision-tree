import os
import sys
import tkinter as tk
import joblib
import pandas as pd
from PIL import Image, ImageTk
import webbrowser

def resource_path(relative_path):
    try:
        # Jika dieksekusi sebagai file .exe
        base_path = sys._MEIPASS
    except AttributeError:
        # Jika dijalankan sebagai script Python biasa
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

#Create UI Application
window = tk.Tk()
window.title("Iris Classification")
window.resizable(False, False)
window.geometry("540x325")
window.iconbitmap("img\Icon.ico")

frameTitle = tk.Frame()
frameTitle.grid(row=0, column=0, columnspan=2)

framePredict = tk.Frame()
framePredict.grid(row=1, column=0)

frameInformation = tk.LabelFrame(text="Information", height=278, width=310)
frameInformation.grid(row=1, column=1, sticky="nw")
frameInformation.pack_propagate(False)

title = tk.Label(frameTitle, height=2, text="Iris Classification Using Decision Tree Method")
title.pack()

frameInput = tk.LabelFrame(framePredict, text="Input")
frameInput.pack(padx=10)

tk.Label(frameInput, text="Sepal Length", width=12, anchor="w").grid(row=0, column=0)
input_sepal_length = tk.Entry(frameInput, width=10)
input_sepal_length.grid(row=0, column=1)
tk.Label(frameInput, text=" cm", width=5, anchor="w").grid(row=0, column=2)

tk.Label(frameInput, text="Sepal Width", width=12, anchor="w").grid(row=1, column=0)
input_sepal_width = tk.Entry(frameInput, width=10)
input_sepal_width.grid(row=1, column=1)
tk.Label(frameInput, text=" cm", width=5, anchor="w").grid(row=1, column=2)

tk.Label(frameInput, text="Petal Length", width=12, anchor="w").grid(row=2, column=0)
input_petal_length = tk.Entry(frameInput, width=10)
input_petal_length.grid(row=2, column=1)
tk.Label(frameInput, text=" cm", width=5, anchor="w").grid(row=2, column=2)

tk.Label(frameInput, text="Petal Width", width=12, anchor="w").grid(row=3, column=0)
input_petal_width = tk.Entry(frameInput, width=10)
input_petal_width.grid(row=3, column=1)
tk.Label(frameInput, text=" cm", width=5, anchor="w").grid(row=3, column=2)

#Predict Model
model_path = resource_path("Model Trained\model.pkl")
model = joblib.load(model_path)
informationCSV = pd.read_csv("Information File\Information.csv")

def predict_result():
    try:
        sepal_length = float(input_sepal_length.get())
        sepal_width = float(input_sepal_width.get())
        petal_length = float(input_petal_length.get())
        petal_width = float(input_petal_width.get())

        input_data = {"sepal.length": [sepal_length], "sepal.width": [sepal_width], 
                      "petal.length": [petal_length], "petal.width": [petal_width]}
        df = pd.DataFrame(input_data)

        predict = model.predict(df)
        output_result.config(text=f"Sepal length : {sepal_length} cm\n"
                                  f"Sepal width  : {sepal_width} cm\n"
                                  f"Petal length : {petal_length} cm\n"
                                  f"Petal width  : {petal_width} cm\n"
                                  f"\n"
                                  f"Predict result : Iris {predict[0]}")
        
        global img
        if(predict[0]=="Setosa"):
            index = 0
        elif(predict[0]=="Versicolor"):
            index = 1
        elif(predict[0]=="Virginica"):
            index = 2
        
        imgOri = Image.open(informationCSV["Image"].loc[index])
        imgResized = imgOri.resize((100, 100))
        img = ImageTk.PhotoImage(imgResized)
        imgInformation.config(image=img)
        textInformation.config(text=informationCSV["Information"].loc[index])
        moreInformation.config( text="More information:")
        linkInformation.config(text=informationCSV["Link"].loc[index])
                
        def open_link(event):
            link = informationCSV["Link"].loc[index]
            webbrowser.open(link)

        linkInformation.bind("<Button-1>", open_link)

    except ValueError:
        output_result.config(text="Error")


bt_submit = tk.Button(frameInput, text="Submit", width=25, command=predict_result)
bt_submit.grid(row=4, column=0, columnspan=3, pady=10)

frameResult = tk.LabelFrame(framePredict, text="Result")
frameResult.pack()

output_result = tk.Label(frameResult, width=27, height=7, justify="left", anchor="nw",)
output_result.pack()

imgInformation = tk.Label(frameInformation)
imgInformation.pack()
textInformation = tk.Message(frameInformation, width=300)
textInformation.pack()
moreInformation = tk.Label(frameInformation, width=300, anchor="sw", padx=5)
moreInformation.pack()
linkInformation = tk.Label(frameInformation, width=300, anchor="nw", fg="blue", cursor="hand2", padx=5)
linkInformation.pack()

window.mainloop()