
import customtkinter
from CTkTable import *
from pyrebase import pyrebase

def table1():
    canv = customtkinter.CTk()
    app = customtkinter.CTkScrollableFrame(master=canv, width=1500, height=800)
    wid = canv.winfo_screenwidth()
    hei = canv.winfo_screenheight()
    canv.geometry("{}x{}+0+0".format(wid, hei))
    config = {
        "apiKey": "AIzaSyCQ2jsvICouZs7m7TA27a2u0MIRiLEKFZE",
        "authDomain": "aods-668cc.firebaseapp.com",
        "database": "https://aods-668cc-default-rtdb.firebaseio.com",
        "projectId": "aods-668cc",
        "storageBucket": "aods-668cc.appspot.com",
        "messagingSenderId": "34841860662",
        "appId": "1:34841860662:web:bcfce82f0319dd1208d697",
        "measurementId": "G-SNMQQ84LS2",
        "databaseURL": "https://aods-668cc-default-rtdb.firebaseio.com",
        "serviceAccount": "aods-668cc-firebase-adminsdk-r20v3-238f70f53a.json"
    }
    print("hi")
    firebase = pyrebase.initialize_app(config)
    database = firebase.database()
    snapshot = database.child("Violator").get()

    # Read the data at the posts reference (this is a blocking operation)
    print(snapshot.each())
    for i in
    # print(s1)
    # s2=s1.val()
    # for child in s1:
    #     print(child.key())
    print(len(s))

    # app.grid(sticky="nsew",padx=(10,10))

    # img = ImageTk.PhotoImage(Image.open(r".\img\08_07_2023_14_50_54.png"))
    value = [["SL.No", "Registration Number", "Picture"]]
    app.pack(expand=True, padx=20, pady=20)
    table = CTkTable(master=app, column=3, values=value)
    # table.grid(sticky="nsew")

    app.grid_rowconfigure(0, weight=1)
    app.grid_columnconfigure(0, weight=1)
    # root.rowconfigure(0,weight=1)
    # root.columnconfigure(0,weight=1)
    # app.grid_rowconfigure(0,weight=1)
    # app.grid_columnconfigure(0,weight=1)
    table.pack(expand=True, fill="both", padx=20, pady=20)

    # table.add_row(index=2,values=("1","klsdgdf",""))
    # table.add_row(index=2,values=("sss","sss",""))
    # # table.grid_columnconfigure(0,weight=0)
    # # table.grid_rowconfigure(0,weight=1)
    # phone_Label = customtkinter.CTkLabel(master=table, text="", image=img,width=300,height=300,
    #                                                   fg_color="transparent")
    # phone_Label.grid(row=1,column=2,sticky='nsew')
    # phone_Label.lift()
    # phone_Label1 = customtkinter.CTkLabel(master=table, text="", image=img,width=300,height=300,
    #                                                   fg_color="transparent")
    # phone_Label1.grid(row=2,column=2,sticky='nsew')
    # phone_Label1.lift()
    k = 1
    v = []
    for j in s:
        print("ji")
        v = [j, "1", ".."]
        print("ki")
        # table.add_row(index=k, values=(j, "h", "h"))
        # k = k + 1
        print(v)

    labels = {}
    k = 1
    # table.configure(values=v)
    # for j in s.val():
    #     emily = database.child("Violator").child(j).child("Pic").get()
    #     a = []
    #     for i in emily.each():
    #         # print(i.val())
    #         a.append(i.val())
    #     img = PIL.Image.fromarray(np.uint8(a))
    #     img1 = ImageTk.PhotoImage(img)
    #     p = "p" + str(k)
    #     if k % 2 == 0:
    #         fg = "#242424"
    #     else:
    #         fg = "#333333"
    #     lab = customtkinter.CTkLabel(master=table, text="", image=img1, width=300, height=300,
    #                                  fg_color=fg)
    #     lab.grid(row=k, column=2, sticky='nsew')
    #     k = k + 1
    #     lab.lift()
    #     labels[p] = lab
    # #     # print(img1)

    app.mainloop()

# customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
# customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green
# app1 = customtkinter.CTk()  # creating cutstom tkinter window
# app1.geometry("350x220")
# app1.title('Reset Password')
#
# def validate_pass(number):
#     pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$'
#     if re.match(pattern, number):
#         return True
#     else:
#         return False
# def but(e1,e2,db,ema,):
#     p1=e1.get()
#     p2=e2.get()
#     if validate_pass(p1):
#         if p1 == p2:
#             try:
#
#                 notification.notify(
#                     title='AODS',
#                     message='Password Changes Successful',
#                     app_icon="C:\\Users\\DELL\\Downloads\\istockphoto-1085043668-612x612 (4).ico",
#                     # Set to a file path to use a custom icon
#                     timeout=10)
#                 #db.child("Users").child(ema).child("Password").set(p1)
#             except Exception as e:
#                 print(e)
#         else:
#             notification.notify(
#                 title='AODS',
#                 message='Password Doesn\'t Match',
#                 app_icon="C:\\Users\\DELL\\Downloads\\istockphoto-1085043668-612x612 (4).ico",
#                 # Set to a file path to use a custom icon
#                 timeout=10)
#     else:
#         notification.notify(
#             title='AODS',
#             message='Should contain 8 characters including lowercase,uppercase and digits',
#             app_icon="C:\\Users\\DELL\\Downloads\\istockphoto-1085043668-612x612 (4).ico",
#             # Set to a file path to use a custom icon
#             timeout=10, toast=True, ticker='AODS'
#             # Duration in seconds for the notification to stay on the screen
#         )
# def hide(entry21, hide_image1, show_image1):
#     show_button = tkinter.Button(app1, image=hide_image1, command=lambda: show(entry21, hide_image1, show_image1),
#                                  relief=FLAT,
#                                  activebackground="grey"
#                                  , borderwidth=0, background="#343638", cursor="hand2")
#     show_button.place(x=340, y=100)
#     entry21.configure(show='*')
#
#
# def show(entry21, hide_image1, show_image1):
#     hide_button = tkinter.Button(app1, image=show_image1, command=lambda: hide(entry21, hide_image1, show_image1),
#                                  relief=FLAT,
#                                  activebackground="white"
#                                  , borderwidth=0, background="#343638", cursor="hand2")
#     hide_button.place(x=340, y=100)
#     entry21.configure(show='')
#
#
# def hide1(entry21, hide_image1, show_image1):
#     show_button = tkinter.Button(app1, image=hide_image1, command=lambda: show1(entry21, hide_image1, show_image1),
#                                  relief=FLAT,
#                                  activebackground="grey"
#                                  , borderwidth=0, background="#343638", cursor="hand2")
#     show_button.place(x=340, y=160)
#     entry21.configure(show='*')
#
#
# def show1(entry21, hide_image1, show_image1):
#     hide_button = tkinter.Button(app1, image=show_image1, command=lambda: hide1(entry21, hide_image1, show_image1),
#                                  relief=FLAT,
#                                  activebackground="white"
#                                  , borderwidth=0, background="#343638", cursor="hand2")
#     hide_button.place(x=340, y=160)
#     entry21.configure(show='')
#
#
# def passgui(database,ema0):
#     hide_image = ImageTk.PhotoImage(Image.open(r".\images\hide2.png"))
#     show_image = ImageTk.PhotoImage(Image.open(r".\images\show1.png"))
#     entry0 = customtkinter.CTkLabel(master=app1, width=250, text='Reset Password')
#     entry0.place(x=50, y=25)
#     entry1 = customtkinter.CTkEntry(master=app1, width=250, placeholder_text='Password', show='*')
#     entry1.place(x=50, y=75)
#     entry2 = customtkinter.CTkEntry(master=app1, width=250, placeholder_text='Confirm Password', show='*')
#     entry2.place(x=50, y=125)
#     show_button = tkinter.Button(app1, image=hide_image, command=lambda: show(entry1, hide_image, show_image),
#                                  relief=FLAT,
#                                  activebackground="grey"
#                                  , borderwidth=0, background="#343638", cursor="hand2")
#     show_button.place(x=340, y=100)
#     show_button1 = tkinter.Button(app1, image=hide_image, command=lambda: show1(entry2, hide_image, show_image),
#                                   relief=FLAT,
#                                   activebackground="grey"
#                                   , borderwidth=0, background="#343638", cursor="hand2")
#     show_button1.place(x=340, y=160)
#     button = customtkinter.CTkButton(master=app1, width=100, text='Submit', command=lambda: but(entry1, entry2,database,ema0))
#     button.place(x=50, y=175)
#
# app1.mainloop()
table1()