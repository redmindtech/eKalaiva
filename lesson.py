import mysql.connector
import mysql.connector as mysql
from flask import Flask, session, redirect, url_for, request
# from flask import Flask
# import tn_db_connection
import json
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

def getlesson(grade):
    print("grade--", grade)
    if(grade == "6_Science_Lesson"):
        res = jsonify({
            "fulfillmentText": "Welcome to the world of Science. Which lesson you would like to select. 1. Food where does it come.. 2. Components of food.. 3. Fibre to Fabric.. 4. Sorting materials group.. 5. Separation of Substances.. 6. Changes around us.. 7. Getting to know plants.. 8. Body Movements.. 9. Living Organisms.. 10. Motion,  measurement.. 11. Light, Shadow, Reflection.. 12. Electricity and Circuits.. 13. Fun with Magnets.. 14. Water.. 15. air around us.. 16. Garbage in, Garbage out..",
            "fulfillmentMessages": [
                {
                    "text": {
                        "text": [
                            "Welcome to the world of Science. Which lesson you would like to select. 1. Food where does it come.. 2. Components of food.. 3. Fibre to Fabric.. 4. Sorting materials group.. 5. Separation of Substances.. 6. Changes around us.. 7. Getting to know plants.. 8. Body Movements.. 9. Living Organisms.. 10. Motion,  measurement.. 11. Light, Shadow, Reflection.. 12. Electricity and Circuits.. 13. Fun with Magnets.. 14. Water.. 15. air around us.. 16. Garbage in, Garbage out..",
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
                                    "textToSpeech": "Welcome to the world of Science. Which lesson you would like to select. 1. Food where does it come.. 2. Components of food.. 3. Fibre to Fabric.. 4. Sorting materials group.. 5. Separation of Substances.. 6. Changes around us.. 7. Getting to know plants.. 8. Body Movements.. 9. Living Organisms.. 10. Motion,  measurement.. 11. Light, Shadow, Reflection.. 12. Electricity and Circuits.. 13. Fun with Magnets.. 14. Water.. 15. air around us.. 16. Garbage in, Garbage out.."
                                }
                            }
                        ]
                        ,
                        "suggestions": [
                    {
                      "title": "Food where does it come"
                    },
                    {
                      "title": "Components of food"
                    },
                    {
                      "title": "Fibre to Fabric"
                    },
                    {
                      "title": "Sorting materials group"
                    },
                    {
                      "title": "Separation of Substances"
                    },
                    {
                      "title": "Changes around us"
                    },
                    {
                      "title": "Getting to know plants"
                    },
                    {
                      "title": "Body Movements"
                    },
                    {
                      "title": "Living Organisms"
                    },
                    {
                      "title": "Motion, measurement"
                    },
                    {
                      "title": "Light, Shadow, Reflection"
                    },
                    {
                      "title": "Electricity and Circuits"
                    },
                    {
                      "title": "Fun with Magnets"
                    },
                    {
                      "title": "Water"
                    },
                    {
                      "title": "air around us"
                    },
                    {
                      "title": "Garbage in, Garbage out"
                    },
                    {
                      "title": "Select Subject"
                    }
                  ]
                    }
                }
            }
        })

    if (grade == "6_Social_Lesson"):
        res = jsonify({
                "fulfillmentText": "Hi, Greetings! Ready to learn Social lessons. Select the lessons to start with,. 1. What, Where, How, When.. 2. Hunt, gather, grow food.. 3. In the earlist cities.. 4. What books, burials tell.. 5. Kingdoms, early republic.. 6. New questions and ideas.. 7. Ashoka, gave up War.. 8. Vital villages, towns.. 9. Trader, King, Pilgrim.. 10. New empires and Kingdoms..",
                "fulfillmentMessages": [
                    {
                        "text": {
                            "text": [
                                "Hi, Greetings! Ready to learn Social lessons. Select the lessons to start with,. 1. What, Where, How, When.. 2. Hunt, gather, grow food.. 3. In the earlist cities.. 4. What books, burials tell.. 5. Kingdoms, early republic.. 6. New questions and ideas.. 7. Ashoka, gave up War.. 8. Vital villages, towns.. 9. Trader, King, Pilgrim.. 10. New empires and Kingdoms..",
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
                                        "textToSpeech": "Hi, Greetings! Ready to learn Social lessons. Select the lessons to start with,. 1. What, Where, How, When.. 2. Hunt, gather, grow food.. 3. In the earlist cities.. 4. What books, burials tell.. 5. Kingdoms, early republic.. 6. New questions and ideas.. 7. Ashoka, gave up War.. 8. Vital villages, towns.. 9. Trader, King, Pilgrim.. 10. New empires and Kingdoms.."
                                    }
                                }
                            ]
                            ,
                            "suggestions": [
                            {
                              "title": "What, Where, How, When"
                            },
                            {
                              "title": "Hunt, gather, grow food"
                            },
                            {
                              "title": "In the earlist cities"
                            },
                            {
                              "title": "What books, burials tell"
                            },
                            {
                              "title": "Kingdoms, early republic"
                            },
                            {
                              "title": "New questions and ideas"
                            },
                            {
                              "title": "Ashoka, gave up War"
                            },
                            {
                              "title": "Vital villages, towns"
                            },
                            {
                              "title": "Trader, King, Pilgrim"
                            },
                            {
                              "title": "New empires and Kingdoms"
                            },
                            {
                              "title": "Select Subject"
                            }
                          ]
                        }
                    }
                }
            })

    if (grade == "6_English_Lesson"):
        res = jsonify({
                "fulfillmentText": "Hi, I know you all love to learn English stories and Poems. Select the lessons to start with., 1. Patrick's Homework.. 2. How Dog Found New Master.. 3. Taro's Reward.. 4. Indo-American Space Woman.. 5. A Different School.. 6. Who I Am.. 7. Fair Play.. 8. A Game of Chance.. 9. Desert Animal.. 10. The Banyan Tree.. 11. A HOUSE A HOME.. 12. THE KITE.. 13. THE QUARREL.. 14. Beauty.. 15. Where do the teachers go.. 16. The Wonderful words.. 17. Vocation.. 18. What if",
                "fulfillmentMessages": [
                    {
                        "text": {
                            "text": [
                                "Hi, I know you all love to learn English stories and Poems. Select the lessons to start with., 1. Patrick's Homework.. 2. How Dog Found New Master.. 3. Taro's Reward.. 4. Indo-American Space Woman.. 5. A Different School.. 6. Who I Am.. 7. Fair Play.. 8. A Game of Chance.. 9. Desert Animal.. 10. The Banyan Tree.. 11. A HOUSE A HOME.. 12. THE KITE.. 13. THE QUARREL.. 14. Beauty.. 15. Where do the teachers go.. 16. The Wonderful words.. 17. Vocation.. 18. What if",
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
                                        "textToSpeech": "Hi, I know you all love to learn English stories and Poems. Select the lessons to start with., 1. Patrick's Homework.. 2. How Dog Found New Master.. 3. Taro's Reward.. 4. Indo-American Space Woman.. 5. A Different School.. 6. Who I Am.. 7. Fair Play.. 8. A Game of Chance.. 9. Desert Animal.. 10. The Banyan Tree.. 11. A HOUSE A HOME.. 12. THE KITE.. 13. THE QUARREL.. 14. Beauty.. 15. Where do the teachers go.. 16. The Wonderful words.. 17. Vocation.. 18. What if"
                                    }
                                }
                            ]
                            ,
                            "suggestions": [
                            {
                              "title": "Patrick's Homework"
                            },
                            {
                              "title": "How Dog Found New Master"
                            },
                            {
                              "title": "Taro's Reward"
                            },
                            {
                              "title": "Indo-American Space Woman"
                            },
                            {
                              "title": "A Different School"
                            },
                            {
                              "title": "Who I Am"
                            },
                            {
                              "title": "Fair Play"
                            },
                            {
                              "title": "A Game of Chance"
                            },
                            {
                              "title": "Desert Animal"
                            },
                            {
                              "title": "The Banyan Tree"
                            },
                            {
                              "title": "A HOUSE A HOME"
                            },
                            {
                              "title": "THE KITE"
                            },
                            {
                              "title": "THE QUARREL"
                            },
                            {
                              "title": "BEAUTY"
                            },
                            {
                              "title": "Where do the teachers go"
                            },
                            {
                              "title": "The Wonderful Words"
                            },
                            {
                              "title": "Vocation"
                            },
                            {
                              "title": "What If"
                            },
                            {
                              "title": "Select Subject"
                            }
                          ]
                        }
                    }
                }
            })

    if (grade == "6_Civics_Lesson"):
        res = jsonify({
                "fulfillmentText": "Hi, Greetings! Ready to learn Civics lessons. Select the lessons to start with,. 1. Understanding diversity.. 2. Diversity and discrimination.. 3. What is Government.. 4. Key elements of a democratic Government.. 5. Panchayat Raj.. 6. Rural administration.. 7. Urban Administration.. 8. Rural Livelihoods.. 9. Urban Livelihoods",
                "fulfillmentMessages": [
                    {
                        "text": {
                            "text": [
                                "Hi, Greetings! Ready to learn Civics lessons. Select the lessons to start with,. 1. Understanding diversity.. 2. Diversity and discrimination.. 3. What is Government.. 4. Key elements of a democratic Government.. 5. Panchayat Raj.. 6. Rural administration.. 7. Urban Administration.. 8. Rural Livelihoods.. 9. Urban Livelihoods",
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
                                        "textToSpeech": "Hi, Greetings! Ready to learn Civics lessons. Select the lessons to start with,. 1. Understanding diversity.. 2. Diversity and discrimination.. 3. What is Government.. 4. Key elements of a democratic Government.. 5. Panchayat Raj.. 6. Rural administration.. 7. Urban Administration.. 8. Rural Livelihoods.. 9. Urban Livelihoods"
                                    }
                                }
                            ]
                            ,
                            "suggestions": [
                            {
                              "title": "Understanding diversity"
                            },
                            {
                              "title": "Diversity, discrimination"
                            },
                            {
                              "title": "What is Government"
                            },
                            {
                              "title": "Key element of Government"
                            },
                            {
                              "title": "Panchayat Raj"
                            },
                            {
                              "title": "Rural administration"
                            },
                            {
                              "title": "Urban Administration"
                            },
                            {
                              "title": "Rural Livelihoods"
                            },
                            {
                              "title": "Urban Livelihoods"
                            },
                            {
                              "title": "Select Subject"
                            }
                          ]
                        }
                    }
                }
            })

    if (grade == "6_Geography_Lesson"):
         res = jsonify({
                "fulfillmentText": "Hi, Greetings! Ready to learn Geography lessons. Select the lessons to start with,. 1. Earth in Solar system.. 2. Latitudes and Longitudes.. 3. Motions of Earth.. 4. Maps.. 5. Major domains of Earth.. 6. Major Landforms of Earth.. 7. Our country, India.. 8. India, Climate, WildLife",
                "fulfillmentMessages": [
                    {
                        "text": {
                            "text": [
                                "Hi, Greetings! Ready to learn Geography lessons. Select the lessons to start with,. 1. Earth in Solar system.. 2. Latitudes and Longitudes.. 3. Motions of Earth.. 4. Maps.. 5. Major domains of Earth.. 6. Major Landforms of Earth.. 7. Our country, India.. 8. India, Climate, WildLife",
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
                                        "textToSpeech": "Hi, Greetings! Ready to learn Geography lessons. Select the lessons to start with,. 1. Earth in Solar system.. 2. Latitudes and Longitudes.. 3. Motions of Earth.. 4. Maps.. 5. Major domains of Earth.. 6. Major Landforms of Earth.. 7. Our country, India.. 8. India, Climate, WildLife"
                                    }
                                }
                            ]
                            ,
                            "suggestions": [
                                {
                                    "title": "Earth in Solar system"
                                },
                                {
                                    "title": "Latitudes and Longitudes"
                                },
                                {
                                    "title": "Motions of Earth"
                                },
                                {
                                    "title": "Maps"
                                },
                                {
                                    "title": "Major domains of Earth"
                                },
                                {
                                    "title": "Major landforms of earth"
                                },
                                {
                                    "title": "Our Country, India"
                                },
                                {
                                    "title": "India, Climate, WildLife"
                                },
                                {
                                    "title": "Select Subject"
                                }
                            ]
                        }
                    }
                }
            })

    return res

if __name__ == "__main__":
    main()
