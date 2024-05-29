def merge(dict1, dict2):
    merged_dict = {}
    
    for name in dict1:
        merged_dict[name] = dict1[name]

    for name in dict2:
        merged_dict[name] = dict2[name]

    return merged_dict


def total_score(score_dict):
    total = 0

    for score in score_dict:
        total = total + score_dict[score]

    return total

