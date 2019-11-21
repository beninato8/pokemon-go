import re

regex = re.compile(r'\d{12}')

with open('wisc_friends.txt', 'r') as f:
    friends = list(regex.findall(f.read()))

with open('wisc-old-friends.txt', 'r') as f:
    old_friends = list(regex.findall(f.read()))

both = list(x for x in friends if x in old_friends)


with open('wisc_friends.txt', 'r') as f:
    friends = f.read().split('\n')
for x in both:
    for y in friends:
        if x in y:
            print(y)

with open('wisc-old-friends.txt', 'r') as f:
    old_friends = list(regex.findall(f.read()))

for x in old_friends:
    if x not in both:
        print(x)