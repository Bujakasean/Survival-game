import random
hpBar = int(100)
stamBar = int(100)
items = int()
tools = int()
wood = int()
rock = int()
food = int()
wtime = int()
hammer = int()
hammerHP = int()
axe = int()
axeHP = int()
mine = int()
mineHP = int()
pick = int()
pickHP = int()
chois = int()
rcount = int()
print('Добро пожаловать в игру')
print()
while hpBar > 0:
    print()
    print('Выберите действие:')
    if items >= 1:
        print('Открыть инвентарь - 1')
    else:
        print('Инвентарь пуст')
    if tools >= 1:
        print('Добывать ресурсы - 2')
    else:
        print('Нет инструментов')
    print('Пошарить окресности - 3')
    if hammer >= 1 or wood >= 5:
        print('Меню крафта - 4')
    else:
        print('Нет молотка для постройки')
    print('Отдохнуть - 5 ')
    print()
    print('У Вас -', hpBar, ' ХП')
    print('У Вас -', stamBar, ' сил')
    print()
    menu = input()
    try:
        menu = int(menu)
    except:
        print('Неверное действие')
    if menu == 1 and items >= 1:
        print('Ваш инвентарь')
        if food >= 1:
            print('Еды - ', food)
        else:
            print('Еды нет')
        if wood >= 1:
            print('Дерева - ', wood)
        else:
            print('Дерева нет')
        if rock >= 1:
            print('Камней - ', rock)
        else:
            print('Камней нет')
        print()
        input('Понятно(нажмите ентер')
    elif menu == 1 and items < 1:
        print('Написано же было что инвентарь пуст!')
    if menu == 2 and tools >= 1:
        if axe >= 1:
            print('Рубить дерево - 1')
        else:
            print('У вас нет топора.')
        if mine >= 1:
            print('Добывать камень - 2')
        else:
            print('У вас нет кирки.')
        if pick >= 1:
            print('Начать охоту - 3')
        else:
            print('У вас нет копья.')
        print()
        chois = int(input())
        if chois == 1 and axe >= 1:
            while chois == 1:
                rcount = random.randint(0, 10)
                wood = wood + rcount
                items = items + rcount
                axeHP = axeHP - rcount
                print('Вы добыли - ', rcount, ' дерева')
                stamBar = stamBar - 2
                if stamBar > 0:
                    if axeHP >= 0:
                        print()
                        print('Добывать дальше - 1')
                        print('Пойти к лагерю - 2')
                        chois = int(input())
                    else:
                        print('Топор сломался')
                        axe = axe - 1
                        chois = 2
                else:
                    print('Я устал.')
        if chois == 2 and mine >= 1:
            chois = 1
            while chois == 1:
                rcount = random.randint(0, 10)
                rock = rock + rcount
                items = items + rcount
                mineHP = mineHP - rcount
                print('Вы добыли - ', rcount, ' камня')
                if stamBar > 0:
                    if mineHP >= 0:
                        print()
                        print('Добывать дальше - 1')
                        print('Пойти к лагерю - 2')
                        chois = int(input())
                    else:
                        print('Кирка сломалась')
                        mine = mine - 1
                        chois = 2
                else:
                    print('Я устал.')
        if chois == 3 and pick >= 1:
            chois = 1
            while chois == 1:
                rcount = random.randint(0, 10)
                food = food + rcount
                items = items + rcount
                pickHP = pickHP - rcount
                print('Вы добыли - ', rcount, ' еды')
                if stamBar > 0:
                    if pickHP >= 0:
                        print()
                        print('Охотиться дальше - 1')
                        print('Пойти к лагерю - 2')
                        chois = int(input())
                    else:
                        print('Копье сломалось')
                        pick = pick - 1
                        chois = 2
                else:
                    print('Я устал.')
    elif menu == 2 and tools < 1:
        print('Без инструмента в лесу делать нечего, может пошарить по округе?')
    if menu == 3:
        rcount = random.randint(0, 2)
        if rcount == 0:
            print('Вы не нашли дерево')
        elif rcount == 1:
            print('Вы нашли 1 деревяху')
        elif rcount == 2:
            print('Вы нашли 2 деревяхи')
        wood = wood + rcount
        items = items + rcount
        rcount = random.randint(0, 2)
        if rcount == 0:
            print('Вы не нашли камней')
        elif rcount == 1:
            print('Вы нашли 1 камень')
        elif rcount == 2:
            print('Вы нашли 2 камня')
        rock = rock + rcount
        items = items + rcount
        stamBar = stamBar - 5
        print()
    if menu == 4 and hammer == 0:
        if wood > 5:
            print('Сделать деревянный молоток(5 дерева) - 1')
            print('Назад - 2')
            chois = int(input())
            if chois == 1:
                print('Молоток добавлен')
                hammer = hammer + 1
                hammerHP = hammerHP + 100
                wood = wood - 5
                items = items - 5
    elif menu == 4 and hammer > 0:
        if wood < 10:
            print("Нужно еще подфармить")
        if wood > 10:
            print('Сделать деревянный топор(10 дерева) - 1')
            print('Сделать деревянную кирку(10 дерева) - 2')
            print('Сделать деревянное копье(10 дерева) - 3')
        if wood > 10 and rock > 10:
            print('Сделать каменный топор(по 10 дерева и камня) - 4')
            print('Сделать каменную кирку(10 дерева и камня) - 5')
            print('Сделать каменное копье(10 дерева и камня) - 6')
        print('Назад - 0')
        chois = int(input())
        if chois == 1:
            wood = wood - 10
            items = items - 10
            axe = axe + 1
            tools = tools + 1
            axeHP = axeHP + 50
            print('Топор добавлен')
        elif chois == 2:
            wood = wood - 10
            items = items - 10
            mine = mine + 1
            tools = tools + 1
            mineHP = mineHP + 50
            print('Кирка добавлена')
        elif chois == 3:
            wood = wood - 10
            items = items - 10
            pick = pick + 1
            tools = tools + 1
            pickHP = pickHP + 50
            print('Копье добавлено')
        elif chois == 4:
            wood = wood - 10
            items = items - 10
            items = items - 10
            rock = rock - 10
            axe = axe + 1
            tools = tools + 1
            axeHP = axeHP + 100
            print('Топор добавлен')
        elif chois == 5:
            wood = wood - 10
            items = items - 10
            items = items - 10
            rock = rock - 10
            mine = mine + 1
            tools = tools + 1
            mineHP = mineHP + 100
            print('Кирка добавлена')
        elif chois == 6:
            wood = wood - 10
            items = items - 10
            items = items - 10
            rock = rock - 10
            pick = pick + 1
            tools = tools + 1
            pickHP = pickHP + 100
            print('Копье добавлено')
        elif chois == 0:
            print('В следующий раз что нибудь скрафчу')
    elif menu == 5:
        print('Добро пожаловать на утренний стояк')
        stamBar = 100