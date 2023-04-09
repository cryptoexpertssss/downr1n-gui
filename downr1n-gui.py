import tkinter as tk
import os

# Create the main window
root = tk.Tk()
root.title("Downr1n Gui")
root.geometry("1280x720")

# Create the label for the dropdown menu
label = tk.Label(root, text="Select iOS version:")
label.pack()

# Create the dropdown menu
options = ["14.1", "14.2", "14.3", "14.4", "14.5", "14.6", "14.7", "15.0", "15.1", "15.2", "15.3", "15.4", "15.5", "15.6", "15.7"]
version = tk.StringVar(root)
version.set(options[0])
dropdown = tk.OptionMenu(root, version, *options)
dropdown.pack()

# Create the checkboxes
boot_var = tk.IntVar()
boot_checkbox = tk.Checkbutton(root, text="Boot", variable=boot_var)
boot_checkbox.pack()

downgrade_var = tk.IntVar()
downgrade_checkbox = tk.Checkbutton(root, text="Downgrade", variable=downgrade_var)
downgrade_checkbox.pack()

# Create the button to run the command
def run_command():
    ios_version = version.get()
    if boot_var.get():
        os.system(f"sudo ./downr1n.sh --boot {ios_version}")
    elif downgrade_var.get():
        os.system(f"sudo ./downr1n.sh --downgrade {ios_version}")

button = tk.Button(root, text="Run Command", command=run_command)
button.pack()

# Start the GUI event loop
root.mainloop()

