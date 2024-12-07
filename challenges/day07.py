'''The grinch 👹 has passed through Santa Claus's workshop! And what a mess he has made. He has changed the order of some packages, so shipments cannot be made.

Luckily, the elf Pheralb has detected the pattern the grinch followed to jumble them. He has written the rules that we must follow to reorder the packages. The instructions are as follows:

You will receive a string containing letters and parentheses.
Every time you find a pair of parentheses, you need to reverse the content within them.
If there are nested parentheses, solve the innermost ones first.
Return the resulting string with parentheses removed, but with the content correctly reversed.
He left us some examples:'''

def fixPackages(packages):
    s = packages  
    while '(' in s:
        close_index = s.find(')')
        open_index = s[:close_index].rfind('(')
        reversed_content = s[open_index + 1:close_index][::-1]
        s = s[:open_index] + reversed_content + s[close_index + 1:]
    
    return s

# find: Returns the index of the first occurrence of a substring, or -1 if not found.
# rfind: Returns the index of the last occurrence of a substring, or -1 if not found.

print(fixPackages('a(cb)de'))  # ➞ "abcde"
print(fixPackages('a(bc(def)g)h'))  # ➞ "agdefcbh"
print(fixPackages('abc(def(gh)i)jk'))  # ➞ "abcighfedjk"
print(fixPackages('a(b(c))e'))  # ➞ "acbe"
