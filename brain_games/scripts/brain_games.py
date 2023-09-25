#!/usr/bin/env python3

from brain_games.cli import welcome_user
from brain_games.cli import debug


def main():
    welcome_user()
    debug("Закончили")


if __name__ == '__main__':
    main()
