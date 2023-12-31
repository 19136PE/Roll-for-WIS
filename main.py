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
    
    #main frame row 4 = help button
    #button frame column 1 = help button
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

    #main frame row 4 = scores button
    #button frame column 2 = scores button
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

    #main frame row 6 quiz results label, shows prev results
    self.quiz_results = Label(self.main_frame,
                              text="",
                              fg="#228B22",
                              font=description_font,
                              justify=CENTER)
    self.quiz_results.grid(row=6, column=0, padx=3, pady=0)
    

  #when run, send user to DisplayHelp class
  def to_help(self):
      DisplayHelp(self)

  #when run, send user to DisplayScore class
  def to_score(self):
      DisplayScore(self)

  #when run, send user to DisplayQuiz class
  def to_quiz(self):
      DisplayQuiz(self)

  
class DisplayHelp:
  def __init__(self, partner):

      #creates new tab
      self.help_box = Toplevel()
      self.help_box.resizable(False, False)

      #disables help button on menu tab
      partner.to_help_button.config(state=DISABLED)

      #if X (close) button is pressed, send user to close_help function
      self.help_box.protocol('WM_DELETE_WINDOW',
                           partial(self.close_help,partner))

      #define help_frame
      self.help_frame = Frame(self.help_box)
      self.help_frame.grid()

      #help frame row 0 = healp heading label
      self.help_heading_label = Label(self.help_frame,
                                    text="Help / Settings",
                                    font=(title_font),
                                    justify=CENTER)
      self.help_heading_label.grid(row=0, pady=6)

      #sets a variable to the help textt for easy editing
      help_text = "Welcome to Roll for WIS! This quiz will test and challange your D&D knowledge!\n\n" \
    "The quiz is made up of 10 questions that you need to answer, challlange your friends, your family, and see who does the best!\n\n" \
    "After completeing the quiz, your last 10 scores will show in the Scoreboard. In the scoreboard you are able to Export all scores and tell you what questions you got wrong for later research to help you improve your D&D Trivia!"

      #help frame row 1 = help text label
      self.help_text_label = Label(self.help_frame,
                                 text=help_text,
                                 wraplength=280,
                                 font=(description_font),
                                 justify=CENTER)
      self.help_text_label.grid(row=1, padx=12, pady=6)

      #help frame row 2 = dismiss button, sends user to close_help function
      self.dismiss_button = Button(self.help_frame,
                                 font=("Arial", "12", "bold"),
                                 text="Dismiss",
                                 borderwidth=2,
                                 relief=SOLID,
                                 command=partial(self.close_help,partner))
      self.dismiss_button.grid(row=2, padx=6, pady=6)

  #when run. destroy help_box/tab and re-enable help button in menu
  def close_help(self, partner):
      partner.to_help_button.config(state=NORMAL)
      self.help_box.destroy()


class DisplayScore:
  def __init__(self, partner):
       
       #creates new tab
       self.score_box = Toplevel()
       self.score_box.resizable(False, False)

       #disables score button on menu tab
       partner.to_score_button.config(state=DISABLED)

       #if X (close) button is pressed, send user to close_help function 
       self.score_box.protocol('WM_DELETE_WINDOW',
                           partial(self.close_score,partner))

       #defines score_frame and adds result_frame and button_frame to score_frame 
       self.score_frame = Frame(self.score_box)
       self.score_frame.grid()
       self.result_frame = Frame(self.score_frame)
       self.result_frame.grid(row=1, column=0, padx=6, pady=6)
       self.button_frame = Frame(self.score_frame)
       self.button_frame.grid(row=2, column=0, padx=6, pady=6)

       #opens scoreboard.txt file for reading and creates list with data
       with open("data/scoreboard.txt", "r") as file:
           scoreboard_list = file.readlines()
        
       #takes data from list, strips off blank lines, sets the results to variables
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

       #score_frame row 0 = score heading label
       self.score_heading = Label(self.score_frame,
                              text="Showing Last 10 Scores",
                              fg=button_fg,
                              font=("Arial", "16", "bold"),
                              justify=CENTER)
       self.score_heading.grid(row=0, padx=12, pady=18)

       #score_frame row 1 = score label 1
       #result frame row 1 column 0 = score label 1
       self.score_label_1 = Label(self.result_frame,
                              text="1: {}".format(score1),
                              fg=button_fg,
                              font=(button_font),
                              justify=CENTER)
       self.score_label_1.grid(row=1, column=0, padx=40, pady=6)

       #score_frame row 1 = score label 2
       #result frame row 1 column 1 = score label 2
       self.score_label_2 = Label(self.result_frame,
                              text="2: {}".format(score2),
                              fg=button_fg,
                              font=(button_font),
                              justify=CENTER)
       self.score_label_2.grid(row=1, column=1, padx=40, pady=6)

       #score_frame row 1 = score label 3
       #result frame row 2 column 0 = score label 3
       self.score_label_3 = Label(self.result_frame,
                              text="3: {}".format(score3),
                              fg=button_fg,
                              font=(button_font),
                              justify=CENTER)
       self.score_label_3.grid(row=2, column=0, padx=40, pady=6)

       #score_frame row 1 = score label 4
       #result frame row 2 column 1 = score label 4
       self.score_label_4 = Label(self.result_frame,
                              text="4: {}".format(score4),
                              fg=button_fg,
                              font=(button_font),
                              justify=CENTER)
       self.score_label_4.grid(row=2, column=1, padx=40, pady=6)

       #score_frame row 1 = score label 5
       #result frame row 3 column 0 = score label 5
       self.score_label_5 = Label(self.result_frame,
                              text="5: {}".format(score5),
                              fg=button_fg,
                              font=(button_font),
                              justify=CENTER)
       self.score_label_5.grid(row=3, column=0, padx=40, pady=6)

       #score_frame row 1 = score label 6
       #result frame row 3 column 1 = score label 6
       self.score_label_6 = Label(self.result_frame,
                              text="6: {}".format(score6),
                              fg=button_fg,
                              font=(button_font),
                              justify=CENTER)
       self.score_label_6.grid(row=3, column=1, padx=40, pady=6)

       #score_frame row 1 = score label 7
       #result frame row 4 column 0 = score label 7
       self.score_label_7 = Label(self.result_frame,
                              text="7: {}".format(score7),
                              fg=button_fg,
                              font=(button_font),
                              justify=CENTER)
       self.score_label_7.grid(row=4, column=0, padx=40, pady=6)

       #score_frame row 1 = score label 8
       #result frame row 4 column 1 = score label 8
       self.score_label_8 = Label(self.result_frame,
                              text="8: {}".format(score8),
                              fg=button_fg,
                              font=(button_font),
                              justify=CENTER)
       self.score_label_8.grid(row=4, column=1, padx=40, pady=6)

       #score_frame row 1 = score label 9
       #result frame row 5 column 0 = score label 9
       self.score_label_9 = Label(self.result_frame,
                              text="9: {}".format(score9),
                              fg=button_fg,
                              font=(button_font),
                              justify=CENTER)
       self.score_label_9.grid(row=5, column=0, padx=40, pady=6)

       #score_frame row 1 = score label 10
       #result frame row 5 column 1 = score label 10
       self.score_label_10 = Label(self.result_frame,
                              text="10: {}".format(score10),
                              fg=button_fg,
                              font=(button_font),
                              justify=CENTER)
       self.score_label_10.grid(row=5, column=1, padx=40, pady=6)

       #score_frame row 2 = dismiss button
       #button_frame row 0 column 0 = dismiss button
       self.dismiss_button = Button(self.button_frame,
                                 font=("Arial", "12", "bold"),
                                 text="Dismiss",
                                 justify=CENTER,
                                 borderwidth=2,
                                 relief=SOLID,
                                 width=6,
                                 command=partial(self.close_score,partner))
       self.dismiss_button.grid(row=0, column=0, padx=4, pady=10)

       #score_frame row 2 = clear button
       #button_frame row 0 column 1 = clear button
       self.clear_button = Button(self.button_frame,
                                 font=("Arial", "12", "bold"),
                                 text="Clear",
                                 justify=CENTER,
                                 borderwidth=2,
                                 relief=SOLID,
                                 width=6,
                                 command=partial(self.clear_score,partner))
       self.clear_button.grid(row=0, column=1, padx=4, pady=10)

       #score_frame row 2 = export button
       #button_frame row 0 column 2 = export button
       self.export_button = Button(self.button_frame,
                                 font=("Arial", "12", "bold"),
                                 text="Export",
                                 justify=CENTER,
                                 borderwidth=2,
                                 relief=SOLID,
                                 width=6,
                                 command=partial(self.export_score))
       self.export_button.grid(row=0, column=2, padx=4, pady=10)

       #detects if export and clear button should be enabled or disabled
       if scoreboard_active == 0:
          self.export_button.config(state=DISABLED)
          self.clear_button.config(state=DISABLED)
       elif scoreboard_active == 1:
          self.export_button.config(state=NORMAL)
          self.clear_button.config(state=NORMAL)

  #when run, close score_box tab and set to_score_button in menu to NORMAL
  def close_score(self, partner):
      partner.to_score_button.config(state=NORMAL)
      self.score_box.destroy()

  #when run, save data in export_file.txt
  def export_score(self):
      #disables export_button for 1.5sec to show that it has been pressed
      self.export_button.config(state=DISABLED)
      self.export_button.after(1500,lambda:self.export_button.config(state=NORMAL))
      
      #set data from score.txt to score_data list
      with open('data/score.txt', 'r') as file:
        score_data = file.readlines()
      
      #trys to create a file called export_file.txt, errors if there is already one
      try:
        with open("export_file.txt", "x") as file:
          file.writelines(score_data)
      #when there is a file and code errors, override export_file.txt with new data
      except:
        with open('export_file.txt', 'w') as file:
          file.writelines(score_data)

  #when run, reset score and everything to do with score
  def clear_score(self, partner):
      
      #activates global variable
      global scoreboard_active
      
      #clears scoreboard.txt
      with open('data/scoreboard.txt', 'w') as file:
          file.writelines("--\n--\n--\n--\n--\n--\n--\n--\n--\n--")
      #clears score.txt
      with open('data/score.txt', 'w') as file:
          file.writelines("")
      
      #resets showing scores/clears showing scores
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

      #tells code it has been reset and dont activate export and clear buttons
      scoreboard_active = 0
      
      #disables export and clear button
      self.export_button.config(state=DISABLED)
      self.clear_button.config(state=DISABLED)
      
      #removes last quiz result from menu screen (if showing)
      partner.quiz_results.config(text="")


class DisplayQuiz:
  def __init__(self, partner):
       
       #shuffles list that sets the order of answers (so that they are randomly ordered)
       random.shuffle(random_answer)
       
       #creates new tab
       self.quiz_box = Toplevel()
       self.quiz_box.resizable(False, False)

       #disables start/continue quiz button on menu tab
       partner.to_quiz_button.config(state=DISABLED)

       #when X (close) button is pressed, send user to close_quiz function
       self.quiz_box.protocol('WM_DELETE_WINDOW',
                           partial(self.close_quiz,partner))
  
       #defines quiz_frame
       self.quiz_frame = Frame(self.quiz_box)
       self.quiz_frame.grid()

       #opens all the data files required and sets their data to lists [questions.txt] [answers(1)] [answers(2)] [answers(3)] [answers(4)]
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
       
       #gets current question/answers, strips blank lines, sets quesiton/answers to variables for reading
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

       # ↓↓ question and answer labels ↓↓
    
       #quiz frame row 0 = quiz question
       self.quiz_question = Label(self.quiz_frame,
                                 text=(question),
                                 wraplength=("200"),
                                 fg=button_fg,
                                 font=(quiz_button_font),
                                 justify=CENTER)
       self.quiz_question.grid(row=0, padx=12, pady=12)

       #quiz_a_button is always correct
       #quiz frame row 1-4 = quiz_a_button
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
       #sets row to random number (1st number after shuffle) from random_answer list (1, 2, 3, or 4)
       self.activeRow = random_answer[0]
       self.quiz_a_button.grid(row=self.activeRow, padx=12, pady=8)

       #quiz_b_button is always incorrect
       #quiz frame row 1-4 = quiz_b_button
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
       #sets row to random number (2nd number after shuffle) from random_answer list (1, 2, 3, or 4)
       self.activeRow = random_answer[1]
       self.quiz_b_button.grid(row=self.activeRow, padx=12, pady=8)

       #quiz_c_button is always incorrect
       #quiz frame row 1-4 = quiz_c_button
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
       #sets row to random number (3rd number after shuffle) from random_answer list (1, 2, 3, or 4)
       self.activeRow = random_answer[2]
       self.quiz_c_button.grid(row=self.activeRow, padx=12, pady=8)

       #quiz_d_button is always incorrect
       #quiz frame row 1-4 = quiz_d_button
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
       #sets row to random number (4th number after shuffle) from random_answer list (1, 2, 3, or 4)
       self.activeRow = random_answer[3]
       self.quiz_d_button.grid(row=self.activeRow, padx=12, pady=8)

  
  #is run when quiz_a_button (always correct) is clicked
  def correct_answer(self, partner):
      
      #activates global variables that hold score, q number, if export/clear scores should be active, and incorrect question variables
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
    
      #sets quiz buttons to disabled, but doesn't change their apperance
      #give the buttons a highlight showing what answer is correct
      self.quiz_a_button.config(highlightbackground="#50C878", highlightthickness=3, state=DISABLED)
      self.quiz_b_button.config(highlightbackground="#C80815", highlightthickness=2, state=DISABLED)
      self.quiz_c_button.config(highlightbackground="#C80815", highlightthickness=2, state=DISABLED)
      self.quiz_d_button.config(highlightbackground="#C80815", highlightthickness=2, state=DISABLED)
    
      #adds 1 to score and current question variables
      questions_total += 1
      questions_right += 1

      #waits 2 sec before destroying the question box
      self.quiz_box.after(2000,lambda:self.quiz_box.destroy())
      #updates question and score labels on main_frame
      partner.current_question.config(text="Question: {}/10".format(questions_total))
      partner.current_score.config(text="Score: {}".format(questions_right))

      #checks to see if the quiz is complete
      if questions_total >= 10:
        #sets binary style variable to tell scoreboard that user can export and clear score
        scoreboard_active = 1
        #shuffles question order list for next use
        random.shuffle(question_number)
        #shuffles list with congradulations
        random.shuffle(congrats)    
        #updates labels/buttons on main_frame
        partner.current_question.config(text=("Question 0/10"))
        partner.current_score.config(text=("Score: 0"))
        partner.to_quiz_button.config(text=("Start Quiz"))
        partner.main_frame.after(2000,lambda:partner.to_quiz_button.config(state=NORMAL))
        
        #opens score list, saves data to list
        with open('data/score.txt', 'r') as file:
            data = file.readlines()
        #inserts a line in before the rest of the data in list
        #how many questions correct/10 and incorrect questions
        data.insert(0, "{}/10. Incorrect Questions: {} {} {} {} {} {} {} {} {} {}\n".format(questions_right, inc1, inc2, inc3, inc4, inc5, inc6, inc7, inc8, inc9, inc10))
        #writes everything back into file with new data in the top line
        with open("data/score.txt", "w") as file:
            file.writelines(data)
        #opens scoreboard list, saves data to list
        with open('data/scoreboard.txt', 'r') as file:
            data = file.readlines()
        #inserts a line in before the rest of the data in list
        #how many questions correct/10
        data.insert(0, "{}/10\n".format(questions_right))
        #writes everything back into file with new data in the top line
        with open("data/scoreboard.txt", "w") as file:
            file.writelines(data)

        #resets incorrect question variables
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
        
        #checks to see if you got < or > than 5 correct
        #updates quiz_results label on main_frame
        #if more or equal to 5 (5,6,7,8,9,10)
        if questions_right >= 5:
            #congradulate with a random congrats line from 'congrats' list
            partner.quiz_results.config(text="{}! You got {}/10".format(congrats[1], questions_right))
        
        #if less than 5 (1,2,3,4)
        else:
          #offer sympathy to user and tell them 'nice try'
          partner.quiz_results.config(text="Nice try, you got {}/10".format(questions_right))
        
        #resets score and question number variables for next use
        questions_total = 0
        questions_right = 0

          
      #if quiz is NOT complete
      else:
        #reset quiz_results in main_frame (incase of prev session)
        partner.quiz_results.config(text="")
        #set 'Start Quiz' button to 'Continue Quiz'
        partner.to_quiz_button.config(text="Continue Quiz")
        partner.main_frame.after(2000,lambda:partner.to_quiz_button.config(state=NORMAL))

  
  #run by quiz_b_button, quiz_c_button, quiz_d_button
  def incorrect_answer(self, partner):
      
      
      #activates global variables that hold score, q number, if export/clear scores should be active, and incorrect question variables
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

      #strips blank lines (\n) off question and saves to variable for showing what question is incorrect
      q = list_of_questions[question_number[questions_total]]
      question = q.strip()

  
      #sets quiz buttons to disabled, but doesn't change their apperance
      #give the buttons a highlight showing what answer is correct
      self.quiz_a_button.config(highlightbackground="#50C878", highlightthickness=3, state=DISABLED)
      self.quiz_b_button.config(highlightbackground="#C80815", highlightthickness=2, state=DISABLED)
      self.quiz_c_button.config(highlightbackground="#C80815", highlightthickness=2, state=DISABLED)
      self.quiz_d_button.config(highlightbackground="#C80815", highlightthickness=2, state=DISABLED)
    
      #add 1 to current question variable
      questions_total += 1
    
      #checks what the question number is and sets current question(stripped) to inc# to export later
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

      #wait 2 sec then destroy question box
      self.quiz_box.after(2000,lambda:self.quiz_box.destroy())
      #updates question number label in main_frame
      partner.current_question.config(text="Question: {}/10".format(questions_total))

      #checks if quiz is complete
      if questions_total >= 10:
        #sets binary style variable to tell scoreboard that user can export and clear score
        scoreboard_active = 1
        #shuffles question order list for next use
        random.shuffle(question_number)
        #shuffles list with congradulations
        random.shuffle(congrats)    
        #updates labels/buttons on main_frame
        partner.current_question.config(text=("Question 0/10"))
        partner.current_score.config(text=("Score: 0"))
        partner.to_quiz_button.config(text=("Start Quiz"))
        partner.main_frame.after(2000,lambda:partner.to_quiz_button.config(state=NORMAL))
        
        #opens score list, saves data to list
        with open('data/score.txt', 'r') as file:
            data = file.readlines()
        #inserts a line in before the rest of the data in list
        #how many questions correct/10 and incorrect questions
        data.insert(0, "{}/10. Incorrect Questions: {} {} {} {} {} {} {} {} {} {}\n".format(questions_right, inc1, inc2, inc3, inc4, inc5, inc6, inc7, inc8, inc9, inc10))
        #writes everything back into file with new data in the top line
        with open("data/score.txt", "w") as file:
            file.writelines(data)
        #opens scoreboard list, saves data to list
        with open('data/scoreboard.txt', 'r') as file:
            data = file.readlines()
        #inserts a line in before the rest of the data in list
        #how many questions correct/10
        data.insert(0, "{}/10\n".format(questions_right))
        #writes everything back into file with new data in the top line
        with open("data/scoreboard.txt", "w") as file:
            file.writelines(data)

        #resets incorrect question variables
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

        #checks to see if you got < or > than 5 correct
        #updates quiz_results label on main_frame
        #if more or equal to 5 (5,6,7,8,9,10)
        if questions_right >= 5:
          #congradulate with a random congrats line from 'congrats' list
          partner.quiz_results.config(text="{}! You got {}/10".format(congrats[1], questions_right))
        
        #if less than 5 (1,2,3,4)
        else:
          #offer sympathy to user and tell them 'nice try'
          partner.quiz_results.config(text="Nice try, you got {}/10".format(questions_right))
        
        #resets score and question number variables for next use
        questions_total = 0
        questions_right = 0

          
      #if quiz is NOT complete
      else:
        #reset quiz_results in main_frame (incase of prev session)
        partner.quiz_results.config(text="")
        #set 'Start Quiz' button to 'Continue Quiz'
        partner.to_quiz_button.config(text="Continue Quiz")
        partner.main_frame.after(2000,lambda:partner.to_quiz_button.config(state=NORMAL))
  
  def close_quiz(self, partner):
      #sets start/continue quiz button's state to normal
      partner.to_quiz_button.config(state=NORMAL)
      #destroys question box
      self.quiz_box.destroy()
  
#main rouine
root = Tk()
root.resizable(False, False)
root.title("Roll for WIS")
menu()
root.mainloop()