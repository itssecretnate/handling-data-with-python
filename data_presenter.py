# Problem #2
cupcake = open('CupcakeInvoices.csv')

# Related to Problem #6
invoices_total = 0

# Problem #3
for line in cupcake:
    print(line.rstrip('\n'))

    # Problem #4
    line = line.split(',')
    print(f'Cupcake type: {line[2]}')
    
    
    # Problem #5
    total = round(float(line[3]) * float(line[4]), 2)
    
    print(f'Total: {total}\n')

    # Problem #6
    invoices_total += total


invoices_total = round(invoices_total, 2)
print(f'Total of all invoices: {invoices_total}')

# Problem #7
cupcake.close()