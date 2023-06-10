"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Marek Dembicky
email: marodembo@gmail.com
discord: Mak D. #8143
"""

def get_comp_number():
    """
    Generovanie nahodneho cisla z 4 original digits
    nezacina nulou
    """
    import random
    temp = []
    first = random.randint(1, 9)#first character
    first = str(first)
    while len(temp) < 3:#next 3 characters
        next = random.randint(0, 9)
        if str(next) not in temp and next != int(first):#original numbers
            temp.append(str(next))
    comp_number = first + (''.join(temp))
    return comp_number


def guess_check(comp_num):
    """
    Prvy poziadavok na hadanie cisla
    """
    print('Hi there!')
    print(47 * '-')
    print('I\'ve generated a random 4 digit number for you.\nLet\'s play a bulls and cows game.')
    print(47 * '-')
    """ 
    Hadanie 4 miestneho cisla a pocet casu na spravny vysledok.
    Pocet pokusou rieseny cez list - za kazdy pokus prida do listu 1, a po uhadnuti vezme pocet pokusou ako len listu.
    """
    print('Enter a number: ')
    print(47 * '-')
    import time
    start_time = time.time() #start for time meassurement
    x = []#pocitanie pokusou pomocou dlzky listu kde sa pridavaju 1 za kazdy pokus
    again = True
    while again == True:
        guess = input('>>> ')
        print(47 * '-')
        if comp_num == guess:#uhadnutie spravneho cisla
            x.append(1)
            pocet_pokusov = len(x)
            print(f'Correct, you\'ve guessed the right number\nin {pocet_pokusov} guess.')
            # time counting from start to end in seconds:
            end_time = time.time()
            diff_time = end_time - start_time
            if diff_time < 60:
                seconds = diff_time
                print('You needed %.1f seconds.' %(seconds))
            elif 60 < diff_time < 3600:
                minutes = diff_time // 60
                seconds = diff_time % 60
                print(f'You needed {minutes} minutes and %.1f seconds.' %(seconds))
            elif diff_time >= 3600:
                hours = diff_time // 3600
                minutes = (diff_time % 3600) // 60
                seconds = (diff_time % 3600) % 60
                print(f'You needed {hours} hours, {minutes} minutes and %.1f seconds.' %(seconds))
            again = False

        if not guess.isdigit():
            print('must be a number')
            x.append(1)
            again = True

        elif comp_num != guess:
            if len(guess) != 4:
                print('must be from 4 digits')
                x.append(1)
                again = True
            elif int(guess[0]) == 0:
                print('number can not start with 0.')
                x.append(1)
                again = True
            elif len(set(guess)) != 4:
                check_duplicity = set()
                for ch in str(guess):
                    check_duplicity.update(ch)
                if len(check_duplicity) != 4:
                    print('no duplicates')
                    x.append(1)
                    again = True
            else:
                buls_comp = []
                buls_guess = []
                if guess.isdigit():
                    for ch in str(comp_num):
                        buls_comp.append(ch)
                    for ch2 in str(guess):
                        buls_guess.append(ch2)
                    cows = 0# counting of cows:
                    for index in range(0,4):
                        if buls_comp[index] == buls_guess[index]:
                            cows += 1
                    buls_cows = 0# counting of buls:
                    for item in buls_comp:
                        if item in buls_guess:
                            buls_cows += 1
                    x.append(1)
                    print('cows=', cows, ' buls=', (buls_cows - cows))

    return comp_num

def main():
    comp_num = get_comp_number()
    guess_check(comp_num)

main()