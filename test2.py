def relation(lt):
    lisedg = [('snake', 'eagle'), ('wolf', 'eagle'), ('rat', 'eagle'), ('frog', 'eagle'), ('bird', 'eagle'), ('rat', 'snake'), ('frog', 'snake'), ('wolf', 'snake'), ('rat', 'wolf'), ('bird', 'wolf'), ('dragonfly', 'bird'), ('fruitfly', 'bird'), ('grasshopper', 'rat'), ('grasshopper', 'frog'), ('butterfly', 'frog'), ('dragonfly', 'frog'), ('fruitfly', 'frog'), ('butterfly', 'dragonfly'), ('fruitfly', 'dragonfly'), ('corn', 'grasshopper'), ('flower', 'butterfly'), ('mango', 'fruitfly')]
    liseat = []
    liseaten = []
    for i in lisedg:
        if i[0] == lt:
            liseaten.append(i[1])
        elif i[1] == lt:
            liseat.append(i[0])