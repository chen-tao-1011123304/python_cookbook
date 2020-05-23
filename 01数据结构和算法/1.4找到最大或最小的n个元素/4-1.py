import heapq


nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]

# sorted[][:3]
print(heapq.nlargest(3, nums))
# sorted[][:3]
print(heapq.nsmallest(3, nums))


print(sorted(nums)[:3])
print(sorted(nums, reverse=True)[:3])
