"""Main application code for displaying a board"""

import time
import getopt
import sys

# pylint: disable=too-many-nested-blocks
# pylint: disable=too-many-branches
# pylint: disable=too-many-instance-attributes

from neopolitan.board_functions.board import Board
from neopolitan.writing.data_transformation import str_to_data
from neopolitan.board_functions.board_data import default_board_data
from neopolitan.os_detection import on_pi
from neopolitan.log import get_logger
# pylint: disable=wildcard-import
from neopolitan.const import *

def process_arguments():
    """Process the command line arguments and return them as a BoardData object"""
    logger = get_logger()
    board_data = default_board_data

    argument_list = sys.argv[1:]
    options = 'm:g:s:w:'
    long_options = ['message=', 'graphical=', 'scroll=', 'wrap=']
    try:
        # args, vals
        args = getopt.getopt(argument_list, options, long_options)
        if len(args[0]) > 0:
            for arg, val in args[0]:
                if arg in ('-m', '--message'):
                    board_data.message = val
                elif arg in ('-g', '--graphical'):
                    if val == 'True':
                        board_data.graphical = True
                    elif val == 'False':
                        board_data.graphical = False
                    else:
                        logger.warning('Could not parse "graphical" argument: %s', val)
                elif arg in ('-s', 'scroll'):
                    if val in ('slow', 'medium', 'fast'):
                        board_data.scroll_speed = val
                        if val == 'slow':
                            board_data.scroll_wait = SCROLL_FAST
                        elif val == 'medium':
                            board_data.scroll_wait = SCROLL_MED
                        else: # fast
                            board_data.scroll_wait = SCROLL_SLOW
                    else:
                        logger.warning('Invalid scroll speed: %s', val)
                elif arg in ('-w', 'wrap'):
                    if val == 'True':
                        board_data.should_wrap = True
                    elif val == 'False':
                        board_data.should_wrap = False
                    else:
                        logger.warning('Could not parse "wrap" argument: %s', val)
        # --- Verify OS for graphical/hardware
        if on_pi() and board_data.graphical:
            logger.warning('This code cannot be run in graphical' \
                            ' mode on a Raspberry Pi, setting graphical to False')
            board_data.graphical = False
        if not on_pi() and not board_data.graphical:
            logger.warning('This code cannot be run in hardware mode when not run'\
            ' on a Raspberry Pi, setting graphical to True')
            board_data.graphical = True
        # --- Done verifying
        logger.info('message set to: %s', board_data.message)
        logger.info('graphical set to: %s', board_data.graphical)
        logger.info('scroll speed set to: %s (%s)', board_data.scroll_speed, board_data.scroll_wait)
        logger.info('wrap set to: %s', {board_data.should_wrap})

    except getopt.error as err:
        logger.error('getopt error: %s', err)

    return board_data

def process_board_data_events(board_data, event_list):
    """Manipulate board data according to events"""

    logger = get_logger()

    first = event_list[0]
    if first == 'speed':
        try:
            speed = event_list[1]
        # pylint: disable=broad-except
        except Exception as err:
            # todo: better explanation
            logger.warning('No second value provided, %s', err)
        if speed == 'slow':
            board_data.scroll_slow()
            logger.info('set speed: slow')
        elif speed == 'medium':
            board_data.scroll_medium()
            logger.info('set speed: medium')
        elif speed == 'fast':
            board_data.scroll_fast()
            logger.info('set speed: fast')
        else:
            try:
                speed = float(speed)
                board_data.set_scroll_wait(speed)
                logger.info('set speed: %s', speed)
            except ValueError:
                logger.warning('Cannot parse speed: %s', speed)
    elif first == 'wrap':
        try:
            wrap = event_list[1]
        # pylint: disable=broad-except
        except Exception as err:
            # todo: better explanation
            logger.warning('No second value provided, %s', err)
        if wrap in ('True', '1'):
            board_data.should_wrap = True
            logger.info('set wrap: True')
        elif wrap in ('False', '0'):
            board_data.should_wrap = False
            logger.info('set wrap: False')
        else:
            logger.warning('Cannot parse wrap: %s', wrap)

    return board_data


class Neopolitan:
    """Main application class for displaying a board"""
    def __init__(self, board_data=process_arguments(), events=None):
        self.board_data = board_data
        self.width = WIDTH
        self.height = HEIGHT
        self.size = WIDTH*HEIGHT
        self.board = None
        self.display = None
        self.board_display = None

        self.events = events

        self.init_board()
        self.board.set_data(str_to_data(board_data.message))

    def __del__(self):
        del self.display

    def init_board(self):
        """Initialize board data"""
        # todo: make better
        if self.board_data.graphical:
            get_logger().info('Initializing graphical display')
            # pylint: disable=import-outside-toplevel
            from neopolitan.display.graphical_display import GraphicalDisplay
            self.board = Board(self.size)
            self.display = GraphicalDisplay(board=self.board)
        else:
            get_logger().info('Initializing hardware display')
            # pylint: disable=import-outside-toplevel
            from neopolitan.display.hardware_display import HardwareDisplay
            self.display = HardwareDisplay(WIDTH*HEIGHT)
            self.board_display = self.display.board_display
            self.board = self.board_display.board

    def loop(self):
        """Main display loop"""
        logger = get_logger()
        while not self.display.should_exit:
            # process events
            # todo: make better
            while self.events and not self.events.empty():
                event = self.events.get()
                logger.info('event: %s', event)
                event_list = event.split()
                first = event_list[0]
                if first == 'exit':
                    return
                if first == 'say':
                    logger.info('say: %s', event)
                    # todo: better handling: this is unintuitive
                    message = ' '
                    for word in event_list[1:]:
                        message += word + ' '
                    logger.info(message)
                    self.board.set_data(str_to_data(message))
                    logger.info('set message: %s', message)
                else: # try board data events
                    self.board_data = process_board_data_events(self.board_data, event_list)
                # todo: error handling
            self.display.loop()
            if self.board_data.scroll_speed:
                self.board.scroll(wrap=self.board_data.should_wrap)

            time.sleep(self.board_data.scroll_wait)
