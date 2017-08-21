import os
import sys
import tempfile
import logging
import fcntl
import errno
import signal
from signal import SIGABRT,  SIGILL, SIGINT, SIGSEGV, SIGTERM, signal, SIGQUIT
import atexit


def signal_handler(signal, frame):
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGQUIT, signal_handler)
    signal.signal(signal.SIGTSTP, signal_handler)


def single_process():
    filename = os.path.abspath(sys.argv[0])
    lock_file_name = filename.lstrip('/').replace('/', '_') + '.lock'

    lock_file_path = os.path.join(
        tempfile.gettempdir(), lock_file_name)
    fd = os.open(lock_file_path, os.O_CREAT | os.O_RDWR, 0o660)
    try:
        fcntl.lockf(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except IOError as e:
        if e.errno in (errno.EACCES, errno.EAGAIN):
            logging.error(
                '%s RUNNING . QUIT' % filename
            )
            sys.exit(0)
        else:
            raise

    def exit(signal, frame):
        os.close(fd)
        os.remove(lock_file_path)
        sys.exit(signal)

    for sig in (SIGABRT,  SIGILL, SIGINT, SIGSEGV, SIGTERM, SIGQUIT):
        signal(sig, exit)
    atexit.register(lambda: exit(0, 0))


if __name__ == "__main__":

    single_process()

    def test():
        from time import sleep
        from datetime import datetime
        for i in range(3):
            print(datetime.now())
            sleep(1)
    test()
