# #
# # n = int(input("How many marks? "))
# #
# # total = 0
# #
# # for i in range(n):
# #     mark = int(input(f"Enter mark {i+1}: "))
# #     total = total + mark
# #
# # average = total / n
# #
# # print("Total:", total)
# # print("Average:", average)
#
#
# # n = int(input("How many marks? "))
# #
# # total = 0
# #
# # for i in range(1, n + 1):
# #     mark = int(input(f"Enter mark {i} (0–100): "))
# #     total += mark
# #
# # average = total / n
# #
# #
# # print("Total marks:", total)
# # print("Average marks:", average)
#
# # sentence = input("Enter a sentence: ")
# #
# # count = 0
# #
# # for ch in sentence:
# #     if ch != " ":
# #         count += 1
# #
# # print("Number of non-space characters:", count)
#
# # n = int(input("How many marks will you enter? "))
# #
# # max_mark = 0
# #
# # for i in range(n):
# #     mark = int(input(f"Enter mark {i + 1}: "))
# #     if mark > max_mark:
# #         max_mark = mark
# #
# # print("Highest mark entered:", max_mark)
#
# # n = int(input("How many marks will you enter? "))
# #
# # pass_count = 0
# #
# # for i in range(n):
# #     mark = int(input(f"Enter mark {i + 1}: "))
# #
# #     if mark >= 40:
# #         print(mark)
# #         pass_count += 1
# #
# # print("Number of students passed:", pass_count)
#
# # n = int(input("How many numbers will you enter? "))
# #
# # numbers = []
# #
# # for i in range(n):
# #     num = int(input(f"Enter number {i + 1}: "))
# #     numbers.append(num)
# #
# # for num in numbers:
#
# word = input("Enter a word: ")
#
# reversed_word = ""
#
# for ch in word:
#     reversed_word = ch + reversed_word
#
# print("Reversed word:", reversed_word)

# for row in range(1, 6):
#     for col in range(row):
#         print("*", end="")
#     print()
#
# for row in range(3):
#     for col in range(4):
#         print("*", end="")
#     print()

for row in range(1, 6):  # Outer loop: row = 1 to 5
    line = ""  # Start with empty line

    for col in range(1, 6):  # Inner loop: col = 1 to 5
        value = row * col
        line = line + f"  {value}"

    print(line)  # Print one complete row

