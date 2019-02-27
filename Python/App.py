import tkinter
#import tkMessageBox

top = tkinter.Tk()

def clicked():
	#tkMessageBox.showinfo("Hello Python","Hello World")
	print("Button Clicked!")

b = tkinter.Button(top,text="click me!",command=clicked)

b.pack()
top.mainloop()