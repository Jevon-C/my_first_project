#Simple program for generating the workout for the day 

import random

#List of machines that can be chosen from or simulated 
machine_list  = ['Barbell', 'Pulley & Cable' , 'Dumbell' , 'LAT Machine']

#Making the input code 
def accepting_muscle_group(): 
	prompt = 'Good Day Mr.Charles'
	prompt += '\nPlease enter your muscle group for tomorrow: '

	muscle_group = input(prompt)
	muscle_group = muscle_group.strip()
	print('------------------------------------------------------------------')
	return muscle_group

#Printing the exercise message 
def exercise_generator(exercise): 
	""" Generating the exercise """
	print("\nYour execrises today will target your: " + exercise.title()) 
	print("\nYour equipment of choice will be: ")
	print("\n - " + random.choice(machine_list)) #Choosing the exercise for the group 
	print("\n - " + random.choice(machine_list)) 
	print("\nEnjoy! ")

exercise_generator(accepting_muscle_group())

""" 
Expand to : 

- Record all the muscles that you've exercised for the week 
- make a list of all exercises for each exercise type and choose 
  randomly from those lists 

- store the output as a text file or pdf so that it can be saved
"""
