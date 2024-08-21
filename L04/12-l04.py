daytimes = int(input('Estimated time : '))
weeks = daytimes//7
timeteraphy = 2.5*daytimes
teraphy = [0,0,0]
for i in range(weeks):
    print(f'Week{i+1}')
    pt = int(input('Physical therapy : '))
    wt = int(input('Weight training : '))
    ft = int(input('Fitness training : '))
    teraphy[0] += pt
    teraphy[1] += wt
    teraphy[2] += ft
if teraphy[0] >= timeteraphy and teraphy[1] >= timeteraphy and teraphy[2] >=timeteraphy:
    print('Buzzy has recovered in time.')
else:
    print('Buzzy has not recovered in time.')