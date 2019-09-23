def convert(number):
    modifiers = {
        3: "Pling",
        5: "Plang",
        7: "Plong"
    }
    output = ""
    for divisor, suffix in modifiers.items():
        if number % divisor == 0:
            output += suffix
    if not output:
        output = str(number)
    return output
