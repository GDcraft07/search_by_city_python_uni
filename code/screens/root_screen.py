from tkinter import *
from config import WIDTH, HEIGHT


def create_root(title: str="Поиск численности населения городов") -> Tk:
    root = Tk()
    root.title(title)
    root.geometry(f"{WIDTH}x{HEIGHT}+{(root.winfo_screenwidth() - WIDTH) // 2}+{(root.winfo_screenheight() - HEIGHT) // 2}")
    root.update()

    return root
