#if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes.
import re
f = open("data2.txt", "r")
lines = f.readlines()
cube_dict = {}
colors_dict = {}
for l in lines:
    game_id = l.split(':')
    cubes = l.split(':')[1:]
    cubes = ''.join(cubes) 
   
    cube_dict[game_id[0]] = cubes.split(';')

sum_of_ids = 0
for k,v in cube_dict.items():
    blue_ok = True
    red_ok = True
    green_ok = True
    

    for draw in v:
        blue = 0
        red=0
        green =0
        check = False
        if 'blue' in draw:
            blue+= int(''.join(re.findall("(\d\d|\d) blue",draw)))
            if blue >14:
                blue_ok = False
        if 'red' in draw:
            red+= int(''.join(re.findall("(\d\d|\d) red",draw)))
            if red > 12:
                red_ok = False
        if 'green' in draw:
            green+= int(''.join(re.findall("(\d\d|\d) green",draw)))

            if green > 13:
                green_ok = False
        check += blue_ok and green_ok and red_ok


    if check:
        sum_of_ids+=int(k.split(' ')[1])


    print("Sum: ",sum_of_ids)







            







