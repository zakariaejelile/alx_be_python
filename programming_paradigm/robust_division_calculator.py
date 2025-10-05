def safe_divide(numerator, denominator):
    try:
        # Try to convert inputs to float
        numerator = float(numerator)
        denominator = float(denominator)

        # Try performing division
        result = numerator / denominator
        return f"The result of the division is {result}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    except ValueError:
        return "Error: Please enter numeric values only."
