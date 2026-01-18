# for row in range(1, 6):
#     for col in range(row):
#         print("*", end="")
#     print()
#
# for row in range(3):
#     for col in range(4):
#         print("*", end="")
#     print()

for row in range(1, 6):
    line = ""

    for col in range(1, 6):
        value = row * col
        line = line + f"  {value}"

    print(line)  # Print one complete row
