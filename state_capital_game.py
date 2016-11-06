print('Greetings!!\n Welcome to the state and capital game\n lets see how well you know the States in Nigeria and their capital!!')
statesAndCapitals = {
'Abuja': 'Abuja', 
'Abia' : 'Umuahia', 
'Adamawa' : 'Yola', 
'Akwa ibom' : 'Uyo', 
'Anambra' : 'Awka', 
'Bauchi' : 'Bauchi', 
'Bayelsa' : 'Yenagoa', 
'Benue' : 'Makurdi', 
'Borno' : 'Maiduguri', 
'Cross River' :'Calaber', 
'Delta' : 'Asaba', 
'Ebonyi' : 'Abakaliki', 
'Edo' : 'Benin', 
'Ekiti' : 'Ado-ekiti', 
'Enugu' : 'Enugu', 
'Gombe' : 'Gombe', 
'Imo' : 'Owerri', 
'Jigawa' : 'Dutse', 
'Kaduna' :'Kaduna',
'Katsina' :'Katsina', 
'Kebbi' : 'Birnin-kebbi', 
'Kogi' :'Lokoja', 
'Kwara' : 'Ilorin', 
'Lagos' : 'Ikeja', 
'Nassarawa' : 'Lafia', 
'Niger' : 'Minna', 
'Ogun' : 'Abeokuta', 
'Ondo' : 'Akure', 
'Osun' : 'Oshogbo', 
'Plateau' : 'Jos', 
'Rivers' : 'Portharcourt', 
'Sokoto' : 'Sokoto', 
'Taraba' :'Jalingo', 
'Yobe' : 'Damaturu', 
'Zamfara' : 'Gusau'}

import random

states = list(statesAndCapitals.keys())
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
  state = random.choice(states)
  capital = statesAndCapitals[state]
  #count_correct_guess = 0
  question = input('What is the capital of ' + state + ' ? > ' )
  print('')
  if question == capital:
    print('Thats correct!')
  #count_correct_guess = count_correct_guess + 1
  else:
    print('Thats incorrect\n the capital of  ' + state + ' is ' + capital +  '\n better up next time!!')
    #print('You got ' + str(count_correct_guess) + ' question(s), out of ten questions right')
#print('You got ' + int(count_correct_guess) + ' question(s), out of ten questions right')
print('Well done!! Game over')








