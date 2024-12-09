from tkinter import *


def razmer_okna(event=None):
    # Получаем значения из текстовых полей
    width = entry_width.get()
    height = entry_height.get()

    # Проверяем, являются ли введенные данные числами
    if width.isdigit() and height.isdigit():
        # Применяем размеры к текстовому полю
        text_widget.config(width=int(width), height=int(height))


def focus_in(event):
    text_widget.config(bg="white")  # Цвет фона белый


def focus_out(event):
    text_widget.config(bg="lightgrey")  # Цвет фона серый



root = Tk()
root.title("Размер окна")

#  ширины и высоты поля
entry_width = Entry(root, width=5)
entry_width.insert(0, "0")  # Значение по умолчанию
entry_width.grid(row=0, column=0, padx=5, pady=5)

entry_height = Entry(root, width=5)
entry_height.insert(0, "0")  # Значение по умолчанию
entry_height.grid(row=1, column=0, padx=5, pady=5)


button = Button(root, text="Изменить", command=razmer_okna)
button.grid(row=0, column=1, rowspan=2, padx=5, pady=5)

# Многострочное текстовое поле
text_widget = Text(root, width=0, height=0, bg="lightgrey")
text_widget.grid(row=2, column=0, columnspan=2, padx=5, pady=5)


text_widget.bind("<FocusIn>", focus_in)
text_widget.bind("<FocusOut>", focus_out)
root.bind("<Return>", razmer_okna)  # нажатие Enter


root.mainloop()
