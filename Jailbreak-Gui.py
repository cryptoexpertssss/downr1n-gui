import subprocess
import tkinter as tk

# Define the function to execute the selected command
def execute_command():
    if boot_var.get() == 1:
        command = f"sudo ./downr1n.sh --boot"
    elif downgrade_var.get() == 1:
        command = f"sudo ./downr1n.sh --downgrade {ios_versions.get()}"
    subprocess.run(command, shell=True)

# Create the main window
window = tk.Tk()
window.title("Downr1n Gui")
window.geometry("1280x720")

# Create the labels
tk.Label(window, text="Select an option:").grid(row=0, column=0, padx=10, pady=10)
tk.Label(window, text="Select the iOS version:").grid(row=1, column=0, padx=10, pady=10)

# Create the check boxes and the drop down menu
boot_var = tk.IntVar()
downgrade_var = tk.IntVar()
tk.Checkbutton(window, text="Boot", variable=boot_var).grid(row=0, column=1, padx=10, pady=10)
tk.Checkbutton(window, text="Downgrade", variable=downgrade_var).grid(row=0, column=2, padx=10, pady=10)
ios_versions = tk.StringVar()
ios_versions.set("14.1") # Set the default value
ios_versions_dropdown = tk.OptionMenu(window, ios_versions, "14.1", "14.2", "14.3", "14.4", "14.5", "14.6", "14.7", "14.8", "15.0", "15.1", "15.2", "15.3", "15.4", "15.5", "15.6", "15.7")
ios_versions_dropdown.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

# Create the button to execute the command
execute_button = tk.Button(window, text="Execute", command=execute_command)
execute_button.grid(row=2, column=1, padx=10, pady=10)

# Create the message label
tk.Label(window, text="Made By Aditya, Uckermark, https://github.com/Aditya20110/ , https://github.com/Uckermark").grid(row=3, column=0, columnspan=3, padx=10, pady=10)

# Start the main loop
window.mainloop()

