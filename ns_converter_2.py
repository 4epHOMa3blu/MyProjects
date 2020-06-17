def get_data():
    global sys_from, sys_to, number
    sys_from = int(input('Convert from what number system: '))
    sys_to = int(input('Convert to what number system: '))
    number = input('Number: ')

def validate_systems(sys_from, sys_to):
    valid_systems = [2, 8, 10, 16]
    if sys_from and sys_to in valid_systems:
        return True
    else:
        return False

def validate_number(number):
    valid_symbols = '0123456789abcdef'
    if all([char in valid_symbols[:sys_from] for char in str(number)]):
        return True
    else:
        return False

def to_dec(sys_from, number):
    global in_dec
    in_dec = int(number, sys_from)
    return in_dec

def final_to(sys_to, in_dec):
    commands = {2:bin, 8:oct, 16:hex}
    command = commands.get(sys_to)
    answer = command(in_dec)
    print(f'Answer: {answer[2:]}\n')

def main():
    while True:
        get_data()
        if validate_systems(sys_from, sys_to) == False:
            print('Invalid system\'s base entered. Try again\n')
            continue
        if validate_number(number) == False:
            print('Invalid symbols entered. Try again\n')
            continue
        if sys_to == 10:
            print(f'Answer: {to_dec(sys_from, number)}\n')
            continue
        if sys_to != 10:
            to_dec(sys_from, number)
            final_to(sys_to, in_dec)
main()
