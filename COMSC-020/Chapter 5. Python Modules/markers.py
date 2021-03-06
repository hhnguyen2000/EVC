# Huu Hung Nguyen
# 09/26/2021
# markers.py
# The program assumes the price of 1 marker is 80 cents, 5 markers is $3.50,
# the tax sale rate is 6.5%, the shipping rate is 5%.
# It prompts the user for the number of markers.
# It calculates and displays the number of packages 5 markers,
# the number of separate markers, the subtotal, the tax cost,
# the shipping cost, and the total cost.

# Assume price of 1 marker, 5 markers, and number of markers per package
PRICE_MARKER = 0.80
PRICE_PACKAGE = 3.50
MARKERS_PER_PACKAGE = 5

# Assume tax rate and shipping rate
TAX_RATE = 0.065
SHIPPING_RATE = 0.05

# Prompt user for number of markers
markers = int(input('How many markers are you buying? '))

# Calculate number of packages 5 markers and separate markers
packages = markers // MARKERS_PER_PACKAGE
separate_markers = markers % MARKERS_PER_PACKAGE

# Calculate subtotal, tax cost, shipping cost, and total cost
subtotal = packages * PRICE_PACKAGE + separate_markers * PRICE_MARKER
tax_cost = subtotal * TAX_RATE
shipping_cost = subtotal * SHIPPING_RATE
total_cost = subtotal + tax_cost + shipping_cost

# Display program
print('''Number of packages: {}
Number of separate markers: {}
Subtotal: ${:.2f}
Tax:      ${:.2f}
Shipping: ${:.2f}
Total:    ${:.2f}'''. format(packages, separate_markers,
                             subtotal, tax_cost, shipping_cost, total_cost))
