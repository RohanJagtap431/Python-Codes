#Fake News Headline Generator

import random

subjects = [
      "Shahrukh khan",
      "Vorat kohali",
      "Niramala sitharama",
      "A Mumbai Cat",
      "A Group of Monkeys",
      "Prime Minister Modi",
      "Auto Rickshaw Driver from Delhi"
]


actions =[
      "launches",
      "cancels",
      "dances with",
      "eats",
      "declares war on",
      "orders",
      "celebrates"
]


places_or_things = [
      "at red fort",
      "in mumbai local train",
      "a plate of samosa",
      "inside parliament",
      "at ganga ghat",
      "during IPL match",
      "at india gate"
]

#start the head line generation loop
while True :
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)
    
    headline = f"BRAKING NEWS : {subject} {action} {place_or_thing}"
    
    
    print("\n"+ headline)
    
    user_input = input("\n Do you want another headline ? (yes/no)").strip().lower()
    
    if user_input == "yes":
        continue 
        
    else :
        print("\n Thanks For Using The Fake News Headline Generator. Have A Fun Day")
        break
    