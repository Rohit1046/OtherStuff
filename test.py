from gradio_client import Client
import tkinter as tk
from tkinter import filedialog

client = Client("robot146/ABAEProject")

# Create the main window
root = tk.Tk()
root.title("ABAE Project Rohit")
root.geometry("600x600")
root.config(bg="lightblue")  # Set window background color

# Add a label with custom colors
label = tk.Label(root, text="Upload a text file containing the students work:", 
                 bg="lightblue", fg="darkblue", font=("Arial", 14))
label.pack(pady=10)

# Add a textbox with custom background and text colors
textbox = tk.Text(root, height=15, width=50, bg="white", fg="black", font=("Arial", 12))
textbox.pack(pady=10)

# Function to open a file and load its contents
def open_file():
    file_path = filedialog.askopenfilename(title="Open a text file", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            content = file.read()
            textbox.delete(1.0, tk.END)  # Clear the textbox
            textbox.insert(tk.END, content)  # Insert the content
    print(textbox.get("1.0", tk.END))

def retrieveFeedback():
    message = textbox.get("1.0", tk.END)
    result = client.predict(
        message=message,
        system_message="You will be given a equation, or a set of equations. You are a tool that scores assignments. Grade the work and give it a score from 1 to 100. Only output their grade. Output the grade in a single line. Do not provide additional explanations. Enter only a single number. Do not provide an explanation. Output their just the grade in a single line. Format your answers as grade: then the value.",
        max_tokens=10,
        temperature=0.1,
        top_p=0.95,
        api_name="/chat"
    )
    textbox.delete(1.0, tk.END)  # Clear the textbox
    textbox.insert(tk.END, result)  # Insert the content

# Add an "Open" button to open the file dialog with custom colors
button = tk.Button(root, text="Open Text File", command=open_file, 
                   bg="lightgreen", fg="black", font=("Arial", 12), 
                   activebackground="lightblue", activeforeground="black", 
                   relief="solid", bd=2, highlightthickness=2, highlightbackground="lightblue")
button.pack(pady=10)

# Add a "Submit" button with custom colors
button2 = tk.Button(root, text="Submit", command=retrieveFeedback, 
                    bg="black", fg="white", font=("Arial", 12), 
                    activebackground="darkblue", activeforeground="white", 
                    relief="solid", bd=2, highlightthickness=2, highlightbackground="lightblue")
button2.pack(pady=10)

# Run the application
root.mainloop()
