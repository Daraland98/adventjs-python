''' Santa Claus 🎅 wants to frame the names of the good children to decorate his workshop 🖼️, but the frame must follow specific rules. Your task is to help the elves generate this magical frame.

Rules:

· Given an array of names, you must create a rectangular frame that contains all of them.
· Each name must be on a line, aligned to the left.
· The frame is built with * and has a border one line thick.
· The width of the frame automatically adapts to the longest name plus a margin of 1 space on each side.

Example of how it works: '''

def create_frame(names):
    max_length = max(len(word) for word in names)
    border = '*' * (max_length + 4)
    framed_words = "\n".join([f"* {word.ljust(max_length)[:-1]}  *" for word in names]) 
    return  f"{border}\n{framed_words}\n{border}" 

# max(len(word) for word in names): Finds the length of the longest word in the list.
# '*' * (max_length + 4): Creates the top and bottom border of the frame.
# word.ljust(max_length): Left-justifies each word to match the length of the longest word.
# [:-1]: This slice removes the last character from the string. 
# "\n".join(...): Joins the framed words into a single string with newline characters.

# Note: In the web compiler, remove the newline before {framed_words} in the return statement. Otherwise, it creates a double line break between the border and the framed words.

result1 = create_frame(['midu', 'madeval', 'educalvolpz'])
print(result1)
# // Expected result:
# ***************
# * midu        *
# * madeval     *
# * educalvolpz *
# ***************

result2 = create_frame(['midu'])
print(result2)
# // Expected result:
# ********
# * midu *
# ********

result3 = create_frame(['a', 'bb', 'ccc'])
print(result3)
# // Expected result:
# *******
# * a   *
# * bb  *
# * ccc *
# *******

result4 = create_frame(['a', 'bb', 'ccc', 'dddd'])
print(result4)
# // Expected result:
# *********
# * a     *
# * bb    *
# * ccc   *
# * dddd  *
# *********
