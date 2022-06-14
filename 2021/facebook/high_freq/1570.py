class SparseVector:
    def __init__(self, nums: List[int]):


    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        if len(nums1) != len(nums2):
            return False
        res = 0
        for i in range(len(nums1)):
            if nums1[i] == 0 or nums2[i] == 0:
                continue
            res += nums1[i]*nums2[i]
        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)

nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]