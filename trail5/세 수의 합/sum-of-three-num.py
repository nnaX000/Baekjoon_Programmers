from collections import defaultdict

n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

answer=0

for i in range(n - 2):

    left = i + 1
    right = n - 1

    while left < right:

        total = arr[i] + arr[left] + arr[right]

        if total < k:
            left += 1
        elif total > k:
            right -= 1
        else:
            # A[left]랑 A[right] 값이 다른 경우
            if arr[left] != arr[right]:
                left_value = arr[left]
                right_value = arr[right]

                left_count = 0
                while left <= right and arr[left] == left_value:
                    left_count += 1
                    left += 1

                right_count = 0
                while left <= right and arr[right] == right_value:
                    right_count += 1
                    right -= 1

                answer += left_count * right_count

            # A[left]랑 A[right] 값이 같은 경우
            else:
                count = right - left + 1
                answer += count * (count - 1) // 2
                break

print(answer)