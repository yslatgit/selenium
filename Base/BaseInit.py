from Base.BaseElementEnmu import Element
from Base.BasePickle import *
from Base.BaseFile import *

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def mk_file():
    destroy()
    #创建需要的文件夹以及文件
    mkdir_file(PATH("../Log/"+Element.INFO_FILE))
    mkdir_file(PATH("../Log/"+Element.SUM_FILE))
    # 读取一个空的data={}
    data = read(PATH("../Log/"+Element.INFO_FILE))

    data["version"] = "2018.11.12"
    data["sum"] = 0
    data["pass"] = 0
    data["fail"] = 0
    #往这个文件中写入data
    write(data=data, path=PATH("../Log/"+Element.SUM_FILE))





def destroy():
    """如果老的文件存在删除它"""
    remove_file(PATH("../Log/"+Element.INFO_FILE))
    remove_file(PATH("../Log/"+Element.SUM_FILE))
    # remove_file(PATH("../Log/"+Element.DEVICES_FILE))


if __name__ == '__main__':
    # destroy()
    # print(destroy())
    # print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    mk_file()
