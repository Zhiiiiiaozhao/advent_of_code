#Advent of code 2022 day 1: calorie counting 


#PART 1
# Loading the data
with open('advent_day1.txt') as file:
    data = file.read().split('\n')
#print(data)

calorie_list = []
calorie_of_each_elf = 0
for i in data:
    if i != '':
        calorie_of_each_elf += int(i)
    else:
        calorie_list.append(calorie_of_each_elf)
        calorie_of_each_elf = 0
        
print('the Elf carrying the most Calories',max(calorie_list))
        
#PART 2
calorie_list.sort(reverse = True)
print('top three Elves carrying',sum(calorie_list[:3]) ,'Calories')

#the Elf carrying the most Calories 71124
#top three Elves carrying 204639 Calories
