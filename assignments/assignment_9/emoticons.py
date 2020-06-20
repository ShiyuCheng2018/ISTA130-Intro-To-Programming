"""
Class: ISTA 130
Section Leader: Pranav Talwar
These functions are for hw9
Date: 04/28/2020
Description: The file contains actual Twitter data about tweets that contained emoticons. Each row in the file
represents a single tweet. Each row contains the emoticon text characters, a tweet ID, a user ID, and a timestamp.
"""


def load_twitter_dicts_from_file(filename, emoticons_to_ids, ids_to_emoticons):
    """
    Write a function called load_twitter_dicts_from_file that takes three parameters: filename (the name of a twitter
    data file to read), emoticons_to_ids (an empty dictionary), and ids_to_emoticons (an empty dictionary).
    :param filename: string
    :param emoticons_to_ids: dict
    :param ids_to_emoticons: dict
    :return: none
    """
    read_file = open(filename, 'r')
    for line in read_file.readlines():
        line_array = line.split()

        # initial variables' assignments
        emoticon = line_array[0][1:-1]
        tweet_id = line_array[1]
        user_id = line_array[2][1:-1]
        date = line_array[3]

        # crate dictionaries
        if emoticon in emoticons_to_ids.keys():
            emoticons_to_ids[emoticon].append(user_id)
        else:
            emoticons_to_ids[emoticon] = [user_id]

        if user_id in ids_to_emoticons.keys():
            ids_to_emoticons[user_id].append(emoticon)
        else:
            ids_to_emoticons[user_id] = [emoticon]


def find_most_common(twitter_dicts):
    """
    Write a function called find_most_common that takes a single dictionary parameter. Assume the keys of the dictionary
     will be strings (e.g. emoticons) and each value will be a list of strings (e.g. user ID's).
    :param twitter_dicts: dict
    :return: string
    """
    max_length = -1 # initial the max-length
    result_key = "Not Found"

    for key, value in twitter_dicts.items():
        if max_length <= len(value):  # compare the numbers
            result_key = key
            max_length = len(value)

    print(result_key.ljust(21)+"occurs"+str(max_length).rjust(9)+" times")

    return result_key


def main():
    emoticons_to_ids = {}
    ids_to_emoticons = {}

    load_twitter_dicts_from_file("twitter_emoticons.dat", emoticons_to_ids, ids_to_emoticons)
    print(f"Emoticons: {len(emoticons_to_ids)}")
    print(f"UserIDs:   {len(ids_to_emoticons)}")

    # repeat 5 times to print
    common_emo = find_most_common(emoticons_to_ids)
    emoticons_to_ids.pop(common_emo)
    common_emo = find_most_common(emoticons_to_ids)
    emoticons_to_ids.pop(common_emo)
    common_emo = find_most_common(emoticons_to_ids)
    emoticons_to_ids.pop(common_emo)
    common_emo = find_most_common(emoticons_to_ids)
    emoticons_to_ids.pop(common_emo)
    common_emo = find_most_common(emoticons_to_ids)
    emoticons_to_ids.pop(common_emo)


if __name__ == '__main__':
    main()


'''
     设定最小值为-1，(list长度不可能小于-1），取变量名为max_length,
     设定最后的结果表情名字为""， 取变量名为result_emo
     
     循环字典的key和value:
        如果value的长度 >= max_length:
            那么max_length = value的长度
            并且， 将这个key赋值给result_emo
        （没有否则）
     
     已找到最大值的表情， 打印

'''