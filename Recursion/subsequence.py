#GENERATE ALL THE SUBSEQUENCE

# def func(idx, subset):
#     if idx >= len(nums):
#         result.append(subset.copy())
#         return
#     subset.append(nums[idx])
#     func(idx + 1, subset)
#     subset.pop()
#     func(idx + 1, subset)

# nums = [5,9,7]
# result = []
# func(0, [])
# print(result)


#Time :- O(2^N)
#Space :- O(N) - Stack Space

# --------------------------------------------------------------------

#GENERATE ALL THE SUBSEQUENCE WIHT SUM K
#Brute
# def func(idx, subset, k):
#     if idx >= len(nums):
#         if sum(subset) == k:
#             result.append(subset.copy())
#         return
#     subset.append(nums[idx])
#     func(idx + 1, subset, k)
#     subset.pop()
#     func(idx + 1, subset, k)


# nums = [5,9,4]
# result = []
# k = 9
# func(0, [], k)
# print(result)

#Time :- O(2^N)
#Space :- O(N) - Stack Space

#OPTIMAL

# def backtrack(idx, total, k, subset):
#     if total == k:
#         result.append(subset.copy())
#         return
#     elif total > k:
#         return
#     if idx >= len(nums):
#         return
    
#     subset.append(nums[idx])
#     Sum = total + nums[idx]
#     backtrack(idx + 1, Sum, k, subset)
#     e = subset.pop()
#     Sum -= e
#     backtrack(idx + 1, Sum, k, subset)


# nums = [5,9,4]
# # result = []
# k = 9
# print(backtrack(0, 0, k, []))

#Time :- O(2^N)
#Space :- O(N) - Stack Space

# -----------------------------------------------------------------------

#CHECK IF THERE EXISTS A SUBSEQUENCE

# def backtrack(idx, total, k):
#     if total == k: return True
#     elif total > k: return False
#     if idx >= len(nums): return False

#     Sum = total + nums[idx]
#     pick = backtrack(idx + 1, Sum, k,)
#     if pick: return True
#     Sum = total
#     not_pick = backtrack(idx + 1, Sum, k)
#     return not_pick

# nums = [5,9,4]
# k = 9
# print(backtrack(0, 0, k))

#Time :- O(2^N)
#Space :- O(N) - Stack Space

# ------------------------------------------------------------------------------------

#CHECK IF THERE EXISTS A SUBSEQUENCE IF EXISTS RETURN THE SUBSEQUENCE

# def backtrack(idx, total, k, subset):
#     if total == k:
#         return subset.copy()
    
#     if idx == len(nums) or total > k:
#         return None
    
#     subset.append(nums[idx])
#     Sum = total + nums[idx]
#     pick = backtrack(idx + 1, Sum, k, subset)
#     if pick is not None: return pick
#     subset.pop()
#     Sum = total
#     not_pick = backtrack(idx + 1, Sum, k, subset)
#     return not_pick

# nums = [5, 9, 4]; k = 9
# ans = backtrack(0, 0, k, [])
# print(ans)

#Time :- O(2^N)
#Space :- O(N) - Stack Space

# -------------------------------------------------------------------------------------------

#COUNT ALL THE SUBSEQUENCE

# def backtrack(idx, total, k):
#     if total == k:
#         return 1
#     elif total > k:
#         return 0
#     if idx >= len(nums):
#         return 0
    
#     Sum = total + nums[idx]
#     pick = backtrack(idx + 1, Sum, k)
#     Sum = total
#     not_pick = backtrack(idx + 1, Sum, k)
#     return pick + not_pick

# nums = [5, 9, 4]
# k = 9
# print(backtrack(0, 0, k))

#Time :- O(2^N)
#Space :- O(N) - Stack Space