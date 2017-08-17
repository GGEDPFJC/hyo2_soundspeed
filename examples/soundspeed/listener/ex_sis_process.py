import logging
import time

from hyo.sis.lib.process import SisProcess

logger = logging.getLogger()


def main():
    # multiprocessing.log_to_stderr(logging.DEBUG)

    print("*** sis process ***")
    p = SisProcess()
    p.start()

    count = 0
    while True:

        if not p.is_alive():
            break

        if count == 3:
            print("trigger termination")
            p.stop()

        count += 1
        time.sleep(0.5)

    print("alive: %s" % p.is_alive())
    print('%s.exitcode = %s' % (p.name, p.exitcode))  # <0: killed with signal; >0: exited with error

if __name__ == "__main__":
    main()
