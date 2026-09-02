prices = {
    "banannas": 1.5,
    "apples": 2.0,
    "oranges": 1.75,
    "grapes": 2.5
}

max_value = max(prices.items(), key=lambda item: item[1])

print(max_value)  