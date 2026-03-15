nums = tuple(map(int, input("Enter numbers separated by space: ").split()))

print("Total items in tuple:", len(nums))

print("Last item:", nums[-1])

print("Reverse order:", nums[::-1])

if 5 in nums:
    print("5 exists in the tuple")
else:
    print("5 does not exist in the tuple")

new_tuple = nums[1:-1]
print("Tuple after removing first and last elements:", new_tuple)