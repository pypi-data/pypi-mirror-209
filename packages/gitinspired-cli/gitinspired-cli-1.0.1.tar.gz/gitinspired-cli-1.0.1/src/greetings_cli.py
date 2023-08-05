import argparse

def greet(args):
    message = f"Hello, {args.name}!"
    print(message)

def main():
    parser = argparse.ArgumentParser(description="CLI tool for greeting.")
    parser.add_argument("name", help="Name to greet")
    args = parser.parse_args()
    greet(args)

if __name__ == "__main__":
    main()
