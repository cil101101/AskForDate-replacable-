import tkinter as tk
import random

# Function for the YES button
def yes_clicked():
    # Hide the main window
    root.withdraw()
    
    # Create a new window for the final message
    final_window = tk.Toplevel()
    final_window.title("Do you love me?")
    final_window.geometry("300x150")
    final_window.resizable(False, False)
    
    # Final message label
    final_label = tk.Label(final_window, 
                           text="Yay! I knew you'd say YES! ❤️.",
                           font=("Arial", 14),
                           justify="center")
    final_label.pack(pady=20)
    
    # Confirm button that will close the entire application
    confirm_button = tk.Button(final_window, text="luv u too", font=("Arial", 12),
                               command=root.destroy)
    confirm_button.pack(pady=10)

# Function to move the NO button when the mouse hovers over it
def move_no_button(event):
    # Ensure the geometry is up to date
    root.update_idletasks()
    btn_width = no_button.winfo_width()
    btn_height = no_button.winfo_height()
    
    # Calculate maximum x and y coordinates so that the button stays within the window
    max_x = 400 - btn_width
    max_y = 200 - btn_height
    new_x = random.randint(0, max_x)
    new_y = random.randint(0, max_y)
    no_button.place(x=new_x, y=new_y)

# Create the main window
root = tk.Tk()
root.title("For chels")
root.geometry("400x200")
root.resizable(False, False)

# Create and place the label
label = tk.Label(root, text="Will u go on a dinner with me?", font=("Arial", 16))
label.place(x=200, y=20, anchor="n")

# Create and place the YES button
yes_button = tk.Button(root, text="YES", font=("Arial", 14), bg="lightgreen", command=yes_clicked)
yes_button.place(x=100, y=100, anchor="center")

# Create and place the NO button
no_button = tk.Button(root, text="NO", font=("Arial", 14), bg="lightcoral")
no_button.place(x=300, y=100, anchor="center")
no_button.bind("<Enter>", move_no_button)  # Bind hover event to move the button

# Start the GUI event loop
root.mainloop()

