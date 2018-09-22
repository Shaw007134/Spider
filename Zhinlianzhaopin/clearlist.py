# This function will clear the string list format

def clearlist(strlist):
    #strlist = list(set(strlist))
    #strlist = [(str.replace("/n",'').strip()) for str in strlist]
    seen = set()
    unique_strlist = []
    for str in strlist:
        if str != "\n" and str not in seen:
            unique_strlist.append(str)
            seen.add(str)
    return unique_strlist