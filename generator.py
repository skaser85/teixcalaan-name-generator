import random
import math
import sys

FIRST_20 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', \
            'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
TENS = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

def print_help(error: str = 'Invalid usage') -> None:
    help_text = f'''
        Error: {error}

        Example Usage: teixcalaan -amount 10 -number 38 -noun poppy

        -amount -> integer: (optional)
                    - the number of random names to return
        -number -> integer/string (1 to 99): (optional) 
                    - a specific number to use in the name(s)
                    - acceptable formats: 38, thirty-eight (capitalization doesn't matter, but spelling does)
                    - if passing in a number, such as 38, in words (i.e., thirty-eight), a dash is the only acceptable separator
        -noun   -> string: (optional)
                    - a specific noun to use in the name(s)
                    - doesn't necessarily need to be a noun, could be any word
                    - will also will accept up to 3 total words (e.g., "poppy", or "north american poppy")
    '''
    print(help_text)

def main() -> None:
    # print(sys.argv)
    amount = 1
    number = 0
    noun = ''
    args = sys.argv[1:]
    if len(args) == 0:
        print(generate_name())
        return
    if args[0].lower() in ['-help', 'help', '-h', 'h']:
        print_help('Help')
        return
    if args[0] == '-amount':
        if args[1].isdigit():
            amount = int(args[1])
        else:
            print_help(f'Invalid amount argument: "{args[1]}"')
            return
        if len(args) > 2:
            args = args[2:]
    if len(args) > 0 and args[0] == '-number':
        number = args[1]
        if number.isdigit():
            number = int(number)
        elif '-' in number:
            first, second = number.split('-')
            ten = str(TENS.index(first.lower()))
            digit = str(FIRST_20.index(second.lower()))
            number = int(f'{ten}{digit}')
        elif number.lower() in TENS:
            number = str(TENS.index(number.lower())) + "0"
        elif number.lower() in FIRST_20:
            number = str(FIRST_20.index(number.lower()))
        else:
            print_help(f'Invalid number format: "{number}"')
            return
        if number < 1 or number > 99:
            print_help(f'Number not within acceptable range: {number}')
            return
        if len(args) > 2:
            args = args[2:]
    if len(args) > 0 and args[0] == '-noun':
        if len(args[1:]) > 3:
            print_help(f'Only 3 words are allowed after the "noun" argument: "{args[1:]}"')
            return
        noun = ' '.join(args[1:])
    for _ in range(amount):
        print(generate_name(noun, number))

def get_noun(noun: str = '') -> str:
    if len(noun) > 0:
        return noun
    with open(r'C:\Users\Steve\Projects\teixcalaan\nouns.txt', 'r') as f:
        nouns = [n.strip() for n in f.readlines()]
        return random.choice(nouns)

def get_random_number() -> int:
    # get a rondom number between 1 and 100 with a higher probability of it being closer to 1
    return math.floor(abs(random.random() - random.random()) * (1 + 100 - 1) + 1)

def get_number(num: int = 0) -> str:
    if num < 1:
        num = get_random_number()
    if num < 20:
        return FIRST_20[num]
    else:
        first, second = str(num)
        if second == '0':
            return TENS[int(first)]
        ten = TENS[int(first)]
        digit = FIRST_20[int(second)]
        return f'{ten}-{digit}'

def generate_name(noun: str ='', number: int = 0) -> str:
    noun = get_noun(noun)
    number = get_number(number)
    return f'{number} {noun}'.title()

if __name__ == '__main__':
    main()