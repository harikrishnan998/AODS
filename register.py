
import concurrent.futures
import multiprocessing
import tkinter
import customtkinter
import tkinter as tk

import ray

import main
import imageio
from PIL import ImageTk
from PIL import Image


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        customtkinter.set_default_color_theme("blue")
        # configure window
        video_path = "video1.mp4"
        self.title("AODS-MVD")
        wid = self.winfo_screenwidth()
        hei = self.winfo_screenheight()
        self.geometry("{}x{}+0+0".format(wid, hei))
        self.state('zoomed')
        # self.resizable(0,0)
        # self.attributes('-fullscreen',True)
        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create canvas
        # self.canvas = tk.Canvas(self, bg="white")
        # self.canvas.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        # self.canvas.grid_columnconfigure(0, weight=1)
        # self.canvas.grid_rowconfigure(0, weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=180, height=hei, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky='nsew')
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="AODS",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Live Cam",
                                                        command=self.disable_but, width=200, height=25,
                                                        font=customtkinter.CTkFont(size=17))
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="New User",
                                                        command=self.sidebar_button_event, width=200, height=25,
                                                        font=customtkinter.CTkFont(size=17))
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, text="Violators",
                                                        command=self.sidebar_button_event, width=200, height=25,
                                                        font=customtkinter.CTkFont(size=17))
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w",
                                                            font=customtkinter.CTkFont(weight="bold"))
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionmenu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                                      values=["Dark", "Light", "System"],
                                                                      command=self.change_appearance_mode_event,
                                                                      width=150)
        self.appearance_mode_optionmenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="Scaling:", anchor="w",
                                                    font=customtkinter.CTkFont(weight="bold"))
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionmenu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                              values=["100%", "90%", "80%", "110%", "120%"],
                                                              command=self.change_scaling_event, width=150)
        self.scaling_optionmenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # create slider_progressbar frame
        self.slider_progressbar_frame = customtkinter.CTkFrame(self, width=100)
        self.slider_progressbar_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.slider_progressbar_frame.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(4, weight=1)
        # self.textbox = customtkinter.CTkTextbox(self.slider_progressbar_frame, width=250)
        # self.textbox.grid(row=2, column=0, padx=(10, 0), pady=(20, 0), sticky="nsew")
        self.progressbar_1 = customtkinter.CTkProgressBar(self.slider_progressbar_frame, width=1200)
        self.progressbar_1.grid(row=1, column=0, padx=(10, 10), pady=(10, 10), sticky="ew")
        self.progressbar_1.configure(mode="indeterminate")
        self.progressbar_1.start()
        self.progressbar_2 = customtkinter.CTkProgressBar(self.slider_progressbar_frame, width=1200)
        self.progressbar_2.grid(row=3, column=0, padx=(20, 10), pady=(700, 10), sticky="ew")
        self.progressbar_2.configure(mode="indeterminate")
        self.progressbar_2.start()
        self.canvas1 = tk.Canvas(self, width=800, height=800, bg='#2B2B2B')
        self.canvas1.grid(row=0, column=1, padx=(35, 12), pady=(30, 0), sticky="ew")
        self.canvas1.grid_columnconfigure(2, weight=1)
        self.canvas1.grid_rowconfigure(4, weight=1)
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.video_path = "video1.mp4"
        self.video = imageio.get_reader(self.video_path)
        self.current_frame = None
        # tk.Misc.lift(self.canvas1)
        # tk.Misc.lift(self.sidebar_frame)

    def disable_but(self):
        self.sidebar_button_1.configure(state="disabled")
        self.update_frame()

    def play_video(self):
        self.canvas1.delete()
        for frame in self.video.iter_data():
            image = Image.fromarray(frame)
            self.current_frame = ImageTk.PhotoImage(image)
            self.canvas1.create_image(0, 0, image=self.current_frame, anchor=tkinter.NW)
            self.canvas1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
            # self.canvas1.update()

    def update_frame(self):
        if self.current_frame is not None:
            self.canvas1.delete(self.current_frame)

        try:
            frame = self.video.get_next_data()
            image = Image.fromarray(frame)
            self.current_frame = ImageTk.PhotoImage(image)
            self.canvas1.create_image(0, 0, image=self.current_frame, anchor=tkinter.NW)
        except imageio.core.format.CannotReadFrameError:
            return

        self.after(50, self.update_frame)

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")

def func3():
    ray.init()
    # Define functions you want to execute in parallel using
    # the ray.remote decorator.
    @ray.remote
    def func1():
        app = App()
        app.mainloop()

    @ray.remote
    def func2():
        main.main()


# Execute func1 and func2 in parallel.
    ray.get([func1.remote(), func2.remote()])

# p1=multiprocessing.Process(target=func1())
# p2=multiprocessing.Process(target=main.main())
# p1.start()
# p2.start()

# with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
#     # Submit the functions for execution
#     future1 = executor.submit(main.main)
#     future2 = executor.submit(func1)
#
#     # Wait for the functions to complete and retrieve their results
#     result1 = future1.result()
#     result2 = future2.result()
