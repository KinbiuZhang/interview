'''

字符A-Z可以编码为0-25。"A"->"0", "B"->"1", ..., "Z"->"25"
现在输入一个数字序列，计算有多少种方式可以解码成字符A-Z组成的序列。

例如：

输入：19
输出：2

输入：258
输出：2

输入：0219
输出：3


'''

def how_many_ways(digitarray):
    # implement here
    def how_many_ways(digitarray):
    digitarray = digitarray.lstrip('0')
    length = len(digitarray)
    if length == 0:
        return 0
    li = list(range(length+1))
    li[0] = 1
    for i in range(length+1):
        if i == 0:
            continue
        if digitarray[i-1] == '0':
            li[i] = 1
        else:
            li[i] = li[i-1]
            #判断当前字符跟前一个字符是否可以凑成一个字母所对应的值
        if (i>1 and int(digitarray[i-1])<=6 and int(digitarray[i-2])==2) or (i>1 and int(digitarray[i-2])==1):
                li[i] += li[i-2]
        # print(li)
    print(li[length])

if __name__ == '__main__':
    how_many_ways('119')
