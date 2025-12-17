numbers = [
    126, 45, 67, 23, 89, 342, 56, 78, 940, 111,
]
n = len(numbers)
for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
mid = n // 2
if n % 2 == 0:
    median = (numbers[mid - 1] + numbers[mid]) / 2
else:
    median = numbers[mid]
print("Sorted list:", numbers)
print("Median =" , median)
