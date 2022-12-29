def countSubStr(el):
    count = el.count("Emma")
    return "Emma appeared "+str(count)+" times"

str_x = "Emma is good developer. Emma is a writer."
print(countSubStr(str_x))