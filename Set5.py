color_set = {'red', 'orange', 'yellow', 'white', 'black'}

color_set.remove('yellow')
print(color_set)


color_set.discard('white')
print(color_set)

deleted_item = color_set.pop()
print(deleted_item)

color_set.clear()
print(color_set)
del color_set