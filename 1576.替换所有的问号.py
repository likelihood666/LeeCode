#暴力遍历
def modifyString(s):
    n = len(s)
    re = ""
    if n == 1:
        if s[0] == "?":
            re += "a"
            return re
        else:
            return s
    for i in range(n):
        if i == 0 and s[0] == "?":
            if s[1] != "a":
                re += "a"
            else:
                re += "b"
        elif i == n - 1 and s[n - 1] == "?":
            if s[i - 1] != "a" and re[i - 1] != "a":
                re += "a"
            else:
                re += "b"
        elif s[i] != "?":
            re += s[i]
        elif 0 < i < n - 1 and s[i] == "?":
            if s[i - 1] != "a" and s[i + 1] != "a" and re[i - 1] != "a":
                re += "a"
            elif s[i - 1] != "b" and s[i + 1] != "b" and re[i - 1] != "b":
                re += "b"
            else:
                re += "c"
    return re
