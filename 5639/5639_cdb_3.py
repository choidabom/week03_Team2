import sys
sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def getPostorder(nums):
    length = len(nums)
    
    if length <= 1:
        return nums

    for i in range(1, length):
        if nums[i] > nums[0]:
            return getPostorder(nums[1:i]) + getPostorder(nums[i:]) + [nums[0]]

    return getPostorder(nums[1:]) + [nums[0]]

if __name__ == '__main__':
    # [50, 30, 24, 5, 28, 45, 98, 52, 60]
    # length = 9
    nums = []
    while True:
        try:
            nums.append(int(input()))
        except:
            break
    
    nums = getPostorder(nums)
    for n in nums:
        print(n)