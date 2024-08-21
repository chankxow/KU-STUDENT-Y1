distance = int(input('Distance from starting point(m.): '))
move = 0
sets = 0

if distance == 0:
    print(move)
    print('Buzz moved 0 set(s)')
else:
    while move != distance:
        if move < distance:
            move += 5
            print(move,end=' ')
            move -= 2
            print(move,end=' ')
        else:
            move -=4
            print(move,end=' ')
            move +=3
            print(move,end=' ')
        sets += 1
    print(f'\nBuzz moved {sets} set(s)')

