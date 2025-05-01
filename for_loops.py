# mesma coisa do "while_loops.py"
# o que muda é porque usamos 'for'

## number we'll find the factorial of
number = 6
## start with our product equal to one
product = 1

## calculate factorial of number with a for loop
for num in range(2, number + 1):
    product *= num

## print the factorial of number
print(product)