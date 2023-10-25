# task 1
# def findNum(nums):
#     for num in nums:
#         if nums.count(num) > len(nums) // 2:
#             return num
#     return 0
#
# print(findNum([1, 4, 4, 4, 9, 9, 9, 9, 9]))

# task 2
# def svoiSis(binNum):
#     decimal_num = 0
#     for digit in binNum:
#         decimal_num = decimal_num * 2 + int(digit)
#     return decimal_num
#
#
# print(svoiSis('10101110011'))
# task 3
# def string_to_int(str):
#     str = str.strip()
#     sign = 1
#
#     if str and str[0] == '-':
#         sign = -1
#         s = str[1:]
#
#     result = 0
#     for char in str:
#         if '0' <= char <= '9':
#             result = result * 10 + (ord(char) - ord('0'))
#         else:
#             break
#
#     return result * sign
#
#
# print(string_to_int('69'))
# print(string_to_int('-69'))
# print(string_to_int('6969 words'))
# task 4
# def delDubl(nums):
#     unique_nums = list(set(nums))
#
#     if len(nums) % 2 != 0:
#         unique_nums.append(nums[-1])
#
#     for i in range(0, len(unique_nums) - 1, 2):
#         unique_nums[i], unique_nums[i + 1] = unique_nums[i + 1], unique_nums[i]
#
#     return unique_nums
#
# print(delDubl([2, 3, 1, 6, 8, 9, 66, 66]))


