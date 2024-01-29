# nums = [1,2,3,4,5,6,7,10]
#          [0,1,2,3,4,5,6,7]
#         l               r
# len = 9
# m = 0 + 9 // 2 --> 4.5

def binary_search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2  # Calculate the middle index

        # Check if the middle element is the target
        if nums[mid] == target:
            return mid  # Return the index of the target element

        # If the target is smaller, ignore the right half
        elif nums[mid] > target:
            right = mid - 1

        # If the target is larger, ignore the left half
        else:
            left = mid + 1

    return -1  # Return -1 if the target is not found

# Example usage:
nums = [1, 2, 3, 4, 5, 6, 7, 8, 10]
search_element = 8
result = binary_search(nums, search_element)

if result != -1:
    print(f"Element {search_element} is present at index {result}.")
else:
    print(f"Element {search_element} is not present in the list.")
