def underscored(camelcase):
    return "".join(list(map(lambda x: "_"+x if x.isupper() else x, camelcase)))


def split(my_string, command):
    result = []
    string = ""
    for each in my_string:
        if each != command:
            string += each
        else:
            result.append(string)
            string = ""
    return result.append(string)

