
import mysql.connector as mysql
from flask import Flask, session, redirect, url_for, request
#from flask import Flask
#import tn_db_connection
import json
import os
from flask import Flask, request, jsonify
app = Flask(__name__)
app.secret_key=0
app.secret_code=0
app.secret_score=0
# enter your server IP address/domain name
HOST = "ekalaiva-ai.com" # or "domain.com"
# database name, if you want just to connect to MySQL server, leave it empty
DATABASE = "u852023448_uwyeF"
# this is the user you create
USER = "u852023448_MfN4p"
# user password
PASSWORD = "xR1smqFRrV"

def email(e_mail):
    print(e_mail)
    try:
       db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD,connection_timeout=60000)
       print("Connected to:", db_connection.get_server_info())
       mycursor = db_connection.cursor() 
       tr="""select username from x8ur_user where email=%s""";
       username=''
       mycursor.execute(tr,(e_mail,))
       username=mycursor.fetchone()
       if username is not None:
           user="welcome {}! Are you Ready for the Quiz?".format(*username)
           return user
           
    except mysql.Error as err:
         print(err)
         print("Error Code:", err.errno)
         print("SQLSTATE", err.sqlstate)
         print("Message", err.msg)
              

def query2(questions,count):
    i=0
    app.secret_key+=1
    i=app.secret_key
    if i<count:
        que=  ''.join(questions[i])
        return que
    else:
        end=app.secret_score
        return end

def ques_count(quiz):
    try:
        db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD,connection_timeout=60000)
        print("Connected to:", db_connection.get_server_info())
        mycursor = db_connection.cursor() 
        string="""SELECT
        qa.questionsummary
        FROM x8ur_quiz_attempts quiza
        JOIN x8ur_question_usages qu ON qu.id = quiza.uniqueid
        JOIN x8ur_question_attempts qa ON qa.questionusageid = qu.id
        JOIN x8ur_question_attempt_steps qas ON qas.questionattemptid = qa.id
        LEFT JOIN x8ur_question_attempt_step_data qasd ON qasd.attemptstepid = qas.id
        WHERE quiza.quiz in (SELECT id from x8ur_quiz where name=%s);"""
        mycursor.execute(string,(quiz,))
        u=mycursor.fetchall()
        e=len(u)
        return e
    except mysql.Error as err:
        print(err)
        print("Error Code:", err.errno)
        print("SQLSTATE", err.sqlstate)
        print("Message", err.msg)    

def query(quiz):
	try:
		db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD,connection_timeout=60000)
		mycursor = db_connection.cursor() 
		string="""SELECT
		qa.questionsummary,qa.rightanswer
		FROM x8ur_quiz_attempts quiza
		JOIN x8ur_question_usages qu ON qu.id = quiza.uniqueid
		JOIN x8ur_question_attempts qa ON qa.questionusageid = qu.id
		JOIN x8ur_question_attempt_steps qas ON qas.questionattemptid = qa.id
		LEFT JOIN x8ur_question_attempt_step_data qasd ON qasd.attemptstepid = qas.id
		WHERE quiza.quiz in (SELECT id from x8ur_quiz where name=%s);"""
		mycursor.execute(string,(quiz,))
		Q=mycursor.fetchall()
		count=len(Q)
		myList = []
		myList1 = []
		for row in Q:
			myList.append(row[0])
			myList1.append(row[1])
			
		return myList,myList1,count
	
	except mysql.Error as err:
		print(err)
		print("Error Code:", err.errno)
		print("SQLSTATE", err.sqlstate)
		print("Message", err.msg)


def main(quiz,i):
    print(quiz)
    try:
        db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD,connection_timeout=60000)
        print("Connected to:", db_connection.get_server_info())
        mycursor = db_connection.cursor()
        string="""SELECT
        qa.questionsummary
        FROM x8ur_quiz_attempts quiza
        JOIN x8ur_question_usages qu ON qu.id = quiza.uniqueid
        JOIN x8ur_question_attempts qa ON qa.questionusageid = qu.id
        JOIN x8ur_question_attempt_steps qas ON qas.questionattemptid = qa.id
        LEFT JOIN x8ur_question_attempt_step_data qasd ON qasd.attemptstepid = qas.id
        WHERE qa.slot=%s AND quiza.quiz in (SELECT id from x8ur_quiz where name=%s);"""
        mycursor.execute(string,(i,str(quiz),))
        for g in mycursor:
            y=g
            #print(y)
        return y
    except mysql.Error as err:
        print(err)
        print("Error Code:", err.errno)
        print("SQLSTATE", err.sqlstate)
        print("Message", err.msg)    

def ques_split(str1):
    s=str1.split(':')
    sym=";"
    opt1=s[1].partition(sym)[0]
    stropt1 = s[1].partition(sym)[2]
    opt2=stropt1.partition(sym)[0]
    stropt2=stropt1.partition(sym)[2]
    opt3=stropt2.partition(sym)[0]
    stropt3=stropt2.partition(sym)[2]
    opt4=stropt3.partition(sym)[0]
    return s[0],opt1,opt2,opt3,opt4

def fetching(quiz):
    try:
        db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD,connection_timeout=60000)
        print("Connected to:", db_connection.get_server_info())
        mycursor = db_connection.cursor() 
        word="""SELECT
        qa.rightanswer
        FROM x8ur_quiz_attempts quiza
        JOIN x8ur_question_usages qu ON qu.id = quiza.uniqueid
        JOIN x8ur_question_attempts qa ON qa.questionusageid = qu.id
        JOIN x8ur_question_attempt_steps qas ON qas.questionattemptid = qa.id
        LEFT JOIN x8ur_question_attempt_step_data qasd ON qasd.attemptstepid = qas.id
        WHERE quiza.quiz in (SELECT id from x8ur_quiz where name=%s);"""
        mycursor.execute(word,(quiz,))
        r=mycursor.fetchall()
        return r
    except mysql.Error as err:
        print(err)
        print("Error Code:", err.errno)
        print("SQLSTATE", err.sqlstate)
        print("Message", err.msg)    

def valid(ans,an,an1,an2,an3,answers):
    v=len(answers)
    print(v)
    j=app.secret_code
    print(j)
    crt=  ''.join(answers[j])
    while j<v:
        if an==crt:
            app.secret_score+=1
            reply='correct answer!!'
        elif an1==crt:
            app.secret_score+=1
            reply='correct answer!!'
        elif an2==crt:
            app.secret_score+=1
            reply='correct answer!!'  
        elif an3==crt:
            app.secret_score+=1
            reply='correct answer!!'      
        elif ans==crt:
            app.secret_score+=1
            reply='correct answer!!'
            #printns(ans)
        else:
            app.secret_score+=0
            reply="Incorrect answer!! the correct answer is {}.".format(crt)
            #print(reply)
        #print(app.secret_score)
        app.secret_code+=1
        return reply,app.secret_score

def re_set():
    app.secret_key=0
    app.secret_code=0
    app.secret_score=0





if __name__=="__main__":
    main()
