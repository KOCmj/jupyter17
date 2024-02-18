from math import pi, radians

def printArea():
    a = {}
    c= {}

    print(f"Let's play a game for areas and circumferences.")
    while True:
        length = int(input(f"What is the length of your house? Enter ('q') if you don't want to play: "))
        if length.__str__() == str('q'):
            break
        width = int(input(f"What is the width of your house? Enter ('q') if you don't want to play: "))
        if width.__str__() == str('q'):
            break
        else:
            for l,w in a.items():
                return(f'The length is {l} and the width is {w}')
            break
    area=int(length)*(width)
    print(area)
    a[length] = width
    pass

    while True:
        radius = float(input(f"Enter a radius, any radius and we shall return the circumference! Enter ('q') if you don't want to play: "))
        if radius.__str__() == str('q'):
            break
        else:
            for r,ci in c.items():
                r,ci=float
                return(float(f'The radius you entered is {r} and the {ci} is'))
            break
    circumference=(float(radius)*(pi)*2)
    print(float(circumference))
    return(float(circumference))
    
printArea()


# def cir():
#     c= {}

#     while True:
#         radius = float(input(f"Enter a radius, any radius and we shall return the circumference! Enter ('q') if you don't want to play: "))
#         if radius.__str__() == 'q':
#             break
#         else:
#             for r,ci in c.items():
#                 r,ci=float
#                 return(float(f'The radius you entered is {r} and the {ci} is'))
#             break
#     circumference=(float(radius)*(pi)*2)
#     return(float(circumference))
# cir()


        
        # from math import pi, radians




        # pi * r
