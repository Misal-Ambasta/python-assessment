from collections import Counter
def analyze_numbers(nums: list[int]) -> dict:
    sum = 0
    for i in nums:
        sum += i

    return {"mean": sum/len(nums), "median": ..., "mode": Counter(nums), "variance": ...}


new_nums = [2,3,4,6,3,3,4,5,1,7,3]
print(analyze_numbers(new_nums))