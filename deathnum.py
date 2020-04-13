import sys
x = sys.stdin.readlines()
print(x)
counties = ['Barnstable', 'Berkshire', 'Bristol', "Dukes", "Essex", "Franklin", "Hampden", "Hampshire", "Middlesex", "Nantucket", "Norfolk", "Plymouth", "Suffolk", "Worcester"]
deathnum = [0]*14
for i in x:
    print(i)
    z = i.split()
    print(z)
    for p in z:
        print(p)
        if p in counties:
            deathnum[counties.index(p)] += 1

print(counties)
print(deathnum)
        
        
