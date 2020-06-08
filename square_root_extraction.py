import math, random, time

print('Here you can upgrade your square root extraction skill')
print('\nPrinciples:',
      '\n• number can\'t end with 2/3/7/8\n'
      '• 3-char numbers 10-31\n'
      '• 4-char numbers 32-99\n'
      '• if ends with 1 -> 1/9\n'
      '• if ends with 4 -> 2/8\n'
      '• if ends with 5 -> 5\n'
      '• if ends with 6 -> 4/6\n'
      '• if ends with 9 -> 3/7\n')
level = int(input('Choose your level:\n1) Starter\n2) Expert\nYour choice: '))
if level == 1:
    print('Enter "0" if you want to finish')
    while True:
        number = (random.randint(11, 99)) ** 2
        if len(str(number)) == 3:
            print(f'\n{number}')
            print('1. 3-char number -> 11≤x≤31')
            print('2. Is the result in interval between 100 and 400 (10-20) or 441 and 961 (21-31)?')
            print('3. Check the last character of the number and find possible endings using principles.')
            print('4. Is the result more or less than square of a 5-ending number in your interval?')
            print('5. Answer the question.')

            answer = int(input('Answer: '))
            if answer == math.sqrt(number):
                print('Correct!')
                time.sleep(0.5)
                continue
            if answer == 0:
                print('Great progress! Try again and get better and better!')
                break
            else:
                print('Mistake! Right answer is ', int(math.sqrt(number)))
                time.sleep(0.5)
                continue
        else:
            print(f'\n{number}')
            print('1. 4-char number -> 32≤x≤99')
            print('2. Between which 2 decades answer is situated? Check first 2 characters and find the nearest smaller square (63.. -> 49 -> 7..)')
            print('3. Check the last character of the number and find possible endings using principles.')
            print('4. Is the result more or less than the square of a 5-ending number in your interval?')
            print('5. Answer the question.')

            answer = int(input('Answer: '))
            if answer == math.sqrt(number):
                print('Correct!')
                time.sleep(0.5)
                continue
            if answer == 0:
                print('Great progress! Try again and get better and better!')
                break
            else:
                print('Mistake! Right answer is ', int(math.sqrt(number)))
                time.sleep(0.5)
                continue
elif level == 2:
    problem_count = 0
    mistake_count = 0
    print('Enter "0" if you want to finish')
    while True:
        number = (random.randint(11, 99)) ** 2
        print(f'\n{number}')
        start = time.time()
        answer = int(input('Answer: '))

        if answer == 0:
            print(mistake_count, 'mistake(-s) made')
            print(problem_count, 'problem(-s) solved')
            break

        elif answer == math.sqrt(number):
            problem_count += 1
            print('Correct!')
            solv_time = round(time.time() - start, 2)
            print(f'Solved in {solv_time} sec')
            time.sleep(0.5)
            continue

        else:
            mistake_count += 1
            print('Mistake! Right answer is ', int(math.sqrt(number)))
            solv_time = round(time.time() - start, 2)
            print(f'Solved in {solv_time} sec')
            time.sleep(0.5)
            continue

else:
    print('Error! Try again')
