'''We have already wrapped hundreds of presents 🎁… but an elf forgot to check if the present, represented by an asterisk *, is inside the box.

The box has a present (*) and counts as "inside the box" if:

· It is completely surrounded by # on the box's edges.
· The * is not on the box's edges.

Keep in mind that the * can be inside, outside, or may not even be there. We must return true if the * is inside the box and false otherwise.

Examples:'''

def inBox(box):
    inside = [x for x in box[1:-1] if "*" in x[1:-1]]
    return inside != []

print(inBox([
    "###",
    "#*#",
    "###"
]))  # ➞ True

print(inBox([
    "####",
    "#* #",
    "#  #",
    "####"
]))  # ➞ True

print(inBox([
    "#####",
    "#   #",
    "#  #*",
    "#####"
]))  # ➞ False

print(inBox([
    "#####",
    "#   #",
    "#   #",
    "#   #",
    "#####"
]))  # ➞ False
