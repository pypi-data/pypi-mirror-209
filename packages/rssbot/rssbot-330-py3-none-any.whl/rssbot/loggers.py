# This file is placed in the Public Domain.
# pylint: disable=C,I,R,E0402


__author__ = "B.H.J. Thate <thatebhj@gmail.com>"
__version__ = 1



from .utility import spl


SKIP = "PING,PONG"


class Logging:

    verbose = False

    @staticmethod
    def debug(txt):
        if Logging.verbose and not doskip(txt, SKIP):
            Logging.raw(txt)

    @staticmethod
    def raw(txt):
        pass


def doskip(txt, skipping):
    for skip in spl(skipping):
        if skip in txt:
            return True
    return False
