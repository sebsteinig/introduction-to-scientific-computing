
with open("calc.txt") as f:
    for line in f:
        parts = line.split()
        lhs = int(parts[0])
        operator = parts[1]
        rhs = int(parts[2])
        
        if operator == "+":
            print(line.strip(), "is", lhs + rhs)
        elif operator == "-":
            print(line.strip(), "is", lhs - rhs)
        elif operator == "*":
            print(line.strip(), "is", lhs * rhs)
        elif operator == "/":
            print(line.strip(), "is", lhs / rhs)
