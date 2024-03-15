class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prod, right_prod = 1, 1
        result = [1] * len(nums)
        n = len(nums)

        for i in range(1, n):
            left_prod *= nums[i-1]
            result[i] *= left_prod 
        
        for i in range(n-2, -1, -1):
            right_prod *= nums[i+1]
            result[i] *= right_prod
        
        return result

        # nums_size = len(nums)
        # cumu_prod = [1]*(nums_size+1) #increased the index in left to tackel the (i-1) index for out of range issue
        # for i in range(1, nums_size+1):
        #     cumu_prod[i] = cumu_prod[i-1]*nums[i-1]
        
        # rotate_cumu_prod = [1]*(nums_size+1) #same reason increased the range for (i+1) issue
        # for i in range(nums_size-1, -1, -1):
        #     rotate_cumu_prod[i] = rotate_cumu_prod[i+1]*nums[i]
            
        # # input array => [1,2,3,4]
        # print(cumu_prod) # [1, 1, 2, 6, 24]
        # print(rotate_cumu_prod) # [24, 24, 12, 4, 1]
        
        # result_list = []
        # for i in range(1, nums_size + 1):
        #     result_list.append(cumu_prod[i-1]*rotate_cumu_prod[i])
        
        # return result_list 

        