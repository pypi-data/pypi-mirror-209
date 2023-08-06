"""Main application function"""

from neopolitan.os_detection import log_os
from neopolitan.log import init_logger
from neopolitan.neopolitan import Neopolitan


def main(events=None, initialize_logger=False):
    """Make a very simple display"""

    if initialize_logger:
        init_logger()
    log_os()

    neopolitan = Neopolitan(events=events)
    neopolitan.loop()
    del neopolitan

if __name__ == '__main__': # todo: is this still true when running from the thread?
    main(initialize_logger=True) # try False maybe? for testing
