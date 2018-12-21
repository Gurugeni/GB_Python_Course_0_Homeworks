# exercise 1

data = ["яблоко", "банан", "киви", "арбуз"]
print("1_{:>8}".format(data[0]))
print("2_{:>8}".format(data[1]))
print("3_{:>8}".format(data[2]))
print("4_{:>8}".format(data[3]))

# exercise 2

our_first_list = [1, 2, 3, 4, 5]
our_second_list = [4, 2, 8]

for i in our_first_list:
    if i in our_second_list:
        our_first_list.remove(i)
print(our_first_list)
print(our_second_list)

# exercise 3

main_list = [8, 4, 54, 9, 44, 11]
answer_list = []
main_list_length = len(main_list)
for i in range(main_list_length):
    if main_list[i] % 2 == 0:
        answer_list.append(main_list[i] / 4)
    else:
        answer_list.append(main_list[i] * 2)
print(answer_list)