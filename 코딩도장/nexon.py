def d(x):
    result = 0
    for i in range(0, len(str(x))):
        result += int(i)
    result = result + x

    return result

# result = sum(set(range(0, 5000)) - {d(i) for i in range(0,5000)})
result = 0
for i in range(0, 5000):
    result += d(i)

print(result)