from tkinter import *
import tkinter.font as font
import random

root = Tk()
root.title("your luck")
# window icon
root.iconbitmap("yang.ico")
# set window size and position
root.geometry('500x600+700+350')
myFont = font.Font(weight="bold")
font2 = font.Font(weight="bold", size=16)
font3 = font.Font(weight="bold", size=14)

# sari erroru kaldirmak icin buraya tekrardan yazdim
global label
global button_start
global button_quit
global points
global guess_limit
global guess
global hidden
global test
global ekran
global label_2
global label_3
global button_1
global button_2
global button_3
global button_4
global button_5
global button_6
global button_7
global button_8
global button_9
global button_0
global button_increase
global button_decrease
global text
global background
global foreground
global button_finish


def text_start():
    global text
    global background
    global foreground
    background = "#E0E0E0"
    foreground = "#808080"
    text = "Guess the number between 1 - 200 "


def text_hit():
    global text
    global background
    global foreground
    text = "Correct! Guess next one"


def text_lower():
    global text
    global background
    global foreground
    global active
    active =  "#000000"
    text = "Guess lower "
    background = "#E0E0E0"
    foreground = "#808080"


def text_higher():
    global text
    global background
    global foreground
    text = " Guess higher "
    foreground = "#E0E0E0"
    background = "#808080"


# opening of the app
def main_menu(font):
    # getting the global buttons
    global label
    global button_start
    global button_quit
    # set window background color
    root.configure(bg='turquoise')

    # informing the player about the game
    label = Label(root, width="30", borderwidth="5",
                  justify="center", bg='#00dfff',
                  font=font2,
                  fg='red',
                  text="""Try your luck
you will have 50 - 75 guesses
Guess the number between 1 - 200 """)

    # start button for the game
    button_start = Button(root, font=font2, bg="#00ffff",
                          text='Start', justify="center",
                          activebackground="blue",
                          command=lambda: erase_widget())

    # quit button for the game
    button_quit = Button(root, font=font2, bg="#00ffff",
                         text='Quit', justify="center",
                         activebackground="#ff0000",
                         command=lambda: sys.exit())

    # customizing the position of the label and buttons
    label.pack(pady=50)
    button_start.pack(pady=50)
    button_quit.pack(pady=10)


# deleting everything in main menu, in order to upload new page
def erase_widget():
    # deleting the buttons in main menu
    button_start.pack_forget()
    button_quit.pack_forget()
    label.pack_forget()

    # starting next page, passing font for the dirrent fonts
    text_start()
    start(myFont)
    # starting the game, it gets random number
    random_sayi()


# function to get the input variables properly
def button_click(sayi):
    # basilan tusu current e ekliyor
    current = ekran.get()
    # basilan tusu siliyor ki daha sonra yeni basilan sayi ile beraber tekrarlanmasin
    ekran.delete(0, END)
    # e ye numarayi ekliyor. her defasinda basilan sayiyi
    # sadece alt taki fonksiyon calisirsa, baslangica ekleniyor
    ekran.insert(0, str(current) + str(sayi))


# random number generator and counting how many the user have guessed
def random_sayi():
    global points
    global guess_limit
    global guess
    global hidden
    # getting the points of the user and guessing counts
    points = 0
    guess_limit = 0
    guess = random.randrange(50, 75)
    hidden = random.randrange(1, 201)
    # print(guess)
    # print(hidden)


# bu fonksiyon ekrandaki yazinin es olup olmadigini deneyecek
def dene():
    global test
    global guess
    global guess_limit
    global hidden
    global points

    # yazilan sayiyi aliyoruz
    test = int(ekran.get())
    # ekrani temizliyoruz
    ekran.delete(0, END)

    if guess_limit < guess:
        if test == hidden:
            erase_test()
            text_hit()
            start(myFont)
            points += 1
            hidden = random.randrange(1, 201)
            # print(hidden)
            # print("you Hit!")
            # print(hidden)
        elif test < hidden:
            erase_test()
            text_higher()
            start(myFont)
            # print("Higher")
            root.configure(bg=foreground)
            guess_limit += 1
        else:
            erase_test()
            text_lower()
            start(myFont)
            # print("Lower")
            root.configure(bg=foreground)
            guess_limit += 1
    else:
        root.configure(bg="turquoise")
        erase_test()
        text_end()
        # print(f"congratulotions! you have gained {points} points")


# bu fonksiyon oyun ekranindan main menu ye dönecek
def erase_screen():
    ekran.grid_forget()
    ekran.grid_forget()
    label_2.grid_forget()
    button_1.grid_forget()
    button_2.grid_forget()
    button_3.grid_forget()
    button_4.grid_forget()
    button_5.grid_forget()
    button_6.grid_forget()
    button_7.grid_forget()
    button_8.grid_forget()
    button_9.grid_forget()
    button_0.grid_forget()
    button_increase.grid_forget()
    button_decrease.grid_forget()
    main_menu(myFont)


def erase_test():
    ekran.grid_forget()
    ekran.grid_forget()
    label_2.grid_forget()
    button_1.grid_forget()
    button_2.grid_forget()
    button_3.grid_forget()
    button_4.grid_forget()
    button_5.grid_forget()
    button_6.grid_forget()
    button_7.grid_forget()
    button_8.grid_forget()
    button_9.grid_forget()
    button_0.grid_forget()
    button_increase.grid_forget()
    button_decrease.grid_forget()


def start(font):
    # ekran input gobal tanimliyoruz, diger fonksiyonlarda da kullanabilelim
    global ekran
    global label_2
    global button_1
    global button_2
    global button_3
    global button_4
    global button_5
    global button_6
    global button_7
    global button_8
    global button_9
    global button_0
    global button_increase
    global button_decrease

    root.configure(bg='turquoise')
    # creating entry where the numbers will be shown
    ekran = Entry(root, width="40", borderwidth="5",
                  justify="center", bg='turquoise',
                  fg="#808080", font=font3)  # .pack()

    # label for information
    label_2 = Label(root, width="30", borderwidth="3",
                    justify="center", bg='turquoise',
                    font=font2,
                    fg="#808080",
                    text=text)

    # creating buttons
    button_1 = Button(root, text="1", padx=20, pady=20, bg=background, font=font2,
                      fg=foreground, activebackground="orange", command=lambda: button_click(1))
    button_2 = Button(root, text="2", padx=20, pady=20, bg=background, font=font2,
                      fg=foreground, activebackground="orange", command=lambda: button_click(2))
    button_3 = Button(root, text="3", padx=20, pady=20, bg=background, font=font2,
                      fg=foreground, activebackground="orange", command=lambda: button_click(3))
    button_4 = Button(root, text="4", padx=20, pady=20, bg=background, font=font2,
                      fg=foreground, activebackground="orange", command=lambda: button_click(4))
    button_5 = Button(root, text="5", padx=20, pady=20, bg=background, font=font2,
                      fg=foreground, activebackground="orange", command=lambda: button_click(5))
    button_6 = Button(root, text="6", padx=20, pady=20, bg=background, font=font2,
                      fg=foreground, activebackground="orange", command=lambda: button_click(6))
    button_7 = Button(root, text="7", padx=20, pady=20, bg=background, font=font2,
                      fg=foreground, activebackground="orange", command=lambda: button_click(7))
    button_8 = Button(root, text="8", padx=20, pady=20, bg=background, font=font2,
                      fg=foreground, activebackground="orange", command=lambda: button_click(8))
    button_9 = Button(root, text="9", padx=20, pady=20, bg=background, font=font2,
                      fg=foreground, activebackground="orange", command=lambda: button_click(9))
    button_0 = Button(root, text="0", padx=20, pady=20, bg=background, font=font2,
                      fg=foreground, activebackground="orange", command=lambda: button_click(0))
    button_increase = Button(root, text="Guess", font=font2, bg="turquoise",
                             padx=60, pady=20, activebackground="orange", command=lambda: dene())
    button_decrease = Button(root, text="Exit", font=font2, bg="red",
                             padx=60, pady=20, activebackground="orange", command=lambda: erase_screen())

    # puting buttons on the window
    ekran.grid(row=0, column=0, columnspan=5, padx=(30, 30), pady=(60, 15))
    label_2.grid(row=1, column=0, columnspan=5, padx=(30, 30), pady=(5, 35))
    button_1.grid(row=3, column=0, padx=(30, 10), pady=20)
    button_2.grid(row=3, column=1, padx=10, pady=20)
    button_3.grid(row=3, column=2, padx=10, pady=20)
    button_4.grid(row=3, column=3, padx=10, pady=20)
    button_5.grid(row=3, column=4, padx=(10, 30), pady=20)
    button_6.grid(row=4, column=0, padx=(30, 10), pady=20)
    button_7.grid(row=4, column=1, padx=10, pady=20)
    button_8.grid(row=4, column=2, padx=10, pady=20)
    button_9.grid(row=4, column=3, padx=10, pady=20)
    button_0.grid(row=4, column=4, padx=(10, 30), pady=20)
    button_increase.grid(row=2, column=1, columnspan=3)
    button_decrease.grid(row=5, column=1, columnspan=3)


def text_end():
    global text
    global label_3
    global button_finish

    text = f"""congratulotions! you have 
gained {points} points"""
    # label_3 = Label(root, width="40", borderwidth="3",
    #                 justify="center", bg='turquoise',
    #                 font=font2,
    #                 fg="#808080",
    #                 text=text)
    # button_finish = Button(root, text="Exit", bg="red", font=font2,
    #                        fg=foreground, activebackground="orange", command=lambda: main_menu(myFont))
    # label_3.grid(row=0, column=0,pady=50)
    # button_finish.grid(row=1, column=0, padx=(30, 10), pady=20)
    label_3 = Label(root, width="30", borderwidth="5",
                    justify="center", bg='#00dfff',
                    font=font2,fg='red',
                    text=text)

    # start button for the game
    button_finish = Button(root, font=font2, bg="#00ffff",
                           text='Exit', justify="center",
                           activebackground="blue",
                           command=lambda: end_function())

    # customizing the position of the label and buttons
    label_3.pack(pady=50)
    button_finish.pack(pady=50)


# son olarak en son fnksiyon. nasil calisiyor bir ben biliyorum bir allah
def end_function():
    label_3.pack_forget()
    button_finish.pack_forget()
    main_menu(myFont)


# def quit_game(self):
#     self.root.destroy()


main_menu(myFont)
root.mainloop()
