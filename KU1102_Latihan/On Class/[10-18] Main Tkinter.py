import tkinter as tk # import module tkinter as tk to the program

root=tk.Tk() # create an instance of the tk.Tk that will create the application window
# by convention, the main windo in tkinter is called root

# print(dir(tk)) # printing the content of the tkinter, can call it without calling the window

'''
Widget
widget = WidgetName (container, **options)
to create a widget that belongs to a container
container: the parent window or frame that you want to place the widget
options: one or more kwyword arguments that specigfy the configurations of the widget
'''

# place a label on the root window
# creating the widget on root window
message=tk.Label(root, text="Hello, World!")
# position the widget in the root window
message.pack() # if pack() is not called, the widget will be invisible

# import arithmetic as ar

# print(ar.kali(2,3)) # this is how to use the def in arithmetic module



root.mainloop() # call the mainloop() method of the main window project
# mainloop will keep the window open, is typically put on last line