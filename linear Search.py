def linear_search(numbers, target):
  for i in range(len(numbers)):
    # Check if the current number is at the target
    if numbers[i] == target:
      # Return the index of the target number if found 
      return i
  # Return -1 if the target number is not found in the list
  return -1

# takes list of numbers from the user
numbers = [int(x) for x in input("Enter a list of numbers: ").split()]

# takes target number from the user
target = int(input("Enter the target number: "))

# Perform the linear search
result = linear_search(numbers, target)

# Print the result
if result == -1:
  print("The target number is not found in the list.")
else:
  print("The target number is found  at index", result)
