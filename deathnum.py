import sys

print('copy data from ms pdf')
x = sys.stdin.readlines()
print('copy prev data from google sheets')
y = sys.stdin.readlines()

for i in range(0, len(y)):
    y[i] = int(y[i].strip('/n'))

counties = ['Barnstable', 'Berkshire', 'Bristol', "Dukes", "Essex", "Franklin", "Hampden", "Hampshire", "Middlesex", "Nantucket", "Norfolk", "Plymouth", "Suffolk", "Worcester"]
for i in x:
    z = i.split()
    for p in z:
        if p in counties:
            y[counties.index(p)] += 1

for i in y:
    print(i)

print("total:" + sum(y))
        

