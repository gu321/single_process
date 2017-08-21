README
=============

SETUP
-------------

:: 

    pip install -U single_process


USE
-------------

Limit python script just run a single process, support python3

You only need to import the single_process.init module directly

::

    import single_process.init


Of course, you can also manually call the single_process function

::

    from single_process import single_process

    single_process()

    def main():
        from time import sleep
        sleep(6000)

    if __name__ == "__main__":
        main()

中文说明
=============

安装
-------------

:: 

    pip install -U single_process


使用
-------------

限制一个python脚本只运行一个进程，支持python3
只需要直接 import single_process.init 模块

::
    
    import single_process.init

当然，你也可以手工调用 single_process 函数

::

    from single_process import single_process

    single_process()

    def main():
        from time import sleep
        sleep(6000)

    if __name__ == "__main__":
        main()
