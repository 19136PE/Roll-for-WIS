import random
import os
from functools import partial
from tkinter import *

#list of question for selecting questions
question_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

#creates a list with data from questions document
with open("data/questions.txt", "r") as file:
       list_of_questions = file.readlines()

#list for answer randomizing
random_answer = [1, 2, 3, 4]

#list to randomize quiz finishing congrats text on menu
congrats = ["Congrats", "Congradulations", "Ka Pai", "Good Work", "Amazing", "WOOOOOO", "Outstanding", "Nothing can stop you"]

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

#used to enable and disable clear and export buttons on score screen
scoreboard_active = 0

#variables used to keep incorrect questions for exporting
inc1 = ""
inc2 = ""
inc3 = ""
inc4 = ""
inc5 = ""
inc6 = ""
inc7 = ""
inc8 = ""
inc9 = ""
inc10 = ""


class menu:
  def __init__(self):
    #used to enable and disable clear and export buttons on score screen
    global scoreboard_active

    #shuffle list options for first 10 questions
    random.shuffle(question_number)

    #when code is run, clears (score.txt), (scoreboard.txt), and deletes (export_file.txt) if it exists
    with open('data/score.txt', 'w') as file:
        file.writelines("")
    with open('data/scoreboard.txt', 'w') as file:
        file.writelines("--\n--\n--\n--\n--\n--\n--\n--\n--\n--")
    if os.path.exists("export_file.txt"):
         os.remove("export_file.txt")
        
    #disables
    scoreboard_active = 0
    
    #define grid layout
    self.main_frame = Frame(padx=6, pady=3)
    self.main_frame.grid(row=5, column=0)
    self.button_frame = Frame(self.main_frame)
    self.button_frame.grid(row=4, column=0)
    
    #main frame row 0 = heading
    self.main_heading = Label(self.main_frame,
                              text="Roll for Wisdom",
                              fg=button_fg,
                              font=(title_font),
                              justify=CENTER)
    self.main_heading.grid(row=0, padx=6, pady=9)

    #main frame row 1 = description
    self.quiz_description = Label(self.main_frame,
                              text="Test your Dungeons & Dragons knowledge with this themed Trivia game!",
                              wraplength=300,
                              fg=button_fg,
                              font=(description_font),
                              justify=CENTER)
    self.quiz_description.grid(row=1, padx=6, pady=3)
    
    #main frame row 2 = score
    self.current_score = Label(self.main_frame,
                              text="Score: 0",
                              fg=button_fg,
                              font=(score_font),
                              justify=CENTER)
    self.current_score.grid(row=2, padx=6, pady=3)
    
    #main frame row 3 = question number
    self.current_question = Label(self.main_frame,
                              text="Question: 0/10",
                              fg=button_fg,
                              font=(score_font),
                              justify=CENTER)
    self.current_question.grid(row=3, padx=6, pady=3)
    
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
    self.to_score_button.grid(row=4, column=1, padx=6, pady=9)

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
    self.to_quiz_button.grid(row=5, column=0, padx=6, pady=3)

    self.quiz_results = Label(self.main_frame,
                              text="",
                              fg="#228B22",
                              font=description_font,
                              justify=CENTER)
    self.quiz_results.grid(row=6, column=0, padx=3, pady=0)
    

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
                                 borderwidth=2,
                                 relief=SOLID,
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
       self.result_frame.grid(row=1, column=0, padx=6, pady=6)
       self.button_frame = Frame(self.score_frame)
       self.button_frame.grid(row=2, column=0, padx=6, pady=6)

       with open("data/scoreboard.txt", "r") as file:
           scoreboard_list = file.readlines()
        
       s1 = scoreboard_list[0]
       score1 = s1.strip()
       s2 = scoreboard_list[1]
       score2 = s2.strip()
       s3 = scoreboard_list[2]
       score3 = s3.strip()
       s4 = scoreboard_list[3]
       score4 = s4.strip()
       s5 = scoreboard_list[4]
       score5 = s5.strip()
       s6 = scoreboard_list[5]
       score6 = s6.strip()
       s7 = scoreboard_list[6]
       score7 = s7.strip()
       s8 = scoreboard_list[7]
       score8 = s8.strip()
       s9 = scoreboard_list[8]
       score9 = s9.strip()
       s10 = scoreboard_list[9]
       score10 = s10.strip()

       self.score_heading = Label(self.score_frame,
                              text="Showing Last 10 Scores",
                              fg=button_fg,
                              font=("Arial", "16", "bold"),
                              justify=CENTER)
       self.score_heading.grid(row=0, padx=12, pady=18)

       self.score_label_1 = Label(self.result_frame,
                              text="1: {}".format(score1),
                              fg=button_fg,
                              font=(button_font),
                              justify=CENTER)
       self.score_label_1.grid(row=1, column=0, padx=40, pady=6)

       self.score_label_2 = Label(self.result_frame,
                              text="2: {}".format(score2),
                              fg=button_fg,
                              font=(button_font),
                              justify=CENTER)
       self.score_label_2.grid(row=1, column=1, padx=40, pady=6)

       self.score_label_3 = Label(self.result_frame,
                              text="3: {}".format(score3),
                              fg=button_fg,
                              font=(button_font),
                              justify=CENTER)
       self.score_label_3.grid(row=2, column=0, padx=40, pady=6)

       self.score_label_4 = Label(self.result_frame,
                              text="4: {}".format(score4),
                              fg=button_fg,
                              font=(button_font),
                              justify=CENTER)
       self.score_label_4.grid(row=2, column=1, padx=40, pady=6)

       self.score_label_5 = Label(self.result_frame,
                              text="5: {}".format(score5),
                              fg=button_fg,
                              font=(button_font),
                              justify=CENTER)
       self.score_label_5.grid(row=3, column=0, padx=40, pady=6)

       self.score_label_6 = Label(self.result_frame,
                              text="6: {}".format(score6),
                              fg=button_fg,
                              font=(button_font),
                              justify=CENTER)
       self.score_label_6.grid(row=3, column=1, padx=40, pady=6)

       self.score_label_7 = Label(self.result_frame,
                              text="7: {}".format(score7),
                              fg=button_fg,
                              font=(button_font),
                              justify=CENTER)
       self.score_label_7.grid(row=4, column=0, padx=40, pady=6)

       self.score_label_8 = Label(self.result_frame,
                              text="8: {}".format(score8),
                              fg=button_fg,
                              font=(button_font),
                              justify=CENTER)
       self.score_label_8.grid(row=4, column=1, padx=40, pady=6)

       self.score_label_9 = Label(self.result_frame,
                              text="9: {}".format(score9),
                              fg=button_fg,
                              font=(button_font),
                              justify=CENTER)
       self.score_label_9.grid(row=5, column=0, padx=40, pady=6)

       self.score_label_10 = Label(self.result_frame,
                              text="10: {}".format(score10),
                              fg=button_fg,
                              font=(button_font),
                              justify=CENTER)
       self.score_label_10.grid(row=5, column=1, padx=40, pady=6)

       self.dismiss_button = Button(self.button_frame,
                                 font=("Arial", "12", "bold"),
                                 text="Dismiss",
                                 justify=CENTER,
                                 borderwidth=2,
                                 relief=SOLID,
                                 width=6,
                                 command=partial(self.close_score,partner))
       self.dismiss_button.grid(row=0, column=0, padx=4, pady=10)
  
       self.clear_button = Button(self.button_frame,
                                 font=("Arial", "12", "bold"),
                                 text="Clear",
                                 justify=CENTER,
                                 borderwidth=2,
                                 relief=SOLID,
                                 width=6,
                                 state=DISABLED,
                                 command=partial(self.clear_score,partner))
       self.clear_button.grid(row=0, column=1, padx=4, pady=10)

       self.export_button = Button(self.button_frame,
                                 font=("Arial", "12", "bold"),
                                 text="Export",
                                 justify=CENTER,
                                 borderwidth=2,
                                 relief=SOLID,
                                 width=6,
                                 command=partial(self.export_score))
       self.export_button.grid(row=0, column=2, padx=4, pady=10)

       if scoreboard_active == 0:
          self.export_button.config(state=DISABLED)
       elif scoreboard_active == 1:
          self.export_button.config(state=NORMAL)


  def close_score(self, partner):
      partner.to_score_button.config(state=NORMAL)
      self.score_box.destroy()

  def export_score(self):
      self.export_button.config(state=DISABLED)
      self.export_button.after(1500,lambda:self.export_button.config(state=NORMAL))
      
      with open('data/score.txt', 'r') as file:
        score_data = file.readlines()
      try:
        with open("export_file.txt", "x") as file:
          file.writelines(score_data)
      except:
        with open('export_file.txt', 'w') as file:
          file.writelines(score_data)

  def clear_score(self, partner):
      global questions_total
      global questions_right
      global scoreboard_active
      
      with open('data/scoreboard.txt', 'w') as file:
          file.writelines("--\n--\n--\n--\n--\n--\n--\n--\n--\n--")
      with open('data/score.txt', 'w') as file:
          file.writelines("")
      self.score_label_1.config(text="1: --")
      self.score_label_2.config(text="2: --")
      self.score_label_3.config(text="3: --")
      self.score_label_4.config(text="4: --")
      self.score_label_5.config(text="5: --")
      self.score_label_6.config(text="6: --")
      self.score_label_7.config(text="7: --")
      self.score_label_8.config(text="8: --")
      self.score_label_9.config(text="9: --")
      self.score_label_10.config(text="10: --")
      scoreboard_active = 0
      self.export_button.config(state=DISABLED)
      partner.quiz_results.config(text="")
      self.clear_button.config(state=DISABLED)
      self.clear_button.after(1500, lambda:self.clear_button.config(state=NORMAL))


class DisplayQuiz:
  def __init__(self, partner):
       
       random.shuffle(random_answer)
       
       self.quiz_box = Toplevel()

       partner.to_quiz_button.config(state=DISABLED)

       self.quiz_box.protocol('WM_DELETE_WINDOW',
                           partial(self.close_quiz,partner))
  
       self.quiz_frame = Frame(self.quiz_box)
       self.quiz_frame.grid()

       with open("data/questions.txt", "r") as file:
           list_of_questions = file.readlines()
         
       with open("data/answers(1).txt", "r") as file:
           list_of_answers_1 = file.readlines()
         
       with open("data/answers(2).txt", "r") as file:
           list_of_answers_2 = file.readlines()
         
       with open("data/answers(3).txt", "r") as file:
           list_of_answers_3 = file.readlines()
         
       with open("data/answers(4).txt", "r") as file:
           list_of_answers_4 = file.readlines()
       
       q = list_of_questions[question_number[questions_total]]
       question = q.strip()
       a1 = list_of_answers_1[question_number[questions_total]]
       answer1 = a1.strip()
       a2 = list_of_answers_2[question_number[questions_total]]
       answer2 = a2.strip()
       a3 = list_of_answers_3[question_number[questions_total]]
       answer3 = a3.strip()
       a4 = list_of_answers_4[question_number[questions_total]]
       answer4 = a4.strip()
    
       self.quiz_question = Label(self.quiz_frame,
                                 text=(question),
                                 wraplength=("200"),
                                 fg=button_fg,
                                 font=(quiz_button_font),
                                 justify=CENTER)
       self.quiz_question.grid(row=0, padx=12, pady=12)

       self.quiz_a_button = Button(self.quiz_frame,
                                 text=(answer1),
                                 fg=button_fg,
                                 font=(button_font),
                                 justify=CENTER,
                                 borderwidth=2,
                                 relief=SOLID,
                                 width=15,
                                 disabledforeground="#000000",
                                 command=lambda:self.correct_answer(partner))
       self.activeRow = random_answer[0]
       self.quiz_a_button.grid(row=self.activeRow, padx=12, pady=8)

       self.quiz_b_button = Button(self.quiz_frame,
                                 text=(answer2),
                                 fg=button_fg,
                                 font=(button_font),
                                 justify=CENTER,
                                 borderwidth=2,
                                 relief=SOLID,
                                 width=15,
                                 disabledforeground="#000000",
                                 command=lambda:self.incorrect_answer(partner))
       self.activeRow = random_answer[1]
       self.quiz_b_button.grid(row=self.activeRow, padx=12, pady=8)

       self.quiz_c_button = Button(self.quiz_frame,
                                 text=(answer3),
                                 fg=button_fg,
                                 font=(button_font),
                                 justify=CENTER,
                                 borderwidth=2,
                                 relief=SOLID,
                                 width=15,
                                 disabledforeground="#000000",
                                 command=lambda:self.incorrect_answer(partner))
       self.activeRow = random_answer[2]
       self.quiz_c_button.grid(row=self.activeRow, padx=12, pady=8)

       self.quiz_d_button = Button(self.quiz_frame,
                                 text=(answer4),
                                 fg=button_fg,
                                 font=(button_font),
                                 justify=CENTER,
                                 borderwidth=2,
                                 relief=SOLID,
                                 width=15,
                                 disabledforeground="#000000",
                                 command=lambda:self.incorrect_answer(partner))
       self.activeRow = random_answer[3]
       self.quiz_d_button.grid(row=self.activeRow, padx=12, pady=8)

  
  def correct_answer(self, partner):
      
      global questions_total
      global questions_right
      global inc1
      global inc2
      global inc3
      global inc4
      global inc5
      global inc6
      global inc7
      global inc8
      global inc9
      global inc10
      global scoreboard_active

      q = list_of_questions[question_number[questions_total]]
      question = q.strip()
    
      self.quiz_a_button.config(highlightbackground="#50C878", highlightthickness=3, state=DISABLED)
      self.quiz_b_button.config(highlightbackground="#C80815", highlightthickness=2, state=DISABLED)
      self.quiz_c_button.config(highlightbackground="#C80815", highlightthickness=2, state=DISABLED)
      self.quiz_d_button.config(highlightbackground="#C80815", highlightthickness=2, state=DISABLED)
    
      questions_total += 1
      questions_right += 1

      self.quiz_box.after(2500,lambda:self.quiz_box.destroy())
      partner.current_question.config(text="Question: {}/10".format(questions_total))
      partner.current_score.config(text="Score: {}".format(questions_right))

      if questions_total >= 10:
        scoreboard_active = 1
        random.shuffle(question_number)
        random.shuffle(congrats)    
        partner.current_question.config(text=("Question 0/10"))
        partner.current_score.config(text=("Score: 0"))
        partner.to_quiz_button.config(text=("Start Quiz"), state=NORMAL)
        
        with open('data/score.txt', 'r') as file:
            data = file.readlines()
        data.insert(0, "{}/10. Incorrect Questions: {} {} {} {} {} {} {} {} {} {}\n".format(questions_right, inc1, inc2, inc3, inc4, inc5, inc6, inc7, inc8, inc9, inc10))
        with open("data/score.txt", "w") as file:
            file.writelines(data)

        with open('data/scoreboard.txt', 'r') as file:
            data = file.readlines()
        data.insert(0, "{}/10\n".format(questions_right))
        with open("data/scoreboard.txt", "w") as file:
            file.writelines(data)

        inc1 = ""
        inc2 = ""
        inc3 = ""
        inc4 = ""
        inc5 = ""
        inc6 = ""
        inc7 = ""
        inc8 = ""
        inc9 = ""
        inc10 = ""
        
        if questions_right >= 5:
          partner.quiz_results.config(text="{}! You got {}/10".format(congrats[1], questions_right))
        
        else:
          partner.quiz_results.config(text="Nice try, you got {}/10".format(questions_right))
        
        questions_total = 0
        questions_right = 0

          
      else:
        partner.quiz_results.config(text="")
        partner.to_quiz_button.config(text="Continue Quiz", state=NORMAL)

  
  def incorrect_answer(self, partner):
      
      global questions_total
      global questions_right
      global inc1
      global inc2
      global inc3
      global inc4
      global inc5
      global inc6
      global inc7
      global inc8
      global inc9
      global inc10
      global scoreboard_active

      q = list_of_questions[question_number[questions_total]]
      question = q.strip()

  
      self.quiz_a_button.config(highlightbackground="#50C878", highlightthickness=3, state=DISABLED)
      self.quiz_b_button.config(highlightbackground="#C80815", highlightthickness=2, state=DISABLED)
      self.quiz_c_button.config(highlightbackground="#C80815", highlightthickness=2, state=DISABLED)
      self.quiz_d_button.config(highlightbackground="#C80815", highlightthickness=2, state=DISABLED)
    
      questions_total += 1
    
      if questions_total == 1: 
        inc1 = question
      elif questions_total == 2: 
        inc2 = question
      elif questions_total == 3: 
        inc3 = question
      elif questions_total == 4: 
        inc4 = question
      elif questions_total == 5: 
        inc5 = question
      elif questions_total == 6: 
        inc6 = question
      elif questions_total == 7: 
        inc7 = question
      elif questions_total == 8: 
        inc8 = question
      elif questions_total == 9: 
        inc9 = question
      elif questions_total == 10: 
        inc10 = question

      self.quiz_box.after(2500,lambda:self.quiz_box.destroy())
      partner.current_question.config(text="Question: {}/10".format(questions_total))

      if questions_total >= 10:
        scoreboard_active = 1
        random.shuffle(question_number)
        random.shuffle(congrats)    
        partner.current_question.config(text=("Question 0/10"))
        partner.current_score.config(text=("Score: 0"))
        partner.to_quiz_button.config(text=("Start Quiz"), state=NORMAL)
        
        with open('data/score.txt', 'r') as file:
            data = file.readlines()
        data.insert(0, "{}/10. Incorrect Questions: {} {} {} {} {} {} {} {} {} {}\n".format(questions_right, inc1, inc2, inc3, inc4, inc5, inc6, inc7, inc8, inc9, inc10))
        with open("data/score.txt", "w") as file:
            file.writelines(data)

        with open('data/scoreboard.txt', 'r') as file:
            data = file.readlines()
        data.insert(0, "{}/10\n".format(questions_right))
        with open("data/scoreboard.txt", "w") as file:
            file.writelines(data)

        inc1 = ""
        inc2 = ""
        inc3 = ""
        inc4 = ""
        inc5 = ""
        inc6 = ""
        inc7 = ""
        inc8 = ""
        inc9 = ""
        inc10 = ""
        
        if questions_right >= 5:
          partner.quiz_results.config(text="{}! You got {}/10".format(congrats[1], questions_right))
        
        else:
          partner.quiz_results.config(text="Nice try, you got {}/10".format(questions_right))
        
        questions_total = 0
        questions_right = 0

          
      else:
        partner.quiz_results.config(text="")
        partner.to_quiz_button.config(text="Continue Quiz", state=NORMAL)
  
  def close_quiz(self, partner):
      partner.to_quiz_button.config(state=NORMAL)
      self.quiz_box.destroy()
  
  def close_quiz_2(self):
      self.quiz_box.destroy()
  
#main rouine
root = Tk()
root.resizable(False, False)
root.title("Roll for WIS")
menu()
root.mainloop()