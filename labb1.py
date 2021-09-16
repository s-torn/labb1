import math
print('Welcome to volume calculator!')
while True:
    choice=input('Would you like to calculate the volume of a cube or a tetrahedon? \nType C or T, or leave empty to exit program.\n')
    if choice=='':
        break
    elif choice=='c' or choice=='C':
        cube=float(input('Enter cube side length in cm:\n'))
        volume=cube**3
        print(f'Cube volume is {volume} cm3.')
    elif choice=='t' or choice=='T':
        tetra=float(input('Enter tetrahedon side length in cm:\n'))
        volume=tetra**3/(6*math.sqrt(2))
        print(f'Tetrahedon volume is {round(volume,2)} cm3.')
