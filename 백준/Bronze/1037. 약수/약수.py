n = int(input())
nums = list(map(int,input().split()))

_min = min(nums)
_max = max(nums)
if _min == _max:
    print(_min**2)
else:
    print(_min * _max)
