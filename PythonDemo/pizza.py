pizzas = ['a','b','c','d','e']
friend_pizzas = pizzas[:]
pizzas.append('f')
friend_pizzas.append('g')

print("My favorite pizzas are: ")
for pizza in pizzas:
    print(pizza,end=" ")
print("\nMy friend favorite pizzas are: ")
for pizza in friend_pizzas:
    print(pizza,end=" ")