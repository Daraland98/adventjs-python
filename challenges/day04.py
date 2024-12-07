'''It's time to put up the Christmas tree at home! 🎄 But this year we want it to be special. We're going to create a function that receives the height of the tree 
(a positive integer between 1 and 100) and a special character to decorate it.

The function should return a string that represents the Christmas tree, constructed as follows:

· The tree is made up of triangles of special characters.
· The spaces on the sides of the tree are represented with underscores _.
· All trees have a trunk of two lines, represented by the # character.
· The tree should always have the same length on each side.
· You must ensure the tree has the correct shape using line breaks \n for each line.

Examples:'''

def createXmasTree(height, ornament):
    tree = []
    
    for level in range(height):
        underscores = height - level - 1
        symbols = 2 * level + 1
        tree.append("_" * underscores + ornament * symbols + "_" * underscores)
    
    trunk = "_" * (height - 1) + "\u0023" + "_" * (height - 1)
    tree.append(trunk)
    tree.append(trunk)
    
    return "\n".join(tree)

# Note: The web compiler does not accept the '#' character as it interprets it as a comment. To fix this, replace '#' with '\u0023' in the trunk generation.

tree = createXmasTree(5, '*')
print(tree)
# Resultado esperado:
# ____*____
# ___***___
# __*****__
# _*******_
# *********
# ____#____
# ____#____


tree2 = createXmasTree(3, '+')
print(tree2)
# Resultado esperado:
#__+__
#_+++_
#+++++
#__#__
#__#__


tree3 = createXmasTree(6, '@')
print(tree3)
# Resultado esperado:
#_____@_____
#____@@@____
#___@@@@@___
#__@@@@@@@__
#_@@@@@@@@@_
#@@@@@@@@@@@
#_____#_____
#_____#_____
