def get_keys(my_dict):
    '''
    Write a function called get_keys that takes a dictionary and a value as arguments. It returns a list of every key
    that maps to the given value.
    :param my_dict: dictionary
    :return: list
    '''
    return my_dict.items

def main():
    '''
    In main, write a line of code that creates a dictionary called my_dict that maps the key 'chocolate' to the list
     ['chip', 'cake']. Write a line of code the adds the item 'ice cream' to the list associated with the key 'chocolate'.
      Given a variable sweet, write an if-else block that checks to see if sweet is a key in the dictionary and if it is,
       adds 'mousse' to the list associated with the key; other wise it creates a new key-value pair with sweet as the key
        and a list containing 'mousse' as the value.
    :return:
    '''

    my_dict = {"chocolate": ["chip", "cake"]}
    my_dict["chocolate"].append("ice cream")

    if not "sweet" in my_dict.keys():
        my_dict["sweet"] = ["mousse"]
    else:
        my_dict["sweet"].append("mousse")


main()