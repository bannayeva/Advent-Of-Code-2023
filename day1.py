#TODO: fix edge case '1twone'
import re
def find_first_num(line):
    matches = re.findall("(?:one|two|three|four|five|six|seven|eight|nine|[1-9])",line)  
    return matches
        

def combine_digits(d1,d2):
    return d1*10+d2

def parser(val):
    digi_dict = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,   
}
    try:
        return int(val)
    except:
        return digi_dict.get(val)
    


f = open("data.txt", "r")
lines = f.readlines()
sum = 0
i = 0
for line in lines:
   
   
   dct = find_first_num(line)
   d1 = parser(dct[0])
   d2 = parser(dct[-1])
   sum+=combine_digits(d1,d2)
   print(sum)

   


    





