import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}


preferences = {}
drink = []

def customer_preferences(questions):
    for key in questions:
        while True:
            output = raw_input(questions[key]+"Y/N:").lower()
            if output == 'y':
                preferences[key] = 'True'
                break
            elif output == 'n':
                preferences[key] = 'False'
                break
    return preferences
        
def  customer_receipe(preferences):
    for key in preferences:
        if preferences[key] == 'True':
            drink.append(ingredients[key])
    print ("Hey {}:".format(customer_receipe.__name__))
    print (random.choice(drink))
    
            
            
'''
Multiple customers: The bartender could ask for the customer's name before they are served. 
They could then remember the customer's preferences for when the same customer asks for another drink.
'''

if __name__ == '__main__':
    customer_preferences(questions)
    customer_receipe(preferences)
    while True:
        acceptance = raw_input("do you want another drink YES/NO:").lower()
        if acceptance == 'yes':
            while True:
                receipe = raw_input("do you want to try different receipe YES/NO:").lower()
                if receipe == 'yes':
                    customer_preferences(questions)
                    customer_receipe(preferences)
                elif receipe == 'no':
                    customer_receipe(preferences)
                    break
        elif acceptance == 'no':
            break
