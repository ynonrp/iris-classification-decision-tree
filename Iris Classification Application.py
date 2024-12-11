import os
import sys
import tkinter as tk
import joblib
import pandas as pd
from PIL import Image, ImageTk

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
window.geometry("530x310")

frameTitle = tk.Frame()
frameTitle.grid(row=0, column=0, columnspan=2)

framePredict = tk.Frame()
framePredict.grid(row=1, column=0)

frameInformation = tk.LabelFrame(text="Information", height=264, width=300)
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
model_path = resource_path("model.pkl")
model = joblib.load(model_path)

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
        
    except ValueError:
        output_result.config(text="Error")


bt_submit = tk.Button(frameInput, text="Submit", width=25, command=predict_result)
bt_submit.grid(row=4, column=0, columnspan=3, pady=10)

frameResult = tk.LabelFrame(framePredict, text="Result")
frameResult.pack()

output_result = tk.Label(frameResult, width=27, height=6, justify="left", anchor="nw",)
output_result.pack()

information = "Iris setosa is a species of flowering plant in the genus Iris of the family Iridaceae, it belongs the subgenus Limniris and the series Tripetalae. It is a rhizomatous perennial from a wide range across the Arctic sea, including Alaska, Maine, Canada (including British Columbia, Newfoundland, Quebec and Yukon), Russia (including Siberia), northeastern Asia, China, Korea and southwards to Japan."

imgOri = Image.open("Iris Setosa.jpg")
imgResized = imgOri.resize((100, 100))
img = ImageTk.PhotoImage(imgResized)

imgInformation = tk.Label(frameInformation, image=img, anchor="nw")
imgInformation.pack()
textInformation = tk.Message(frameInformation, text=information, width=280)
textInformation.pack()

window.mainloop()