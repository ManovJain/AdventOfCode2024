arr1 = []
arr2 = []

## Read the locationID file
with open("/Users/manovski/Desktop/AdventOfCode/day1/input.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line)
        num1, num2 = map(int, line.strip().split())
        arr1.append(num1)
        arr2.append(num2)

## Sort the arrays
arr1.sort()
arr2.sort()


sum = 0
repeatCount = 0

for i in range(len(arr1)):
    sum += abs(arr1[i] - arr2[i])

    if arr1[i] in arr2:
        count = 0
        for j in range(len(arr2)):
            if arr1[i] == arr2[j]:
                count += 1
        repeatCount += count * arr1[i]
print(repeatCount)
print(sum)

