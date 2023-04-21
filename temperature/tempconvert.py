#!/usr/local/bin/python
# Python 3.9.16
# khurram.subhani(dot)live.com
# temperature.py
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('val',help='A value to convert expressed an integer',type=int)
parser.add_argument('-v','--verbose',help='Print more details',action='store_true')
contype = parser.add_mutually_exclusive_group(required=True)
contype.add_argument('-f','--fahr',help='Enable to convert from fahrenheit to centigrate',action='store_true')
contype.add_argument('-c','--cent',help='Enable to convert from centigrate to fahrenheit',action='store_true')
args = parser.parse_args()

if args.verbose and args.fahr:    
    c = (args.val - 32)/1.8
    #print(f"{args.val}f is {c:.2f}c")
    print(f"centigrate -> ({args.val}°f - 32)/1.8 = {c}°c")
    exit(0)

if args.fahr:
    c = (args.val - 32)/1.8
    print(f"{args.val}°f is {c:.2f}°c")
    exit(0)

if args.verbose and args.cent:
    f = (args.val * 9 /5)/32
    #print(f"{args.val}c is {f:.2f}f")
    print(f"fahrenhiet -> ({args.val}°c * 9/5)/32 = {f}°f")
    exit(0)

if args.cent:
    f = (args.val * 9 /5)/32
    print(f"{args.val}°c is {f:.2f}°f")
    exit(0)