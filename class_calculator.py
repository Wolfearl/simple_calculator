import re
from tkinter import StringVar, Frame, Label, Button
from tkinter.ttk import Combobox, Style


class Calculator(Frame):
    def __init__(self, root):
        super().__init__(root)

        #----------------Инициализация----------------------
        self.root = root
        self.configure(bg=self.root.cget("bg"))
        self.test = True
        self.number = "0"
        self.calculation = ""
        #---------------------------------------------------

        #-------------------Init Combobox-------------------
        self.var = StringVar()
        self.style = Style()
        self.style.theme_use('alt')
        self.style.configure("TCombobox", background="#336B87")
        self.combo = Combobox(self, textvariable=self.var)
        self.combo.set('Тема')
        #----------------------------------------------------

        #-------------------Create Labels--------------------
        self.lbl_up = Label(self, text=self.calculation, font=("Time New Roman", 8), bg="#2A3132", foreground="#CDCDC0", anchor="e")
        self.lbl_up.place(x=15, y=25, width=216, height=20)

        self.lbl_down = Label(self, text=self.number, font=("Time New Roman", 16, "bold"), bg="#2A3132", foreground="#CDCDC0", anchor="e")
        self.lbl_down.place(x=15, y=45, width=216, height=30)
        #----------------------------------------------------

        self.butt = [] # Список для хранения кнопок

        self.create_combobox()

        self.create_buttons()

    def create_combobox(self):
        #---------------Create Combobox---------------------
        themes = ('Dark', 'Light', 'Sea', 'Modern', 'Standard')
        self.combo['values'] = themes
        self.combo['state'] = 'readonly'
        self.combo.place(x=174, y=0, width=70, height=20)
        self.root.bind('<Control-z>', self.select_option1)
        self.root.bind('<Control-x>', self.select_option2)
        self.root.bind('<Control-c>', self.select_option3)
        self.root.bind('<Control-v>', self.select_option4)
        self.root.bind('<Control-b>', self.select_option5)
        self.combo.bind('<<ComboboxSelected>>', self.callback)
        #---------------------------------------------------

    def create_buttons(self):
        #---------------Create Button-----------------------
        buttons = [
            ["C", 15, 90, 40, 35], ["DEL", 59, 90, 40, 35], ["B", 103, 90, 40, 35], ["x^2", 147, 90, 40, 35], ["√", 191, 90, 40, 35],
            ["1", 15, 130, 40, 35], ["2", 59, 130, 40, 35], ["3", 103, 130, 40, 35], ["/", 147, 130, 40, 35], ["1/x", 191, 130, 40, 35],
            ["4", 15, 170, 40, 35], ["5", 59, 170, 40, 35], ["6", 103, 170, 40, 35], ["+", 147, 170, 40, 35], ["%", 191, 170, 40, 35],
            ["7", 15, 210, 40, 35], ["8", 59, 210, 40, 35], ["9", 103, 210, 40, 35], ["-", 147, 210, 40, 35], ["=", 191, 210, 40, 75],
            [".", 15, 250, 40, 35], ["0", 59, 250, 40, 35], ["+/-", 103, 250, 40, 35], ["*", 147, 250, 40, 35]
        ]
        for bt in buttons:
            com = lambda x=bt[0]: self.logicalc(x)
            if bt[0].isdigit():
                btn = Button(self, text=bt[0], bg="#5D9B9B", font=("Time New Roman", 12), command=com)
            else:
                btn = Button(self, text=bt[0], bg="#336B87", font=("Time New Roman", 12), command=com)

            btn.place(x=bt[1], y=bt[2], width=bt[3], height=bt[4])
            self.butt.append(btn)
        #----------------------------------------------------

    #-----Изменение стилей (вызывается из Combobox)------
    def callback(self, event):
        match self.var.get():
            case "Dark":
                self["bg"] = '#000'
                self.lbl_up.config(bg="#022027", foreground="#FFF")
                self.lbl_down.config(bg="#022027", foreground="#FFF")
                self.style.configure("TCombobox", background="#022027")
                for bot in self.butt:
                    if bot.cget('text').isdigit():
                        bot.config(bg="#23282B", foreground="#FFF")
                    else:
                        bot.config(bg="#022027", foreground="#FFF")
            case "Light":
                self["bg"] = '#FFF5EE'
                self.lbl_up.config(bg="#FFFAFA", foreground="#000")
                self.lbl_down.config(bg="#FFFAFA", foreground="#000")
                self.style.configure("TCombobox", background="#FFFAFA")
                for bot in self.butt:
                    if bot.cget('text').isdigit():
                        bot.config(bg="#FAEBD7", foreground="#000")
                    else:
                        bot.config(bg="#FFFAFA", foreground="#000")
            case "Sea":
                self["bg"] = '#003153'
                self.lbl_up.config(bg="#3E5F8A", foreground="#1D1E33")
                self.lbl_down.config(bg="#3E5F8A", foreground="#1D1E33")
                self.style.configure("TCombobox", background="#3E5F8A")
                for bot in self.butt:
                    if bot.cget('text').isdigit():
                        bot.config(bg="#4285B4", foreground="#1D1E33")
                    else:
                        bot.config(bg="#3E5F8A", foreground="#1D1E33")
            case "Modern":
                self["bg"] = '#2F3D4C'
                self.lbl_up.config(bg="#CED9DD", foreground="#2F3D4C")
                self.lbl_down.config(bg="#CED9DD", foreground="#2F3D4C")
                self.style.configure("TCombobox", background="#CED9DD")
                for bot in self.butt:
                    if bot.cget('text').isdigit():
                        bot.config(bg="#EDEAE5", foreground="#2F3D4C")
                    else:
                        bot.config(bg="#CED9DD", foreground="#2F3D4C")
            case 'Standard':
                self["bg"] = '#90AFC5'
                self.lbl_up.config(bg="#2A3132", foreground="#CDCDC0")
                self.lbl_down.config(bg="#2A3132", foreground="#CDCDC0")
                self.style.configure("TCombobox", background="#336B87")
                for bot in self.butt:
                    if bot.cget('text').isdigit():
                        bot.config(bg="#5D9B9B", foreground="#000")
                    else:
                        bot.config(bg="#336B87", foreground="#000")

    #----------------------------------------------------

    #----------Функции для работы горячих клавиш---------
    def select_option1(self, event):
        self.var.set('Dark')
        self.callback(event)

    def select_option2(self, event):
        self.var.set('Light')
        self.callback(event)

    def select_option3(self, event):
        self.var.set('Sea')
        self.callback(event)

    def select_option4(self, event):
        self.var.set('Modern')
        self.callback(event)

    def select_option5(self, event):
        self.var.set('Standard')
        self.callback(event)

    #----------------------------------------------------

    #------------Логика работы калькулятора--------------
    def logicalc(self, operation):
        match operation:
            case "C":
                self.number = ""
                self.calculation = ""

            case "DEL":
                self.number = self.number[:-1]

            case "B":
                if len(self.calculation) > 1 or self.calculation.isdigit():
                    self.calculation = str(re.sub(r'\d+\.*\d*.$', "", self.calculation))
                try:
                    self.number = str(re.findall(r'\d+\.*\d*', self.calculation)[-1])
                except IndexError:
                    self.number = "0"

            case "x^2":
                p = str(eval(self.number + "**2"))
                if (len(self.calculation) > 1 and self.calculation[-1].isdigit()) or self.calculation.isdigit():
                    self.calculation = str(re.sub(r'\d+\.*\d*$', p, self.calculation))
                else:
                    self.calculation += p
                self.number = p
                self.test = False

            case "%":
                if self.test and len(self.number) > 0 and len(self.calculation) > 1 and not self.calculation[-1].isdigit():
                    per = str(eval("(" + self.number + "/100) * " + re.findall(r'\d+\.*\d*$', self.calculation[:-1])[0]))
                    self.calculation += per
                    self.number = per
                self.test = False

            case "√":
                p = str(eval(self.number + "**1/2"))
                if (len(self.calculation) > 1 and self.calculation[-1].isdigit()) or self.calculation.isdigit():
                    if self.number.count('-') == 0:
                        self.calculation = str(re.sub(r'\d+\.*\d*$', p, self.calculation))
                    else:
                        self.calculation = str(re.sub(r'.\d+\.*\d*$', p, self.calculation))
                else:
                    self.calculation += p
                self.number = p
                self.test = False

            case "+/-":
                if self.number.count('.') == 0:
                   self.number = str(-1 * int(self.number))
                else:
                    self.number = str(-1 * float(self.number))

            case "1/x":
                p = str(eval("1/" + self.number))
                if (len(self.calculation) > 1 and self.calculation[-1].isdigit()) or self.calculation.isdigit():
                    if self.number.count('-') == 0:
                        self.calculation = str(re.sub(r'\d+\.*\d*$', p, self.calculation))
                    else:
                        self.calculation = str(re.sub(r'.\d+\.*\d*$', p, self.calculation))
                else:
                    self.calculation += p
                self.number = p
                self.test = False

            case "=":
                if self.test:
                    self.calculation += self.number
                else:
                    self.calculation = self.calculation[:-1]
                try:
                    self.number = str(eval(self.calculation))
                except IndexError and ZeroDivisionError:
                    self.number = "0"
                self.calculation = ""
                self.test = True

            case _:
                if operation.isdigit() or operation == ".":
                   if self.number == "0":
                       self.number = ""
                   self.add_number(operation)
                else:
                    if len(self.calculation) > 0:
                        if self.test and not self.calculation[-1].isdigit():
                            self.calculation += self.number
                            self.number = str(eval(self.calculation))
                            self.calculation += operation
                            self.test = False
                        elif self.test and self.calculation[-1].isdigit():
                            self.calculation = self.number + operation
                            self.test = False
                        elif self.calculation[-1].isdigit():
                            self.calculation += operation
                            self.test = False
                        else:
                            self.calculation = self.calculation[:-1] + operation
                            self.test = False
                    elif self.test:
                        self.calculation += self.number + operation
                        self.test = False


        self.update()

    def add_number(self, operation):
        if operation == "." and self.number.count(".") == 0:
            self.number += operation
        elif self.test and operation != ".":
            self.number += operation
        elif not self.test:
            self.number = operation
        self.test = True

    #----------------------------------------------------

    def update(self):
        if self.number == "":
            self.number = "0"
        self.lbl_up.configure(text=self.calculation)
        self.lbl_down.configure(text=self.number)