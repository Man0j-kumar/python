def removethird(int_list):
    pos=2
    idx=0
    len_list=(len(int_list))
    while len_list>0:
        idx=(pos+idx)%len_list
        print(int_list.pop(idx))
        len_list-=1
nums=[int(x) for x in input().split()]
removethird(nums)