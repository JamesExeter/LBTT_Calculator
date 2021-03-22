import sys

# function used to tidy up the display of values
def tidy_output(val):
    # if value has a trailing zero, remove it
    if int(val) - val == 0:
        return int(val)
    
    # else return to 2.d.p
    return round(val,2)

# function to calculate the lbtt 
# this could be done recursively 
def calculate_basic_lbtt(price):
    # first do error checking on type and value for cases where prior validation has not occurred
    if type(price) not in [float, int]:
        raise TypeError('The price must be either an integer or a float, no strings are permitted')
    
    if price < 0:
        raise ValueError('The price cannot be negative')
    
    # define the tax bounds and the tax associated with each bound
    tax_bounds = {250000:0.05, 325000:0.1, 750000:0.12}
    # extract just the bound values and reverse their order as shown in the dictionary above
    bound_vals = list(tax_bounds.keys())
    bound_vals.reverse()
    
    # check the price against the first bound value
    if price <= bound_vals[len(bound_vals)-1]:
        return 0 # base case, don't iterate if this is the case, negative values are also caught here if not validated
    
    # base case not satisfied so now we iterate down the tax bounds from greatest to smallest
    total_tax = 0
    for idx in range(0, len(bound_vals)):
        # if the price is greater than the bound, 
        # tax all of the value above that bound to get the difference in tax for that bound
        # then add the result to the running tax
        # update the new price to be the value of the current bound, so that for all lower bounds, we tax the full amount
        # for each bound until we reach the last one, updating the total tax as we go
        if price > bound_vals[idx]:
            difference = price - bound_vals[idx]
            price = bound_vals[idx]
            total_tax += difference*tax_bounds[bound_vals[idx]]        
    
    # return the final tax to 2.d.p
    return round(total_tax, 2)

# function used to validate the price
def validate_price(price):
    try:
        # try converting the price to a float and check the value is positive
        purchase_amount = float(price)
        if purchase_amount > 0:
            # valid price
            return True
        else:
            # not greater than 0
            return False
    except ValueError:
        # not a float / int
        return False    

# used to recieve input from the user if it is not already provided
def recieve_input():
    valid = False
    purchase_amount = 0
    # validate the input to ensure it is a number
    # keep asking until a valid value is given
    while not valid:
        purchase_amount = input("\nPlease enter the purchase price of the house: ")
        # validate the price, ask again is invalid
        if validate_price(purchase_amount):
            purchase_amount = float(purchase_amount)
            valid = True
        else:
            print("The price entered was not valid, please enter a positive number.")        
    
    purchase_amount = round(purchase_amount, 2) # ensure it is to 2.d.p for pennies
    return purchase_amount

# enter the program logic here
if __name__ == "__main__":
    # get the input price, first test if a price is provided in the program arguments
    price = 0
    if len(sys.argv) == 2:
        # there is a program argument
        price = sys.argv[1]
        if validate_price(price):
            # if the provided price is valid, use it and ensure it is a float
            price = float(price)
        else:
            # it is not valid so get the user to enter is manually
            print("The provided argument was not valid.")
            price = recieve_input()
    else:
        # no provided argument so get user input
        price = recieve_input()
    
    # with a valid house purchase price, calculate the tax
    lbtt = calculate_basic_lbtt(price)
    # display the tax and tidy the output to remove trailing decimal zeros / round to 2.d.p
    print("The tax on the property valued at £{} comes to £{}".format(tidy_output(price), tidy_output(lbtt)))
    
    # as a small extra, calculate the effective tax rate and then display it in a tidy manner
    effective_tax_rate = (lbtt/price)*100
    to_print = None
    if effective_tax_rate > 1:
        # print tax rate to 2.d.p
        to_print = round(effective_tax_rate, 2)        
    else:
        # only print the first significant digit if tax rate below zero
        to_print = eval("%.0e" % (effective_tax_rate))
        
    print("The effective tax rate is {}%".format(to_print))