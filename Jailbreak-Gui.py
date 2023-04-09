import tkinter as tk
import os

# Create a new tkinter window
window = tk.Tk()
window.title("jailbreak-gui")
window.geometry("1280x720")

# Create a label
label = tk.Label(window, text="Select iOS version:")
label.pack()

# Create a dropdown menu
ios_versions = ["14.1", "14.2", "14.3", "14.4", "14.5", "14.6", "14.7", "14.8", "15.0", "15.1", "15.2", "15.3", "15.4", "15.5", "15.6", "15.7"]
selected_version = tk.StringVar(window)
selected_version.set(ios_versions[0])
version_dropdown = tk.OptionMenu(window, selected_version, *ios_versions)
version_dropdown.pack()

# Define a function to be called when the button is clicked
def start_jailbreak():
    version = selected_version.get()
    command = f"sudo ./downr1n.sh --jailbreak {version}"
    os.system(command)

# Create a button
start_button = tk.Button(window, text="Jailbreak!", command=start_jailbreak)
start_button.pack()

# Create a label for the message
message = tk.Label(window, text="Made By Aditya, Uckermark, https://github.com/Aditya20110/, https://github.com/Uckermark")
message.pack(side=tk.BOTTOM)

# Start the tkinter event loop
window.mainloop()
