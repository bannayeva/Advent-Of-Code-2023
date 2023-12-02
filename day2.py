#if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes.
import re
f = open("data2.txt", "r")
lines = f.readlines()
cube_dict = {}
colors_dict = {}
summ = 0
for l in lines:
    game_id = l.split(':')
    cubes = l.split(':')[1:]
    cubes = ''.join(cubes) 
   
    cube_dict[game_id[0]] = cubes.split(';')


for k,v in cube_dict.items():
    max_blue = -1000
    max_green = -1000
    max_red = -1000
    for draw in v:

        blue = 0
        red=0
        green =0

        if 'blue' in draw:
            blue+= int(''.join(re.findall("(\d\d|\d) blue",draw)))
     
            temp = 0
            if blue > max_blue: 
                max_blue = blue 

        if 'red' in draw:
            red+= int(''.join(re.findall("(\d\d|\d) red",draw)))
       
            if red > max_red: 
                max_red = red 
        if 'green' in draw:
            green+= int(''.join(re.findall("(\d\d|\d) green",draw)))

            if green > max_green: 
                max_green = green 
    mult = max_red*max_blue*max_green
    summ+=mult
    print(summ)


 





            







