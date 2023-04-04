#Advent of code 2022 day 2: Rock Paper Scissors
#basic score
#A-> Rock <- X(1)
#B-> Paper <-Y(2)
#C-> Scissors <-Z(3)
#outcome Win-> 6 draw-> 3 lose-> 0

#loading the data
with open('advent_day2.txt') as file:
    data = file.read().split('\n')
#print(len(data))

#PART 1 
total_score = 0
for each_round in data:
    opponent = each_round[0] 
    myself = each_round[2]   
# if draw 
    if (opponent == 'A' and myself == 'X') or (opponent == 'B' and myself == 'Y') or (opponent == 'C' and myself == 'Z'):
        outcome = 3
# I win
    elif (opponent == 'A' and myself == 'Y') or (opponent == 'B' and myself == 'Z') or (opponent == 'C' and myself == 'X'):
        outcome = 6
# I lose
    else:
        outcome = 0
#basic score  
    if myself == 'X':
        basic_score = 1
    elif myself == 'Y':
        basic_score = 2
    else:
        basic_score = 3
        
    total_score += outcome + basic_score
print('the total score for part one is',total_score)

#

#PART 2
#X-> lose(0) Y-> draw(3) Z-> win(6)
total_score2 = 0
for each_round2 in data:
    opponent = each_round2[0]
    second_column = each_round2[2]
#when second column == 'X', we need to lose
    if second_column == 'X': 
        if opponent == 'A':
            score = 3
        elif opponent == 'B':
            score = 1
        else:
            score = 2
#when second column == 'Y', we need to end the round in a draw
    elif second_column == 'Y':
        if opponent == 'A':
            score = 4
        elif opponent == 'B':
            score = 5
        else:
            score = 6
#when second column == 'Z', we need to win
    else:
        if opponent == 'A':
            score = 8
        elif opponent == 'B':
            score = 9
        else:
            score = 7
    
    total_score2 += score
print('the total score for part two is',total_score2)


