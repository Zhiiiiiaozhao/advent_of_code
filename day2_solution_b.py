#define different combinations, return the combination list
def combo_A1(rounds):
    return [round for round in rounds if round =='A X'] #part2: lose  A-Z

def combo_A2(rounds):
    return [round for round in rounds if round =='A Y'] #part2: draw  A-X

def combo_A3(rounds):
    return [round for round in rounds if round =='A Z'] #part2: win   A-Y

def combo_B1(rounds):
    return [round for round in rounds if round =='B X'] #part2: lose  B-X

def combo_B2(rounds):
    return [round for round in rounds if round =='B Y'] #part2: draw  B-Y

def combo_B3(rounds):
    return [round for round in rounds if round =='B Z'] #part2: win   B-Z

def combo_C1(rounds):
    return [round for round in rounds if round =='C X'] #part2: lose  C-Y

def combo_C2(rounds):
    return [round for round in rounds if round =='C Y'] #part2: draw  C-Z

def combo_C3(rounds):
    return [round for round in rounds if round =='C Z'] #part2: win   C-X

#loading the data
with open('advent_day2.txt') as file:
    data = file.read().split('\n')

#calculate the total score of different combinations
print('the total score for part one is',4*len(combo_A1(data))+8*len(combo_A2(data))+3*len(combo_A3(data))+len(combo_B1(data))+5*len(combo_B2(data))+9*len(combo_B3(data))+7*len(combo_C1(data))+2*len(combo_C2(data))+6*len(combo_C3(data)))
#the total score for part one is 10595

print('the total score for part two is',3*len(combo_A1(data))+4*len(combo_A2(data))+8*len(combo_A3(data))+len(combo_B1(data))+5*len(combo_B2(data))+9*len(combo_B3(data))+2*len(combo_C1(data))+6*len(combo_C2(data))+7*len(combo_C3(data)))
#the total score for part two is 9541
