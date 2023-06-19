import argparse

def basic_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="Input video file path")
    parser.add_argument("--output", help="Output gif file path")

    return parser