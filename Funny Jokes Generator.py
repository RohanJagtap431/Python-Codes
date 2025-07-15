#Funny jokes Generator 

import random
#sport category 
sports_english =[
      "Why did the batsman bring string to the match?\n👉 Because he wanted to tie the score!",
     
       "Umpire: “You’re out!”\nBatsman:\n“But I just came in!”\nUmpire: “Exactly.” 😆",
       
       "Why did the cricket team go to the bakery?\n👉 To get their “batter” ready!",
       
       
       "Why was the football stadium so hot?\n👉 Because all the fans left!",
       
       
       "Tennis coach: “Why do you keep hitting the ball into the crowd?”\nPlayer: “Because I want everyone to get involved!” 😂",
       
       "Why did the basketball player sit on the sideline and sketch pictures of chickens?\n👉 He was learning to draw fowls! (fouls) 😆",
       
       "Why did the boxer go to art school?\n👉 To learn how to draw! 🎨🥊",
       
       "What’s a boxer’s favorite part of a joke?\n👉 The punchline!",
       
       "Teacher: Virat, what's the capital of Australia?\nVirat: Sydney 100%! I’ve scored the most runs there! 😆",
       
       "Anchor: \"What’s your biggest weakness?\"\nVirat: “Sometimes... I run too fast between wickets. My partners get confused whether it’s a run or a workout!” 🏃‍♂️💨"
]

sports_marathi = [
      "Virat Kohli gym ला गेला…\nTrainer: \"आज काय करायचं?\"\nVirat: “Opposition ला heavy lifting करायला लावायचं!”",
      
      
      "विराट – \"मी क्रिकेटमध्ये इतका धडाडीचा खेळतो की बॉल मला पाहून स्वतःच आउट होतो!\"\nधोनी – \"हो ना! आणि कॅमेरे फक्त तुझ्यावरच फोकस करतात!\" 😄",
      
      "शिक्षक: गोल म्हणजे काय?\nविद्यार्थी: जो फुटबॉलमध्ये होतो आणि भारताच्या टीममध्ये फारसा होत नाही! 😆",
      
      "एक मुलगा - \"माझं हेल्मेट हरवलं.\"\nदुसरा - \"धोनीसारखं स्टाइलमध्ये मागे ठेवतोस ना, म्हणून गेलं!\" 😄",
      
      "मास्तर: कोणता खेळ श्वास रोखून खेळतात?\nविद्यार्थी: परीक्षेचा पेपर!\nमास्तर: मी कबड्डी विचारलं! 😅",
      
      "सचिन – मी क्रिकेटमध्ये इतकी सिक्स मारतो, की बॉल कंपन्या मला ‘ब्रँड अँबेसडर’ करतात!\nगाववाले – मग आमच्या खिडक्या का फोडतोस! 😆",
      
      "मुलगा: मी रोज बॅडमिंटन खेळतो!\nमैत्रीण: मग फिट दिसत का नाहीस?\nमुलगा: मी ड्रीम ११ मध्ये खेळतो! 🤣",
      
      "आई: अभ्यास करतोस का?\nमुलगा: मी स्पोर्ट्समन आहे आई!\nआई: बोर्डात 11 मार्क आले तर \"खेल खत्म\" 😆",
      
      "विराट – मी इतका फास्ट धावतो की… रन काढण्याआधी बॉल पिचवर येतो!\nधोनी – मग तुला फुल्पिचचा ‘कबड्डी’ खेळ वाटतो का? 😄",
      
      "मुलगा: आई, मला अभ्यासात काहीच लक्ष लागत नाही!\nआई: का रे?\nमुलगा: रोज फक्त बॅट आणि बॉल दिसतो डोळ्यांसमोर! 🙈",
      
]

#Education category 
Educations_english = [
      "Teacher: Why are you late?\nStudent: Because of the sign on the road.\nTeacher: What sign?\nStudent: \"School Ahead, Go Slow.\" 😄",
      
      
      "Teacher: Name a liquid that turns solid when heated.\nStudent: An egg!\nTeacher: ...Okay, you're not wrong. 😅",
      
      
      "Teacher: Why is your homework not done?\nStudent: I put it on silent mode last night. 📴",
      
      
      "Student: I studied everything… except what came in the exam. 😭",
      
      
      "Teacher: Who invented exams?\nStudent: The person who hated children the most! 😆",
      
      
      "Teacher: If you had 4 pencils and I took away 2, what would you have?\nStudent: A fight! 😤✏️",
      
      
      "Teacher: Are you sleeping in my class?\nStudent: No ma’am, I’m attending with my eyes closed! 😴💻",
      
      
      "Teacher: Why are you talking during my lecture?\nStudent: Because I don’t want to interrupt your silence! 😜",
      
      
      "Teacher: Why didn’t you do your homework?\nStudent: My dog ate it.\nTeacher: You don’t have a dog!\nStudent: I borrowed one just for this! 🐶",
      
      
      "Teacher: Spell “dog.”\nStudent: D-A-W-G\nTeacher: That’s wrong!\nStudent: Not in my neighborhood. 😎"
      
]

Educations_marathi = [
      "शिक्षक: वर्गात उशीर का झाला?\nविद्यार्थी: सर, झोपेत स्वप्नात अभ्यास करत होतो, त्यातून उठायलाच उशीर झाला! 😴📚",
      
      "विद्यार्थी: परीक्षा म्हणजे,\"तुम्ही शिकलेलं काहीच न येण्याची खात्री!\" 😅",
      
      "आई: तू किती वेळ अभ्यास करतोस?\nमुलगा: वेळ बघायचं असतं का आई? मी भावना देतो अभ्यासाला! 😄📖",
      
      "शिक्षक: हे तोंड का लपवलं?\nविद्यार्थी: ऑनलाईन क्लास आहे ना सर, कॅमेरा ऑफ केला! 🎥🚫",
      
      "शिक्षक: तू अभ्यास केला नाहीस तर भविष्य अंधारात जाईल!\nविद्यार्थी: मग लाइट लावून अभ्यास करतो! 💡😂",
      
      "शिक्षक: प्रोजेक्ट कुठे आहे?\nविद्यार्थी: त्याला मी सुट्टी दिली! तो उद्या येईल! 🤭",
      
      "शिक्षक: Translate – \"माझं पेन तुटलं.\"\nविद्यार्थी: My pen is broke up with me! 💔✍️",
      
      "मित्र: अभ्यास करतोस का?\nदुसरा: अभ्यास फक्त त्यालाच शोभतो ज्याला शिकायचं असतं… आणि मला सुट्टी हवीय! 😎",
      
      "शिक्षक: ७ चा पाढा म्हण!\nविद्यार्थी: ७-१-७, ७-२-14, ७-३-मम्मी!! 🙈", 
      
      "शिक्षक: एवढं सोपं प्रश्न होतं, तरी चुकीचं उत्तर?\nविद्यार्थी: सर, मी बुद्धीने नाही… दिलाने उत्तर दिलं! ❤️🧠"
      
      
]

#randoms jokes
Randoms = [
      "तो: माझं तुझ्यावर जीवापाड प्रेम आहे!\nती: किती?\nतो: एवढं की माझं हृदय तुझ्या नावावर “लोन” घेतंय! 💘🏦",
      
      "मुलगी: तू लग्न का करतोस?\nमुलगा: मोबाईल अपडेट करता करता... विचार केला, आयुष्याचं पण अपडेट करून टाकावं! 😂📱👰",
      
      "पत्नीनं: माझं डोकं खूप दुखतंय!\nनवऱ्याने: मग थोडावेळ बोलू नकोस… बघ पटकन बरं वाटेल! 😅",
      
      "डॉक्टर: तुझं वजन वाढतंय!\nपेशंट: मी विचारांचं खूप खातो! 🤔🍛",
      
      "शिक्षक: बोर्डकडे बघ आणि उत्तर दे!\nविद्यार्थी: बोर्ड mute वर आहे सर, आवाज नाही येत! 📺🔇",
      
      "मुलगा: मी online गाढव मागवलं होतं,\nमित्र: मग आलं का?\nमुलगा: हो, पण त्यानं तुझा पत्ता दिला! 🤣🫏",
      
      "ती: मी तुझी नाही झालो, तर काय करशील?\nतो: मग \"जळून\" टाकीन तुला... आपल्या आठवणींमध्ये! 🔥💔",
      
      "बायको: स्वप्नात मला काय म्हणालास?\nनवरा: मी फक्त स्वप्नातच बोलतो का? 🤐",
      
      "मित्र: तू इतका वेळ फेसबुकवर काय करतोस?\nदुसरा: लोकांचे फोटो बघतो आणि मनातल्या मनात टीका करतो! 😎📸", 
      
      "पोरं भांडत होती: कोण हिरो आहे?\nएकानं उत्तर दिलं: जो आई-बाबा समोर मोबाईलवर गेम खेळतो… तोच खरा हिरो! 😄🎮"
      
      
]


print("☆ ☆ ☆ 🤪 Funny jokes All Categories 🤪 ☆ ☆ ☆")
print("1.Sport Jokes In English")
print("2.Sports Jokes In Marathi")
print("3.Education Jokes In English")
print("4.Education Jokes In Marathi")
print("5.Random Jokes ")
print("6.Joke Save")
print("7.Exit")

while True :
      user_input = input("\n● Choice Here : ").strip().lower()
      
    #sport categorys
      sport_english= random.choice(sports_english)
      sport_marathi= random.choice(sports_marathi)
      
      
      #education category 
      education_english = random.choice(Educations_english)
      education_marathi = random.choice(Educations_marathi)
      
      #random
      randoms = random.choice(Randoms)
      
      
      
      
      if user_input == "1":
        
        last_joke = f"》《》《FUNNY JOKES》《》《\n{sport_english}"
        
        print("\n"+ last_joke)
        
      elif user_input =="2":
        last_joke = f"》《》《FUNNY JOKES》《》《\n{sport_marathi}"
        
        print("\n"+ last_joke)
        
        
      elif user_input == "3":
          last_joke = f"》《》《FUNNY JOKES》《》《\n{education_english}"
        
          print("\n"+ last_joke)
          
      elif user_input == "4":
          last_joke = f"》《》《FUNNY JOKES》《》《\n{education_marathi}"
        
          print("\n"+ last_joke)
          
      elif user_input == "5":
          last_joke = f"》《》《FUNNY JOKES》《》《\n{randoms}"
        
          print("\n"+ last_joke)
          
          
      elif user_input == '6':
        filename = input("File ka naam likho (example: output.txt): ")
        with open(filename, 'w',encoding ='utf-8') as file:
            file.write(last_joke)
        print(f"Output '{filename}' file mein save hua.")
        

      elif user_input == "7":
           print("\n Thanks For Using The Funny jokes Generator. Have A Fun Day")
           break
        
        
        
      else :
        print("Invalid Choice")