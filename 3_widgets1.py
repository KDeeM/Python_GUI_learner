import tkinter as tk

window = tk.Tk()

# Label widgets contain text that is passed to the window
msg = "Hi, this is label widget text"
# Widgets contain a long list of parameters, specifying which argument you send
# is thus an important action
hello_label = tk.Label(text=msg)

# the label is created but requires to be added to the window
# One way is using the inbuilt widget .pack() method, also having its own optional parameters
hello_label.pack()

window.mainloop()
