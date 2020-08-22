import mysql.connector
from flask import Flask, session, redirect, url_for, request
# from flask import Flask
import json
import os
from flask import Flask, request, jsonify

app = Flask(__name__)
mydb = mysql.connector.connect(host="127.0.0.1", user="bn_moodle", passwd="a4386605f1", database="bitnami_moodle")
mycursor = mydb.cursor()
app.secret_key = 1
app.secret_code = 0
app.secret_score = 0


def score_update(x, score):
    speech = """UPDATE mdl_quiz_attempts
    SET sumgrades = %s
    WHERE userid = %s;"""
    mycursor.execute(speech, (x, score,))
    print("the score is:", score)
    print(type(score))
    mydb.commit()


def query2(d):
    i = 0
    count = ques_count(d)
    app.secret_key += 1
    i = app.secret_key
    if i <= count:
        w = query(i, d)
        return w
    else:
        end = app.secret_score
        return end


def ques_count(d):
    string = """SELECT 
    questionsummary
    FROM mdl_question_attempts 
    WHERE questionusageid in (SELECT uniqueid from mdl_quiz_attempts where quiz=(SELECT id from mdl_quiz where course=(SELECT courseid from mdl_enrol where id=(SELECT enrolid from mdl_user_enrolments where userid=%s))));"""
    mycursor.execute(string, (d,))
    u = mycursor.fetchall()
    e = len(u)
    print(e)
    return e


def query(i, d):
    string = """SELECT
    qa.questionsummary
    FROM mdl_quiz_attempts quiza
    JOIN mdl_question_usages qu ON qu.id = quiza.uniqueid
    JOIN mdl_question_attempts qa ON qa.questionusageid = qu.id
    JOIN mdl_question_attempt_steps qas ON qas.questionattemptid = qa.id
    LEFT JOIN mdl_question_attempt_step_data qasd ON qasd.attemptstepid = qas.id
    WHERE qa.slot=%s AND quiza.quiz in (SELECT id from mdl_quiz where course=(SELECT courseid from mdl_enrol where id=(SELECT enrolid from mdl_user_enrolments where userid=%s)));"""
    mycursor.execute(string, (i, d,))
    for g in mycursor:
        y = g
        # print(y)

    return y


def main(u_id, i):
    string = """SELECT
    qa.questionsummary
    FROM mdl_quiz_attempts quiza
    JOIN mdl_question_usages qu ON qu.id = quiza.uniqueid
    JOIN mdl_question_attempts qa ON qa.questionusageid = qu.id
    JOIN mdl_question_attempt_steps qas ON qas.questionattemptid = qa.id
    LEFT JOIN mdl_question_attempt_step_data qasd ON qasd.attemptstepid = qas.id
    WHERE qa.slot=%s AND quiza.quiz in (SELECT id from mdl_quiz where course=(SELECT courseid from mdl_enrol where id=(SELECT enrolid from mdl_user_enrolments where userid=%s)));"""
    mycursor.execute(string, (i, u_id,))
    for g in mycursor:
        y = g
        # print(y)

    return y


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


def fetching(d):
    word = """SELECT qa.rightanswer
    FROM mdl_quiz_attempts quiza
    JOIN mdl_question_usages qu ON qu.id = quiza.uniqueid
    JOIN mdl_question_attempts qa ON qa.questionusageid = qu.id
    JOIN mdl_question_attempt_steps qas ON qas.questionattemptid = qa.id
    LEFT JOIN mdl_question_attempt_step_data qasd ON qasd.attemptstepid = qas.id
    WHERE quiza.quiz in (SELECT id from mdl_quiz where course=(SELECT courseid from mdl_enrol where id=(SELECT enrolid from mdl_user_enrolments where userid=%s)));"""
    mycursor.execute(word, (d,))
    r = mycursor.fetchall()
    return r


def valid(ans, an, an1, an2, an3, d):
    u = fetching(d)
    v = len(u)
    print(v)
    j = app.secret_code
    print(j)
    crt = ''.join(u[j])
    while j <= v:
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
            # printns(ans)
        else:
            app.secret_score += 0
            reply = "Incorrect answer!! the correct answer is {}.".format(crt)
            # print(reply)
        # print(app.secret_score)
        app.secret_code += 2
        return reply, app.secret_score


def re_set():
    app.secret_key = 1
    app.secret_code = 0
    app.secret_score = 0


if __name__ == "__main__":
    main()
