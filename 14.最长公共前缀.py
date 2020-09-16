def longestCommonPrefix(strs):
    ans = ""
    #zip函数用来将strs中每一项的元素按照下标组合成一个新的元组
    for i in zip(*strs):
        #set函数是用来去重的，如果i里面全是同一个字符，则set(i)只保留一个
        if len(set(i)) == 1:
            ans += i[0]
        else:
            break
    return ans