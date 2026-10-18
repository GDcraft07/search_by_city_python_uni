import root_screen
from tkinter import *
from tkinter import ttk
from config import STANDARD_FONT


def authorization_screen(is_register: bool) -> None:
    root = root_screen("Регистрация" if is_register else "Вход")

    frame = ttk.Frame(master=root, borderwidth=1, relief=SOLID)
    frame.pack(expand=True, anchor=CENTER, fill=X, padx=(root.winfo_width() // 4))

    frame_heading = ttk.Frame(master=frame, borderwidth=1, relief=SOLID)
    frame_heading.pack(anchor=NW, fill=X, padx=20, pady=20)

    frame_get_data = ttk.Frame(master=frame, borderwidth=1, relief=SOLID)
    frame_get_data.pack(anchor=NW, fill=X, padx=20, pady=20)
    frame_get_data.update()


    text_heading = StringVar(value=("Регистрация" if is_register else "Вход"))

    label_heading = ttk.Label(master=frame_heading, textvariable=text_heading, justify=CENTER, font=STANDARD_FONT)
    label_heading.pack(pady=5)

    label_login = ttk.Label(master=frame_get_data, text="Логин: ", font=STANDARD_FONT)
    label_login.pack(anchor=NW, padx=5, pady=5)

    entry_login = ttk.Entry(master=frame_get_data, justify=CENTER, width=frame_get_data.winfo_width())
    entry_login.pack(padx=5)

    label_password = ttk.Label(master=frame_get_data, text="Пароль: ", font=STANDARD_FONT)
    label_password.pack(anchor=NW, padx=5, pady=5)

    entry_password = ttk.Entry(master=frame_get_data, justify=CENTER, width=frame_get_data.winfo_width(), show="*")
    entry_password.pack(padx=5)
    entry_password.update()

    error_message = StringVar()

    error_label = ttk.Label(master=frame_get_data, foreground="red", textvariable=error_message, wraplength=entry_password.winfo_width())
    error_label.pack(padx=5, pady=3)

    text_button = StringVar(value="Зарегистрироваться" if is_register else "Войти")

    button_authorization = ttk.Button(master=frame_get_data, textvariable=text_button)
    button_authorization.pack(fill=X, padx=5, pady=2)

    root.mainloop()
    