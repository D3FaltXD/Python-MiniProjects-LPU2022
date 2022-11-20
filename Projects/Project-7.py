# Story Generator

import random


names = [' Aditya',' Harshit',' Ajay',' Ishaan',' Virat',' Anil',' Sahil',' Nikhil',' Iswar','Aman','Krishna','Mohit','Pranav','Shaurya']

places =[' Mumbai',' Kolkata',' Bhagyanagar',' Vijaywada',' Indore',' Patna',' Ranchi',' Kochi',' Jalandhar',' Delhi',' Ludhiana',' Banglore', ]

body = [' went a grand building and took a photograph',' met very famous celebrity ',' went to the most beautiful spot where he wanted to visit eagerly ',' Collected stamps & old currencies',' learnt their tradition dance',' celebrated New Year',' tasted their local foods']

roles = ['a college student','a youtuber',' a vlogger','a school student','a normie guy','a retired army officer','a professer',' a LPU verto',' a adventurous guy']

weather = [' a very hot and humid day',' a cloudy day',' a rainy day',' a cold night',' a sunny day']

word = ['Once upon a time','A long time ago','In earlier times','On 20Th January']

saying = [' whose name was ',' named ',' known as ']

whom = [' to his family.',' to his friends.',' to his classmates.', ' to his mother.',' to his father.',' to his grandparents.']

next= ['5 days later','2 days later','3 days later','After 5 days']

gone= [',after office he did not returned to his home',',after his work he did not returned to his quater',' ,he got suddenly disappeared on the way between of his home & office','after going for shopping he did not came his home again']

scene=['.All his family members started searching him','.His father did a police complaint ','.His friends started bothering about him']

then=[' he somehow did a call to his family',' his father received a call from him',' he did a call to his friend rohit']

know = [' they all went to his stated location',' they reached that location told by him']

after = [' he talked about mishappened occur with him',' he explained all that incident',' he described what happenend to him']

insane = [' he told that one of his friend baited him in the name of party',' he described that how his friend has said that " let us have a party tonight',' he told whole story to his family memebers that his friend alok offered him to join tonight party']

plot = [' but his friend was involved on drug peddling',' but his friend wss a drug supplier']

cheated = [' , his friend cheated him and mixed drug pills in his softdrink ',' , his friend suspiciously gave him drug pills by mixing in his drink',' ,his friend forced him consume harddrinks heavily']

addiction = [' to make him get addicted of it',' so that he will get addicted to it and would spend more money on it']

profit = [' .For his own profit he betrayed his own childhood friend',' .Greedy for money he cheated his own bestfriend','.For reaching his sales target from his supplier he betrayed his own friend']

case = [' .This whole scenario was stated to the higher officials ',' .This whole scenario was stated to the police officers'] 

accused = [' and they consolidated the victim that accused would not be spared', 'and they sentenced the victim that culprit would not be exempted']

news = [' .This whole news was covered on television', ' .This whole news was covered in newspaper headlines' ]

solve = [' .Later This case was solved with the help of special cops']

end = [' .From this unabridged story we can retrain that after some virtuous experiences one can also face a miserable stage ']

learnings = [' ,In addition from this narrative we can assimilate that we should never blind-trust and sometimes acquire a skeptic approach.']

randomname = random.choice(names)
randomplace = random.choice(places)
randombody = random.choice(body)
randomrole = random.choice(roles)
randomweather = random.choice(weather)
randomword = random.choice(word)
randomsaying = random.choice(saying)
randomwhom = random.choice(whom)
randomnext = random.choice(next)
randomgone = random.choice(gone)
randomscene = random.choice(scene)
randomthen = random.choice(then)
randomknow = random.choice(know)
randomafter = random.choice(after)
randomplot = random.choice(plot)
randomcheated = random.choice(cheated)
randomprofit= random.choice(profit)
randomcase= random.choice(case)
randomaccused= random.choice(accused)
randomnews= random.choice(news)
randomsolve= random.choice(solve)
randomend= random.choice(end)
randomlearnings= random.choice(learnings)

story = randomword + randomrole + randomsaying + randomname +' travelled a beautiful city called' +randomplace +' where it was' + randomweather + ' and in this place'  +' he' + randombody + ' after that he shared his experiences' + randomwhom + randomnext + randomgone +randomscene+randomthen + randomknow + randomafter + randomplot + randomcheated + randomprofit + randomcase + randomaccused + randomnews + randomsolve + randomend + randomlearnings
print(story)