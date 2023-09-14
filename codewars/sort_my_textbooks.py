def sorter(textbooks):
    #Cramming before a test can't be that bad?
    return sorted(textbooks, key=str.lower)

print(sorter(['Algebra', 'History', 'Geometry', 'English']))
print(sorter(['Algebra', 'history', 'Geometry', 'english']))
print(sorter(['Alg#bra', '$istory', 'Geom^try', '**english']))