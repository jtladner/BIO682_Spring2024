#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("num1", type=float, help="First number to use in calculation")
parser.add_argument("num2", type=float, help="Second number to use in calculation")
parser.add_argument("-o", "--oper", default="+", choices=["+", "-", "*", "/", "**"], help="Operation to perform")

args = parser.parse_args()

if args.oper == "+":
    print(args.num1 + args.num2)
elif args.oper == "*":
    print(args.num1 * args.num2)
elif args.oper == "-":
    print(args.num1 - args.num2)
elif args.oper == "/":
    print(args.num1 / args.num2)
elif args.oper == "**":
    print(args.num1 ** args.num2)
