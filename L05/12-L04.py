def min_time_to_defeat_zombies(n, m, times):
    def is_possible(time):
        total_zombies = 0
        for t in times:
            total_zombies += time // t
            if total_zombies >= m:
                return True
        return total_zombies >= m
    
    left, right = 1, max(times) * m
    while left < right:
        mid = (left + right) // 2
        if is_possible(mid):
            right = mid
        else:
            left = mid + 1
    
    return left

n, m = map(int, input().strip().split())
times = []
for _ in range(n):
    times.append(int(input().strip()))

result = min_time_to_defeat_zombies(n, m, times)
print(result)
