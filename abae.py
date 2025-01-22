from gradio_client import Client
import tkinter as tk
from tkinter import filedialog
import numpy as np
import pandas as pd

client = Client("robot146/ABAEProject")
root = tk.Tk()
root.title("ABAE Project Rohit")
root.geometry("600x600")
root.config(bg="lightblue")


#the label
label = tk.Label(root, text="Upload a text file containing the students work:",bg="lightblue",fg="black")
label.pack(pady=10)

#the textbox
textbox = tk.Text(root, height=15, width=50,bg="lightblue",fg="black")
textbox.pack(pady=10)

def open_file():
    #get text file and open text
    file_path = filedialog.askopenfilename(title="Open a text file", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            content = file.read()
            textbox.delete(1.0, tk.END) 
            textbox.insert(tk.END, content) 
    print(textbox.get("1.0", tk.END))
    
def retrieveFeedback():
    #get text from box
    message = textbox.get("1.0", tk.END)
    #send it to ai on space
    result = client.predict(
		message=message,
		system_message="You will be given a equation, or a set of equations. You are a tool that scores assignments. Grade the work and give it a score from 1 to 100. Only output their grade. Output the grade in a single line. Do not provide additional explanations. Enter only a single number. Do not provide an explanation. Output their just the grade in a single line. Format your answers as grade: then the value.",
		max_tokens=10,
		temperature=0.1,
		top_p=0.95,
		api_name="/chat"
    )
    #put in result
    textbox.delete(1.0, tk.END)
    textbox.insert(tk.END, result) 


#button to open text file
#nice colors?
button = tk.Button(root, text="Open Text File of Student Work", command=open_file,bg="lightblue",fg="black",activebackground="lightblue",activeforeground="black",highlightthickness=2,highlightbackground="lightblue")
button.pack(pady=10)

#button to submit
button2 = tk.Button(root, text="Submit to AI Grader", command=retrieveFeedback,bg="lightblue",fg="black",activebackground="lightblue",activeforeground="black",highlightthickness=2,highlightbackground="lightblue")
button2.pack(pady=10)

#loop thing
root.mainloop()


