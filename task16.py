
data = [123, "apple", "banana", "cat", 456, "mango", "elephant"]

result = list(filter(lambda x: len(x) > 5, data))
print(result)
