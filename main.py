from tkinter import *
from GUI import GUI

def createWindow():
    root = Tk()
    root.resizable(False, False)
    root.title("Sewdewko")
    root.configure(background="black")
    app = GUI(root)

    return app

def main():
    board = GUI()
    board.master.mainloop()

main()