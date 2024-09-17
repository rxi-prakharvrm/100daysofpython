ip = "192.168.110.179"

str = ip.split(".")

nums = []
for s in str:
    # nums.append(s[-1:-len(str):-1])
    nums.append(s[::-1])

ip_reversed = ".".join(nums)
print(ip_reversed)