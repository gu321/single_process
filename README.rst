Limit python script just run a single process

::

    from single_process import single_process

    single_process()

    def main():
        from time import sleep
        sleep(6000)

    if __name__ == "__main__":
        main()
