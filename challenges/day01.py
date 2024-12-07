'''Santa Claus 🎅 has received a list of magical numbers representing gifts 🎁, but some of them are duplicated and must be removed to avoid confusion. 
Additionally, the gifts must be sorted in ascending order before being delivered to the elves.

Your task is to write a function that receives a list of integers (which may include duplicates) and returns a new list without duplicates, sorted in ascending order.'''

def prepare_gifts(gifts):
   return sorted(set(gifts))

# set(gifts): Removes duplicates from the list.
# sorted(): Sorts the elements of the list in ascending order.

gifts1 = [3, 1, 2, 3, 4, 2, 5]
prepared_gifts1 = prepare_gifts(gifts1)
print(prepared_gifts1)  # [1, 2, 3, 4, 5]

gifts2 = [6, 5, 5, 5, 5]
prepared_gifts2 = prepare_gifts(gifts2)
print(prepared_gifts2)  # [5, 6]

gifts3 = []
prepared_gifts3 = prepare_gifts(gifts3)
print(prepared_gifts3)  # [] There are no gifts, the list remains empty