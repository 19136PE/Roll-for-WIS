import tkinter
from tkinter import *
import random
import time


class menu:
  
  def __init__(self):
    
    window_width = 300 #width of menu window
    window_height = 400 #height of menu window
    
    #common format for all labels and buttons
    title_font = ("Arial", "16", "bold") #arial, size 16, bold
    description_font = ("Arial", "10") #arial, size 10
    score_font = ("Arial", "16") #arial, size 16
    button_font = ("Arial", "16") #arial, size 16
    button_fg = "#000000" #black text
    
    #define grid layout
    self.main_frame = Frame(padx=15, pady=15)
    self.main_frame.grid(row=5, column=0)
    self.button_frame = Frame(self.main_frame)
    self.button_frame.grid(row=4, column=0)
    
    #main frame row 0 = heading
    self.main_heading = Label(self.main_frame,
                              text="Quiz Name",
                              fg=button_fg,
                              font=(title_font),
                              justify=CENTER)
    self.main_heading.grid(row=0, padx=6, pady=6)

    #main frame row 1 = description
    self.main_heading = Label(self.main_frame,
                              text="Description",
                              fg=button_fg,
                              font=(description_font),
                              justify=CENTER)
    self.main_heading.grid(row=1, padx=6, pady=6)
    
    #main frame row 2 = score
    self.main_heading = Label(self.main_frame,
                              text="Score: 0",
                              fg=button_fg,
                              font=(score_font),
                              justify=CENTER)
    self.main_heading.grid(row=2, padx=6, pady=6)
    
    #main frame row 3 = question number
    self.main_heading = Label(self.main_frame,
                              text="Question 0/0",
                              fg=button_fg,
                              font=(score_font),
                              justify=CENTER)
    self.main_heading.grid(row=3, padx=6, pady=6)
    
    #main frame row 4 = help and score buttons
    #button frame column 1 = help/settings button
    self.to_help_button = Button(self.button_frame,
                                 text="Help",
                                 fg=button_fg,
                                 font=(button_font),
                                 justify=CENTER,
                                 width=10)
                                 #command=self.to_help
    self.to_help_button.grid(row=4, column=0, padx=6, pady=6)

    #button frame column 2 = scores/export button
    self.to_score_button = Button(self.button_frame,
                                 text="Scores",
                                 fg=button_fg,
                                 font=(button_font),
                                 justify=CENTER,
                                 width=10)
                                 #command=self.to_score
    self.to_score_button.grid(row=4, column=1, padx=6, pady=6)

    #main frame row 5 = start/continue quiz button
    self.to_start_quiz_button = Button(self.main_frame,
                                 text="Start Quiz",
                                 fg=button_fg,
                                 font=(button_font),
                                 justify=CENTER,
                                 width=23)
                                 #command=self.to_quiz
    self.to_start_quiz_button.grid(row=5, column=0, padx=6, pady=6)

#main rouine
root = Tk()
root.title("Quiz Name")
#root.geometry("300x400")
menu()
root.mainloop()