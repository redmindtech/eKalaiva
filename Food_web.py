#- * - coding: utf8 -*-

import json
import os
# import mysql.connector

# from flask import Flask, session, redirect, url_for, request
from flask import Flask
from flask import request
from flask import make_response
from flask import jsonify

import course

app = Flask(__name__)
app.secret_key=0
app.secret_code=1
app.secret_count=0
app.secret_ques=0
app.secret_ans=0
app.email=0


@app.route("/food", methods=['POST', 'GET'])
def food():
    try:
        invoke_next_question = True
        req = request.get_json(silent=True, force=True)

        print("----------------START-------------------")
        print("Request:")
        print(req)

        current_reply = req.get("queryResult").get("action")
        print("current_reply done")
        current_intent = req.get("queryResult").get("outputContexts")[0].get("parameters").get("current-intent")
        print("current_intent done")

        print("current_intent - ", current_intent)
        print("current_reply - ", current_reply)
        
        #emailid = "meetarun@gmail.com"
        value = (req.get('queryResult'))
        print("value -- ",value)
        name = value.get('parameters')
        emailid = name.get('option')
        #email1=emailid
        #print(emailid)
        #start=name.get('ready')
        #ans = name.get('option')
        #close = name.get('exit')
        #q_name = name.get('quizname')
        #print(q_name)

        if emailid is not None and app.email == 0:
            e_mail = ''.join(emailid)
            email1 = course.email(e_mail)
            print("result--",email1)
            if email1 is not None:
                app.email = 1
            if email1 is not None and email1.find("Are you Ready for the Quiz?"):
                bot_reply = {
                    "fulfillmentText": email1,
                    "followupEventInput": {
                        "name": "6_Subjects",

                    }
                 }
                
            else:
                bot_reply = {
                    "fulfillmentText": "You have to be a registered user to login",
                    "followupEventInput": {
                        "name": "Unauthorised_user",

                    }
                 }
                
            
            if (bot_reply):
                res = jsonify(bot_reply)
                return res

        elif close is not None:
            course.re_set()

        if current_intent.endswith("Keypoints"):
            next_intent = current_intent
            print("Keypoints executed")

        else:
            next_index = str(int(current_intent[-1:]) + 1)
            print("next_index---", next_index)
            next_intent = current_intent[:-1] + next_index
        print("next intent - ", next_intent)

        if current_reply == "Next_Lesson":
            print("came here")
            str_array = current_intent.split("_")
            print("couldnt do", len(str_array))
            print("(str_array(3)--", int(str_array[3]) + 1)

            current_intent = str_array[0] + "_" + str_array[1] + "_" + str_array[2] + "_" + str(int(str_array[3]) + 1)
            print("current-intent--", current_intent)
            bot_reply = {
                "followupEventInput": {
                    "name": current_intent,
                    "data": {
                        "user-answer": current_intent + "." + current_reply
                    }
                }
            }
        if current_reply == "start_lesson":
            # this is to find whether the lesson is started
            str_array = current_intent.split("_")
            print("length--", len(str_array))

            if len(str_array) == 4:
                current_intent = current_intent + "_1"
            elif len(str_array) == 5:
                if (current_intent.endswith("Keypoints")):
                    current_intent = current_intent[:-10]
                else:
                    current_intent = current_intent[:-2]
            # elif current_intent == "6_Science_Lesson_1_6":
            #   current_intent= current_intent[:-2]
            # elif current_intent == "6_Science_Lesson_2_7":
            #   current_intent = current_intent[:-2]
            # elif current_intent == "6_Social_Lesson_2_8":
            #   current_intent = current_intent[:-2]
            # elif current_intent == "6_Social_Lesson_1_8":
            #   current_intent = current_intent[:-2]

            # elif current_intent.find("Keypoints"):
            #   current_intent= current_intent[:-10]
            # else:

            # current_intent = current_intent + "_1"
            print(current_intent)
            bot_reply = {
                "followupEventInput": {
                    "name": current_intent,
                    "data": {
                        "user-answer": current_intent + "." + current_reply
                    }
                }
            }
        elif current_reply == "Watch_video":
            current_intent = current_intent + "_Video"
            bot_reply = {
                "followupEventInput": {
                    "name": current_intent,
                    "data": {
                        "user-answer": current_intent + "." + current_reply
                    }
                }
            }
            print(bot_reply)
        elif current_reply == "repeat":

            bot_reply = {
                "followupEventInput": {
                    "name": current_intent,
                    "data": {
                        "user-answer": current_intent + "." + current_reply
                    }
                }
            }
            print(bot_reply)
        elif current_reply == "next_topic":
            bot_reply = {
                "followupEventInput": {
                    "name": next_intent,
                    "data": {
                        "user-answer": next_intent + "." + current_reply
                    }
                }
            }
            print(bot_reply)

        elif current_reply == "back_to_lesson":
            print("current-intent--", current_intent)
            str_array = current_intent.split("_")
            current_intent = str_array[0] + "_" + str_array[1] + "_" + str_array[2] + "_" + str_array[3]
            # current_intent = current_intent[:-6]
            print("current-intent--", current_intent)
            bot_reply = {
                "followupEventInput": {
                    "name": current_intent,
                    "data": {
                        "user-answer": next_intent + "." + current_reply
                    }
                }
            }
            print(bot_reply)

        elif current_reply == "Keypoints":
            str_array = current_intent.split("_")
            if len(str_array) == 5:
                next_index = str(int(str_array(3) + 1))
                str_array = str_array.remove(str_array(4))
                print("New array--", str_array)
                for ele in str_array:
                    current_intent += ele
                    current_intent += "_"
                print("next_index---", next_index)
                current_intent = current_intent[:-1]
            current_intent = current_intent + "_Keypoints"
            bot_reply = {
                "followupEventInput": {
                    "name": current_intent,
                    "data": {
                        "user-answer": current_intent + "." + current_reply
                    }
                }
            }

        print("reached here...")

        if (bot_reply):
            res = jsonify(bot_reply)
        return res



    except:
        speech = "Error occurred"
        bot_reply = {
            "speech": speech,

            "displayText": speech,
            "source": "VA webhook"
        }

    if (bot_reply):
        res = jsonify(bot_reply)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    print(bot_reply)
    print("###############################")
    return res


if __name__ == '__main__':
    app.run()
