games=['Cyberpunk']
game= input('Название игры: ')
while game!='0':
    if game in games:
        print('эта игра уже записана: ')
    else:
        games.append(game)
    game = input('Название игры')
games.sort()
print(games)

