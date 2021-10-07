#!/usr/bin/env python3

# Created by: Seti Ngabo
# Created on: Oct 2021
# This program uses a nested loop


def main():
    # this function uses a nested loop

    first_counter = 0
    second_counter = 0
    third_counter = 0

    # process & output
    for first_counter in range(256):
        for second_counter in range(256):
            for third_counter in range(256):
                print("RGB({0}, {1}, {2})".format(first_counter, second_counter, third_counter))


if __name__ == "__main__":
    main()
