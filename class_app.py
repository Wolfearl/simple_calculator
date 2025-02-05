from class_calculator import Calculator
from tkinter import Tk, Menu, Toplevel


class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Калькулятор")
        self.geometry("246x300+600+200")
        self.background_color = "#90AFC5"
        self.configure(bg=self.background_color)
        self.resizable(False, False)

        self.menubar = Menu(self)
        self.build_menu()
        self.config(menu=self.menubar)
        self.new_menu = None

        self.calculator_frame = Calculator(self)
        self.calculator_frame.pack(expand=True, fill='both')

    def build_menu(self, root=None):
        if root is None:
            file_menu = Menu(self.menubar, tearoff=0)
            self.menubar.add_cascade(label="Файл", menu=file_menu)
            file_menu.add_command(label="Новый", command=self.open_calculator)
            file_menu.add_separator()
            file_menu.add_command(label="Выход", command=self.destroy)
        else:
            file_menu = Menu(self.new_menu, tearoff=0)
            self.new_menu.add_cascade(label="Файл", menu=file_menu)
            file_menu.add_command(label="Новый", command=self.open_calculator)
            file_menu.add_separator()
            file_menu.add_command(label="Выход", command=root.destroy)

    def open_calculator(self):
        geo = self.geometry()
        size, px, py = geo.split('+')
        width, height = map(int, size.split('x'))

        if len(self.winfo_children()) == 2:
            current_x = self.winfo_x() + 30
            current_y = self.winfo_y() + 30
        else:
            last_window = self.winfo_children()[-1]
            current_x = last_window.winfo_x() + 30
            current_y = last_window.winfo_y() + 30

        new_window = Toplevel(self)
        new_window.geometry(f'{width}x{height}+{current_x}+{current_y}')
        new_window.resizable(False, False)
        new_window.configure(bg=self.background_color)

        self.new_menu = Menu(new_window)
        self.build_menu(new_window)
        new_window.config(menu=self.new_menu)

        calculator_frame = Calculator(new_window)
        calculator_frame.pack(expand=True, fill='both')

    def exit_calculator(self):
        self.destroy()