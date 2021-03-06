# - * - coding: utf8 -*-

import json
import os
# import mysql.connector

# from flask import Flask, session, redirect, url_for, request
from flask import Flask , session
from flask import request
from flask import make_response
from flask import jsonify

import course
import lesson

app = Flask(__name__)

app.secret_key = 0
app.secret_code = 1
app.secret_count = 0
app.secret_ques = 0
app.secret_ans = 0

app.email=0

@app.route("/food", methods=['POST', 'GET'])
def food():
    try:
        invoke_next_question = True
        req = request.get_json(silent=True, force=True)

        # to navigate through lessons
        current_reply = req.get("queryResult").get("action")
        current_intent = req.get("queryResult").get("outputContexts")[0].get("parameters").get("current-intent")
        print("current_intent - ", current_intent)
        print("current_reply - ", current_reply)

        # to retrieve email and quiz options
        value = (req.get('queryResult'))
        emailid = ""
        ans=""
        q_name=""
        close=""

        #for user login email id
        if (req.get("queryResult").get("intent").get("displayName") == "welcome - next" or req.get("queryResult").get("intent").get("displayName") == "Get_Email"):
            emailid = req.get("queryResult").get("parameters").get("email")
            app.email = 0
            print(emailid)

        # for quiz answers
        if (req.get("queryResult").get("intent").get("displayName") == "ans_code"):
            ans = req.get("queryResult").get("parameters").get("option")
            print("ans--",ans)

            # after quiz completion, ask user to change subject or change lesson
            if(ans == "change_lesson"):
                bot_reply = {
                    "fulfillmentText": "change_lesson",
                    "followupEventInput": {
                        "name": "change_lesson"
                    }
                }
                print("bot_reply--", bot_reply)
                res = jsonify(bot_reply)
                return res

            if (ans == "select_subject"):
                bot_reply = {
                    "fulfillmentText": "select_subject",
                    "followupEventInput": {
                        "name": "6_Subjects"
                    }
                }
                print("bot_reply--", bot_reply)
                res = jsonify(bot_reply)
                return res

        # to start quiz
        if (req.get("queryResult").get("intent").get("displayName") == "Quiz"):
            ready = req.get("queryResult").get("parameters").get("ready")
            q_name = req.get("queryResult").get("outputContexts")[6].get("parameters").get("current-intent") + "_Quiz"
            print("quiz name--" , q_name)
            #q_name = "Science Quiz"
            print(ready)


        # End of conversation
        if (req.get("queryResult").get("intent").get("displayName") == "Exit"):
            close = req.get("queryResult").get("parameters").get("exit")
            print(close)

        # to display list of lessons compatible for both google assistant and botcopy
        displayintent = req.get("queryResult").get("intent").get("displayName")
        if (displayintent == "6_English_Lesson" or displayintent == "6_Geography_Lesson" or displayintent == "6_Science_Lesson" or displayintent == "6_Social_Lesson" or displayintent == "6_Civics_Lesson" or displayintent == "6_Geography_Lesson" ):
            res = lesson.getlesson(displayintent)
            return res

        # validate user login
        if (emailid != "") and (app.email == 0):
            e_mail = ''.join(emailid)
            email1 = course.email(e_mail)
            print("result--", email1)
            # print(app.email)
            if email1 is not None:
                app.email = 1
                bot_reply = {
                    "fulfillmentText": email1,
                    "followupEventInput": {
                        "name": "6_Welcome_Subjects",
                        "parameters": {
                            "username": email1.capitalize()
                        }
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

        # to invoke first question in the quiz
        elif q_name != "":
            app.secret_key = q_name
            quiz = ''.join(app.secret_key)

            firstques, firstquesoptions = course.main(quiz, i=1)

            q1 = firstques

            Q1 = ''.join(q1)

            opt1 = firstquesoptions[0]
            opt2 = firstquesoptions[1]
            opt3 = firstquesoptions[2]
            opt4 = firstquesoptions[3]
            # for suggestion chips length, it has to be taken care in the db itself
            if (len(opt1) > 25):
                opt1 = opt1 [ 0:24 ]
            if (len(opt2) > 25):
                opt2 = opt2  [ 0:24 ]
            if (len(opt3) > 25):
                opt3 = opt3 [ 0:24 ]
            if (len(opt4) > 25):
                opt4 = opt4  [ 0:24 ]

            op1 = ''.join(opt1)            
            op2 = ''.join(opt2)
            op3 = ''.join(opt3)
            op4 = ''.join(opt4)
            res = jsonify({
                "fulfillmentText": Q1,
                "fulfillmentMessages": [
                    {
                        "text": {
                            "text": [
                                Q1,
                            ]
                        }
                    },
                    {
                        "text": {
                            "text": [
                                "The options are :",
                            ]
                        }
                    },
                    {
                        "text": {
                            "text": [
                                op1 + "; " + op2 + "; " + op3 + "; " + op4 + ";",
                            ]
                        }
                    }
                ],
                "payload": {
                    "google": {
                        "expectUserResponse": True,
                        "richResponse": {
                            "items": [
                                {
                                    "simpleResponse": {
                                        "textToSpeech": Q1
                                    }
                                },
                                {
                                    "simpleResponse": {
                                        "textToSpeech": "The options are, " + op1 + "; " + op2 + "; " + op3 + "; " + op4 + "."
                                    }
                                }

                            ],
                            "suggestions": [
                                {
                                    "title": op1
                                },
                                {
                                    "title": op2
                                },
                                {
                                    "title": op3
                                },
                                {
                                    "title": op4
                                }
                            ]
                        }
                    }
                }
            })
            return res

        # from 2 to 5 questions in quiz
        elif ans != "":
            print ( "my quiz name",app.secret_key)
            quiz = ''.join(app.secret_key)

            qu, options, answer = course.query(quiz)

            app.secret_ques = qu
            app.secret_ans = answer
            questions = app.secret_ques
            answers = app.secret_ans
            x = app.secret_key
            quiz = ''.join(x)
            ques , opts = course.query2(questions,options)
            print("ques--",ques)
            print("options--",opts)
            an = ans.title()
            an1 = ans.upper()
            an2 = ans.lower()
            an3 = ans.capitalize()
            reply, score = course.valid(ans, an, an1, an2, an3, answers)
            print("Score in main--",score)
            if type(ques) is not int:
                #str1 = ''.join(ques)
                str2 = ''.join(reply)
                str3 = str(score)

                Q1 = ''.join(ques)
                opt1 = opts[0]
                opt2 = opts[1]
                opt3 = opts[2]
                opt4 = opts[3]
                if (len(opt1) > 25):
                    opt1 = opt1[0:24]
                if (len(opt2) > 25):
                    opt2 = opt2[0:24]
                if (len(opt3) > 25):
                    opt3 = opt3[0:24]
                if (len(opt4) > 25):
                    opt4 = opt4[0:24]

                op1 = ''.join(opt1)
                op2 = ''.join(opt2)
                op3 = ''.join(opt3)
                op4 = ''.join(opt4)
                res = jsonify({
                    "fulfillmentText": Q1,
                    "fulfillmentMessages": [
                        {
                            "text": {
                                "text": [
                                    str2,
                                ]
                            }
                        },
                        {
                            "text": {
                                "text": [
                                    "Next question is --> " + "   " + Q1,
                                ]
                            }
                        },
                        {
                            "text": {
                                "text": [
                                    "The options are :",
                                ]
                            }
                        },
                        {
                            "text": {
                                "text": [
                                    op1 + "; " + op2 + "; " + op3 + "; " + op4,
                                ]
                            }
                        },
                        {
                            "text": {
                                "text": [
                                    "current score = " + str3,
                                ]
                            }
                        }
                    ],
                    "payload": {
                        "google": {
                            "expectUserResponse": True,
                            "richResponse": {
                                "items": [
                                    {
                                        "simpleResponse": {
                                            "textToSpeech": Q1
                                        }
                                    },
                                    {
                                        "simpleResponse": {
                                            "textToSpeech": "The options are, " + op1 + "; " + op2 + "; " + op3 + "; " + op4 + "."
                                        }
                                    }
                                ],
                                "suggestions": [
                                    {
                                        "title": op1
                                    },
                                    {
                                        "title": op2
                                    },
                                    {
                                        "title": op3
                                    },
                                    {
                                        "title": op4
                                    }
                                ]
                            }
                        }
                    }
                })
                return res
            else:

                # end quiz
                course.re_set()
                app.email = 0
                #app.secret_key = 0
                res = jsonify({
                    "fulfillmentText": "QUIZ ENDED. Your total score is {} out of 5. Do you want to change lesson or select subject?".format(score),
                    "fulfillmentMessages": [
                        {
                            "text": {
                                "text": [
                                    "QUIZ ENDED. Your total score is {} out of 5".format(score),
                                ]
                            }
                        },
                        {
                            "text": {
                                "text": [
                                    "Do you want to change lesson or select subject?",
                                ]
                            }
                        }
                    ],
                    "payload": {
                        "google": {
                            "expectUserResponse": True,
                            "richResponse": {
                                "items": [
                                    {
                                        "simpleResponse": {
                                            "textToSpeech": "QUIZ ENDED. Your total score is {} out of 5. Do you want to change lesson or select subject?".format(score),
                                        }
                                    }
                                ],
                                "suggestions": [
                                    {
                                        "title": "change_lesson"
                                    },
                                    {
                                        "title": "select_subject"
                                    }
                                ]
                            }
                        }
                    }
                })
            return res

        elif close is not None:
            course.re_set()


        # to decide about the next intent
        if (current_intent.endswith("Video") == 0):
            if current_intent.endswith("Keypoints"):
                next_intent = current_intent

            else:
                str_array = current_intent.split("_")
                if (len(str_array) == 5):
                    next_intent = str_array[0] + "_" + str_array[1] + "_" + str_array[2] + "_" + str_array[3] + "_" + str(int(str_array[4]) + 1)
                    print("next intent - ", next_intent)

        # Next lesson
        if current_reply == "Next_Lesson":
            str_array = current_intent.split("_")
            current_intent = str_array[0] + "_" + str_array[1] + "_" + str_array[2] + "_" + str(int(str_array[3]) + 1)
            bot_reply = {
                "followupEventInput": {
                    "name": current_intent,
                    "data": {
                        "user-answer": current_intent + "." + current_reply
                    }
                }
            }

        # fetch details about video link and AR link from DB. This table is added in moodle db
        if current_reply == "Watch_Video":
            str_array = current_intent.split("_")
            if(len(str_array) >= 4):
                current_lesson = str_array[0] + "_" + str_array[1] + "_" + str_array[2] + "_" + str_array[3]
                current_intent = str_array[0] + "_" + str_array[1] + "_" + str_array[2] + "_" + str_array[3] + "_Video"
            link,image = course.getvideo (current_lesson)

            res = jsonify({
                    "fulfillmentText": "Food is needed for all living organisms. Click here to watch the video",
                    "fulfillmentMessages": [
                        {
                        "platform": "ACTIONS_ON_GOOGLE",
                        "simpleResponses": {
                        "simpleResponses": [
                             {
                            "textToSpeech": "Food is needed for all living organisms. Click here to watch the video"
                            }
                            ]
                         }
                         },
                         {
                        "platform": "ACTIONS_ON_GOOGLE",
                        "basicCard": {
                            "title": "food",
                            "image": {
                            "imageUri": image,
                            "accessibilityText": "food"
                            },
                            "buttons": [
                            {
                            "title": "Click here to watch video",
                             "openUriAction": {
                            "uri": link
                             }
                                }
                            ]
                         }
                         },
                        {
                        "platform": "ACTIONS_ON_GOOGLE",
                        "suggestions": {
                        "suggestions": [
                            {
                            "title": "change_lesson"
                            },
                            {
                            "title": "select_subject"
                            },
                            {
                            "title": "start lesson"
                            }
                            ]
                        }
                        }]
                    })
            return res

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
                    str_array = current_intent.split("_")
                    current_intent = str_array[0] + "_" + str_array[1] + "_" + str_array[2] + "_" + str_array[3] + "_1"
            print(current_intent)
            bot_reply = {
                "followupEventInput": {
                    "name": current_intent,
                    "data": {
                        "user-answer": current_intent + "." + current_reply
                    }
                }
            }

        if current_reply == "repeat":
            bot_reply = {
                "followupEventInput": {
                    "name": current_intent,
                    "data": {
                        "user-answer": current_intent + "." + current_reply
                    }
                }
            }
            print(bot_reply)

        if current_reply == "next_topic":
            bot_reply = {
                "followupEventInput": {
                    "name": next_intent,
                    "data": {
                        "user-answer": next_intent + "." + current_reply
                    }
                }
            }
            print(bot_reply)

        if current_reply == "back_to_lesson":
            print("current-intent--", current_intent)
            str_array = current_intent.split("_")
            if (len(str_array) >= 4):
                current_intent = str_array[0] + "_" + str_array[1] + "_" + str_array[2] + "_" + str_array[3]
            bot_reply = {
                "followupEventInput": {
                    "name": current_intent
                }
            }
            print(bot_reply)

        if current_reply == "change_lesson" or current_reply == "select_lesson":
            print("current-intent--", current_intent)
            str_array = current_intent.split("_")
            current_intent = str_array[0] + "_" + str_array[1] + "_" + str_array[2]

            bot_reply = {
                "followupEventInput": {
                    "name": current_intent
                }
            }
            print(bot_reply)

        if current_reply == "Keypoints":
            str_array = current_intent.split("_")
            if (len(str_array) >= 4):
                current_intent = str_array[0] + "_" + str_array[1] + "_" + str_array[2] + "_" + str_array[3] + "_Keypoints"
            print("Keypoints--",current_intent)
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
    return res

if __name__ == '__main__':
    app.run()
