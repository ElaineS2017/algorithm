#-*- coding:utf-8 -*-
def reCodeStr(string):
    rst = ''
    tmp = 1
    for _i,j in enumerate(string):
        if _i + 1 < len(string) and j == string[_i + 1]:
            tmp += 1
        else:
            rst = rst + str(tmp) + j
            tmp = 1
    return rst 

print "重新编码字符串"
test = 'AAAABCCDAA'
print reCodeStr(test)


def lastWordLength(string):
    """
        计算字符串最后一个单词的长度，单词以空格隔开
    """
    return string.strip()[string.strip().rindex(" ") + 1 : ]

print "字符串最后一个单词"
string = "hello world"
print lastWordLength(string)


"""
    KMP 算法
"""
def pattern_next(s):  
    prefix = [s[:i+1] for i in range(len(s)-1)]
    suffix = [s[i+1:] for i in range(len(s)-1)]
    l = list(set(prefix) & set(suffix))
    return len(l)

def match(target, pattern):
    i = j = 0
    n, m = len(target), len(pattern)
    while i < n and j < m:
        # 如果字符相等则目标和模板的下标都向右移
        if target[i] == pattern[j]:
            print "目标和模板的下标都向右移"
            i, j = i+1, j+1
        else:
            # 这里通过next 函数来判断位移个数
            i = i - j + pattern_next(pattern[:j])
            j = 0
            print "通过next 函数来判断位移个数i=",i
    if j == m:
        return i - j
    return -1

print "KMP"
# print match("aaaaaaaaaaaaaaaaaaaab", "aaab")

def getNext(pattern, next):
    j = 0
    plen = len(pattern)
    next.append(0)
    for i in range(1, plen):
        while j > 0 and pattern[j] != pattern[i]:
            j = next[j-1]
        if pattern[i] == pattern[j]:
            j = j + 1
        next.append(j)

def kmp_search(text, pattern, next):
        j = 0;
        plen = len(pattern)
        tlen = len(text)
 
        for i in range(0, tlen):
                while j > 0 and text[i] != pattern[j]:
                        j = next[j-1]
 
                if text[i] == pattern[j] :
                        j = j + 1;
 
                if j == plen :
                    print "from ", i-j+1, "to ", i
                    j = next[j-1]
# text = "aaaaaaaaaaaaaaaaaaaab"
# pattern = "aaab"
# next = []
# getNext(pattern, next)
# print next
# kmp_search(text, pattern, next)
# print text
# print pattern

# text1 = ("abababababababababa")
# pattern1 = ("ababab")
# next1 = []
# getNext(pattern1, next1)
# print next1
# kmp_search(text1, pattern1, next1)
# print text1
# print pattern1

next = []
getNext("agctagcagctagctg", next)
print '*',next