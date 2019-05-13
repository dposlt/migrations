#!/usr/bin/env python3

from colorama import init, Fore, Style

init()
init(autoreset=True)

def red(warning):
    return Fore.RED + warning

def green(message):
    return Fore.GREEN + message

def yellow(warning):
    return Fore.YELLOW + warning


#Style.RESET_ALL
