from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def fun(i):
    return i ** 2


def pr(con):
    p = con.result()
    print(p)


if __name__ == '__main__':
    p_pool = ProcessPoolExecutor(max_workers=4)  #创建一个含有四个进程的池
    for i in range(10): #10个任务
        p = p_pool.submit(fun, i)  #任务提交
        p.add_done_callback(pr)  #指定回调函数
    p_pool.shutdown()#关闭池
