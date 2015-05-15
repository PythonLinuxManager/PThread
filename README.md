# PThread
Python Thread Study
1.  Python Thread 基础
        在sleep千分之一秒后可以发现，多线程的随机运行
        线程的创建：
            继承threading.Thread类，覆写run方法
                run方法是设定线程的工作，比如输出，操作字符串，文件，列表等
        线程的运行：
            创建“继承threading.Thread类”，调用对象的start()方法，线程运行
            每个对象的start方法只能调用一次
        需要注意的是：
            每个线程一定会有一个名字，尽管上面的例子中没有指定线程对象的name，但是python会自动为线程指定一个名字。
            当线程的run()方法结束时该线程完成。
            无法控制线程调度程序，但可以通过别的方式来影响线程调度的方式。
            基本的运行里没有共享数据，没有锁的实现
2.  Python 