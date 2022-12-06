

with open("01/calories.txt", mode='r') as file:
    data = file.read()

elves = data.split('\n\n')
elves = [elf.split('\n') for elf in elves] # results a list of calories for each elf

calories = []
for elf in elves:
    calorie_sum = 0
    for calorie in elf:
        if calorie != '':
            calorie_sum += int(calorie)
    calories.append(calorie_sum)

print("Maxumum amount of calories one elf has:", max(calories))


# Top three elves total calories

calories.sort(reverse=True)

print(calories[:3])
print("Total calories of top three elves is: ", sum(calories[:3]))
