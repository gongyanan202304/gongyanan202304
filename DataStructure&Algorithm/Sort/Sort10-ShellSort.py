# 希尔排序（ShellSort）


def shellsort(numberslist):
    n = len(numberslist)
    gap = n // 2
    
    while gap > 0:
        for i in range(gap, n):
            
            curnum, preindex = numberslist[i], i - gap
            
            while preindex >= 0 and curnum < numberslist[preindex]:
                numberslist[preindex + gap] = numberslist[preindex]
                preindex -= gap
            
            numberslist[preindex + gap] = curnum
        
        gap = gap // 2
    
    return numberslist


# 主函数
if __name__ == "__main__":
    nums = [3, 4, 5, 6, 9, 2, 1, 0, 10, 7, 12, 8]
    print('>> shell sort:')
    print(shellsort(nums))
