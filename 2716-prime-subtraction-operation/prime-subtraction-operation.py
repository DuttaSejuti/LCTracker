# 1. we create a prime number list in the range 1 to 1000
# 2. we travere the array, and for each element we select the smallest prime closest to the element
# 3. after substracting the prime from the element, if the prev >= substraction result, we can not update the nums[i]
# we will perform the same operation with the second smallest prime, and update the element
# 4. after traversing and performing the operation the updated array need to be checked if it's sorted or not 
class Solution:
    def createPrimeList(self) -> List[int]:
        flag = 0
        primes = [2]
        for num in range(3, 1000):
            for i in range(2, num):
                if num % i == 0:
                    flag = 0
                    break
                if i == num - 1 and flag == 0:
                    flag = 1
            if flag == 1:
                primes.append(num)
            flag = 0
        
        return primes
    
    # we find a prime that is smaller than num
    def findSmallestPrime(self, prime_list: List[int], num: int) -> int:
        prev = 0
        prime = 0
        for p in prime_list:
            if p > num:
                break
            if prev < p < num:
                prime = p
            prev = p
        return prime

    def checkSorted(self, nums) -> bool:
        for i in range(len(nums)-1):
            if nums[i] >= nums[i+1]:
                return False
        return True

    def primeSubOperation(self, nums: List[int]) -> bool:
        prime_list = self.createPrimeList()
        l = len(nums)
        prev = 0
        
        for i in range(l):
            smallest_prime = self.findSmallestPrime(prime_list, nums[i])
            updated_num = nums[i] - smallest_prime
            # if the increasing order does not maintain after first substraction, we do the same thing for second time
            while prev >= updated_num and smallest_prime > 2:
                second_smallest_prime = self.findSmallestPrime(prime_list, smallest_prime)
                smallest_prime = second_smallest_prime
                updated_num = nums[i] - second_smallest_prime

            if(updated_num > prev):
                nums[i] = updated_num
            prev = nums[i]

        print(nums)
        return self.checkSorted(nums)
