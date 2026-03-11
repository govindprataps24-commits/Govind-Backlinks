"""Simple command-line calculator."""

from __future__ import annotations


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


OPERATIONS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculate(a: float, operator: str, b: float) -> float:
    if operator not in OPERATIONS:
        raise ValueError(f"Unsupported operator: {operator}")
    return OPERATIONS[operator](a, b)


def main() -> None:
    print("Calculator")
    print("Supported operators: +, -, *, /")

    while True:
        raw = input("Enter expression (e.g. 2 + 2) or 'q' to quit: ").strip()
        if raw.lower() in {"q", "quit", "exit"}:
            print("Goodbye!")
            break

        parts = raw.split()
        if len(parts) != 3:
            print("Please use the format: <number> <operator> <number>")
            continue

        left, operator, right = parts

        try:
            a = float(left)
            b = float(right)
            result = calculate(a, operator, b)
        except ValueError as error:
            print(f"Error: {error}")
            continue

        if result.is_integer():
            print(f"Result: {int(result)}")
        else:
            print(f"Result: {result}")


if __name__ == "__main__":
    main()
