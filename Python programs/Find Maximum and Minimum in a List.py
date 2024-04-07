def find_max_min(lst):
    return max(lst), min(lst)

lst = [int(x) for x in input("Enter space-separated integers: ").split()]
max_num, min_num = find_max_min(lst)
print("Maximum:", max_num)
print("Minimum:", min_num)
