
def SearchJSONList(list, target, targetField):
    found = False
    for i in list:

        if i[targetField] == target:
            found = True
            return i
    return None
