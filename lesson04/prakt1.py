# Кожен пише суму списку за допомогою for та while
lst = list(map(int, input().split()))
sum_for = 0
for el in lst:
    sum_for += el
print(f"sum obtained via for is {sum_for}")
sum_while = 0
i = 0
while i < len(lst):
    sum_while += lst[i]
    i += 1
print(f"sum obtained via while is {sum_while}")

