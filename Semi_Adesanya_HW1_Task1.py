# Task 1: Find the next greater element in the array using a stack
# if there is no greater element to the right of the element return -1
# solution should be O(n)

def greater_element(arr):
    n = len(arr)
    result = [-1] * n
    stack = []

    # the process will start from the right to the left to make sure there is something always next
    # to it
    for i in range(n -1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop() # to remove elements from the stack that are smaller or equal to the number
                        # before it/ the current number
        if stack:
            result[i] = stack[-1] # if the stack is not empty then the top element is the next
                                  # greater element to the right
        stack.append(arr[i]) # to push the element onto the stack
    return result


# driver code
if __name__ == "__main__":
    print(greater_element([2,1,4,3]))
    print(greater_element([]))
    print(greater_element([5]))
    print(greater_element([5, 4, 3]))      
    print(greater_element([1, 2, 3, 4]))   
    print(greater_element([3, 3, 3]))          
