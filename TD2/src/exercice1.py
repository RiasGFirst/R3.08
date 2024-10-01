

def divide(a: float, b: float) -> float:
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        try:
            return a / b
        except ZeroDivisionError as err:
            return f"Zero not allowed: {err}"
        except Exception as err:
            return f"An error occured: {err}"
    else:
        return "This is not a float or int values..."


if __name__ == "__main__":
    print(divide(10, 2))
    print(divide(10, 0))
    print(divide("10", 2))