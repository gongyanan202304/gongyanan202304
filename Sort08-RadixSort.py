# 基数排序（Radix Sort）
# 基数排序的基本思想：
# 对数据元素中的每一位元素从低位到高位进行排序，基数排序是基于分别排序、分别收集，因此是稳定的。
# 加入数组中的最大值是3位数，需要从个位开始一直到百位的数据，依次要进行个位入桶、个位出桶、十位入桶、十位出桶、百位入桶、百位出桶操作。
# 桶中的数据元素是按照先进后出的方式

# 基数排序的基本步骤：
# （1）取数据中最大的数据，并取得位数，即为迭代的次数N；
# （2）在原始数组中，从最低位开始取每个位组成基数数组Radix;
# （3）对基数数组进行收集；
# （4）将Radix数组依次赋给原数组；
# （5）重复步骤（2）（3）（4）N次。


# 基数排序算法设计：
def radixsort(datalist):
    
    # 基数为10
    base, div = 10, 1
    # 最高的位数
    highbit = len(str(max(datalist)))
    
    # 构建10个桶（0～9）
    bucket = [[] for _ in range(base)]
    
    while highbit:
        for item in datalist:
            # 由列表中的数据元素的位上的数据获取进入中的编号
            bucketno = (item // div) % base   # 先整除再求余数
            
            # 数据按照所求的数据位上的数据来安排进入桶
            bucket[bucketno].append(item)
            
        # 数据元素出桶
        i = 0
        for subbucket in bucket:
            # 当前子桶内的数据依次赋给原数组
            while subbucket:
                datalist[i] = subbucket.pop(0)
                i += 1
        
        div *= 10
        highbit -= 1
    
    return datalist


# 主函数
if __name__ == "__main__":
    nums = [53, 35, 24, 25, 27, 29, 28, 82, 39, 93, 64, 46, 2, 20, 10, 11, 9, 90, 8, 18, 46]
    print(radixsort(nums))

# 思考：
# 基数排序中求出低位，次低位，次高位，高位、最高位的方法是一样的：先整除再求余数
# 在基数排序中，基数是指Radix的取值范围，例如：是整数的数据大小比较的话，基就是10进制（0～9），
# 如果是字母，则是26个字母。

# 暂时思考一下，后期继续！
