# alist = ["ram", "shyam", "hari", "sita"]
# blist = [1, 2, 3, 4, 5, 6, 7]
# for item in alist:
#     print(item)
# for item in blist:
#     print(item)

alist = []
total_sum = 0
for i in range(10):
    num = int(input("enter number : "))
    total_sum = total_sum + num
    alist.append(num)

print(alist)
print(total_sum)

