import argparse
import sys, os
from .core import encrypt, decrypt 

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Byte-shift encryptor (Caesar cipher on bytes).")
    p.add_argument("action", choices=["encrypt", "decrypt"],
                   help="what to do with the file")
    p.add_argument("file", metavar="INPOT",
                   help="path to the file you wnat to process")
    p.add_argument("key", type=int,
                   help="integer 0-255 - shift magnitude")
    p.add_argument("-o", "--output", help="output file name")
    p.add_argument("-d", "--dir", default=".",
                   help="directory to save result (default: current)")
    return p.parse_args()

def main() -> None:
    args = parse_args()

    if not os.path.exists(args.file):
        sys.exit("Input file does not exist")

    with open(args.file, "rb") as f_in:
        data = f_in.read()
    func = encrypt if args.action == "encrypt" else decrypt
    try:
        result = func(data, args.key)
    except ValueError as e:
        sys.exit(str(e))

    os.makedirs(args.dir, exist_ok=True)
    out_name = args.output or f"{args.action}.{os.path.basename(args.file)}"
    out_path = os.path.join(args.dir, out_name)
    with open(out_path, "wb") as f_out:
        f_out.write(result)

    print("Done ->", out_path)

if __name__ == "__main__":
    main()