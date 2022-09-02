import tkinter as tk
from tkinter import ttk


class Hands(ttk.Frame):
    def __init__(self, parent, controller, show_timer):
        super().__init__(parent)
        
        self["style"] = "Background.TFrame"

        self.columnconfigure(0, weight=1)
        self.rowconfigure(4, weight=1)

        settings_container = ttk.Frame(
            self,
            padding = "30 15 30 15",
            style="Background.TFrame"
        )

        settings_container.grid(row=0, column=0, sticky="EW", padx = 10, pady = 10)
        settings_container.columnconfigure(0, weight = 1)
        settings_container.rowconfigure(1, weight=1)

        # pomodoro_label = ttk.Label(
        #     settings_container,
        #     text="Pomodoro:",
        #     style="LightText.TLabel"
        # )
        # pomodoro_label.grid(column=0, row=0, sticky="W")

        # pomodoro_input = tk.Spinbox(
        #     settings_container,
        #     from_ = 0,
        #     to=120,
        #     increment=1,
        #     justify="center",
        #     textvariable=controller.pomodoro,
        #     width=10
        # )
        # pomodoro_input.grid(column=1, row=0, sticky="EW")
        # pomodoro_input.focus()

        # long_break_label = ttk.Label(
        #     settings_container,
        #     text="Long break time:",
        #     style="LightText.TLabel"
        # )
        # long_break_label.grid(column=0, row=1, sticky="W")

        # long_break_input = tk.Spinbox(
        #     settings_container,
        #     from_ = 0,
        #     to=60,
        #     increment=1,
        #     justify="center",
        #     textvariable=controller.long_break,
        #     width=10
        # )
        # long_break_input.grid(column=1, row=1, sticky="EW")

        # short_break_label = ttk.Label(
        #     settings_container,
        #     text="Short break time:",
        #     style="LightText.TLabel"
        # )
        # short_break_label.grid(column=0, row=2, sticky="W")

        # short_break_input = tk.Spinbox(
        #     settings_container,
        #     from_ = 0,
        #     to=60,
        #     increment=1,
        #     justify="center",
        #     textvariable=controller.short_break,
        #     width=10
        # )
        # short_break_input.grid(column=1, row=2, sticky="EW")        

        # for child in settings_container.winfo_children():
        #     child.grid_configure(padx=5, pady=5)

        # button_container = ttk.Frame(self, style="Background.TFrame")
        # button_container.grid(sticky="EW", padx=10)
        # button_container.columnconfigure(0, weight=1)

        # timer_button = ttk.Button(
        #     button_container,
        #     text="<- Back",
        #     command=show_timer,
        #     style="PomodoroButton.TButton",
        #     cursor="hand2"
        # )

        # timer_button.grid(column=0, row=0, sticky="EW", padx=2)

        left_common_value = tk.IntVar()
        right_common_value = tk.IntVar()


        self.left_thumb = Hand_sliders(settings_container, "Left Thumb", 0, 0)
        self.left_index = Hand_sliders(settings_container, "Lext Index", 0, 1)
        self.left_middle = Hand_sliders(settings_container, "Left Middle", 0, 2)
        self.left_ring = Hand_sliders(settings_container, "Left Ring", 0, 3)
        self.left_little = Hand_sliders(settings_container, "Left Little", 0, 4)
        self.right_thumb = Hand_sliders(settings_container, "Right Thumb", 1, 0)
        self.right_index = Hand_sliders(settings_container, "Right Index", 1, 1)
        self.right_middle = Hand_sliders(settings_container, "Right Middle", 1, 2)
        self.right_ring = Hand_sliders(settings_container, "Right Ring", 1, 3)
        self.right_little = Hand_sliders(settings_container, "Right Little", 1, 4)

class Hand_sliders():

    def __init__(self, container, text, slider_column, slider_row):

        self.current_value = tk.IntVar()

        self.slider = tk.Scale(
            container,
            orient = "horizontal",
            from_= 0,
            to = 10,
            command = self.handle_scale_change,
            variable = self.current_value,
            # tickinterval=1,#uncomment this if you want to have the ticks displayed
            length = 400,
            resolution=1,
            showvalue=True,
            label=text,
            relief = "solid"
        )
        self.name = text
        self.previous_value = tk.IntVar()
        self.current_value.set(value=5)

        self.slider.grid(column=slider_column, row=slider_row, padx=(20, 100), pady=(10,10))

    def handle_scale_change(self, event):
        print(f"{self.name} is: {self.slider.get()}")

