import multiprocessing
from time import ctime

def consumer(input_q):
    print("Into consumer:", ctime())
    while True:
        # 处理锁
        item = input_q.get()
        if item == None:
            break
        print("pull", item, "out of q")# 此处替换为有用的工作

    print("Out of consumer:", ctime()) #此句未执行

def producer(sequence, output_q):
    print("Into producer:", ctime())
    for item in sequence:
        output_q.put(item)
        print("put", item, "into q")
    print("Out of producer:", ctime())

if __name__ == '__main__':
    q = multiprocessing.Queue()
    cons_q1 = multiprocessing.Process(target=consumer, args=(q, ))
    cons_q1.start()

    cons_q2 = multiprocessing.Process(target=consumer, args=(q,))
    cons_q2.start()

    sequence = [1,2,3,4]
    producer(sequence, q)

    q.put(None)
    q.put(None)

    cons_q1.join()
    cons_q2.join()