import multiprocessing
from time import ctime

def consumer(input_q):
    print("Into consumer:", ctime())
    while True:
        # 处理锁
        item = input_q.get()
        print("pull", item, "out of q")# 此处替换为有用的工作
        input_q.task_done()# 发出信号通知任务完成
    print("Out of consumer:", ctime()) #此句未执行

def producer(sequence, output_q):
    print("Into producer:", ctime())
    for item in sequence:
        output_q.put(item)
        print("put", item, "into q")
    print("Out of producer:", ctime())

if __name__ == '__main__':
    q = multiprocessing.JoinableQueue()
    cons_q = multiprocessing.Process(target=consumer, args=(q, ))
    cons_q.daemon = True
    cons_q.start()

    sequence = [1,2,3,4]
    producer(sequence, q)
    cons_q.join()