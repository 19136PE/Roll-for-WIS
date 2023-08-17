from tkinter import *
from functools import partial
import random
import time

#common format for all labels and buttons
title_font = ("Arial", "18", "bold") #arial, size 16, bold
description_font = ("Arial", "10") #arial, size 10
score_font = ("Arial", "14") #arial, size 14
button_font = ("Arial", "14") #arial, size 14
quiz_button_font = ("Arial", "16") #arial, size 16
button_fg = "#000000" #black text

score = "0"
question = "1"

#score variables for last 10 scores
r_score_1 = ""
r_score_2 = ""
r_score_3 = ""
r_score_4 = ""
r_score_5 = ""
r_score_6 = ""
r_score_7 = ""
r_score_8 = ""
r_score_9 = ""
r_score_10 = ""

class menu:
  
  def __init__(self):
    
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
                              text="Brief Description",
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
                                 borderwidth=2,
                                 relief=SOLID,
                                 width=10,
                                 command=self.to_help)
    self.to_help_button.grid(row=4, column=0, padx=6, pady=6)

    #button frame column 2 = scores/export button
    self.to_score_button = Button(self.button_frame,
                                 text="Scores",
                                 fg=button_fg,
                                 font=(button_font),
                                 justify=CENTER,
                                 borderwidth=2,
                                 relief=SOLID,
                                 width=10,
                                 command=self.to_score)
    self.to_score_button.grid(row=4, column=1, padx=6, pady=6)

    #main frame row 5 = start/continue quiz button
    self.to_quiz_button = Button(self.main_frame,
                                 text="Start / Continue Quiz",
                                 fg=button_fg,
                                 font=(quiz_button_font),
                                 justify=CENTER,
                                 borderwidth=2,
                                 relief=SOLID,
                                 width=20,
                                 command=self.to_quiz)
    self.to_quiz_button.grid(row=5, column=0, padx=6, pady=6)

  def to_help(self):
      DisplayHelp(self)

  def to_score(self):
      DisplayScore(self)
  
  def to_quiz(self):
      DisplayQuiz(self)

  
class DisplayHelp:
  
  def __init__(self, partner):
      self.help_box = Toplevel()

      partner.to_help_button.config(state=DISABLED)

      self.help_box.protocol('WM_DELETE_WINDOW',
                           partial(self.close_help,partner))

      self.help_frame = Frame(self.help_box)

      self.help_frame.grid()

      self.help_heading_label = Label(self.help_frame,
                                    text="Help / Settings",
                                    font=(title_font),
                                    justify=CENTER)
      self.help_heading_label.grid(row=0, pady=6)

      help_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. \n\n" \
    "Pellentesque nec nam aliquam sem et tortor consequat id. Pellentesque id nibh tortor id aliquet. Vitae elementum curabitur vitae nunc sed velit. \n\n" \
    "Cras ornare arcu dui vivamus arcu. Tempus egestas sed sed risus pretium quam vulputate. Morbi tristique senectus et netus."

      self.help_text_label = Label(self.help_frame,
                                 text=help_text,
                                 wraplength=280,
                                 font=(description_font),
                                 justify=CENTER)
      self.help_text_label.grid(row=1, padx=12, pady=6)

      self.dismiss_button = Button(self.help_frame,
                                 font=("Arial", "12", "bold"),
                                 text="Dismiss",
                                 command=partial(self.close_help,partner))
      self.dismiss_button.grid(row=2, padx=6, pady=6)

  def close_help(self, partner):
      partner.to_help_button.config(state=NORMAL)
      self.help_box.destroy()


class DisplayScore:
  def __init__(self, partner):
       self.score_box = Toplevel()

       partner.to_score_button.config(state=DISABLED)

       self.score_box.protocol('WM_DELETE_WINDOW',
                           partial(self.close_score,partner))

       self.score_frame = Frame(self.score_box)
       self.score_frame.grid()
       self.result_frame = Frame(self.score_frame)
       self.result_frame.grid(row=1, column=0)

       self.score_heading = Label(self.score_frame,
                              text="Showing 10 Scores",
                              fg=button_fg,
                              font=(title_font),
                              justify=CENTER)
       self.score_heading.grid(row=0, padx=6, pady=6)

       self.score_scores_1 = Label(self.result_frame,
                              text="1 {}".format(r_score_1),
                              fg=button_fg,
                              font=(button_font),
                              justify=CENTER)
       self.score_scores_1.grid(row=1, column=0, padx=6, pady=6)

       self.score_scores_2 = Label(self.result_frame,
                              text="2 {}".format(r_score_2),
                              fg=button_fg,
                              font=(button_font),
                              justify=CENTER)
       self.score_scores_2.grid(row=1, column=1, padx=6, pady=6)


  def close_score(self, partner):
      partner.to_score_button.config(state=NORMAL)
      self.score_box.destroy()


class DisplayQuiz:
  def __init__(self, partner):
       self.quiz_box = Toplevel()

       partner.to_quiz_button.config(state=DISABLED)

       self.quiz_box.protocol('WM_DELETE_WINDOW',
                           partial(self.close_quiz,partner))

       self.quiz_frame = Frame(self.quiz_box)
       self.quiz_frame.grid()

       self.quiz_question = Label(self.quiz_frame,
                                 text="Question",
                                 fg=button_fg,
                                 font=(quiz_button_font),
                                 justify=CENTER)
       self.quiz_question.grid(row=0, padx=12, pady=12)

       self.quiz_a_button = Button(self.quiz_frame,
                                 text="Answer A",
                                 fg=button_fg,
                                 font=(button_font),
                                 justify=CENTER,
                                 borderwidth=2,
                                 relief=SOLID,
                                 width=15)
       self.quiz_a_button.grid(row=1, padx=12, pady=8)

       self.quiz_b_button = Button(self.quiz_frame,
                                 text="Answer B",
                                 fg=button_fg,
                                 font=(button_font),
                                 justify=CENTER,
                                 borderwidth=2,
                                 relief=SOLID,
                                 width=15)
       self.quiz_b_button.grid(row=2, padx=12, pady=8)

       self.quiz_c_button = Button(self.quiz_frame,
                                 text="Answer C",
                                 fg=button_fg,
                                 font=(button_font),
                                 justify=CENTER,
                                 borderwidth=2,
                                 relief=SOLID,
                                 width=15)
       self.quiz_c_button.grid(row=3, padx=12, pady=8)

       self.quiz_d_button = Button(self.quiz_frame,
                                 text="Answer D",
                                 fg=button_fg,
                                 font=(button_font),
                                 justify=CENTER,
                                 borderwidth=2,
                                 relief=SOLID,
                                 width=15)
       self.quiz_d_button.grid(row=4, padx=12, pady=8)

  def close_quiz(self, partner):
      partner.to_quiz_button.config(state=NORMAL)
      self.quiz_box.destroy()
  
#main rouine
root = Tk()
root.title("Quiz Name")
menu()
root.mainloop()