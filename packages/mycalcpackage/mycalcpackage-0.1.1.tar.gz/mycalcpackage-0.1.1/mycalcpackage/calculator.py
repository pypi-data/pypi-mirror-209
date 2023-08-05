import argparse
import toml

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def load_config():
    config = toml.load("config.toml")
    return config

def main():
    parser = argparse.ArgumentParser(description="Calculator CLI")
    parser.add_argument("operation", choices=["add", "subtract", "multiply", "divide"], help="Mathematical operation")
    parser.add_argument("a", type=float, help="First number")
    parser.add_argument("b", type=float, help="Second number")
    args = parser.parse_args()

    if args.operation == "add":
        result = add(args.a, args.b)
    elif args.operation == "subtract":
        result = subtract(args.a, args.b)
    elif args.operation == "multiply":
        result = multiply(args.a, args.b)
    elif args.operation == "divide":
        result = divide(args.a, args.b)

    print(f"Result: {result:.{load_config()['settings']['precision']}f}")

if __name__ == "__main__":
    main()
