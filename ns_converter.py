while True:
    ns_from = int(input('Convert from what number system: '))
    if ns_from != 2 and ns_from != 8 and ns_from != 10 and ns_from != 16:
        print('Invalid values entered. Try again.\n')
        continue
    ns_to = int(input('Convert to what number system: '))
    if ns_to != 2 and ns_to != 8 and ns_to != 10 and ns_to != 16:
        print('Invalid values entered. Try again.\n')
        continue
    number = int(input('Your number: '))

    def converter(ns_from, ns_to, number):

        if ns_from == 10 and ns_to == 2:
            answer = str(bin(number))
            print(answer[2:], '\n')
        if ns_from == 10 and ns_to == 8:
            answer = str(oct(number))
            print(answer[2:], '\n')
        if ns_from == 10 and ns_to == 16:
            answer = str(hex(number))
            print(answer[2:], '\n')

        if ns_from == 2 and ns_to == 10:
            answer = int(str(number), 2)
            print(str(answer), '\n')
        if ns_from == 8 and ns_to == 10:
            answer = int(str(number), 8)
            print(str(answer), '\n')
        if ns_from == 16 and ns_to == 10:
            answer = int(str(number), 16)
            print(str(answer), '\n')

        if ns_from == 2 and ns_to == 8:
            preanswer = int(str(number), 2)
            answer = str(oct(preanswer))
            print(answer[2:], '\n')
        if ns_from == 2 and ns_to == 16:
            preanswer = int(str(number), 2)
            answer = str(hex(preanswer))
            print(answer[2:], '\n')

        if ns_from == 8 and ns_to == 2:
            preanswer = int(str(number), 8)
            answer = str(bin(preanswer))
            print(answer[2:], '\n')
        if ns_from == 8 and ns_to == 16:
            preanswer = int(str(number), 8)
            answer = str(hex(preanswer))
            print(answer[2:], '\n')

        if ns_from == 16 and ns_to == 2:
            preanswer = int(str(number), 16)
            answer = str(bin(preanswer))
            print(answer[2:], '\n')
        if ns_from == 16 and ns_to == 8:
            preanswer = int(str(number), 16)
            answer = str(oct(preanswer))
            print(answer[2:], '\n')

    converter(ns_from, ns_to, number)