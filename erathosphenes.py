#! usr/env/python python
import cProfile

# asimpthotic:
# 1 + (ln(n) * ln(n)) + (ln(n) * ln(n)) = ln(n)
def get_first_greater(pos, nums):
    return pos+1 if nums[pos+1] else get_first_greater(pos+1, nums)

def filter_with_step(pos, nums):
    count = 0
    while count < len(nums) - pos:
        count += pos
        if nums[count] % pos == 0 and nums[count] != pos:
            nums[count] = False
        continue
    return nums

def end_or_repeat(nums, pos=2):
    if pos**2 > len(nums):
        return [num for num in nums if num]
    prime = filter_with_step(pos, nums)
    pos = get_first_greater(pos, prime)
    return end_or_repeat(prime, pos)

def erathosphenes(up_to):
    nums = range(up_to+1)
    return end_or_repeat(nums)

def test_runtime():
    return cProfile.runctx('erathosphenes(100)', globals(), locals())
