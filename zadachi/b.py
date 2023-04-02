import re
txt = str(input())
pattern = r'(.+?)([A-Z])'

def to_snake(txt):
    return txt.group(1).lower()+"_" +txt.group(2).lower()

ans = re.sub(pattern, to_snake, txt)
print(ans)


# find all letters+_  'the_ hello bye one_' -> ['the_', 'one_']