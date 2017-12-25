import c
parser = argparse.ArgumentParser()
parser.add_argument("arg", type=int)
parser.add_argument("-v", "--verbose", action="store_true",
                    help="increase output verbosity")

args = parser.parse_args()
if args.arg == 1:
    print ('One')
elif args.arg ==2:
    print ('two')