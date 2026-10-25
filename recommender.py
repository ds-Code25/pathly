from data.rules import RULES

def gen_recommendations(interests):

    #variables (The different categories of suggestions)
    courses = []
    projects = []
    careers = []

    #goes through all the interests the user selectes
    for i in interests:

        #if the dictionary has the interest chosen
        if i in RULES:

            courses += RULES[i]["courses"]
            projects += RULES[i]["projects"]
            careers += RULES[i]["careers"]

    return courses, projects, careers

def get_available_interests():
    return list(RULES.keys())
