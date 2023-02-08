# word = "Kazakh British Technical University"
#
# cnt = 0
# for i in word:
#     if i == "B":
#         cnt += 1
# print('Count:', cnt)

tabu = None
for i in 'Kazakh':
    if i == 'l':
        tabu = True
        break
else:
    tabu = False
print(tabu)