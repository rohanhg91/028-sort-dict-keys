def solution(dic):
    """Enter Code Here"""
    i = 0
    f = []

    while i < len(dic):
        field, value = dic.items()[i]
        f.append(field)
        i = i + 1
    return f



'''
a = solution({1: 12, 2: 23, 5: 34,8: 90})
print a
'''
