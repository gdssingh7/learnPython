#sorting
def selection_sort(arr):
    # Traverse through all elements in the array
    for i in range(len(arr)):
        # Assume the first element of the unsorted part is the smallest
        min_idx = i
        
        # Find the smallest element in the remaining unsorted part
        for j in range(i + 1, len(arr)):
            # Update min_idx if the element at j is smaller than the current minimum
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap the smallest element found with the first unsorted element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Example usage:
nums = [29, 10, 14, 37, 13]
selection_sort(nums)
print("Sorted array (Selection Sort):", nums)

#bubble sort with outer loop as backward
def bubble_sort(arr):
    n = len(arr)
    # Traverse through the array backwards with the outer loop
    for i in range(n - 1, 0, -1):
        swapped = False  # To track if any swaps occurred

        # Inner loop goes from 0 to i, comparing adjacent elements
        for j in range(i):
            # If the current element is greater than the next one, swap them
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True  # A swap happened, so we need to continue

        # If no swaps occurred, the array is already sorted, so we can stop early
        if not swapped:
            break

# Example usage:
nums = [29, 10, 14, 37, 13]
bubble_sort(nums)
print("Sorted array (Bubble Sort, with backward outer loop):", nums)

#bubble sort with outer loop forward
def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Set a flag to detect if a swap happened
        swapped = False
        
        # Last i elements are already sorted, so we don't need to check them
        for j in range(0, n - i - 1):
            # Compare adjacent elements and swap if they are in the wrong order
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no elements were swapped in this pass, the array is already sorted
        if not swapped:
            break

# Example usage:
nums = [29, 10, 14, 37, 13]
bubble_sort(nums)
print("Sorted array (Bubble Sort):", nums)



def insertion_sort(arr):
    # Traverse from the second element to the end of the array
    for i in range(1, len(arr)):
        # Store the current element to be compared
        key = arr[i]
        j = i - 1
        
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead
        # of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Place the key in its correct position in the sorted part
        arr[j + 1] = key

# Example usage:
nums = [29, 10, 14, 37, 13]
insertion_sort(nums)
print("Sorted array (Insertion Sort):", nums)


class Solution:
    # Function to merge two sorted halves of the array
    def merge(self, arr, l, m, r): 
        """
        Merges two sorted subarrays:
        arr[l:m+1] (left half) and arr[m+1:r+1] (right half).
        """
        low = l       # Starting index of the left subarray
        high = m + 1  # Starting index of the right subarray
        temp = []     # Temporary array to store the merged sorted values

        # While there are elements in both subarrays, merge them
        while low <= m and high <= r:
            if arr[low] < arr[high]:
                temp.append(arr[low])  # Append the smaller element
                low += 1               # Move the pointer of the left subarray
            else:
                temp.append(arr[high]) # Append the smaller element
                high += 1              # Move the pointer of the right subarray
        
        # Copy any remaining elements from the left subarray (if any)
        while low <= m:
            temp.append(arr[low])
            low += 1

        # Copy any remaining elements from the right subarray (if any)
        while high <= r:
            temp.append(arr[high])
            high += 1

        # Copy the merged elements back into the original array
        # We use i - l to correctly copy elements from temp back to arr[l:r+1]
        for i in range(l, r + 1):
            arr[i] = temp[i - l]  # i-l makes sure we access temp from index 0
        
        return arr  # Return the array after merging
    
    # Recursive merge sort function
    def mergeSort(self, arr, l, r):
        """
        Recursively splits the array into two halves, sorts them, and merges them.
        arr: the array to be sorted
        l: left index (start of the subarray)
        r: right index (end of the subarray)
        """
        # Base case: If the subarray has only one element, it's already sorted
        if l == r:
            return
        
        # Find the middle point to divide the array into two halves
        m = (l + r) // 2

        # Recursively sort the first half: arr[l:m]
        self.mergeSort(arr, l, m)

        # Recursively sort the second half: arr[m+1:r]
        self.mergeSort(arr, m + 1, r)

        # Merge the two sorted halves back together
        self.merge(arr, l, m, r)
        
        return arr  # Return the sorted array



class Solution:
    # Function to sort the array using Quick Sort algorithm
    def quickSort(self, arr, low, high):
        """
        Quick Sort recursively sorts the array by dividing it into two parts 
        around a pivot, and sorting each part separately.
        """
        # We can only sort if there is more than one element in this part of the array
        if low < high:
            # Partition the array and get the index where the pivot ends up
            parti = self.partition(arr, low, high)
            
            # Recursively apply quick sort to the left of the pivot
            self.quickSort(arr, low, parti - 1)
            
            # Recursively apply quick sort to the right of the pivot
            self.quickSort(arr, parti + 1, high)
        
        # Return the sorted array after sorting the entire array
        return arr

    # Function to partition the array into two halves
    def partition(self, arr, low, high):
        """
        Partition the array so that elements smaller than the pivot are to the left,
        and elements greater than the pivot are to the right. The function returns the 
        index where the pivot element ends up.
        """
        pivot = arr[low]  # Choose the first element as the pivot
        i = low           # Start i at the beginning of the array
        j = high          # Start j at the end of the array

        # Continue until i and j cross each other
        while i < j:
            # Move i to the right until an element larger than or equal to the pivot is found
            # This ensures all elements on the left side of i are smaller than or equal to the pivot
            while pivot >= arr[i] and i < high:
                i += 1
            
            # Move j to the left until an element smaller than the pivot is found
            # This ensures all elements on the right side of j are greater than the pivot
            while pivot < arr[j] and j > low:
                j -= 1

            # Swap arr[i] and arr[j] only if i is still less than j
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]

        # Place the pivot element at its correct position by swapping arr[low] with arr[j]
        arr[low], arr[j] = arr[j], arr[low]
        
        # Return the index where the pivot element now resides
        return j




class Solution: 
    #loop from i to end and find the minimum element and store it at i it's like take the minimums at start
    def select(self, arr, i):
        # code here 
        minp = i
        for k in range(i, len(arr)):
            if arr[k]<arr[minp]:
                minp = k
        return minp
            
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(len(arr)):
            minp = self.select(arr,i)
            arr[i],arr[minp] =arr[minp], arr[i]
        return arr


class Solution:
    #Function to sort the array using bubble sort algorithm.
    # one loop backward, inner loop forward till i an keep one swaping adjacent element, kind of like taking the biggest element to the last
    def bubbleSort(self,arr, n):
        # code here
        swap = False
        for i in range(len(arr)-1,0,-1):
            for j in range(0,i):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1],arr[j]
                    swap=True
            if not swap:
                break
        return arr
    
class Solution:
    def insert(self, alist, index, n):
        #code here
        pass
        
    #Function to sort the list using insertion sort algorithm.   
    # loop and take an element and place it at right order 
    def insertionSort(self, alist, n):
        for i in range(len(alist)):
            j=i
            while (j>0 and alist[j-1]>alist[j]):
                alist[j], alist[j-1] = alist[j-1], alist[j]
                j-=1
        return alist