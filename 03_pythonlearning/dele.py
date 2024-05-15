def trim_strongholds(strongholds):
    new_list = strongholds
    del new_list[0]
    del new_list[-2:]
    return new_list

