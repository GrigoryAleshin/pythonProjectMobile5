from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config

"""Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '600')"""


class MainApp(App):
    def build(self):
        # здесь я добавляю основной и остальные экраны в менеджера экранов, устанавливаю название и иконку,
        # этот класс больше ничего не делает
        sm.add_widget(MainScreen())
        sm.add_widget(FirstScreen())
        sm.add_widget(SecondScreen())
        sm.add_widget(ThirdScreen())
        sm.add_widget(FirstScreenLesson1())
        sm.add_widget(FirstScreenLesson2())
        sm.add_widget(FirstScreenLesson3())
        sm.add_widget(FirstScreenLesson4())
        sm.add_widget(FirstScreenLesson5())
        sm.add_widget(FirstScreenLesson6())
        sm.add_widget(FirstScreenLesson7())
        sm.add_widget(FirstScreenLesson8())
        sm.add_widget(SecondScreenLesson1())
        sm.add_widget(SecondScreenLesson3())
        sm.add_widget(SecondScreenLesson4())
        sm.add_widget(SecondScreenLesson5())
        sm.add_widget(SecondScreenLesson6())
        sm.add_widget(SecondScreenLesson7())
        sm.add_widget(ThirdScreenLesson1())
        sm.add_widget(ThirdScreenLesson2())
        sm.add_widget(ThirdScreenLesson3())
        sm.add_widget(ThirdScreenLesson4())
        sm.add_widget(ThirdScreenLesson5())

        self.title = "Приложение по Python"
        self.icon = 'icon-computer.png'
        return sm  # Позже я возвращаю менеджера для работы с ним


class MainScreen(Screen):
    def __init__(self):
        super().__init__()

        self.name = 'MainScreen'  # установка значения экранного имени для диспетчера экранов
        # (удобнее обращаться по имени, а не по классу)

        main_layout = FloatLayout()  # создание пустого макета, не привязанного к экрану

        self.add_widget(main_layout)  # добавление макета на экран

        hello = Label(text="Добро пожаловать",
                      font_size=24,
                      bold=True,
                      pos_hint={'center_x': .5, 'center_y': .95}
                      )
        hello_2 = Label(text="Данное приложение содержит преимущественно теоретический материал "
                             "с примерами использования",
                        text_size=[450, None],
                        font_size=20,
                        halign='center',
                        pos_hint={'center_x': .5, 'center_y': .85}
                        )

        # Кнопка
        Go_Screen2_1 = Button(text='Основы Python',
                              size_hint=(.7, None),
                              pos_hint={'center_x': .5, 'center_y': .70},
                              font_size=24
                              )
        Go_Screen2_2 = Button(text='ООП',
                              size_hint=(.7, None),
                              pos_hint={'center_x': .5, 'center_y': .55},
                              font_size=24
                              )
        Go_Screen2_3 = Button(text='Списки, кортежи, словари',
                              size_hint=(.7, None),
                              pos_hint={'center_x': .5, 'center_y': .40},
                              font_size=24
                              )
        Go_Screen2_4 = Button(text='Продолжение когда-то будет',
                              size_hint=(.7, None),
                              pos_hint={'center_x': .5, 'center_y': .25},
                              font_size=24
                              )
        # настройка кнопок для выполнения действия при нажатии
        Go_Screen2_1.bind(on_press=self.to_second_scrn_first)
        Go_Screen2_2.bind(on_press=self.to_second_scrn_second)
        Go_Screen2_3.bind(on_press=self.to_second_scrn_third)

        # добавление меток и кнопок в макет
        main_layout.add_widget(hello)
        main_layout.add_widget(hello_2)
        main_layout.add_widget(Go_Screen2_1)
        main_layout.add_widget(Go_Screen2_2)
        main_layout.add_widget(Go_Screen2_3)
        main_layout.add_widget(Go_Screen2_4)

    def to_second_scrn_first(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'FirstScreen'  # выбор экрана по названию
        return 0

    def to_second_scrn_second(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'SecondScreen'
        return 0

    def to_second_scrn_third(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'ThirdScreen'
        return 0


class FirstScreen(Screen):
    def __init__(self):
        super().__init__()
        # на этом остальных подобных экранах я делаю все то же самое,
        # что и на главном экране, чтобы иметь возможность переключаться туда и обратно
        self.name = 'FirstScreen'
        second_layout = FloatLayout()
        self.add_widget(second_layout)

        first_label = Label(text="Основы Python",
                            font_size=24,
                            bold=True,
                            pos_hint={'center_x': .5, 'center_y': .95}
                            )

        Go_Back = Button(text='<',
                         bold=True,
                         font_size='28',
                         halign='center',
                         size_hint=(.1, .07),
                         pos_hint={'center_x': .05, 'center_y': 0.95},
                         )

        Go_Back.bind(on_press=self.to_main_scrn)

        Button_1 = Button(text='Основы написания программ',
                          text_size=[200, None],
                          halign='center',
                          size_hint=(.4, None),
                          pos_hint={'center_x': .25, 'center_y': 0.8}
                          )
        Button_2 = Button(text='Переменные и типы данных',
                          text_size=[200, None],
                          halign='center',
                          size_hint=(.4, None),
                          pos_hint={'center_x': .25, 'center_y': 0.6}
                          )
        Button_3 = Button(text='Арифметические операции',
                          text_size=[200, None],
                          halign='center',
                          size_hint=(.4, None),
                          pos_hint={'center_x': .25, 'center_y': 0.4}
                          )
        Button_4 = Button(text='Условные выражения',
                          text_size=[200, None],
                          halign='center',
                          size_hint=(.4, None),
                          pos_hint={'center_x': .25, 'center_y': 0.2}
                          )
        Button_5 = Button(text='Циклы',
                          text_size=[200, None],
                          halign='center',
                          size_hint=(.4, None),
                          pos_hint={'center_x': .75, 'center_y': 0.8}
                          )
        Button_6 = Button(text='Функции',
                          text_size=[200, None],
                          halign='center',
                          size_hint=(.4, None),
                          pos_hint={'center_x': .75, 'center_y': 0.6}
                          )
        Button_7 = Button(text='Лямбда-выражения',
                          text_size=[200, None],
                          halign='center',
                          size_hint=(.4, None),
                          pos_hint={'center_x': .75, 'center_y': 0.4}
                          )
        Button_8 = Button(text='Преобразование типов',
                          text_size=[200, None],
                          halign='center',
                          size_hint=(.4, None),
                          pos_hint={'center_x': .75, 'center_y': 0.2}
                          )

        Button_1.bind(on_press=self.to_one_scrn)
        Button_2.bind(on_press=self.to_two_scrn)
        Button_3.bind(on_press=self.to_three_scrn)
        Button_4.bind(on_press=self.to_four_scrn)
        Button_5.bind(on_press=self.to_five_scrn)
        Button_6.bind(on_press=self.to_six_scrn)
        Button_7.bind(on_press=self.to_seven_scrn)
        Button_8.bind(on_press=self.to_eight_scrn)

        second_layout.add_widget(first_label)
        second_layout.add_widget(Button_1)
        second_layout.add_widget(Button_2)
        second_layout.add_widget(Button_3)
        second_layout.add_widget(Button_4)
        second_layout.add_widget(Button_5)
        second_layout.add_widget(Button_6)
        second_layout.add_widget(Button_7)
        second_layout.add_widget(Button_8)
        second_layout.add_widget(Go_Back)

    def to_main_scrn(self, *args):  # вместе с нажатием кнопки она передает информацию о себе.
        # Чтобы не выскакивала ошибка, я добавляю в функцию *args
        self.manager.transition.direction = 'right'
        self.manager.current = 'MainScreen'
        return 0

    def to_one_scrn(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'FirstScreenLesson1'
        return 0

    def to_two_scrn(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'FirstScreenLesson2'
        return 0

    def to_three_scrn(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'FirstScreenLesson3'
        return 0

    def to_four_scrn(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'FirstScreenLesson4'
        return 0

    def to_five_scrn(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'FirstScreenLesson5'
        return 0

    def to_six_scrn(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'FirstScreenLesson6'
        return 0

    def to_seven_scrn(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'FirstScreenLesson7'
        return 0

    def to_eight_scrn(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'FirstScreenLesson8'
        return 0


class FirstScreenLesson1(Screen):
    def __init__(self):
        super().__init__()
        self.name = 'FirstScreenLesson1'
        firstScreenLesson1_layout = FloatLayout()
        self.add_widget(firstScreenLesson1_layout)
        label_1 = Label(text="Основы написания программ",
                        font_size=24,
                        bold=True,
                        pos_hint={'center_x': .5, 'center_y': 0.95}
                        )
        label_2 = Label(text="Программа на языке Python состоит из набора инструкций. "
                             "Каждая инструкция помещается на новую строку. Например:",
                        text_size=[450, None],
                        color=(1, 1, 1),
                        pos_hint={'center_x': .5, 'center_y': 0.85}
                        )
        label_2_1 = Label(text="1.print('Hello')",
                          font_size=20,
                          bold=True,
                          pos_hint={'center_x': .5, 'center_y': 0.77}
                          )
        label_3 = Label(text="Большую роль в Python играют отступы. "
                             "Неправильно поставленный отступ фактически является ошибкой."
                             "Поэтому стоит помещать новые инструкции сначала строки.",
                        text_size=[450, None],
                        font_size=20,
                        bold=False,
                        halign='left',
                        pos_hint={'center_x': .5, 'center_y': 0.65}
                        )
        label_3_1 = Label(text="1.    print('Hello')",
                          font_size=20,
                          bold=True,
                          pos_hint={'center_x': .5, 'center_y': 0.55}
                          )
        label_4 = Label(text="Некоторые конструкции языка могут состоять из нескольких строк. "
                             "Например, условная конструкция if. здесь уже должен быть отступ, так как инструкция "
                             "print('Hello') используется не сама по себе, а как часть условной конструкции if. "
                             "Причем отступ, согласно руководству по оформлению кода, желательно делать из такого "
                             "количество пробелов, которое кратно 4",
                        text_size=[450, None],
                        font_size=20,
                        bold=False,
                        halign='left',
                        pos_hint={'center_x': .5, 'center_y': 0.35}
                        )
        label_4_1 = Label(text="1.if 1 < 2:",
                          font_size=20,
                          bold=True,
                          pos_hint={'center_x': .5, 'center_y': 0.18}
                          )
        label_4_2 = Label(text="2.  print('Hello')",
                          font_size=20,
                          bold=True,
                          pos_hint={'center_x': .55, 'center_y': 0.15}
                          )

        Go_Back = Button(text='<',
                         bold=True,
                         font_size='28',
                         size_hint=(.1, .07),
                         halign='center',
                         pos_hint={'center_x': .05, 'center_y': 0.95},
                         )

        Go_Back.bind(on_press=self.to_back_scrn)

        firstScreenLesson1_layout.add_widget(Go_Back)
        firstScreenLesson1_layout.add_widget(label_1)
        firstScreenLesson1_layout.add_widget(label_2)
        firstScreenLesson1_layout.add_widget(label_2_1)
        firstScreenLesson1_layout.add_widget(label_3)
        firstScreenLesson1_layout.add_widget(label_3_1)
        firstScreenLesson1_layout.add_widget(label_4)
        firstScreenLesson1_layout.add_widget(label_4_1)
        firstScreenLesson1_layout.add_widget(label_4_2)

    def to_back_scrn(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'FirstScreen'
        return 0


class FirstScreenLesson2(Screen):
    def __init__(self):
        super().__init__()
        self.name = 'FirstScreenLesson2'
        firstScreenLesson2_layout = FloatLayout()
        self.add_widget(firstScreenLesson2_layout)

        hello = Label(text="Переменные и типы данных",
                      font_size=24,
                      bold=True,
                      pos_hint={'center_x': .5, 'center_y': .95}
                      )
        label_1 = Label(text="Переменные предназначены для хранения данных. Название переменной в Python может "
                             "содержать алфавитно-цифровые символы и знак подчеркивания. И  название переменной не "
                             "должно совпадать с названием ключевых слов языка Python.",
                        text_size=[450, None],
                        color=(1, 1, 1),
                        pos_hint={'center_x': .5, 'center_y': 0.8}
                        )
        label_2 = Label(text="Пример создания переменной:",
                        text_size=[450, None],
                        color=(1, 1, 1),
                        pos_hint={'center_x': .5, 'center_y': 0.7}
                        )
        label_2_1 = Label(text="1.name = 'Tom'",
                          color=(1, 1, 1),
                          font_size="20",
                          bold=True,
                          pos_hint={'center_x': .5, 'center_y': 0.66}
                          )
        label_3 = Label(text="Типы данных",
                        font_size=24,
                        bold=True,
                        pos_hint={'center_x': .5, 'center_y': .6}
                        )
        label_4 = Label(text="Переменная хранит данные одного из типов данных. В Python существует множество различных "
                             "типов данных. Базовые типы: bool, int, float, complex и str.",
                        text_size=[450, None],
                        color=(1, 1, 1),
                        pos_hint={'center_x': .5, 'center_y': 0.53}
                        )
        label_4_1 = Label(text="Тип bool представляет два логических значения: True (верно, истина) или False "
                               "(неверно, ложь)",
                          text_size=[450, None],
                          color=(1, 1, 1),
                          pos_hint={'center_x': .5, 'center_y': 0.45}
                          )
        label_4_2 = Label(text="Тип int представляет целое число, например, 1, 4, 8, 50. ",
                          text_size=[450, None],
                          color=(1, 1, 1),
                          pos_hint={'center_x': .5, 'center_y': 0.38}
                          )
        label_4_3 = Label(text="Тип float представляет число с плавающей точкой, например, 1.2 или 34.76. В качесте "
                               "разделителя целой и дробной частей используется точка.",
                          text_size=[450, None],
                          color=(1, 1, 1),
                          pos_hint={'center_x': .5, 'center_y': 0.30}
                          )
        label_4_4 = Label(text="Тип complex представляет комплексные числа в формате вещественная_часть+мнимая_частьj "
                               "- после мнимой части указывается суффикс j",
                          text_size=[450, None],
                          color=(1, 1, 1),
                          pos_hint={'center_x': .5, 'center_y': 0.20}
                          )
        label_4_5 = Label(text="Тип str представляет строки. Строка представляет последовательность символов, "
                               "заключенную в одинарные или двойные кавычки.",
                          text_size=[450, None],
                          color=(1, 1, 1),
                          pos_hint={'center_x': .5, 'center_y': 0.10}
                          )
        Go_Back = Button(text='<',
                         bold=True,
                         font_size='28',
                         size_hint=(.1, .07),
                         halign='center',
                         pos_hint={'center_x': .05, 'center_y': 0.95},
                         )

        Go_Back.bind(on_press=self.to_back_scrn)

        firstScreenLesson2_layout.add_widget(Go_Back)
        firstScreenLesson2_layout.add_widget(hello)
        firstScreenLesson2_layout.add_widget(label_1)
        firstScreenLesson2_layout.add_widget(label_2)
        firstScreenLesson2_layout.add_widget(label_2_1)
        firstScreenLesson2_layout.add_widget(label_3)
        firstScreenLesson2_layout.add_widget(label_4)
        firstScreenLesson2_layout.add_widget(label_4_1)
        firstScreenLesson2_layout.add_widget(label_4_2)
        firstScreenLesson2_layout.add_widget(label_4_3)
        firstScreenLesson2_layout.add_widget(label_4_4)
        firstScreenLesson2_layout.add_widget(label_4_5)

    def to_back_scrn(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'FirstScreen'
        return 0


class FirstScreenLesson3(Screen):
    def __init__(self):
        super().__init__()
        self.name = 'FirstScreenLesson3'
        firstScreenLesson3_layout = FloatLayout()
        self.add_widget(firstScreenLesson3_layout)
        hello = Label(text="Арифметические операции",
                      font_size=24,
                      bold=True,
                      pos_hint={'center_x': .5, 'center_y': .95}
                      )
        label_1 = Label(text="Python поддерживает все распространенные арифметические операции, среди который сложение"
                             ", вычитание, умножение, деление, целочисленное деление (данная операция возвращает "
                             "целочисленный результат деления), возведение в степень и остаток от деления",
                        text_size=[450, None],
                        color=(1, 1, 1),
                        pos_hint={'center_x': .5, 'center_y': 0.8}
                        )
        label_2 = Label(text="Если производится несколько арефм. операций, то они выполняются в соответствии с их "
                             "приоритетом.",
                        text_size=[450, None],
                        color=(1, 1, 1),
                        pos_hint={'center_x': .5, 'center_y': 0.67}
                        )
        label_2_1 = Label(text="1.number = 3 + 4 * 5 ** 2 + 7",
                          color=(1, 1, 1),
                          font_size="20",
                          bold=True,
                          pos_hint={'center_x': .5, 'center_y': 0.62}
                          )
        label_3 = Label(text="Приоритет операций:",
                        text_size=[450, None],
                        color=(1, 1, 1),
                        pos_hint={'center_x': .5, 'center_y': 0.57}
                        )
        label_3_1 = Label(text="1 - **",
                          text_size=[450, None],
                          font_size="20",
                          color=(1, 1, 1),
                          bold=True,
                          pos_hint={'center_x': .5, 'center_y': 0.52}
                          )
        label_3_2 = Label(text="2 - *, /, //, %",
                          text_size=[450, None],
                          font_size="20",
                          color=(1, 1, 1),
                          bold=True,
                          pos_hint={'center_x': .5, 'center_y': 0.47}
                          )
        label_3_3 = Label(text="3 - +, -",
                          text_size=[450, None],
                          font_size="20",
                          color=(1, 1, 1),
                          bold=True,
                          pos_hint={'center_x': .5, 'center_y': 0.42}
                          )
        label_4 = Label(text="Округление чисел.",
                        font_size="20",
                        color=(1, 1, 1),
                        bold=True,
                        pos_hint={'center_x': .5, 'center_y': 0.39}
                        )
        label_4_1 = Label(text="При операциях с числами типа float надо учитывать, что результат операций с ними может "
                               "быть не совсем точным. Поэтому для более точного результата можно использовать функцию"
                               "round().",
                          text_size=[450, None],
                          color=(1, 1, 1),
                          pos_hint={'center_x': .5, 'center_y': 0.30}
                          )
        label_4_2 = Label(text="В функцию round() передается число, которое надо округлить. Если передается одно число,"
                               "то оно округлится до ближайшего целого. Также в функцию можно передать второе число, "
                               "которое будет означать сколько знаков после запятой останется.",
                          text_size=[450, None],
                          color=(1, 1, 1),
                          pos_hint={'center_x': .5, 'center_y': 0.16}
                          )
        label_4_3 = Label(text="1.print(round(46.4756028, 3))   # 46.476",
                          font_size="20",
                          color=(1, 1, 1),
                          bold=True,
                          pos_hint={'center_x': .5, 'center_y': 0.05}
                          )
        Go_Back = Button(text='<',
                         bold=True,
                         font_size='28',
                         size_hint=(.1, .07),
                         halign='center',
                         pos_hint={'center_x': .05, 'center_y': 0.95},
                         )

        Go_Back.bind(on_press=self.to_back_scrn)

        firstScreenLesson3_layout.add_widget(Go_Back)
        firstScreenLesson3_layout.add_widget(hello)
        firstScreenLesson3_layout.add_widget(label_1)
        firstScreenLesson3_layout.add_widget(label_2)
        firstScreenLesson3_layout.add_widget(label_2_1)
        firstScreenLesson3_layout.add_widget(label_3)
        firstScreenLesson3_layout.add_widget(label_3_1)
        firstScreenLesson3_layout.add_widget(label_3_2)
        firstScreenLesson3_layout.add_widget(label_3_3)
        firstScreenLesson3_layout.add_widget(label_4)
        firstScreenLesson3_layout.add_widget(label_4_1)
        firstScreenLesson3_layout.add_widget(label_4_2)
        firstScreenLesson3_layout.add_widget(label_4_3)

    def to_back_scrn(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'FirstScreen'
        return 0


class FirstScreenLesson4(Screen):
    def __init__(self):
        super().__init__()
        self.name = 'FirstScreenLesson4'
        firstScreenLesson4_layout = FloatLayout()
        self.add_widget(firstScreenLesson4_layout)
        hello = Label(text="Условные выражения",
                      font_size=24,
                      bold=True,
                      pos_hint={'center_x': .5, 'center_y': .95}
                      )
        label_1 = Label(text="Ряд операций представляют условные выражения. Принимает два операднда и возвращает True "
                             "или False. ",
                        text_size=[450, None],
                        color=(1, 1, 1),
                        pos_hint={'center_x': .5, 'center_y': 0.8}
                        )

        label_2 = Label(text="Простейшие условные выражения представляют операции сравнения, которые сравнивают два "
                             "значения. Python поддерживает следующие операции сравнения: ==, !=, >, <, >=, <=",
                        text_size=[450, None],
                        color=(1, 1, 1),
                        pos_hint={'center_x': .5, 'center_y': 0.7}
                        )
        label_2_1 = Label(text="1.print(5 != 1)  # True",
                          color=(1, 1, 1),
                          font_size="20",
                          bold=True,
                          pos_hint={'center_x': .5, 'center_y': 0.6}
                          )
        label_3 = Label(text="Для создания составных условных выражений применяются логические операции. В Python "
                             "имеются следующие логические операторы: and, or, not",
                        text_size=[450, None],
                        color=(1, 1, 1),
                        pos_hint={'center_x': .5, 'center_y': 0.5}
                        )
        label_4 = Label(text="Оператор in возвращает True если в некотором наборе значений есть определенное значение. "
                             "Он имеет следующую форму: значение in набор_значений",
                        text_size=[450, None],
                        color=(1, 1, 1),
                        pos_hint={'center_x': .5, 'center_y': 0.38}
                        )
        label_4_1 = Label(text="1.message = 'hello world!'              "
                               "2.print('hello' in message) # True "
                               "3.print('well' in message) # False",
                          text_size=[270, None],
                          bold=True,
                          color=(1, 1, 1),
                          pos_hint={'center_x': .5, 'center_y': 0.25}
                          )
        Go_Back = Button(text='<',
                         bold=True,
                         font_size='28',
                         size_hint=(.1, .07),
                         halign='center',
                         pos_hint={'center_x': .05, 'center_y': 0.95},
                         )

        Go_Back.bind(on_press=self.to_back_scrn)

        firstScreenLesson4_layout.add_widget(Go_Back)
        firstScreenLesson4_layout.add_widget(hello)
        firstScreenLesson4_layout.add_widget(label_1)
        firstScreenLesson4_layout.add_widget(label_2)
        firstScreenLesson4_layout.add_widget(label_2_1)
        firstScreenLesson4_layout.add_widget(label_3)
        firstScreenLesson4_layout.add_widget(label_4)
        firstScreenLesson4_layout.add_widget(label_4_1)

    def to_back_scrn(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'FirstScreen'
        return 0


class FirstScreenLesson5(Screen):
    def __init__(self):
        super().__init__()
        self.name = 'FirstScreenLesson5'
        firstScreenLesson5_layout = FloatLayout()
        self.add_widget(firstScreenLesson5_layout)
        hello = Label(text="Циклы",
                      font_size=24,
                      bold=True,
                      pos_hint={'center_x': .5, 'center_y': .95}
                      )
        label_1 = Label(text="Циклы позволяют выполнять некоторое действие в зависимости от соблюдения некоторого "
                             "условия. В языке Python есть следующие типы циклов: while и for",
                        text_size=[450, None],
                        color=(1, 1, 1),
                        pos_hint={'center_x': .5, 'center_y': 0.8}
                        )
        label_2 = Label(text="Цикл while проверяет истинность некоторого условия, и если условие истинно, то выполняет "
                             "инструкции цикла. Определение цикла выглядит следующим образом:",
                        text_size=[450, None],
                        color=(1, 1, 1),
                        pos_hint={'center_x': .5, 'center_y': 0.68}
                        )
        label_2_1 = Label(text="1.while условное_выражение: "
                               "2.   инструкции",
                          text_size=[260, None],
                          bold=True,
                          color=(1, 1, 1),
                          pos_hint={'center_x': .5, 'center_y': 0.56}
                          )
        label_3 = Label(text="Цикл for пробегается по набору значений, помещает каждое значение в переменную. После с "
                             "этой перменной можно проводить различные действия. Определение цикла выглядит следующим "
                             "образом:",
                        text_size=[450, None],
                        color=(1, 1, 1),
                        pos_hint={'center_x': .5, 'center_y': 0.45}
                        )
        label_3_1 = Label(text="1.for переменная in набор_значений: "
                               "2.   инструкции",
                          text_size=[320, None],
                          bold=True,
                          color=(1, 1, 1),
                          pos_hint={'center_x': .5, 'center_y': 0.35}
                          )
        Go_Back = Button(text='<',
                         bold=True,
                         font_size='28',
                         size_hint=(.1, .07),
                         halign='center',
                         pos_hint={'center_x': .05, 'center_y': 0.95},
                         )

        Go_Back.bind(on_press=self.to_back_scrn)

        firstScreenLesson5_layout.add_widget(Go_Back)
        firstScreenLesson5_layout.add_widget(hello)
        firstScreenLesson5_layout.add_widget(label_1)
        firstScreenLesson5_layout.add_widget(label_2)
        firstScreenLesson5_layout.add_widget(label_2_1)
        firstScreenLesson5_layout.add_widget(label_3)
        firstScreenLesson5_layout.add_widget(label_3_1)

    def to_back_scrn(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'FirstScreen'
        return 0


class FirstScreenLesson6(Screen):
    def __init__(self):
        super().__init__()
        self.name = 'FirstScreenLesson6'
        firstScreenLesson6_layout = FloatLayout()
        self.add_widget(firstScreenLesson6_layout)
        hello = Label(text="Функции",
                      font_size=24,
                      bold=True,
                      pos_hint={'center_x': .5, 'center_y': .95}
                      )
        label_1 = Label(text="Функции представляют блок кода, который выполняет определенную задачу и который можно "
                             "повторно использовать в других частях программы. Определение функции выглядит следующим "
                             "образом:",
                        text_size=[450, None],
                        color=(1, 1, 1),
                        pos_hint={'center_x': .5, 'center_y': 0.8}
                        )
        label_1_1 = Label(text="1.def имя_функции ([параметры]): "
                               "2.   инструкции",
                          text_size=[300, None],
                          bold=True,
                          color=(1, 1, 1),
                          pos_hint={'center_x': .5, 'center_y': 0.68}
                          )
        label_2 = Label(text="Для вызова функции указывается имя функции, после которого в скобках идет передача "
                             "значений для всех ее параметров:",
                        text_size=[450, None],
                        color=(1, 1, 1),
                        pos_hint={'center_x': .5, 'center_y': 0.60}
                        )
        label_2_1 = Label(text="1.имя_функции ([параметры])",
                          text_size=[300, None],
                          bold=True,
                          color=(1, 1, 1),
                          pos_hint={'center_x': .5, 'center_y': 0.52}
                          )
        label_3 = Label(text="Одни функции могут определяться внутри других функций - внутренние функции еще называют "
                             "локальными. Локальные функции можно использовать только внутри той функции, в которой они"
                             " определены.",
                        text_size=[450, None],
                        color=(1, 1, 1),
                        pos_hint={'center_x': .5, 'center_y': 0.4}
                        )
        label_3_1 = Label(text="1.def print_messages():      ",
                          text_size=[340, None],
                          bold=True,
                          color=(1, 1, 1),
                          pos_hint={'center_x': .5, 'center_y': 0.3}
                          )
        label_3_2 = Label(text="2.    # определение локальных функций "
                               "3.    def say_hello(): print('Hello')                    "
                               "4.    say_hello()                                                    "
                               "5.                                                       "
                               "6.print_messages() ",
                          text_size=[340, None],
                          bold=True,
                          color=(1, 1, 1),
                          pos_hint={'center_x': .5, 'center_y': 0.21}
                          )
        Go_Back = Button(text='<',
                         bold=True,
                         font_size='28',
                         size_hint=(.1, .07),
                         halign='center',
                         pos_hint={'center_x': .05, 'center_y': 0.95},
                         )

        Go_Back.bind(on_press=self.to_back_scrn)

        firstScreenLesson6_layout.add_widget(Go_Back)
        firstScreenLesson6_layout.add_widget(hello)
        firstScreenLesson6_layout.add_widget(label_1)
        firstScreenLesson6_layout.add_widget(label_1_1)
        firstScreenLesson6_layout.add_widget(label_2)
        firstScreenLesson6_layout.add_widget(label_2_1)
        firstScreenLesson6_layout.add_widget(label_3)
        firstScreenLesson6_layout.add_widget(label_3_1)
        firstScreenLesson6_layout.add_widget(label_3_2)

    def to_back_scrn(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'FirstScreen'
        return 0


class FirstScreenLesson7(Screen):
    def __init__(self):
        super().__init__()
        self.name = 'FirstScreenLesson7'
        firstScreenLesson7_layout = FloatLayout()
        self.add_widget(firstScreenLesson7_layout)
        hello = Label(text="Лямбда-выражения",
                      font_size=24,
                      bold=True,
                      pos_hint={'center_x': .5, 'center_y': .95}
                      )
        label_1 = Label(text="Лямбда-выражения в языке Python представляют небольшие функции, которые определяются с "
                             "помощью оператора lambda. Определение выглядит следующим образом:",
                        text_size=[450, None],
                        color=(1, 1, 1),
                        pos_hint={'center_x': .5, 'center_y': 0.8}
                        )
        label_1_1 = Label(text="1.lambda [параметры] : инструкция",
                          text_size=[300, None],
                          bold=True,
                          color=(1, 1, 1),
                          pos_hint={'center_x': .5, 'center_y': 0.7}
                          )
        label_2 = Label(text="Пример простого лямбда-выражения:",
                        text_size=[450, None],
                        color=(1, 1, 1),
                        pos_hint={'center_x': .5, 'center_y': 0.65}
                        )
        label_2_1 = Label(text="1.message = lambda: print('hello') "
                               "2.message()   # hello",
                          text_size=[300, None],
                          bold=True,
                          color=(1, 1, 1),
                          pos_hint={'center_x': .5, 'center_y': 0.58}
                          )
        label_3 = Label(text="Если лямбда-выражение имеет параметры, то они определяются после ключевого слова lambda. "
                             "Если лямбда-выражение возвращает какой-то результат, то он указывается после двоеточия.",
                        text_size=[450, None],
                        color=(1, 1, 1),
                        pos_hint={'center_x': .5, 'center_y': 0.48}
                        )
        label_3_1 = Label(text="1.square = lambda n: n * n "
                               "2.print(square(8))    # 64",
                          text_size=[300, None],
                          bold=True,
                          color=(1, 1, 1),
                          pos_hint={'center_x': .5, 'center_y': 0.38}
                          )
        label_4 = Label(text="Аналогичным образом можно создавать лямбда-выражения, которые принимают несколько "
                             "параметров:",
                        text_size=[450, None],
                        color=(1, 1, 1),
                        pos_hint={'center_x': .5, 'center_y': 0.29}
                        )
        label_4_1 = Label(text="1.sum = lambda a, b: a + b "
                               "2.print(sum(9, 2))    # 11",
                          text_size=[300, None],
                          bold=True,
                          color=(1, 1, 1),
                          pos_hint={'center_x': .5, 'center_y': 0.2}
                          )
        Go_Back = Button(text='<',
                         bold=True,
                         font_size='28',
                         size_hint=(.1, .07),
                         halign='center',
                         pos_hint={'center_x': .05, 'center_y': 0.95},
                         )

        Go_Back.bind(on_press=self.to_back_scrn)

        firstScreenLesson7_layout.add_widget(Go_Back)
        firstScreenLesson7_layout.add_widget(hello)
        firstScreenLesson7_layout.add_widget(label_1)
        firstScreenLesson7_layout.add_widget(label_1_1)
        firstScreenLesson7_layout.add_widget(label_2)
        firstScreenLesson7_layout.add_widget(label_2_1)
        firstScreenLesson7_layout.add_widget(label_3)
        firstScreenLesson7_layout.add_widget(label_3_1)
        firstScreenLesson7_layout.add_widget(label_4)
        firstScreenLesson7_layout.add_widget(label_4_1)

    def to_back_scrn(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'FirstScreen'
        return 0


class FirstScreenLesson8(Screen):
    def __init__(self):
        super().__init__()
        self.name = 'FirstScreenLesson8'
        firstScreenLesson8_layout = FloatLayout()
        self.add_widget(firstScreenLesson8_layout)
        hello = Label(text="Преобразование типов",
                      font_size=24,
                      bold=True,
                      pos_hint={'center_x': .5, 'center_y': .95}
                      )
        label_1 = Label(text="Если же два операнда операции представляют разные типы данных, то Python пытается "
                             "автоматически выполнить преобразования к одному из типов по следующми правилами:",
                        text_size=[450, None],
                        color=(1, 1, 1),
                        pos_hint={'center_x': .5, 'center_y': 0.8}
                        )
        label_1_1 = Label(text="Если один из операндов комплексное число, то другой операнд также преобразуется к "
                               "типу complex",
                          text_size=[450, None],
                          color=(1, 1, 1),
                          pos_hint={'center_x': .5, 'center_y': 0.7}
                          )
        label_1_2 = Label(text="Если один из операндов представляет тип float, то второй операнд также преобразуется к "
                               "типу float",
                          text_size=[450, None],
                          color=(1, 1, 1),
                          pos_hint={'center_x': .5, 'center_y': 0.6}
                          )
        label_1_3 = Label(text="Иначе, оба операнда должны представлять тип int, и в этом случае преобазование не "
                               "требуется",
                          text_size=[450, None],
                          color=(1, 1, 1),
                          pos_hint={'center_x': .5, 'center_y': 0.5}
                          )
        label_2 = Label(text="В некоторых случаях возникает необходимость вручную выполнить преобразование типов. "
                             "Для преобразования типов Python предоставляет ряд встроенных функций:",
                        text_size=[450, None],
                        color=(1, 1, 1),
                        pos_hint={'center_x': .5, 'center_y': 0.4}
                        )
        label_2_1 = Label(text="int(): преобразует значение в целое число          "
                               "float(): преобразует значение в вещественное число "
                               "str(): преобразует значение в строку               ",
                          text_size=[445, None],
                          bold=True,
                          color=(1, 1, 1),
                          pos_hint={'center_x': .5, 'center_y': 0.25}
                          )
        label_3 = Label(text="1.a = float(15)  # a = 15.0 "
                             "2.b = int(3.7)  # b = 3           "
                             "3.c = str(5)   # c = '5' ",
                        text_size=[210, None],
                        bold=True,
                        color=(1, 1, 1),
                        pos_hint={'center_x': .5, 'center_y': 0.15}
                        )
        Go_Back = Button(text='<',
                         bold=True,
                         font_size='28',
                         size_hint=(.1, .07),
                         halign='center',
                         pos_hint={'center_x': .05, 'center_y': 0.95},
                         )

        Go_Back.bind(on_press=self.to_back_scrn)

        firstScreenLesson8_layout.add_widget(Go_Back)
        firstScreenLesson8_layout.add_widget(hello)
        firstScreenLesson8_layout.add_widget(label_1)
        firstScreenLesson8_layout.add_widget(label_1_1)
        firstScreenLesson8_layout.add_widget(label_1_2)
        firstScreenLesson8_layout.add_widget(label_1_3)
        firstScreenLesson8_layout.add_widget(label_2)
        firstScreenLesson8_layout.add_widget(label_2_1)
        firstScreenLesson8_layout.add_widget(label_3)

    def to_back_scrn(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'FirstScreen'
        return 0


class SecondScreen(Screen):
    def __init__(self):
        super().__init__()
        self.name = 'SecondScreen'
        second_layout = FloatLayout()
        self.add_widget(second_layout)

        first_label = Label(text="ООП",
                            font_size=24,
                            bold=True,
                            pos_hint={'center_x': .5, 'center_y': .95}
                            )

        Go_Back = Button(text='<',
                         bold=True,
                         font_size='28',
                         halign='center',
                         size_hint=(.1, .07),
                         pos_hint={'center_x': .05, 'center_y': 0.95},
                         )

        Go_Back.bind(on_press=self.to_main_scrn)

        Button_1 = Button(text='Классы и объекты',
                          text_size=[200, None],
                          halign='center',
                          size_hint=(.4, None),
                          pos_hint={'center_x': .25, 'center_y': 0.8}
                          )
        Button_3 = Button(text='Наследование',
                          text_size=[200, None],
                          halign='center',
                          size_hint=(.4, None),
                          pos_hint={'center_x': .25, 'center_y': 0.6}
                          )
        Button_4 = Button(text='Атрибуты классов',
                          text_size=[200, None],
                          halign='center',
                          size_hint=(.4, None),
                          pos_hint={'center_x': .25, 'center_y': 0.4}
                          )
        Button_5 = Button(text='Статические методы',
                          text_size=[200, None],
                          halign='center',
                          size_hint=(.4, None),
                          pos_hint={'center_x': .75, 'center_y': 0.8}
                          )
        Button_6 = Button(text='Строковое представление объекта',
                          text_size=[200, None],
                          halign='center',
                          size_hint=(.4, None),
                          pos_hint={'center_x': .75, 'center_y': 0.6}
                          )
        Button_7 = Button(text='Перегрузка операторов',
                          text_size=[200, None],
                          halign='center',
                          size_hint=(.4, None),
                          pos_hint={'center_x': .75, 'center_y': 0.4}
                          )

        Button_1.bind(on_press=self.to_one_scrn)
        Button_3.bind(on_press=self.to_three_scrn)
        Button_4.bind(on_press=self.to_four_scrn)
        Button_5.bind(on_press=self.to_five_scrn)
        Button_6.bind(on_press=self.to_six_scrn)
        Button_7.bind(on_press=self.to_seven_scrn)

        second_layout.add_widget(first_label)
        second_layout.add_widget(Button_1)
        second_layout.add_widget(Button_3)
        second_layout.add_widget(Button_4)
        second_layout.add_widget(Button_5)
        second_layout.add_widget(Button_6)
        second_layout.add_widget(Button_7)
        second_layout.add_widget(Go_Back)

    def to_main_scrn(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'MainScreen'
        return 0

    def to_one_scrn(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'SecondScreenLesson1'
        return 0

    def to_three_scrn(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'SecondScreenLesson3'
        return 0

    def to_four_scrn(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'SecondScreenLesson4'
        return 0

    def to_five_scrn(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'SecondScreenLesson5'
        return 0

    def to_six_scrn(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'SecondScreenLesson6'
        return 0

    def to_seven_scrn(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'SecondScreenLesson7'
        return 0


class SecondScreenLesson1(Screen):
    def __init__(self):
        super().__init__()
        self.name = 'SecondScreenLesson1'
        secondScreenLesson1_layout = FloatLayout()
        self.add_widget(secondScreenLesson1_layout)
        hello = Label(text="Классы и объекты",
                      font_size=24,
                      bold=True,
                      pos_hint={'center_x': .5, 'center_y': .95}
                      )
        label_1 = Label(text="Python позволяет определять собственные типы с помощью классов. Класс представляет "
                             "некоторую сущность. Конкретным воплощением класса является объект.",
                        text_size=[450, None],
                        color=(1, 1, 1),
                        pos_hint={'center_x': .5, 'center_y': 0.8}
                        )
        label_2 = Label(text="В языке Python класс определяется с помощью ключевого слова class. Внутри класса "
                             "определяются его атрибуты, которые хранят различные характеристики класса, и методы - "
                             "функции класса.",
                        text_size=[450, None],
                        color=(1, 1, 1),
                        pos_hint={'center_x': .5, 'center_y': 0.67}
                        )
        label_2_1 = Label(text="1.class название_класса: "
                               "2.    атрибуты_класса        "
                               "3.    методы_класса",
                          text_size=[220, None],
                          bold=True,
                          color=(1, 1, 1),
                          pos_hint={'center_x': .5, 'center_y': 0.55}
                          )
        label_3 = Label(text="Атрибуты хранят состояние объекта. Для определения и установки атрибутов внутри класса "
                             "можно применять слово self.",
                        text_size=[450, None],
                        color=(1, 1, 1),
                        pos_hint={'center_x': .5, 'center_y': 0.45}
                        )
        label_4 = Label(text="Методы класса фактически представляют функции, которые определенны внутри класса и "
                             "которые определяют его поведение. Используя имя объекта, мы можем обратиться к его "
                             "методам.",
                        text_size=[450, None],
                        color=(1, 1, 1),
                        pos_hint={'center_x': .5, 'center_y': 0.35}
                        )
        label_5 = Label(text="Пример класса:",
                        text_size=[450, None],
                        color=(1, 1, 1),
                        pos_hint={'center_x': .5, 'center_y': 0.27}
                        )
        label_6 = Label(text="1.class Person:                                         "
                             "2.    #конструктор класса                    "
                             "3.    def __init__(self, name, age):         "
                             "4.        self.name = name #атрибут      "
                             "5.    #метод класса                                     "
                             "6.    def hi_hello(self):                               "
                             "7.        print('Hello')",
                        text_size=[300, None],
                        bold=True,
                        color=(1, 1, 1),
                        pos_hint={'center_x': .5, 'center_y': 0.15}
                        )
        Go_Back = Button(text='<',
                         bold=True,
                         font_size='28',
                         size_hint=(.1, .07),
                         halign='center',
                         pos_hint={'center_x': .05, 'center_y': 0.95},
                         )

        Go_Back.bind(on_press=self.to_back_scrn)

        secondScreenLesson1_layout.add_widget(Go_Back)
        secondScreenLesson1_layout.add_widget(hello)
        secondScreenLesson1_layout.add_widget(label_1)
        secondScreenLesson1_layout.add_widget(label_2)
        secondScreenLesson1_layout.add_widget(label_2_1)
        secondScreenLesson1_layout.add_widget(label_3)
        secondScreenLesson1_layout.add_widget(label_4)
        secondScreenLesson1_layout.add_widget(label_5)
        secondScreenLesson1_layout.add_widget(label_6)

    def to_back_scrn(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'SecondScreen'
        return 0


class SecondScreenLesson3(Screen):
    def __init__(self):
        super().__init__()
        self.name = 'SecondScreenLesson3'
        secondScreenLesson3_layout = FloatLayout()
        self.add_widget(secondScreenLesson3_layout)

        hello = Label(text="Наследование",
                      font_size=24,
                      bold=True,
                      pos_hint={'center_x': .5, 'center_y': .95}
                      )
        label_1 = Label(text="Наследование позволяет создавать новый класс на основе уже существующего класса. "
                             "Ключевыми понятиями наследования являются подкласс (дочерний класс) и суперкласс "
                             "(базовый класс). Подкласс наследует от суперкласса все публичные атрибуты и методы.",
                        text_size=[450, None],
                        color=(1, 1, 1),
                        pos_hint={'center_x': .5, 'center_y': 0.8}
                        )
        label_2 = Label(text="Синтаксис для наследования классов выглядит следующим образом:",
                        text_size=[450, None],
                        color=(1, 1, 1),
                        pos_hint={'center_x': .5, 'center_y': 0.68}
                        )
        label_2_1 = Label(text="1.class подкласс (суперкласс): "
                               "2.    методы_подкласса ",
                          text_size=[270, None],
                          bold=True,
                          color=(1, 1, 1),
                          pos_hint={'center_x': .5, 'center_y': 0.6}
                          )
        label_3 = Label(text="Также Python поддерживает множественное наследование, то есть один класс можно "
                             "унаследовать от нескольких классов.",
                        text_size=[450, None],
                        color=(1, 1, 1),
                        pos_hint={'center_x': .5, 'center_y': 0.5}
                        )
        label_4 = Label(text="1.class Employee:                        "
                             "2.    def work(self):                        "
                             "3.        print('Employee works')",
                        text_size=[250, None],
                        bold=True,
                        color=(1, 1, 1),
                        pos_hint={'center_x': .39, 'center_y': 0.4}
                        )
        label_5 = Label(text="4.class Student:                           "
                             "5.    def study(self):                       "
                             "6.        print('Student studies')",
                        text_size=[250, None],
                        bold=True,
                        color=(1, 1, 1),
                        pos_hint={'center_x': .39, 'center_y': 0.3}
                        )
        label_6 = Label(text="7.class WorkingStudent(Employee, Student): "
                             "8.    pass",
                        text_size=[360, None],
                        bold=True,
                        color=(1, 1, 1),
                        pos_hint={'center_x': .5, 'center_y': 0.21}
                        )
        Go_Back = Button(text='<',
                         bold=True,
                         font_size='28',
                         size_hint=(.1, .07),
                         halign='center',
                         pos_hint={'center_x': .05, 'center_y': 0.95},
                         )

        Go_Back.bind(on_press=self.to_back_scrn)

        secondScreenLesson3_layout.add_widget(Go_Back)
        secondScreenLesson3_layout.add_widget(hello)
        secondScreenLesson3_layout.add_widget(label_1)
        secondScreenLesson3_layout.add_widget(label_2)
        secondScreenLesson3_layout.add_widget(label_2_1)
        secondScreenLesson3_layout.add_widget(label_3)
        secondScreenLesson3_layout.add_widget(label_4)
        secondScreenLesson3_layout.add_widget(label_5)
        secondScreenLesson3_layout.add_widget(label_6)

    def to_back_scrn(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'SecondScreen'
        return 0


class SecondScreenLesson4(Screen):
    def __init__(self):
        super().__init__()
        self.name = 'SecondScreenLesson4'
        secondScreenLesson4_layout = FloatLayout()
        self.add_widget(secondScreenLesson4_layout)

        hello = Label(text="Атрибуты класса",
                      font_size=24,
                      bold=True,
                      pos_hint={'center_x': .5, 'center_y': .95}
                      )
        label_1 = Label(text="Кроме атрибутов объектов в классе можно определять атрибуты классов. Подобные атрибуты "
                             "определяются в виде переменных уровня класса.",
                        text_size=[450, None],
                        color=(1, 1, 1),
                        pos_hint={'center_x': .5, 'center_y': 0.85}
                        )
        label_2 = Label(text="Для обращения к атрибутам класса мы можем использовать имя класса.",
                        text_size=[450, None],
                        color=(1, 1, 1),
                        pos_hint={'center_x': .5, 'center_y': 0.75}
                        )
        label_3 = Label(text="Атрибуты класса могут применяться для таких ситуаций, когда нам надо определить некоторые"
                             " общие данные для всех объектов. Например:",
                        text_size=[450, None],
                        color=(1, 1, 1),
                        pos_hint={'center_x': .5, 'center_y': 0.65}
                        )
        label_3_1 = Label(text="1.class Per:                               "
                               "2.    no_name = 'No_Name'    "
                               "3.    def __init__(self, name): "
                               "4.        if name:                           "
                               "5.            self.name = name       "
                               "6.        else:  ",
                          text_size=[230, None],
                          bold=True,
                          color=(1, 1, 1),
                          pos_hint={'center_x': .39, 'center_y': 0.5}
                          )
        label_3_1_1 = Label(text="7.            self.name = Per.no_name",
                            bold=True,
                            color=(1, 1, 1),
                            pos_hint={'center_x': .43, 'center_y': 0.4}
                            )
        label_3_2 = Label(text="8.first = Per('Jade')                        "
                               "9.second = Per("")                              "
                               "10.print(first.name)  # Jade "
                               "11.print(second.name)  # No_Name",
                          text_size=[300, None],
                          bold=True,
                          color=(1, 1, 1),
                          pos_hint={'center_x': .46, 'center_y': 0.33}
                          )
        label_4 = Label(text="В примере no_name хранит имя по умолчанию. И если в конструктор передается пустое имя, то"
                             " установится имя по умолчанию, иначе будет записано указанное имя.",
                        text_size=[450, None],
                        color=(1, 1, 1),
                        pos_hint={'center_x': .5, 'center_y': 0.2}
                        )
        Go_Back = Button(text='<',
                         bold=True,
                         font_size='28',
                         size_hint=(.1, .07),
                         halign='center',
                         pos_hint={'center_x': .05, 'center_y': 0.95},
                         )

        Go_Back.bind(on_press=self.to_back_scrn)

        secondScreenLesson4_layout.add_widget(Go_Back)
        secondScreenLesson4_layout.add_widget(hello)
        secondScreenLesson4_layout.add_widget(label_1)
        secondScreenLesson4_layout.add_widget(label_2)
        secondScreenLesson4_layout.add_widget(label_3)
        secondScreenLesson4_layout.add_widget(label_3_1)
        secondScreenLesson4_layout.add_widget(label_3_1_1)
        secondScreenLesson4_layout.add_widget(label_3_2)
        secondScreenLesson4_layout.add_widget(label_4)

    def to_back_scrn(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'SecondScreen'
        return 0


class SecondScreenLesson5(Screen):
    def __init__(self):
        super().__init__()
        self.name = 'SecondScreenLesson5'
        secondScreenLesson5_layout = FloatLayout()
        self.add_widget(secondScreenLesson5_layout)

        hello = Label(text="Статические методы",
                      font_size=24,
                      bold=True,
                      pos_hint={'center_x': .5, 'center_y': .95}
                      )
        label_1 = Label(text="Кроме обычных методов класс может определять статические методы. Такие методы "
                             "предваряются аннотацией @staticmethod и относятся в целом к классу. Статические методы "
                             "обычно определяют поведение, которое не зависит от конкретного объекта.",
                        text_size=[450, None],
                        color=(1, 1, 1),
                        pos_hint={'center_x': .5, 'center_y': 0.8}
                        )
        label_1_1 = Label(text="1.class Per:                          "
                               "2.    __type = 'Per'                "
                               "3.    @staticmethod              "
                               "4.    def print_type():          "
                               "5.        print(Person.__type)",
                          text_size=[210, None],
                          bold=True,
                          color=(1, 1, 1),
                          pos_hint={'center_x': .35, 'center_y': 0.62}
                          )
        label_1_2 = Label(text="6.Per.print_type() #обращение к статическому методу через имя класса",
                          text_size=[400, None],
                          bold=True,
                          color=(1, 1, 1),
                          pos_hint={'center_x': .54, 'center_y': 0.51}
                          )
        label_2 = Label(text="Здесь в классе Per определен атрибут класса, который хранит название класса. Также в "
                             "классе определен статический метод, который выводит название класса. Действие этого "
                             "метода не зависит от конкретного объекта и относится в целом ко всему классу. Поэтому "
                             "такой метод можно сделать статическим.",
                        text_size=[450, None],
                        color=(1, 1, 1),
                        pos_hint={'center_x': .5, 'center_y': 0.35}
                        )
        Go_Back = Button(text='<',
                         bold=True,
                         font_size='28',
                         size_hint=(.1, .07),
                         halign='center',
                         pos_hint={'center_x': .05, 'center_y': 0.95},
                         )

        Go_Back.bind(on_press=self.to_back_scrn)

        secondScreenLesson5_layout.add_widget(Go_Back)
        secondScreenLesson5_layout.add_widget(hello)
        secondScreenLesson5_layout.add_widget(label_1)
        secondScreenLesson5_layout.add_widget(label_1_1)
        secondScreenLesson5_layout.add_widget(label_1_2)
        secondScreenLesson5_layout.add_widget(label_2)

    def to_back_scrn(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'SecondScreen'
        return 0


class SecondScreenLesson6(Screen):
    def __init__(self):
        super().__init__()
        self.name = 'SecondScreenLesson6'
        secondScreenLesson6_layout = FloatLayout()
        self.add_widget(secondScreenLesson6_layout)

        hello = Label(text="Строковое представление объекта",
                      font_size=24,
                      bold=True,
                      pos_hint={'center_x': .5, 'center_y': .95}
                      )
        label_1 = Label(text="Начиная с 3-й версии в языке программирования Python все классы неявно имеют один общий "
                             "суперкласс - object и все классы по умолчанию наследуют его методы. Одним из наиболее "
                             "используемых методов класса object является метод __str__() и считается хорошей практикой"
                             " его переопределять.",
                        text_size=[450, None],
                        color=(1, 1, 1),
                        pos_hint={'center_x': .5, 'center_y': 0.8}
                        )
        label_2 = Label(text="Когда необходимо получить строковое представление объекта или вывести объект в виде "
                             "строки, то Python как раз вызывает этот метод.",
                        text_size=[450, None],
                        color=(1, 1, 1),
                        pos_hint={'center_x': .5, 'center_y': 0.65}
                        )
        label_2_1 = Label(text="1.class Per:                                   "
                               "2.    def __init__(self, age):         "
                               "3.        self.age = age                 "
                               "4.    def __str__(self):                "
                               '5.        return f"Age: {self.age}"',
                          text_size=[240, None],
                          bold=True,
                          color=(1, 1, 1),
                          pos_hint={'center_x': .5, 'center_y': 0.52}
                          )
        label_2_2 = Label(text='6.age = Per(228)           '
                               '7.print(age) # Age: 228',
                          text_size=[210, None],
                          bold=True,
                          color=(1, 1, 1),
                          pos_hint={'center_x': .47, 'center_y': 0.42}
                          )
        label_3 = Label(text="Метод __str__ должен возвращать строку. И в данном случае мы возвращаем количество лет.",
                        text_size=[450, None],
                        color=(1, 1, 1),
                        pos_hint={'center_x': .5, 'center_y': 0.33}
                        )
        Go_Back = Button(text='<',
                         bold=True,
                         font_size='28',
                         size_hint=(.1, .07),
                         halign='center',
                         pos_hint={'center_x': .05, 'center_y': 0.95},
                         )

        Go_Back.bind(on_press=self.to_back_scrn)

        secondScreenLesson6_layout.add_widget(Go_Back)
        secondScreenLesson6_layout.add_widget(hello)
        secondScreenLesson6_layout.add_widget(label_1)
        secondScreenLesson6_layout.add_widget(label_2)
        secondScreenLesson6_layout.add_widget(label_2_1)
        secondScreenLesson6_layout.add_widget(label_2_2)
        secondScreenLesson6_layout.add_widget(label_3)

    def to_back_scrn(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'SecondScreen'
        return 0


class SecondScreenLesson7(Screen):
    def __init__(self):
        super().__init__()
        self.name = 'SecondScreenLesson7'
        secondScreenLesson7_layout = FloatLayout()
        self.add_widget(secondScreenLesson7_layout)

        hello = Label(text="Перегрузка операторов",
                      font_size=24,
                      bold=True,
                      pos_hint={'center_x': .5, 'center_y': .95}
                      )
        label_1 = Label(text="Чтобы определить оператор для некоторого класса, данный класс должен реализовать "
                             "соответствующую функцию. Так, для определения оператора сложения применяется функция "
                             "__add__(), поэтому внутри класса нам надо определить данную функцию.",
                        text_size=[450, None],
                        color=(1, 1, 1),
                        pos_hint={'center_x': .5, 'center_y': 0.8}
                        )
        label_1_1 = Label(text="1.class Counter:                                                                  "
                               "2.    def __init__(self, value):                                            "
                               "3.        self.value = value                                                   "
                               "4.    # переопределение оператора сложения   "
                               "5.    def __add__(self, other):                                           "
                               "6.        return Counter(self.value + other.value)",
                          text_size=[400, None],
                          bold=True,
                          color=(1, 1, 1),
                          pos_hint={'center_x': .5, 'center_y': 0.6}
                          )
        label_1_2 = Label(text="7.counter1 = Counter(5)                                   "
                               "8.counter2 = Counter(15)                   "
                               "9.counter3 = counter1 + counter2                       "
                               "10.print(counter3.value)                ",
                          text_size=[350, None],
                          bold=True,
                          color=(1, 1, 1),
                          pos_hint={'center_x': .45, 'center_y': 0.45}
                          )
        label_2 = Label(text="Здесь определен класс Counter, который имеет атрибут value - условное некоторое число. С "
                             "помощью функции __add__ определяем для типа Counter оператор сложения. В данном случае "
                             "переопределили оператор так, что можно складывать с другим объектом Counter. В результате"
                             " возвращаем новый объект Counter, в который помещается сумма атрибутов value обоих "
                             "объектов.",
                        text_size=[450, None],
                        color=(1, 1, 1),
                        pos_hint={'center_x': .5, 'center_y': 0.25}
                        )
        Go_Back = Button(text='<',
                         bold=True,
                         font_size='28',
                         size_hint=(.1, .07),
                         halign='center',
                         pos_hint={'center_x': .05, 'center_y': 0.95},
                         )

        Go_Back.bind(on_press=self.to_back_scrn)

        secondScreenLesson7_layout.add_widget(Go_Back)
        secondScreenLesson7_layout.add_widget(hello)
        secondScreenLesson7_layout.add_widget(label_1)
        secondScreenLesson7_layout.add_widget(label_1_1)
        secondScreenLesson7_layout.add_widget(label_1_2)
        secondScreenLesson7_layout.add_widget(label_2)

    def to_back_scrn(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'SecondScreen'
        return 0


class ThirdScreen(Screen):
    def __init__(self):
        super().__init__()
        self.name = 'ThirdScreen'
        third_layout = FloatLayout()
        self.add_widget(third_layout)

        first_label = Label(text="Списки, кортежи, словари",
                            font_size=24,
                            bold=True,
                            pos_hint={'center_x': .5, 'center_y': .95}
                            )

        Go_Back = Button(text='<',
                         bold=True,
                         font_size='28',
                         halign='center',
                         size_hint=(.1, .07),
                         pos_hint={'center_x': .05, 'center_y': 0.95},
                         )

        Go_Back.bind(on_press=self.to_main_scrn)

        Button_1 = Button(text='Списки',
                          text_size=[200, None],
                          halign='center',
                          size_hint=(.4, None),
                          pos_hint={'center_x': .25, 'center_y': 0.8}
                          )
        Button_2 = Button(text='Кортежи',
                          text_size=[200, None],
                          halign='center',
                          size_hint=(.4, None),
                          pos_hint={'center_x': .25, 'center_y': 0.6}
                          )
        Button_3 = Button(text='Диапазоны',
                          text_size=[200, None],
                          halign='center',
                          size_hint=(.4, None),
                          pos_hint={'center_x': .25, 'center_y': 0.4}
                          )
        Button_4 = Button(text='Словари',
                          text_size=[200, None],
                          halign='center',
                          size_hint=(.4, None),
                          pos_hint={'center_x': .75, 'center_y': 0.8}
                          )
        Button_5 = Button(text='Множества',
                          text_size=[200, None],
                          halign='center',
                          size_hint=(.4, None),
                          pos_hint={'center_x': .75, 'center_y': 0.6}
                          )

        Button_1.bind(on_press=self.to_one_scrn)
        Button_2.bind(on_press=self.to_two_scrn)
        Button_3.bind(on_press=self.to_three_scrn)
        Button_4.bind(on_press=self.to_four_scrn)
        Button_5.bind(on_press=self.to_five_scrn)

        third_layout.add_widget(first_label)
        third_layout.add_widget(Button_1)
        third_layout.add_widget(Button_2)
        third_layout.add_widget(Button_3)
        third_layout.add_widget(Button_4)
        third_layout.add_widget(Button_5)
        third_layout.add_widget(Go_Back)

    def to_main_scrn(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'MainScreen'
        return 0

    def to_one_scrn(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'ThirdScreenLesson1'
        return 0

    def to_two_scrn(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'ThirdScreenLesson2'
        return 0

    def to_three_scrn(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'ThirdScreenLesson3'
        return 0

    def to_four_scrn(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'ThirdScreenLesson4'
        return 0

    def to_five_scrn(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'ThirdScreenLesson5'
        return 0


class ThirdScreenLesson1(Screen):
    def __init__(self):
        super().__init__()
        self.name = 'ThirdScreenLesson1'
        thirdScreenLesson1_layout = FloatLayout()
        self.add_widget(thirdScreenLesson1_layout)
        hello = Label(text="Списки",
                      font_size=24,
                      bold=True,
                      pos_hint={'center_x': .5, 'center_y': .95}
                      )
        label_1 = Label(text="Список (list) представляет тип данных, который хранит набор или последовательность "
                             "элементов. Во многих других ЯП это называется массивом.",
                        text_size=[450, None],
                        color=(1, 1, 1),
                        pos_hint={'center_x': .5, 'center_y': 0.85}
                        )
        label_2 = Label(text="Для создания списка применяются квадратные скобки [], внутри которых через запятую могут"
                             " перечисляются элементы списка. Также для создания списка можно использовать "
                             "функцию-конструктор list()",
                        text_size=[450, None],
                        color=(1, 1, 1),
                        pos_hint={'center_x': .5, 'center_y': 0.72}
                        )
        label_2_1 = Label(text="1.numbers=[]     "
                               "2.numbers=list()",
                          text_size=[150, None],
                          bold=True,
                          color=(1, 1, 1),
                          pos_hint={'center_x': .5, 'center_y': 0.59}
                          )
        label_3 = Label(text="Список необязательно должен содержать только однотипные объекты. Для проверки элементов "
                             "списка можно использовать стандартную функцию print, которая выводит содержимое списка.",
                        text_size=[450, None],
                        color=(1, 1, 1),
                        pos_hint={'center_x': .5, 'center_y': 0.47}
                        )
        label_3_1 = Label(text="1.numbers = [1, 2, 3, 4, 5]        "
                               "2.print(numbers)  # [1, 2, 3, 4, 5]",
                          text_size=[270, None],
                          bold=True,
                          color=(1, 1, 1),
                          pos_hint={'center_x': .5, 'center_y': 0.36}
                          )
        label_4 = Label(text="Для обращения к элементам списка надо использовать индексы, которые представляют номер "
                             "элемента в списка. Индексы начинаются с нуля.",
                        text_size=[450, None],
                        color=(1, 1, 1),
                        pos_hint={'center_x': .5, 'center_y': 0.25}
                        )
        label_4_1 = Label(text="1.numbers = [1, 2, 3, 4, 5]        "
                               "2.print(numbers[3])  # 4",
                          text_size=[200, None],
                          bold=True,
                          color=(1, 1, 1),
                          pos_hint={'center_x': .5, 'center_y': 0.16}
                          )
        Go_Back = Button(text='<',
                         bold=True,
                         font_size='28',
                         size_hint=(.1, .07),
                         halign='center',
                         pos_hint={'center_x': .05, 'center_y': 0.95},
                         )

        Go_Back.bind(on_press=self.to_back_scrn)

        thirdScreenLesson1_layout.add_widget(Go_Back)
        thirdScreenLesson1_layout.add_widget(hello)
        thirdScreenLesson1_layout.add_widget(label_1)
        thirdScreenLesson1_layout.add_widget(label_2)
        thirdScreenLesson1_layout.add_widget(label_2_1)
        thirdScreenLesson1_layout.add_widget(label_3)
        thirdScreenLesson1_layout.add_widget(label_3_1)
        thirdScreenLesson1_layout.add_widget(label_4)
        thirdScreenLesson1_layout.add_widget(label_4_1)

    def to_back_scrn(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'ThirdScreen'
        return 0


class ThirdScreenLesson2(Screen):
    def __init__(self):
        super().__init__()
        self.name = 'ThirdScreenLesson2'
        thirdScreenLesson2_layout = FloatLayout()
        self.add_widget(thirdScreenLesson2_layout)

        hello = Label(text="Кортежи",
                      font_size=24,
                      bold=True,
                      pos_hint={'center_x': .5, 'center_y': .95}
                      )
        label_1 = Label(text="Кортеж (tuple) представляет последовательность элементов, которая во многом похожа на "
                             "список за тем исключением, что кортеж является неизменяемым (immutable) типом.",
                        text_size=[450, None],
                        color=(1, 1, 1),
                        pos_hint={'center_x': .5, 'center_y': 0.85}
                        )
        label_2 = Label(text="Для создания кортежа используются круглые скобки, в которые помещаются его значения, "
                             "разделенные запятыми. Также для определения кортежа мы можем просто перечислить значения "
                             "через запятую без применения скобок",
                        text_size=[450, None],
                        color=(1, 1, 1),
                        pos_hint={'center_x': .5, 'center_y': 0.7}
                        )
        label_2_1 = Label(text="1.numb = (1, 2, 'Jade') "
                               "2.fare = 1, 2, 'Jade'",
                          text_size=[200, None],
                          bold=True,
                          color=(1, 1, 1),
                          pos_hint={'center_x': .5, 'center_y': 0.59}
                          )
        label_3 = Label(text="Обращение к элементам в кортеже происходит также, как и в списке, по индексу.",
                        text_size=[450, None],
                        color=(1, 1, 1),
                        pos_hint={'center_x': .5, 'center_y': 0.52}
                        )
        label_3_1 = Label(text="1.numb = (1, 2, 'Jade') "
                               "2.print(numb[2] # Jade",
                          text_size=[200, None],
                          bold=True,
                          color=(1, 1, 1),
                          pos_hint={'center_x': .5, 'center_y': 0.45}
                          )
        label_4 = Label(text="Но так как кортеж - неизменяемый тип (immutable), то мы не сможем изменить его элементы. "
                             "То есть следующая запись работать не будет:",
                        text_size=[450, None],
                        color=(1, 1, 1),
                        pos_hint={'center_x': .5, 'center_y': 0.35}
                        )
        label_4_1 = Label(text="1.numb[1] = 'Topaz' ",
                          text_size=[200, None],
                          bold=True,
                          color=(1, 1, 1),
                          pos_hint={'center_x': .5, 'center_y': 0.28}
                          )
        Go_Back = Button(text='<',
                         bold=True,
                         font_size='28',
                         size_hint=(.1, .07),
                         halign='center',
                         pos_hint={'center_x': .05, 'center_y': 0.95},
                         )

        Go_Back.bind(on_press=self.to_back_scrn)

        thirdScreenLesson2_layout.add_widget(Go_Back)
        thirdScreenLesson2_layout.add_widget(hello)
        thirdScreenLesson2_layout.add_widget(label_1)
        thirdScreenLesson2_layout.add_widget(label_2)
        thirdScreenLesson2_layout.add_widget(label_2_1)
        thirdScreenLesson2_layout.add_widget(label_3)
        thirdScreenLesson2_layout.add_widget(label_3_1)
        thirdScreenLesson2_layout.add_widget(label_4)
        thirdScreenLesson2_layout.add_widget(label_4_1)

    def to_back_scrn(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'ThirdScreen'
        return 0


class ThirdScreenLesson3(Screen):
    def __init__(self):
        super().__init__()
        self.name = 'ThirdScreenLesson3'
        thirdScreenLesson3_layout = FloatLayout()
        self.add_widget(thirdScreenLesson3_layout)

        hello = Label(text="Диапозоны",
                      font_size=24,
                      bold=True,
                      pos_hint={'center_x': .5, 'center_y': .95}
                      )
        label_1 = Label(text="Диапазоны или range представляют неизменяемый последовательный набор чисел. Для "
                             "создания диапазов применяетя range, которая имеет следующие формы:",
                        text_size=[450, None],
                        color=(1, 1, 1),
                        pos_hint={'center_x': .5, 'center_y': 0.85}
                        )
        label_2 = Label(text="1 - range(stop): возвращает все целые числа от 0 до stop",
                        text_size=[450, None],
                        bold=True,
                        color=(1, 1, 1),
                        pos_hint={'center_x': .5, 'center_y': 0.75}
                        )
        label_3 = Label(text="2 - range(start, stop): возвращает все целые числа в промежутке от start (включая) до "
                             "stop (не включая)",
                        text_size=[450, None],
                        bold=True,
                        color=(1, 1, 1),
                        pos_hint={'center_x': .5, 'center_y': 0.68}
                        )
        label_4 = Label(text="3 - range(start, stop, step): возвращает целые числа в промежутке от start (включая) до "
                             "stop (не включая), которые увеличиваются на значение step",
                        text_size=[450, None],
                        bold=True,
                        color=(1, 1, 1),
                        pos_hint={'center_x': .5, 'center_y': 0.6}
                        )
        label_5 = Label(text="Пример диапозона:",
                        text_size=[450, None],
                        color=(1, 1, 1),
                        pos_hint={'center_x': .5, 'center_y': 0.5}
                        )
        label_5_1 = Label(text="1.range(4, 11, 2) # 4, 6, 8, 10 ",
                          text_size=[230, None],
                          bold=True,
                          color=(1, 1, 1),
                          pos_hint={'center_x': .5, 'center_y': 0.45}
                          )
        Go_Back = Button(text='<',
                         bold=True,
                         font_size='28',
                         size_hint=(.1, .07),
                         halign='center',
                         pos_hint={'center_x': .05, 'center_y': 0.95},
                         )

        Go_Back.bind(on_press=self.to_back_scrn)

        thirdScreenLesson3_layout.add_widget(Go_Back)
        thirdScreenLesson3_layout.add_widget(hello)
        thirdScreenLesson3_layout.add_widget(label_1)
        thirdScreenLesson3_layout.add_widget(label_2)
        thirdScreenLesson3_layout.add_widget(label_3)
        thirdScreenLesson3_layout.add_widget(label_4)
        thirdScreenLesson3_layout.add_widget(label_5)
        thirdScreenLesson3_layout.add_widget(label_5_1)

    def to_back_scrn(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'ThirdScreen'
        return 0


class ThirdScreenLesson4(Screen):
    def __init__(self):
        super().__init__()
        self.name = 'ThirdScreenLesson4'
        thirdScreenLesson4_layout = FloatLayout()
        self.add_widget(thirdScreenLesson4_layout)

        hello = Label(text="Словари",
                      font_size=24,
                      bold=True,
                      pos_hint={'center_x': .5, 'center_y': .95}
                      )
        label_1 = Label(text="Словарь (dictionary) в языке Python хранит коллекцию элементов, где каждый элемент имеет "
                             "уникальный ключ и ассоциированое с ним некоторое значение. Определение словаря имеет "
                             "следующий синтаксис:",
                        text_size=[450, None],
                        color=(1, 1, 1),
                        pos_hint={'center_x': .5, 'center_y': 0.8}
                        )
        label_1_1 = Label(text="1.users = {1: 'Jade', 2: 'Topaz'} ",
                          text_size=[260, None],
                          bold=True,
                          color=(1, 1, 1),
                          pos_hint={'center_x': .5, 'center_y': 0.68}
                          )
        label_2 = Label(text="В словаре users в качестве ключей используются числа, а в качестве значений - строки.",
                        text_size=[450, None],
                        color=(1, 1, 1),
                        pos_hint={'center_x': .5, 'center_y': 0.6}
                        )
        label_3 = Label(text="Для обращения к элементам словаря после его названия в квадратных скобках указывается "
                             "ключ элемента:",
                        text_size=[450, None],
                        color=(1, 1, 1),
                        pos_hint={'center_x': .5, 'center_y': 0.5}
                        )
        label_3_1 = Label(text="1.users = {1: 'Jade', 2: 'Topaz'} "
                               "2.print(users[2] # Topaz",
                          text_size=[260, None],
                          bold=True,
                          color=(1, 1, 1),
                          pos_hint={'center_x': .5, 'center_y': 0.4}
                          )
        label_4 = Label(text="Также ещё словари можно копировать и объединять с помощью методов copy() update() "
                             "соответственно.",
                        text_size=[450, None],
                        color=(1, 1, 1),
                        pos_hint={'center_x': .5, 'center_y': 0.32}
                        )
        label_4_1 = Label(text="1.users = {1: 'Jade', 2: 'Topaz'} "
                               "2.emplyes = users.copy()",
                          text_size=[260, None],
                          bold=True,
                          color=(1, 1, 1),
                          pos_hint={'center_x': .5, 'center_y': 0.23}
                          )
        label_4_2 = Label(text="1.users = {1: 'Jade', 2: 'Topaz'} "
                               "2.users_2 = {5: 'Diamond'} "
                               "3.users.update(users_2)",
                          text_size=[280, None],
                          bold=True,
                          color=(1, 1, 1),
                          pos_hint={'center_x': .5, 'center_y': 0.13}
                          )

        Go_Back = Button(text='<',
                         bold=True,
                         font_size='28',
                         size_hint=(.1, .07),
                         halign='center',
                         pos_hint={'center_x': .05, 'center_y': 0.95},
                         )

        Go_Back.bind(on_press=self.to_back_scrn)

        thirdScreenLesson4_layout.add_widget(Go_Back)
        thirdScreenLesson4_layout.add_widget(hello)
        thirdScreenLesson4_layout.add_widget(label_1)
        thirdScreenLesson4_layout.add_widget(label_1_1)
        thirdScreenLesson4_layout.add_widget(label_2)
        thirdScreenLesson4_layout.add_widget(label_3)
        thirdScreenLesson4_layout.add_widget(label_3_1)
        thirdScreenLesson4_layout.add_widget(label_4)
        thirdScreenLesson4_layout.add_widget(label_4_1)
        thirdScreenLesson4_layout.add_widget(label_4_2)

    def to_back_scrn(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'ThirdScreen'
        return 0


class ThirdScreenLesson5(Screen):
    def __init__(self):
        super().__init__()
        self.name = 'ThirdScreenLesson5'
        thirdScreenLesson5_layout = FloatLayout()
        self.add_widget(thirdScreenLesson5_layout)

        hello = Label(text="Множества",
                      font_size=24,
                      bold=True,
                      pos_hint={'center_x': .5, 'center_y': .95}
                      )
        label_1 = Label(text="Множество (set) представляют еще один вид набора, который хранит только уникальные "
                             "элементы. Для определения множества используются фигурные скобки, в которых перечисляются"
                             " элементы:",
                        text_size=[450, None],
                        color=(1, 1, 1),
                        pos_hint={'center_x': .5, 'center_y': 0.8}
                        )
        label_1_1 = Label(text="1.users = {'Jade', 'Topaz', 'Diamond', 'Topaz'} "
                               "2.print(users) # {'Jade', 'Topaz', 'Diamond'}",
                          text_size=[300, None],
                          bold=True,
                          color=(1, 1, 1),
                          pos_hint={'center_x': .5, 'center_y': 0.67}
                          )
        label_2 = Label(text="Также для определения множества может применяться функция set(), в которую передается "
                             "список или кортеж элементов:",
                        text_size=[450, None],
                        color=(1, 1, 1),
                        pos_hint={'center_x': .5, 'center_y': 0.57}
                        )
        label_2_1 = Label(text="1.people = ['Jade', 'Topaz', 'Diamond', 'Topaz'] "
                               "2.users = set(people)",
                          text_size=[300, None],
                          bold=True,
                          color=(1, 1, 1),
                          pos_hint={'center_x': .5, 'center_y': 0.47}
                          )
        label_3 = Label(text="Добавление элемента производится с помощью метода add(), а удаление методами remove() и "
                             "discard().",
                        text_size=[450, None],
                        color=(1, 1, 1),
                        pos_hint={'center_x': .5, 'center_y': 0.37}
                        )
        Go_Back = Button(text='<',
                         bold=True,
                         font_size='28',
                         size_hint=(.1, .07),
                         halign='center',
                         pos_hint={'center_x': .05, 'center_y': 0.95},
                         )

        Go_Back.bind(on_press=self.to_back_scrn)

        thirdScreenLesson5_layout.add_widget(Go_Back)
        thirdScreenLesson5_layout.add_widget(hello)
        thirdScreenLesson5_layout.add_widget(label_1)
        thirdScreenLesson5_layout.add_widget(label_1_1)
        thirdScreenLesson5_layout.add_widget(label_2)
        thirdScreenLesson5_layout.add_widget(label_2_1)
        thirdScreenLesson5_layout.add_widget(label_3)

    def to_back_scrn(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'ThirdScreen'
        return 0


sm = ScreenManager()  # необходимо создать переменную sm, которая будет собирать экраны и управлять ими

if __name__ == '__main__':
    MainApp().run()
