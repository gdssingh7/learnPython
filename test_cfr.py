def extractDigit(N):
    count = 0
    while N>0:
        print(N%10)
        N=N//10
        count+=1
    return count

def ReverseDigit(N: int):
    reversed = 0
    while N>0:
        lastdigit = N%10
        reversed = reversed*10+lastdigit
        N = N//10
    print(reversed)
    return reversed

def checkArmstrong(n):
    #write your code here !!!!!!!!!
    noOfDigit = 0
    m=n
    digits = []
    while (m>0):
        digits.append(m%10)
        m=m//10
    sumOfArm = 0
    for i in digits:
        sumOfArm = sumOfArm + i**len(digits) 
    print(digits)
    print(sumOfArm)
    if sumOfArm==n:
        return "true"
    else:
        return "false"
class Solution:    
    #Complete this function
    def printNos(self, n):
        if n == 0:
            return
        self.printNos(n-1)
        print(n, end = ' ')
class Solution:
    # def sumOfSeries(self,n):
    #     return int(n*(n+1)/2)**2
    def sumOfSeries(self,n):
        if n ==1:
            return 1
        else:
            return n*n*n+self.sumOfSeries(n-1)
        
class Solution:
    def f(self,arr, i,j):
        if i>=j:
            return
        arr[i],arr[j]= arr[j],arr[i]
        self.f(arr,i+1,j-1)
    
    def reverseArray(self, arr):
        self.f(arr,0,len(arr)-1)
        return arr
class Solution:

    
    def reverseArray(self, arr):
        n = len(arr)
        for i in range(n // 2):
            # Swap elements at positions i and n-1 - i
            arr[i], arr[n - 1 - i] = arr[n - 1 - i], arr[i]
        return arr
class Solution:
    # Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr, N, P):
        # Step 1: Replace all elements greater than N with 0 (ignore them)
        for i in range(N):
            if arr[i] > N:
                arr[i] = 0

        # Step 2: Count occurrences by using the original value (via modulus) and add N to mark counts
        for i in range(N):
            # Use arr[i] % N to always get the original value, even if arr[i] has been modified
            index = (arr[i] % N) - 1
            if index >= 0:  # Ensure the index is valid (within bounds 0 to N-1)
                arr[index] += N

        # Step 3: Normalize the values by dividing each element by N
        for i in range(N):
            arr[i] = arr[i] // N
        
        return arr
            
class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        maxFreq = 1
        nums = sorted(nums)  
        left=0
        right = 0
        total=0
        while right < len(nums):
            total +=nums[right]
            while(nums[right]*(right-left+1)> total+k):
                total -= nums[left]
                left+=1
            maxFreq = max(maxFreq, right-left+1)
            right+=1
        return maxFreq
                