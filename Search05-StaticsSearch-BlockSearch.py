# 分块查找（索引顺序查找）（BlockSearch）

# 分块查找的基本思想：
# 数据表分成多个子表（分块），子表中的起始位置和子表中的最大关键字构成一个索引顺序表；
# 数据表中的数据可以无序；
# 索引顺序表中的数据有序；
# 分块有序的概念：
#   第二个分块中的所有关键字大于第一个分块中的最大关键字，第三个分块中的所有关键字都大于第二个分块中的最大关键字，依次类推

# 如何保证分块有序? 这个问题需要进一步的研究，先设计对有序表的分块查找算法的程序设计。

# 分块的基本方式：一般是将数据表均匀分成b块，但是根据平均查找性能分析，分块的数据是数据列表元素个数的平方根
# 假定数据表有序

# 分块查找算法的程序设计：
def blocksearch(datalist, blocks, keyvalue):
    """datalist: 待查找的数据列表
         blocks: 分块数目
       keyvalue: 待查关键字
    """
    
    # 创建索引顺序表
    indexseqlist = []
    
    # 块平均长度
    blockavglen = len(datalist)//blocks
    
    # 创建索引顺序表
    for i in range(blocks):
        blockstartindex = blockavglen * i
        blockendindex = blockavglen * (i+1) if i < blocks-1 else len(datalist)
        block = datalist[blockstartindex:blockendindex]
        maxblockkey = max(block)
        indexseqlist.append([maxblockkey, blockstartindex, blockendindex])

        # 查找关键字
        if keyvalue <= maxblockkey:
            # 计算式子后面不要+1，因为blockstartindex位置上的元素就是block中的0号元素
            return blockstartindex + block.index(keyvalue)
            
  
# 主函数
if __name__ == "__main__":
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    print(blocksearch(nums, 3, 15))
