import mysql.connector
import mysql.connector as mysql
from flask import Flask, session, redirect, url_for, request
# from flask import Flask
# import tn_db_connection
import json
import os
from flask import Flask, request, jsonify

app = Flask(__name__)
app.secret_key1 = 0
app.secret_code1 = 0
app.secret_score = 0
# enter your server IP address/domain name
HOST = "redmindtechnologies.com"  # or "domain.com"
# database name, if you want just to connect to MySQL server, leave it empty
DATABASE = "u852023448_uwyeF"
# this is the user you create
USER = "u852023448_MfN4p"
# user password
PASSWORD = "xR1smqFRrV"


def email(e_mail):
    print(e_mail)
    try:
        db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD,
                                      connection_timeout=60000)
        print("Connected to:", db_connection.get_server_info())
        mycursor = db_connection.cursor()
        tr = """select username from x8ur_user where email=%s""";
        username = ''
        mycursor.execute(tr, (e_mail,))
        username = mycursor.fetchone()
        if username is not None:
            #user = "welcome {}! Are you Ready for the Quiz?".format(*username)
            user = "{}".format(*username)
            return user

    except mysql.Error as err:
        print(err)
        print("Error Code:", err.errno)
        print("SQLSTATE", err.sqlstate)
        print("Message", err.msg)


# def query2(questions):
#     i = 0
#     app.secret_key1 += 1
#     i = app.secret_key1
#     if i < 5:
#         que = ''.join(questions[i])
#         return que
#     else:
#         end = app.secret_score
#         return end

def query2(questions, options):
    i = 0
    app.secret_key1 += 1
    i = app.secret_key1
    if i < 5:
        que = ''.join(questions[i])
        return que, options[i]
    else:
        end = app.secret_score
        emptylist=[]
        return end,emptylist
    
# def ques_count(quiz):
#     try:
#         db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD,connection_timeout=60000)
#         print("Connected to:", db_connection.get_server_info())
#         mycursor = db_connection.cursor()
#         string="""SELECT questionsummary
#         FROM x8ur_question_attempts
#         WHERE questionusageid in (SELECT uniqueid from x8ur_quiz_attempts where quiz in (SELECT id from x8ur_quiz where course in (SELECT courseid from x8ur_enrol where id in (SELECT enrolid from x8ur_user_enrolments where userid=%s))));"""
#         mycursor.execute(string,(quiz,))
#         u=mycursor.fetchall()
#         e=len(u)
#         return e
#     except mysql.Error as err:
#         print(err)
#         print("Error Code:", err.errno)
#         print("SQLSTATE", err.sqlstate)
#         print("Message", err.msg)

# def query(quiz):
#     try:
#         db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD,
#                                       connection_timeout=60000)
#         mycursor = db_connection.cursor()
#         string = """SELECT questionsummary, rightanswer FROM x8ur_question_attempts 
#                 WHERE questionusageid in (SELECT id FROM `x8ur_quiz_attempts` WHERE quiz in (select id from x8ur_quiz where name = %s));"""
#         print("query--",string)
#         mycursor.execute(string, (quiz,))
#         Q = mycursor.fetchall()
#         myList = []
#         myList1 = []

#         for row in Q:
#             print("row--",row)
#             myList.append(row[0])
#             myList1.append(row[1])
#             print("row completed")
#         return myList, myList1

#     except mysql.Error as err:
#         print(err)
#         print("Error Code:", err.errno)
#         print("SQLSTATE", err.sqlstate)
#         print("Message", err.msg)

def query(quiz):
    try:       
        queslist=[]
        quesoptionlistoflist=[]
        quesresultlist=[]
        
        queslist, quesoptionlistoflist, quesresultlist = quizdetails(quiz)
        return queslist, quesoptionlistoflist, quesresultlist

    except mysql.Error as err:
        print(err)
        print("Error Code:", err.errno)
        print("SQLSTATE", err.sqlstate)
        print("Message", err.msg)


# def main(quiz, i):
#     print(quiz)
#     try:
#         db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD,
#                                       connection_timeout=60000)
#         print("Connected to:", db_connection.get_server_info())
#         mycursor = db_connection.cursor()
#         string = """SELECT questionsummary FROM x8ur_question_attempts 
#         WHERE slot = %s AND questionusageid in (SELECT id FROM `x8ur_quiz_attempts` WHERE quiz in (select id from x8ur_quiz where name = %s))"""
#         print("query--", string)
#         mycursor.execute(string, (i, str(quiz),))
#         for g in mycursor:
#             y = g
#             print(y)
#         return y
#     except mysql.Error as err:
#         print(err)
#         print("Error Code:", err.errno)
#         print("SQLSTATE", err.sqlstate)
#         print("Message", err.msg)

def main(quiz, i):
    print(quiz)
    try:       
        queslist=[]
        quesoptionlistoflist=[]
        quesresultlist=[]
        
        queslist, quesoptionlistoflist, quesresultlist = quizdetails(quiz)
        return queslist[0], quesoptionlistoflist[0]
    except mysql.Error as err:
        print(err)
        print("Error Code:", err.errno)
        print("SQLSTATE", err.sqlstate)
        print("Message", err.msg)

# For the input Quiz Lesson, the quizdetails method fetches all distinct 
# Questions in a list, options for the all the questions in a list of lists, 
# correct answers for the all questions in a list
        
def quizdetails(quiz):
    print(quiz)
    try:
        db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD,
                                      connection_timeout=60000)
        print("Connected to:", db_connection.get_server_info())
        mycursor = db_connection.cursor()
        query = """select distinct ans.question, ques.questiontext from x8ur_question as ques 
        JOIN x8ur_question_answers as ans ON ans.question = ques.id
        JOIN x8ur_quiz_slots as slots ON ans.question = slots.questionid
        JOIN x8ur_quiz as quiz ON quiz.id = slots.quizid
        where quiz.name=%s order by ans.question"""
        print("query--",query)
        
        mycursor.execute(query, (quiz,))
        Q = mycursor.fetchall()
        myQuesList = []
        myOptionsList = []
        myCorrectAnsList = []
        myOptionsListofList=[]
    
        for row in Q:
            #print("row--",row)
            #print('row[1] question --', row[1])
            myQuesList.append(row[1])
            myOptionsList = []
            
            query1="""select distinct ans.answer, if(ans.fraction,ans.answer,0) correctans from x8ur_question as ques 
            JOIN x8ur_question_answers as ans ON ans.question = ques.id
            JOIN x8ur_quiz_slots as slots ON ans.question = %s
            JOIN x8ur_quiz as quiz ON quiz.id = slots.quizid
            where quiz.name=%s"""
            #print("query1--",query1)

            mycursor.execute(query1, (row[0],quiz))
            optcur = mycursor.fetchall()
            
            for optrow in optcur:
                myOptionsList.append(optrow[0])
                if (optrow[1] !=  "0"):
                    myCorrectAnsList.append(optrow[1])
                    
            myOptionsListofList.append(myOptionsList)

        #print('MyQuesList --', myQuesList)
        #print('myOptionsList --', myOptionsListofList)
        #print('MyAnswerList --', myCorrectAnsList)
        return myQuesList, myOptionsListofList, myCorrectAnsList
    
    except mysql.Error as err:
        print(err)
        print("Error Code:", err.errno)
        print("SQLSTATE", err.sqlstate)
        print("Message", err.msg)


def ques_split(str1):
    s = str1.split(':')
    sym = ";"
    opt1 = s[1].partition(sym)[0]
    stropt1 = s[1].partition(sym)[2]
    opt2 = stropt1.partition(sym)[0]
    stropt2 = stropt1.partition(sym)[2]
    opt3 = stropt2.partition(sym)[0]
    stropt3 = stropt2.partition(sym)[2]
    opt4 = stropt3.partition(sym)[0]
    return s[0], opt1, opt2, opt3, opt4


def fetching(quiz):
    try:
        db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD,
                                      connection_timeout=60000)
        print("Connected to:", db_connection.get_server_info())
        mycursor = db_connection.cursor()
        word = """SELECT questionsummary FROM x8ur_question_attempts 
                WHERE questionusageid in (SELECT id FROM `x8ur_quiz_attempts` WHERE quiz in (select id from x8ur_quiz where name = %s));"""
        mycursor.execute(word, (quiz,))
        r = mycursor.fetchall()
        return r
    except mysql.Error as err:
        print(err)
        print("Error Code:", err.errno)
        print("SQLSTATE", err.sqlstate)
        print("Message", err.msg)


def valid(ans, an, an1, an2, an3, answers):
    v = len(answers)
    print(v)
    print ("secret code--", app.secret_code1)
    j = app.secret_code1
    print(j)
    crt = ''.join(answers[j])
    while j < v:
        if an == crt:
            app.secret_score += 1
            reply = 'correct answer!!'
        elif an1 == crt:
            app.secret_score += 1
            reply = 'correct answer!!'
        elif an2 == crt:
            app.secret_score += 1
            reply = 'correct answer!!'
        elif an3 == crt:
            app.secret_score += 1
            reply = 'correct answer!!'
        elif ans == crt:
            app.secret_score += 1
            reply = 'correct answer!!'
            #print(ans)
        else:
            app.secret_score += 0
            reply = "Incorrect answer!! the correct answer is {}.".format(crt)
        print("ans in course--", crt)
        print("app.secret_score--",app.secret_score)
        app.secret_code1 += 1

        return reply, app.secret_score


def re_set():
    print("Session clearer")
    app.secret_key1 = 0
    app.secret_code1 = 0
    app.secret_score = 0
    app.email=0

def getvideo(lesson):
    try:
        db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD,
                                      connection_timeout=60000)
        print("Connected to:", db_connection.get_server_info())
        mycursor = db_connection.cursor()
        tr = """select videolink, image from x8ur_video_image where lesson=%s""";
        username = ''
        mycursor.execute(tr, (lesson,))
        row = mycursor.fetchone()

        print("link--",row[0])
        print('image--',row[1])
        return row[0] , row[1]

    except mysql.Error as err:
        print(err)
    print("Error Code:", err.errno)
    print("SQLSTATE", err.sqlstate)
    print("Message", err.msg)

if __name__ == "__main__":
    main()
