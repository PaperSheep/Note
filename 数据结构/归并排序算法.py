def merge(left, right):
    '''合并和排序'''
    i = 0
    j = 0
    result = []
    length_left = len(left)
    length_right = len(right)
    
    while i < length_left and j < length_right:
        # 逐个比较两个列表的元素
        # 小的添加进新列表，大的留下继续比较
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    # 最后加上未比较的元素
    result.extend(left[i:])
    result.extend(right[j:])
    # print(result)
    return result
    
def merge_sort(lists):
    '''归并排序入口，拆分列表'''
    # 递归退出条件判断
    length = len(lists)
    if length <= 1:
        return lists
        
    # 递归拆分，取整，兼容py3
    mid = length // 2
    left = merge_sort(lists[:mid])
    right = merge_sort(lists[mid:])
    
    # 合并排序（归并排序）
    return merge(left, right)


import random
 
lists = random.sample(range(2000000), 1000000)
# lists = [4,3,7,82,34,1,5,2,36,8,6,75,8,49,1,90,2,301,3,78,42,3,6,7,85]
result = merge_sort(lists)
print(result)
