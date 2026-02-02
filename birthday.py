def Birthday(candles):
    tallest = candles[0]
    for c in candles:
        if c > tallest:
            tallest = c
        count = 0
    for c in candles:
        if c == tallest:
            count += 1
    return count

candles = [6, 9, 1, 4]
result = Birthday(candles)
print(result)