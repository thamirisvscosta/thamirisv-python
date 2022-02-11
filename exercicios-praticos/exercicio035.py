n = int(input('em que ano você nasceu? '))
i = 2021 - n
if i < 18:
    print(' Fique sossegado! Ainda não é o momento de se alistar.')
elif i == 18:
    print(' Fique atento! Já está na hora de se alistar!')
elif i > 18:
    print('Caramba, guri! Já passou a hora de se alistar,hein ?!')