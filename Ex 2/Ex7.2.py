import os


def get_files():
    files_list = []
    for files in os.listdir('.'):
        if files.endswith('.txt'):
            files_list.append(files)
    return files_list


def safeguard(file):
    if 'merge.txt' in file:
        file.remove('merge.txt')


def len_sort(files):
    merge = {}
    for name in files:
        with open(name, encoding='UTF-8') as file:
            temp = file.readlines()
            count = len(temp)
            temp.insert(0, f'{count}\n')
            merge[name] = temp
    merge_sorted = dict(sorted(merge.items(), key=lambda x: x[1]))
    return merge_sorted


def write_result(merged_files):
    with open('merge.txt', 'w') as file:
        for i in merged_files.keys():
            file.write(f'{i} \n')
            file.write(' '.join(merged_files.get(i)))
            file.write('\n')


def main():
    file = get_files()
    safeguard(file)
    merge = len_sort(file)
    write_result(merge)


main()
