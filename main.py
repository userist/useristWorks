from handle import open_file, count_words, show_result, save_result

if __name__ == '__main__':
    words = open_file()
    ret = count_words(words)
    show_result(ret)
    save_result(ret)
