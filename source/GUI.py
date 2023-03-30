import tkinter
from BinaryTree import *
Tree=BinarySearchTree()
okno=tkinter.Tk()
okno.title("Binary Search Tree")
canvas=tkinter.Canvas(okno,width=1200,height=800,bg="white")
canvas.pack(side="right")
L1=tkinter.Label(okno, text="Number:")
Number=tkinter.Entry(okno,bd=2)
Add=tkinter.Button(okno,text="Add", command=lambda:(Tree.insert(Number.get()),kresliGUI()))
Remove=tkinter.Button(okno, text="Remove", command=lambda:(Tree.delete(int(Number.get())),kresliGUI()))
test=tkinter.Button(okno,text="test",command=lambda:(Tree.printTree(),kresliGUI()))
test.pack()
L1.pack()
Number.pack()
Add.pack()
Remove.pack()

def kresliGUI():
    canvas.delete(tkinter.ALL)
    Tree.kresli(canvas)





canvas.mainloop()