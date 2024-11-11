# 1. we create a prime number list in the range 1 to 1000
# 2. we travere the array, and for each element we select the smallest prime closest to the element
# 3. after substracting the prime from the element, if the prev >= substraction result, we can not update the nums[i]
# we will perform the same operation till we get a valid increasing sequence, and update the element
# 4. after traversing and performing the operation the updated array need to be checked if it's sorted or not 
class Solution:
    # TC: O(n^2)
    def createPrimeList(self) -> List[int]:
        primes = []
        for num in range(2, 1000):
            flag = 1
            for i in range(2, num):
                if num % i == 0:
                    flag = 0
                    break
            if flag == 1:
                primes.append(num)
        
        return primes
    
    # we find a prime that is smaller than num
    # TC: O(p)
    def findSmallestPrimeIndex(self, prime_list: List[int], num: int) -> int:
        prime_index = 0
        for idx in range(len(prime_list)):
            if prime_list[idx] >= num:
                break
            prime_index = idx
        return prime_index

    # TC: O(n)
    def checkSorted(self, nums) -> bool:
        for i in range(len(nums)-1):
            if nums[i] >= nums[i+1]:
                return False
        return True

    # TC: O(n) + O(n * p * p) + O(n)
    def primeSubOperation(self, nums: List[int]) -> bool:
        prime_list = self.createPrimeList()
        l = len(nums)
        prev = 0
        
        for i in range(l):
            smallest_prime_index = self.findSmallestPrimeIndex(prime_list, nums[i])
            smallest_prime = prime_list[smallest_prime_index]
            updated_num = nums[i] - smallest_prime
            
            # if the increasing order does not maintain after first substraction, we do the same thing till we get a valid sequence
            while prev >= updated_num and smallest_prime_index >= 0:
                # the 2nd smallest or later prime will be in index-1 in prime list
                second_smallest_prime_index = smallest_prime_index - 1
                smallest_prime = prime_list[second_smallest_prime_index]
                updated_num = nums[i] - smallest_prime
                smallest_prime_index = second_smallest_prime_index

            if prev < updated_num:
                nums[i] = updated_num
            prev = nums[i]

        return self.checkSorted(nums)
