"""
Problem:
Monitoring how much swap space is being used to avoid cache thrashing issues,
and notifying the user when space is low.

Useful for when running a system on a small drive

Consider later: A long-running script that runs at startup and tracks state or use a temporary file to track,
so as to prevent unwanted duplicate notifications.
"""
import subprocess

def get_swap():
    swap_warn_level = .75

    swap = subprocess.run(['cat', '/proc/swaps'], stdout=subprocess.PIPE)
    # idx 7 is size, idx 8 is free swap
    result = swap.stdout.decode('utf-8').split()

    decimal_percent_used = int(result[8]) / int(result[7])

    if decimal_percent_used > swap_warn_level:
        subprocess.run(
            ['notify-send', 'WARNING', 'Swap usage is {0:.2f}%'.format(decimal_percent_used*100), '-u', 'critical'])


if __name__ == '__main__':
    get_swap()
