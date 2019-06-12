import time
import _thread as thread


def loop1(in1):
    print('start loop 1 at:', time.ctime())
    print("我是参数", in1)
    time.sleep(4)
    print('End loop 1 at:', time.ctime())

def loop2(in1, in2):
    print('start loop 2 at:', time.ctime())
    print("我是参数", in1, "和参数", in2)
    time.sleep(2)
    print('End loop 2 at:', time.ctime())

def main():
    print('starting at:', time.ctime())
    # 参数两个，一个需要运行的函数名，第二个是函数的参数作为元祖使用
    # 注意：如果函数只有一个参数，需要参数后有一个逗号
    thread.start_new_thread(loop1, ("1", ))

    thread.start_new_thread(loop2, ("1", "2"))

    print('All done at:', time.ctime())


if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)