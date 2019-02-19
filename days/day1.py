import sys


def first_half(fin):
    nums = [int(i) for i in fin]
    return sum(nums)


def second_half(fin):
    nums = [int(i) for i in fin]
    seen = set()
    x = 0
    while True:
        for i in nums:
            x += i
            if x in seen:
                return x
            seen.add(x)


if __name__ == "__main__":
    print(second_half(sys.stdin))
