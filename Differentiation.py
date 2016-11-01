def main():
    option = input("""\
Welcome
Type 1 to differentiate a polynomial.
Type 2 for other options
> """)
    if option == "1":
        gp = getPolynomial()
        printPolynomial(polynomial(gp[0], gp[1]))
    else:
        option = 0

def getInt(inputText):
    number = input(inputText)
    try:
        result = int(number)
    except ValueError:
        print("Please enter an integer")
        return getInt(inputText)
    else:
        return result

def monomial(coefficient, power):
    if power == 0:
        return (0, 0)
    return (power * coefficient, power - 1)

#print (monomial(2, 3)) -> 2x^3. Returns (6, 2) -> 6x^2.

def polynomial (degree, coefficients):
    result = []
    for x in range (0, degree + 1):
        if x == len(coefficients) - 1:
            coefficients[x] = 0
            continue
        result.append( monomial(coefficients[x], len(coefficients) - 1 - x) )
    return result

#print(polynomial(2, [2, 3, 4])) -> 2x^2 + 3x + 4. Returns [(4, 1), (3, 0)]
                                #-> 4x + 3

def getPolynomial():
    coefficients = []
    degree = getInt("Type in the highest power of the variable: ")
    for x in range (0, degree + 1):
        txt = "Type in the coefficient of x ^ " + str(x) + ": "
        coefficients.append(getInt(txt))
    coefficients.reverse()
    return [degree, coefficients]

def printPolynomial(poly):
    txt = "Derivative: "
    for x in range(0, len(poly) - 1):
        txt += str(poly[x][0]) + "x^" + str(poly[x][1]) + " + "
    txt += str(poly[len(poly) - 1][0])
    print(txt)



main()
