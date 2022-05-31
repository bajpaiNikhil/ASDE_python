arr = [335, 501, 170, 725, 479, 359, 963, 465, 706, 146, 282, 828, 962, 492, 996, 943, 828, 437, 392, 605, 903, 154, 293, 383, 422, 717, 719, 896, 448, 727, 772, 539, 870, 913, 668, 300, 36, 895, 704, 812, 323, 334]

# s = "335 501 170 725 479 359 963 465 706 146 282 828 962 492 996 943 828 437 392 605 903 154 293 383 422 717 719 896 448 727 772 539 870 913 668 300 36 895 704 812 323 334"
# l=[]
# for i in s.split(" "):
#     l.append(int(i))
# print(l)
target = 468

left = 0
right = len(arr) - 1
arr.sort()
print(arr[left], arr[right])

while left < right:
    if arr[left] + arr[right] == target:
        print("Yes")
        break
    elif arr[left] + arr[right] > target:
        right -= 1
    else:
        left += 1
print("No")
