import cmath

# Take input from the user
a = float(input("Enter the coefficient of x^2: "))
b = float(input("Enter the coefficient of x: "))
c = float(input("Enter the constant term: "))

# Calculate the discriminant
d = (b**2) - (4*a*c)

# Find the roots of the equation using the quadratic formula
root1 = (-b - cmath.sqrt(d)) / (2*a)
root2 = (-b + cmath.sqrt(d)) / (2*a)

# Print the roots of the equation
print("The roots of the quadratic equation are: {0} and {1}".format(
    root1, root2))
# In this program, the user is prompted to enter the coefficients of the quadratic equation(a, b, and c), which are then used to calculate the discriminant(d).
#  If the discriminant is positive, the quadratic equation has two real roots. If it is zero, the equation has one real root(which is repeated).
#  If the discriminant is negative, the equation has two complex roots. The roots are then calculated using the quadratic formula and printed to the console.
#  Note that we're using the cmath module to handle complex numbers.
