import os, re, pathlib

def get_dir(dirname = str(pathlib.Path.home())):
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")

    list_dirs = list()
    content = list()

    dir_dict = dict()

    step = 0

    for i in os.listdir(dirname):
        if os.path.isdir(dirname + "/" + i):
            step += 1
            dir_dict[step] = i
            content.append("{num}   {dir}\n".format(num = step, dir = i))
        content_result = "".join(content)

    selected = input("已选择的文件夹'{selected}'\n\n请输入要选择的文件夹(按q确认):\n{content}\n".format(selected = dirname,content = content_result))

    if selected == "q":
        return 0
    else:
        result = dirname + "/" + dir_dict[int(selected)]
        get_dir(result)
        return result



def find_file(root_dir, file_type):
    list_dir = os.listdir(root_dir)
    list_file = list()
    compile = re.compile(r"^(.*?)..{}$".format(file_type))
    for dir in list_dir:
        dir = "{root_dir}/{dir}".format(root_dir=root_dir, dir=dir)
        if os.path.isdir(dir):
            list_file = list_file + find_file(dir, file_type)
        elif re.findall(compile, dir):
            list_file.append(dir)
    return list_file


if __name__ == '__main__':
    dir = get_dir()
    find = input("请输入要查找的文件扩展名:\n")
    print(find_file(dir, find))
