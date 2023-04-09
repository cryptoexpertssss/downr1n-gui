import tkinter as tk
import subprocess

def on_start_clicked():
    ios_version = ios_var.get() # Get the selected iOS version from the dropdown menu
    command = f"./downr1n.sh --jailbreak {ios_version}" # Construct the command with the selected iOS version
    output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT).decode() # Run the command and capture the output
    output_text.delete("1.0", tk.END) # Clear the previous output
    output_text.insert(tk.END, output) # Display the new output in the Text widget

# Create a tkinter window
window = tk.Tk()
window.title("jailbreak Gui")
window.geometry("1280x720")

# Create a dropdown menu for selecting the iOS version
ios_var = tk.StringVar()
ios_var.set("iOS 14.3")
ios_menu = tk.OptionMenu(window, ios_var, "iOS 14.3", "iOS 14.2", "iOS 14.1")
ios_menu.pack()

# Create a button to start the jailbreak and a Text widget to display the output
start_button = tk.Button(text="Start", command=on_start_clicked)
start_button.pack()
output_text = tk.Text(window, height=20, width=80)
output_text.pack()

# Run the tkinter event loop
window.mainloop()

