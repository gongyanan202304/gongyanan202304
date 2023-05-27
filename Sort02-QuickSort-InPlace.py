# 快速排序-本地排序（Quick-Sort-Inplace）

def inplace_quick_sort(lst, a, b):
    if a >= b:
        return
    pivot = lst[b]
    left = a
    right = b - 1
    
    while left <= right:
        
        while left <= right and lst[left] < pivot:
            left += 1
        
        while left <= right and pivot < lst[right]:
            right -= 1
        
        if left <= right:
            lst[left], lst[right] = lst[right], lst[left]
            left, right = left + 1, right - 1
    
    lst[left], lst[b] = lst[b], lst[left]

    inplace_quick_sort(lst, a, left - 1)
    inplace_quick_sort(lst, left + 1, b)


# 主函数
if __name__ == "__main__":
    nums = [27, 34, 43, 79, 98, 86, 58, 65]
    inplace_quick_sort(nums, 0, len(nums)-1)
    print(nums)
