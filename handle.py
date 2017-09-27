import re, csv
from settings import SETTING_STR

str_re = SETTING_STR['str_re']
str_path = SETTING_STR['str_path']
str_path_out = SETTING_STR['str_path_out']
is_revese = SETTING_STR['is_reverse']
max_show = SETTING_STR['max_show']


def open_file():
    with open(str_path, 'r', encoding="utf-8") as f:
        result_list = []
        for line in f:
            result_list.extend(re.findall(str_re, line))

    return result_list


def count_words(word_list):
    ret = {}
    for item in word_list:
        ret[item] = ret.get(item, 0) + 1

    return ret


def show_result(dic_ret):
    for k, count in sorted(dic_ret.items(), key=lambda x: x[1], reverse=is_revese)[:max_show]:
        print("{0:11}{1}".format(k, count))


def save_result(dic_ret):
    with open(str_path_out, "w") as csvfile:
        writer = csv.writer(csvfile)
        for key in dic_ret:
            writer.writerow([key, dic_ret[key]])
