import sys

TOLERANCE = 1e-9  # relative tolerance to compare floats


def isclose(a, b, rel_tol=TOLERANCE):
    return abs(a - b) <= rel_tol * max(abs(a), abs(b))


def result(positive=True, comment=None, pt="Arithmetic"):
    print "Result: {}".format(
        "{} progresion detected!".format(pt) if positive else "Progression not detected"
    )
    if comment: print comment
    sys.exit(0 if positive else 1)


try:
    s = sys.argv[1]

except IndexError:
    print "progr.py\n\nDetects progression. It detects both arithmetic and geometric progression.\n"
    print "usage: python progr.py progression"
    print "progression: sequence of natural numbers, comma separated, no spaces"
    sys.exit(1)

# print sys.argv

try:
    numbers = map(float, s.split(','))
except ValueError:
    result(False, "Input string is not comma separated natural numbers")

if len(numbers) < 3:
    result(False, "Need more then 2 numbers to detect progression")

print "Trying to detect progression in:", numbers

# -------------------------------------------

# It's better to use numpy, but I am not using it to use only standard lib

# -------------------------------------------
# Try to detect arithmetic progression

pd = [n1 - n0 for n0, n1 in zip(numbers, numbers[1:])]
eq = [isclose(n0, n1) for n0, n1 in zip(pd, pd[1:])]

if all(eq): result()

# -------------------------------------------
# Try to detect geomeric progression

try:
    pd = [n1 / n0 for n0, n1 in zip(numbers, numbers[1:])]
except ZeroDivisionError:
    result(False, "Division by zero")

eq = [isclose(n0, n1) for n0, n1 in zip(pd, pd[1:])]

if all(eq): result(pt="Geometric")

result(False)