import random


print('\t\t ****Coin Tossing Game****\n\t\t\tBy Mark Mourice\n') 


print('For Head enter H, for Tail enter T. There you go...')

def play_game():
	
	attempts=6
	entry=[]
	correct_answer=[]
	
	while attempts:
		choices=['H','T']
		correct_count=0
		total=6
		answer=random.choice(choices)
		guess=input('Enter your guess: ')
		attempts -=1
		entry.append(guess.upper())
		correct_answer.append(answer)
		if len(guess)>1:
			print('Please enter only one letter')
		elif not guess.isalpha():
			print('Please enter a letter')
		elif guess=='':
			print('Please enter a letter')
		elif guess.upper() !=answer:
			print(f'Nope it was a {answer} and you entered a {guess.upper()}')
		else:
			print('Congrats! You got it!')
	
			
		for i,j in zip(entry,correct_answer):
			if i==j:
				correct_count  +=1
				
	print('\n')
	print(f'You entered: {entry}')
	print(f'The correct entries were: {correct_answer}')
	print('Your final results are as follows: ')
	print(f'{correct_count} out of {total} ({(correct_count/total)*100}%).')
	play_again=input('Wish to play again?(Y/N)')
	if play_again.upper()=='Y':
		play_game()
	elif play_again.upper()=='N':
		print('Goodbye, hope you enjoyed the game!')
		quit
play_game()
			
