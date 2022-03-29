import argparse
import hplang
import sys


def entry_point():
  parser = argparse.ArgumentParser()
  parser.add_argument("input", type=argparse.FileType())
  args = parser.parse_args()

  input = args.input.read()
  args.input.close()

  hplang.translate(input, progress=True)
