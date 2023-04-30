#import requests to get the API's used
import requests
import json


#ask user how many different facts they would like
user_input = int(input('How many dog facts would you like, pick a number between 1-5.'))


#grab the amount of infromation the user wants from the website
response = requests.get(f'http://dog-api.kinduff.com/api/facts?number={user_input}')


#iterate for however many facts the user wants
for data in range(0, user_input):
#print out a fact
   print(response.json()['facts'][user_input-5])
#add 1 to the user_input so that the next fact is different from the one before it
   user_input += 1