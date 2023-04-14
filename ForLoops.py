edutainers = ['Aubri', 'Adam', 'Vonne', 'Justin', 'Daniel']
attempts = range(3)
print('Edutainers: ', edutainers)

for edutainer in edutainers:
    print('Edutainer: ', edutainer)

favorite_number = 7
for attempt in attempts:
    guess = int(input("What is Vonne's favorite number? \n"))
    if guess == favorite_number:
        print('Yay! You win!')
        break
    else:
        print('Try again')

for index, edutainer in enumerate(edutainers):
    print(index, ': ', edutainer)
