import pandas as pd
import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont

# Dictionary with funny names
funny_name_dict = {
    'A': 'Avocado',
    'B': 'Banana',
    'C': 'Cheeseburger',
    'D': 'Doughnut',
    'E': 'Elephant',
    'F': 'Flamingo',
    'G': 'Gummy Bear',
    'H': 'Hippo',
    'I': 'Ice Cream',
    'J': 'Jellyfish',
    'K': 'Kangaroo',
    'L': 'Lollipop',
    'M': 'Moose',
    'N': 'Noodle',
    'O': 'Octopus',
    'P': 'Pineapple',
    'Q': 'Quokka',
    'R': 'Rainbow',
    'S': 'Sloth',
    'T': 'Taco',
    'U': 'Unicorn',
    'V': 'Volcano',
    'W': 'Watermelon',
    'X': 'Xylophone',
    'Y': 'Yeti',
    'Z': 'Zebra'
}

# Load phonetic data from CSV
data = pd.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (_, row) in data.iterrows()}

# GUI setup
window = tk.Tk()
window.title("Word to Phonetic Converter")
window.geometry("500x300")
window.resizable(False, False)

# Custom font
custom_font = tkfont.Font(size=12)


# Function to convert word to phonetic representation
def convert_word():
    user_word = input_entry.get().upper()
    output = []
    if option_var.get() == "Funny":
        output = [funny_name_dict.get(letter, letter) for letter in user_word]
    else:
        output = [phonetic_dict.get(letter, letter) for letter in user_word]

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, " ".join(output))


# Create colorful background
bg_color = "#FFC107"  # Yellow
canvas = tk.Canvas(window, bg=bg_color, width=500, height=300)
canvas.pack(fill="both", expand=True)

# Create frame for content
frame = tk.Frame(canvas, bg="white", padx=20, pady=20)
frame.place(relx=0.5, rely=0.5, anchor="center")

# Create input label and entry
input_label = tk.Label(frame, text="Enter a word:", font=custom_font, fg="black", bg="white")
input_label.pack()

input_entry = tk.Entry(frame, font=custom_font)
input_entry.pack()

# Create option label and radio buttons
option_label = tk.Label(frame, text="Select output type:", font=custom_font, fg="black", bg="white")
option_label.pack()

option_var = tk.StringVar(value="Regular")

regular_radio = tk.Radiobutton(frame, text="Regular", variable=option_var, value="Regular", font=custom_font,
                               fg="black", bg="white")
regular_radio.pack()

funny_radio = tk.Radiobutton(frame, text="Creative", variable=option_var, value="Funny", font=custom_font, fg="black",
                             bg="white")
funny_radio.pack()

# Create conversion button
convert_button = tk.Button(frame, text="Convert", command=convert_word, font=custom_font, fg="Green",
                           bg="#2196F3")  # Yellow letter, blue background
convert_button.pack(pady=10)

# Customize button colors and text visibility
convert_button.config(activeforeground="#c01b15", activebackground="#c01b15")

# Create output label and text widget
output_label = tk.Label(frame, text="Output:", font=custom_font, fg="black", bg="white")
output_label.pack()

output_text = tk.Text(frame, height=5, width=30, font=custom_font)
output_text.pack()

# Adjust canvas to fit frame
canvas.create_window(250, 150, window=frame)

window.mainloop()
