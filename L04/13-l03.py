n = 1
c_dis = 100
p_dis = 0
while True :
    dis = int(input('Input distance: '))
    
    p_dis += dis
    c_dis += 2**n
    print(f'Police distance: {p_dis}')
    print(f'Criminal distance: {c_dis}')

    n += 1
    
    if p_dis >= c_dis:
        print('Caught him!')
        break



