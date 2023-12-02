# f = lambda str, dir: min((str[::dir].find(num[::dir])%99, i) for i, num in enumerate(
#     '1 2 3 4 5 6 7 8 9 one two three four five six seven eight nine'.split()))[1]%9+1
# summ = 0
# for x in open('data.txt'):
#     summ += 10*f(x, 1) + f(x, -1)
#     print(summ)
# # print(sum(10*f(x, 1) + f(x, -1) for x in open('data.txt')))




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
#    print(dct)
   d1 = parser(dct[0])
   d2 = parser(dct[-1])
#    print(d1,d2)
   sum+=combine_digits(d1,d2)
   print(sum)
   if (sum == 1678):
    print(i)
    print(dct)
    print(d1, d2)
    print("combo: ", combine_digits(d1,d2))
   i = i + 1
   
   


    





