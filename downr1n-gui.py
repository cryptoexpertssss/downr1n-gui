import tkinter as tk
import os

# Create the GUI window
window = tk.Tk()
window.title("Downr1n Gui")
window.geometry("1280x720")

# Add the boot checkbox
boot_var = tk.IntVar()
boot_checkbox = tk.Checkbutton(window, text="Boot", variable=boot_var)
boot_checkbox.pack()

# Add the downgrade checkbox
downgrade_var = tk.IntVar()
downgrade_checkbox = tk.Checkbutton(window, text="Downgrade", variable=downgrade_var)
downgrade_checkbox.pack()

# Add the iOS version dropdown
ios_versions = ["14.1", "14.2", "14.3", "14.4", "14.5", "14.6", "14.7", "14.8", "15.0", "15.1", "15.2", "15.3", "15.4", "15.5", "15.6", "15.7"]
ios_var = tk.StringVar(window)
ios_var.set("Select iOS version")
ios_dropdown = tk.OptionMenu(window, ios_var, *ios_versions)
ios_dropdown.pack()

# Function to run the selected command
def run_command():
    ios_version = ios_var.get()
    if boot_var.get() == 1:
        command = f"./downr1n.sh --boot"
    elif downgrade_var.get() == 1:
        command = f"./downr1n.sh --downgrade {ios_version}"
    os.system(command)
    result_label.config(text=f"Command '{command}' has been executed.")

# Add the run button
run_button = tk.Button(window, text="Run Command", command=run_command)
run_button.pack()

# Add the result label
result_label = tk.Label(window, text=" ")
result_label.pack()

# Add the message label
message_label = tk.Label(window, text="Made By Aditya, Uckermark, https://github.com/Aditya20110/ , https://github.com/Uckermark")
message_label.pack()

# Start the GUI event loop
window.mainloop()

