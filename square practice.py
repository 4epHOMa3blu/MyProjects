import time, random, math


print ('Here you can upgrade your exponention skill')

mode = int(input('\nChoose mode:\n1) Single exponention\n2) Multiple exponention\nYour choice: '))

if mode == 1:
	level = int(input('\nChoose your level:\n1) Starter\n2) Expert\nYour choice: '))
	if level == 1:
		print('\nEnter "0" if you want to finish')
		while True:
			number = random.randint(11, 99)
			print('\n'+str(number)+'²')
			print('Exponentiation guide:')
			print('1. Find the nearest 0-ending number and the difference between it and your number.')
			print ('2. Add/subtract the same difference in another direction (26<-28->30).')
			print('3. Multiply 2 received values (26*30).')
			print ('4. Add a square of the received difference to the result.')
			print('5. Answer the question.')
			answer = int(input('Answer: '))
			
			if answer == number**2:
				print('Correct!')
				time.sleep(0.5)
				continue
			if answer == 0:
				print ('Great progress! Try again and get better and better!')
				break
			else:
				print ('Mistake! Right answer is ', number**2)
				time.sleep(0.5)
				continue
		
	if level == 2:
			problem_count = 0
			mistake_count = 0
			print('\nEnter "0" if you want to finish')
			while True:
				number = random.randint(11, 99)
				print('\n'+str(number)+'²')
				start = time.time()
				answer = int(input('Answer: '))
			
				if answer == number**2:
					print('Correct!')
					print('Solved in %s sec' % round(time.time()-start, 2))
					problem_count += 1
					time.sleep(0.5)
					continue
				if answer == 0:
					print(mistake_count, 'mistake(-s) made')
					print(problem_count, 'problem(-s) solved')
					break
				else:
					print ('Mistake! Right answer is ', number**2)
					mistake_count += 1
					time.sleep(0.5)
					continue

else:
	while True:	
		bottom = int(input('\nFrom what number: '))
		top = int(input('To what number: '))
		nums = []
		mistake_count = 0

		for num in range(bottom, top+1):
			square = num**2
			print(str(num) + '² = ', square)
			nums.append(square)
			num += 1

		update_nums = random.shuffle(nums)
		nap = int(input('How much time do you need: '))
		time.sleep(nap)

		print('\n'*50, '\nLet\'s start!')
		while len(nums) != 0:
			question = int(math.sqrt(nums[0]))
			print('\nQuestion: ', str(question) + '²')
			answer = int(input('Answer: '))
			
			if answer == nums[0]:
				print('Correct!')
				del nums[0]
				time.sleep(0.4)
			else:
				print('Mistake!')
				mistake_count += 1
				nums.append(nums[0])
				del nums[0]
				time.sleep(0.4)
		print('You\'ve made %s mistake(-s)' % 		mistake_count, '\n')