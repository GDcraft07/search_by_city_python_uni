import root_screen
from tkinter import *
from tkinter import ttk
from config import STANDARD_FONT


def base_screen(isAdmin: bool) -> None:
    root = root_screen()

    frame_search = ttk.Frame(master=root)
    frame_search.place(relx=0.5, rely=0.5, anchor=CENTER, width=root.winfo_width() // 3)
    frame_search.update()

    frame_utilities = ttk.Frame(master=root)
    frame_utilities.place(relx=0, rely=0, anchor=NW, width=root.winfo_width() // 3)

    frame_account = ttk.Frame(master=root)
    frame_account.place(x=frame_search.winfo_x() + frame_search.winfo_width(), rely=0, width=root.winfo_width() // 3)


    frame_searching = ttk.Frame(master=frame_search, borderwidth=1, relief=SOLID)
    frame_searching.pack(expand=True, anchor=CENTER, fill=X)
    frame_searching.update()

    label_search = ttk.Label(master=frame_searching, text="Поиск", font=STANDARD_FONT, justify=CENTER)
    label_search.pack(pady=5)

    entry_search = ttk.Entry(master=frame_searching, justify=CENTER)
    entry_search.pack(pady=5, fill=X, padx=5)
    
    button_search = ttk.Button(master=frame_searching, text="Узнать численность")
    button_search.pack(ipadx=25)


    button_history = ttk.Button(master= frame_utilities, text="История запросов", width=30)
    button_history.pack(anchor=NW, padx=5, pady=5)

    user_login = StringVar(value="GDcraft")
    label_login = ttk.Label(master=frame_account, textvariable=user_login, font=STANDARD_FONT, justify=RIGHT)
    label_login.pack(padx=5, pady=5, anchor=NE)

    button_change_password = ttk.Button(master=frame_account, text="Изменить пароль", width=30)
    button_change_password.pack(anchor=NE, padx=5, pady=2)
    button_change_password.update()

    button_logout = ttk.Button(master=frame_account, text="Выйти", width=30)
    button_logout.pack(anchor=NE, padx=5, pady=2)

    if isAdmin:
        button_user_requests = ttk.Button(master=frame_utilities, text="Запросы пользователей", width=30)
        button_user_requests.pack(anchor=NW, padx=5, pady=2)

        button_admin_panel = ttk.Button(master=frame_utilities, text="Админская панель", width=30)
        button_admin_panel.pack(anchor=NW, padx=5, pady=2)


    root.mainloop()
