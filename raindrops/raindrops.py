def convert(number):
    output = []
    if not number % 3:
        output.append("Pling")
    if not number % 5:
        output.append("Plang")
    if not number % 7:
        output.append("Plong")

    return "".join(output) if output else str(number)
