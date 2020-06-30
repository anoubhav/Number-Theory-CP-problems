from bisect import bisect_left, bisect_right
arr = [2, 3, 4, 4, 4, 5]

print(bisect_left(arr, 2))
print(bisect_left(arr, 3))
print(bisect_left(arr, 4))
print(bisect_right(arr, 4))
print(bisect_right(arr, 5))
print(bisect_right(arr, 4) - bisect_left(arr, 4))

# IN A SORTED ARRAY.
# bisect left: gives the number of elements less than x.
# bisect right: gives the number of elements less than equal to x.
# bisect right - bisect left: gives the number of elements equal to x.