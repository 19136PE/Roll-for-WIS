from tkinter import *
import random
import time


class menu:
  
  def __init__(self):
    #common format for all buttons
    #arial, size 12, bold, white text
    button_font = ("Arial", "16", "bold")
    button_fg = "#000000"
    
    self.main_frame = Frame(padx=15, pady=10)
    self.main_frame.grid()
    self.button_frame = Frame(self.main_frame)
    self.button_frame.grid(row=3)
    self.main_heading = Label(self.main_frame,
                              text="quiz name",
                              font=("Arial", "16", "bold"),
                              justify="center")
    self.main_heading.grid(row=0, padx=5, pady=5)
    
    self.to_help_button = Button(self.button_frame,
                                 text="Help",
                                 fg=button_fg,
                                 font=button_font,
                                 width=12)
                                 #command=self.to_help
    self.to_help_button.grid(row=3, column=0, padx=5, pady=5)

    self.to_score_button = Button(self.button_frame,
                                 text="Scores",
                                 fg=button_fg,
                                 font=button_font,
                                 width=12)
                                 #command=self.to_help
    self.to_score_button.grid(row=3, column=1, padx=5, pady=5)

    self.to_start_quiz_button = Button(self.main_frame,
                                 text="Start Quiz",
                                 fg=button_fg,
                                 font=button_font,
                                 width=12)
                                 #command=self.to_help
    self.to_start_quiz_button.grid(row=4, column=0, padx=5, pady=5)

#main rouine
root = Tk()
root.title("Quiz Name")
#root.geometry("300x400")
menu()
root.mainloop()