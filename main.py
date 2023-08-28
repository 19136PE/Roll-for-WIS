from tkinter import *
from functools import partial
import random
import time

#list of question for selecting
question_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,                     21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

#list for answer randomizing
random_answer = [1, 2, 3, 4]

#common format for all labels and buttons
title_font = ("Arial", "18", "bold") #arial, size 16, bold
description_font = ("Arial", "10") #arial, size 10
score_font = ("Arial", "14") #arial, size 14
button_font = ("Arial", "14") #arial, size 14
quiz_button_font = ("Arial", "16") #arial, size 16
button_fg = "#000000" #black text

#scorekeeping and question total variables
score = 0
questions_right = 0
questions_total = 0

class menu:
  def __init__(self):
    
    #shuffle list options for first 10 questions
    random.shuffle(question_number)
    
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
    self.quiz_description = Label(self.main_frame,
                              text="Brief Description",
                              fg=button_fg,
                              font=(description_font),
                              justify=CENTER)
    self.quiz_description.grid(row=1, padx=6, pady=6)
    
    #main frame row 2 = score
    self.current_score = Label(self.main_frame,
                              text="Score: 0",
                              fg=button_fg,
                              font=(score_font),
                              justify=CENTER)
    self.current_score.grid(row=2, padx=6, pady=6)
    
    #main frame row 3 = question number
    self.current_question = Label(self.main_frame,
                              text="Question 0/10",
                              fg=button_fg,
                              font=(score_font),
                              justify=CENTER)
    self.current_question.grid(row=3, padx=6, pady=6)
    
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
                                 text="Start Quiz",
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

      help_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.  " \
    "Pellentesque nec nam aliquam sem et tortor consequat id. Pellentesque id nibh tortor id aliquet. Vitae elementum curabitur vitae nunc sed velit. " \
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
                              text="1 {}".format("FIX"),
                              fg=button_fg,
                              font=(button_font),
                              justify=CENTER)
       self.score_scores_1.grid(row=1, column=0, padx=6, pady=6)

       self.score_scores_2 = Label(self.result_frame,
                              text="2 {}".format("FIX"),
                              fg=button_fg,
                              font=(button_font),
                              justify=CENTER)
       self.score_scores_2.grid(row=1, column=1, padx=6, pady=6)


  def close_score(self, partner):
      partner.to_score_button.config(state=NORMAL)
      self.score_box.destroy()


class DisplayQuiz:
  def __init__(self, partner):
       
       random.shuffle(random_answer)
       
       self.quiz_box = Toplevel()

       partner.to_quiz_button.config(state=DISABLED)

       self.quiz_box.protocol('WM_DELETE_WINDOW',
                           partial(self.close_quiz,partner))
  
       self.quiz_frame = Frame(self.quiz_box)
       self.quiz_frame.grid()

       print("{}".format(question_number[0]))
       print("{}".format(question_number[1]))
       print("{}".format(question_number[2]))
       print("{}".format(question_number[3]))
       print("{}".format(question_number[4]))
       print("{}".format(question_number[5]))
       print("{}".format(question_number[6]))
       print("{}".format(question_number[7]))
       print("{}".format(question_number[8]))
       print("{}".format(question_number[9]))
       print("")

       with open("questions.txt", "r") as file:
           list_of_questions = file.readlines()
         
       with open("answers(1).txt", "r") as file:
           list_of_answers_1 = file.readlines()
         
       with open("answers(2).txt", "r") as file:
           list_of_answers_2 = file.readlines()
         
       with open("answers(3).txt", "r") as file:
           list_of_answers_3 = file.readlines()
         
       with open("answers(4).txt", "r") as file:
           list_of_answers_4 = file.readlines()
       
       self.quiz_question = Label(self.quiz_frame,
                                 text=(list_of_questions[question_number[questions_total]]),
                                 wraplength=("200"),
                                 fg=button_fg,
                                 font=(quiz_button_font),
                                 justify=CENTER)
       self.quiz_question.grid(row=0, padx=12, pady=12)

       self.quiz_a_button = Button(self.quiz_frame,
                                 text=(list_of_answers_1[question_number[questions_total]]),
                                 fg=button_fg,
                                 font=(button_font),
                                 justify=CENTER,
                                 borderwidth=2,
                                 relief=SOLID,
                                 width=15,
                                 command=lambda:self.correct_answer(partner))
       self.activeRow = random_answer[0]
       self.quiz_a_button.grid(row=self.activeRow, padx=12, pady=8)

       self.quiz_b_button = Button(self.quiz_frame,
                                 text=(list_of_answers_2[question_number[questions_total]]),
                                 fg=button_fg,
                                 font=(button_font),
                                 justify=CENTER,
                                 borderwidth=2,
                                 relief=SOLID,
                                 width=15,
                                 command=lambda:self.incorrect_answer(partner))
       self.activeRow = random_answer[1]
       self.quiz_b_button.grid(row=self.activeRow, padx=12, pady=8)

       self.quiz_c_button = Button(self.quiz_frame,
                                 text=(list_of_answers_3[question_number[questions_total]]),
                                 fg=button_fg,
                                 font=(button_font),
                                 justify=CENTER,
                                 borderwidth=2,
                                 relief=SOLID,
                                 width=15,
                                 command=lambda:self.incorrect_answer(partner))
       self.activeRow = random_answer[2]
       self.quiz_c_button.grid(row=self.activeRow, padx=12, pady=8)

       self.quiz_d_button = Button(self.quiz_frame,
                                 text=(list_of_answers_4[question_number[questions_total]]),
                                 fg=button_fg,
                                 font=(button_font),
                                 justify=CENTER,
                                 borderwidth=2,
                                 relief=SOLID,
                                 width=15,
                                 command=lambda:self.incorrect_answer(partner))
       self.activeRow = random_answer[3]
       self.quiz_d_button.grid(row=self.activeRow, padx=12, pady=8)

  
  def correct_answer(self, partner):
      
      global questions_right
      global questions_total
    
      print("correct")
      self.quiz_a_button.config(highlightbackground="#50C878", highlightthickness=3, state=DISABLED, disabledforeground="#000000")
      self.quiz_b_button.config(highlightbackground="#C80815", highlightthickness=2, state=DISABLED, disabledforeground="#000000")
      self.quiz_c_button.config(highlightbackground="#C80815", highlightthickness=2, state=DISABLED, disabledforeground="#000000")
      self.quiz_d_button.config(highlightbackground="#C80815", highlightthickness=2, state=DISABLED, disabledforeground="#000000")

      questions_right += 1
      questions_total += 1
      
      self.quiz_box.after(2500,lambda:self.quiz_box.destroy())
      partner.current_question.config(text="Question {}/10".format(questions_total))
      partner.current_score.config(text="Score: {}".format(questions_right))
      partner.to_quiz_button.config(state=NORMAL)

      if questions_total >= 10:
        partner.to_quiz_button.config(text="Start Quiz", state=DISABLED)
        print("end")
      else:
        partner.to_quiz_button.config(text="Continue Quiz", state=NORMAL)

  
  def incorrect_answer(self, partner):
      
      global questions_total
    
      print("incorrect")
      self.quiz_a_button.config(highlightbackground="#50C878", highlightthickness=3, state=DISABLED, disabledforeground="#000000")
      self.quiz_b_button.config(highlightbackground="#C80815", highlightthickness=2, state=DISABLED, disabledforeground="#000000")
      self.quiz_c_button.config(highlightbackground="#C80815", highlightthickness=2, state=DISABLED, disabledforeground="#000000")
      self.quiz_d_button.config(highlightbackground="#C80815", highlightthickness=2, state=DISABLED, disabledforeground="#000000")
    
      questions_total += 1
      
      self.quiz_box.after(2500,lambda:self.quiz_box.destroy())
      partner.current_question.config(text="Question {}/10".format(questions_total))

      if questions_total >= 10:
        #partner.to_quiz_button.config(text="Start Quiz", state=DISABLED)
        print("end")
        self.finish_quiz()
      else:
        partner.to_quiz_button.config(text="Continue Quiz", state=NORMAL)
  
  def close_quiz(self, partner):
      partner.to_quiz_button.config(state=NORMAL)
      self.quiz_box.destroy()

  def finish_quiz(self):
      FinishQuiz(self)


class FinishQuiz:
  def __init__(self, partner):

      congrats = ["Congrats", "Congradulations", "Ka Pai", "Good Work", "Amazing", "WOOOOOO"]
      random.shuffle(congrats)
    
      self.finish_box = Toplevel()
      self.finish_frame = Frame(self.finish_box, padx=15, pady=15)
      self.finish_frame.grid(row=2, column=0)

      self.finish_box.protocol('WM_DELETE_WINDOW',
                           partial(self.close_finish_quiz,partner))
      
      self.finish_congrats = Label(self.finish_frame,
                              text="{}!".format(congrats[0]),
                              fg=button_fg,
                              font=(title_font),
                              justify=CENTER)
      self.finish_congrats.grid(row=0, padx=6, pady=6)

      self.final_score = Label(self.finish_frame,
                                 text=("{} / 10".format(questions_right)),
                                 fg=button_fg,
                                 font=(score_font),
                                 justify=CENTER)
      self.final_score.grid(row=1, padx=12, pady=12)

      self.finish_quiz_button = Button(self.finish_frame,
                                 text=("Finish Quiz"),
                                 fg=button_fg,
                                 font=(quiz_button_font),
                                 justify=CENTER,
                                 borderwidth=2,
                                 relief=SOLID,
                                 width=16,
                                 command=lambda:self.close_finish_quiz(partner))
      self.finish_quiz_button.grid(row=2, padx=12, pady=12)

  def close_finish_quiz(self, partner):
      global questions_total
      global questions_right
      print("close")
      partner.to_quiz_button.config(text="Start Quiz", state=DISABLED)
      self.finish_box.destroy()
      questions_total = 0
      questions_right = 0
      partner.current_question.config(text=("Question {}/10".format(questions_total)))
      partner.current_score.config(text=("Score: {}".format(questions_right)))

      
  
#main rouine
root = Tk()
root.title("Quiz Name")
menu()
root.mainloop()