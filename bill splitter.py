import random


def unlucky_mode(final_bill, friends_list):
    print('No one is going to be lucky')
    fee_per_person = round(final_bill / number_of_people, 2)
    bill = dict.fromkeys(friends_list, fee_per_person)
    print(bill)


def lucky_mode(friends, fin_bill):
    lucky_person = random.choice(friends)
    print(f'{lucky_person} is the lucky one!\n')
    bill_per_person = fin_bill / (len(friends) - 1)
    bill = dict.fromkeys(friends, 0)
    for i in range(len(friends)):
        if list(bill.keys())[i] != lucky_person:
            bill[friends[i]] = bill_per_person
    print(bill)


def not_enough_people():
    print('\nNo one is joining for the party')


def enough_people():
    print('\nEnter the name of every friend (including you), each on a new line:')
    i = 0
    friends_list = []
    while i < number_of_people:
        friends_list.append(input())
        i += 1
    final_bill = eval(input('\nEnter the total bill value:'))
    bill = dict.fromkeys(friends_list)
    lucky = input('\nDo you want to use the "who is lucky?" feature? Write Yes/No:\n')
    if lucky.capitalize() == 'Yes':
        lucky_mode(friends_list, final_bill)
    else:
        unlucky_mode(final_bill, friends_list)


number_of_people = eval(input('Enter the number of friends joining (including you):\n'))

if number_of_people <= 0:
    not_enough_people()
else:
    enough_people()
