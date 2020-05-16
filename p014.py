big_list = [None for i in range(1000000 - 1)]
big_list[0] = 1

def find_collatz_length(number, big_list):
    if number < 1000000 and big_list[number - 1] is not None:
        return big_list[number - 1]
    else:
        if number % 2 == 0:
            length = 1 + find_collatz_length(number // 2, big_list)
        else:
            length = 1 + find_collatz_length(number * 3 + 1, big_list)
        if number < 1000000:
            big_list[number - 1] = length
        return length

max_len = 0
# for i in len(big_list):
for i in range(1000000 - 1):
    length = find_collatz_length(i + 1, big_list)
    if length > max_len:
        print(i + 1)
        max_len = length
