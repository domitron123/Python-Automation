import tkinter as tk 
import ttkbootstrap as ttk

macroOption = ["left click", 
               "right click", 
               "middle click", 
               "scroll up", 
               "scroll down", 
               "scroll left", 
               "scroll right", 
               "press key", 
               "press key combo", 
               "move mouse", 
               "move mouse to", 
               "move mouse to pixel", 
               "wait"]



#** window setup
window = ttk.Window()
window.title('Automated Macro Application')
window.geometry("800x650")

# Instructions frame with contents
instructionsFrame = ttk.Frame(master = window)

#!! -------------------------------------------------------
# Create a style for the button
style = ttk.Style()
style.configure("Custom.TButton", background="red", foreground="white")

# # Create a style for the button
# style = ttk.Style()
# style.configure("Custom.TButton", background="red", foreground="white")
#!! -------------------------------------------------------

# image = tk.PhotoImage(width=15, height=15)

firstSelection = ttk.Label(master = instructionsFrame, text = "Select a macro to add:")
firstSelection.pack(side = 'left')
dropDown = ttk.Combobox(master = instructionsFrame, values = macroOption)
dropDown.pack(side = 'left')
#!! -------------------------------------------------------
button = ttk.Button(instructionsFrame, text="Colorful Button", style="Custom.TButton")
button.pack()

# button = ttk.Button(instructionsFrame, text="Y", image=image, compound="center", )
# button.pack()
#!! -------------------------------------------------------

# if firstSelection == "left click":
#     print("left click")
#     cursorChords = ttk.Label(master = instructionsFrame, text = "Cursor coordinates:")
#     print(cursorChords)
#     cursorChords.pack(side = 'right')
    

instructionsFrame.pack()




#** run 
window.mainloop()