numbers = [
    45, 50, 55, 60, 65, 70, 75, 80, 85, 90,
    50, 55, 60, 60, 65, 70, 70, 70, 75, 80,
    55, 60, 65, 65, 65, 70, 75, 75, 80, 85
]
frequency = {}
for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1
max_frequency = 0
for count in frequency.values():
    if count > max_frequency:
        max_frequency = count
        
modes = []
for num, count in frequency.items():
    if count == max_frequency:
        modes.append(num)
print("Numbers:")
print(numbers)
print("\nFrequency Table:")
for num in sorted(frequency):
    print(num, ":", frequency[num])
print("\nHighest Frequency:", max_frequency)
print("Mode(s):", modes)
