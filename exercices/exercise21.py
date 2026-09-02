#A set in Python is an unordered, mutable collection of unique, hashable elements

set_products = {"bread", "milk", "eggs", "cheese", "butter"}

market = set()

market.add("bread")
market.add("milk")
market.add("meat")
market.add("cookies")

new_market_products = market.union(set_products)

print(new_market_products)