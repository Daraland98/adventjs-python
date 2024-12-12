'''You are in a very special market where Christmas trees 🎄 are sold. Each one comes decorated with a series of very peculiar ornaments, and the price of the tree is determined by the ornaments it has.

· *: Snowflake - Value: 1
· o: Christmas Ball - Value: 5
· ^: Decorative Tree - Value: 10
· #: Shiny Garland - Value: 50
· @: Polar Star - Value: 100

Normally, you would sum up all the values of the ornaments and that's it…

But, watch out! If an ornament is immediately to the left of another of greater value, instead of adding, its value is subtracted.'''

def calculate_price(ornaments: str) -> int:
    values = {'*': 1, 'o': 5, '^': 10, '#': 50, '@': 100}
    for char in ornaments:
      if char not in values: return None
    total = 0
    prev_value = 0
    for char in ornaments:
      current_value = values[char]
      if prev_value < current_value: total -= prev_value 
      else: total += prev_value  
      prev_value = current_value
    total += prev_value 
    return total


print(calculate_price('***'))  # 3   (1 + 1 + 1)
print(calculate_price('*o'))  # 4   (5 - 1)
print(calculate_price('o*'))  # 6   (5 + 1)
print(calculate_price('*o*'))  # 5  (-1 + 5 + 1) 
print(calculate_price('**o*')) # 6  (1 - 1 + 5 + 1) 
print(calculate_price('o***')) # 8   (5 + 3)
print(calculate_price('*o@'))  # 94  (-5 - 1 + 100)
print(calculate_price('*#'))  # 49  (-1 + 50)
print(calculate_price('@@@'))  # 300 (100 + 100 + 100)
print(calculate_price('#@'))  # 50  (-50 + 100)
print(calculate_price('#@Z'))  # undefined (Z is unknown)