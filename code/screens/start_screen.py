import root_screen
from tkinter import *
from tkinter import ttk


def start_screen():
    root = root_screen()

    frame = ttk.Frame(master=root, borderwidth=1, relief=SOLID)
    frame.pack(expand=True, anchor=CENTER, fill=X, padx=(root.winfo_width() // 4))
    
    frame_search = ttk.Frame(master=frame)
    frame_search.pack(anchor=NW, fill=X, padx=20, pady=20)
    frame_search.update()

    frame_authorization = ttk.Frame(master=frame)
    frame_authorization.pack(anchor=NW, fill=X, padx=20, pady=20)


    label_offline_search = ttk.Label(master=frame_search, text="Оффлайн поиск:", font=("Arial", 10, "bold"), justify=CENTER)
    label_offline_search.pack(pady=5)

    entry_search = ttk.Entry(master=frame_search, justify=CENTER, width=frame_search.winfo_width())
    entry_search.pack(pady=5)

    button_search = ttk.Button(master=frame_search, text="Узнать численность")
    button_search.pack(ipadx=25)


    button_register = ttk.Button(master=frame_authorization, text="Регистрация")
    button_register.pack(fill=X, ipady=5)

    button_login = ttk.Button(master=frame_authorization, text="Войти")
    button_login.pack(fill=X, ipady=5, pady=5)

    root.mainloop()
