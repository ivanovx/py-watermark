#!/usr/bin/env python

import os
import argparse

def main():
    parser = argparse.ArgumentParser(description='Add watermark to image')
    parser.add_argument('-i', '--image', help='The image')
    parser.add_argument('-w', '--watermark', help='The watermark')
    args = parser.parse_args()

    if args.image:
        print(args.image)

        if args.watermark:
            print(args.watermark)

if __name__ == '__main__':
    main()