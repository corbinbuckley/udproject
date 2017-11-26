def ask_change():
    return int(raw_input('How many cents?'))
    #cents = int(cents)


# I would like to pass the value I got from ask_change and put in where the 88 is
#       in the make_change( )
# I think I dont understand passing and how functions work
# I can make it work if I do not put the above code into a function, but then it
#       is global i think and that is not good to do.

def make_change(cents):
    # Use modulo to find the quarters
    parts = divmod(cents,25)
    quarters = parts[0]
    remaining_cents = parts[1]
    # Use modulo to find the dimes from remaining cents([1])
    parts = divmod(remaining_cents, 10)
    dimes = parts[0]
    remaining_cents = parts[1]
    # Use modulo to find the nickels from remaing cents ([1])
    parts = divmod(remaining_cents,5)
    nickels = parts[0]
    remaining_cents = parts[1]
    # Pennies is the remaing cents ([1])
    pennies = remaining_cents

    #ask_change(cents)

    print "Change for: ",cents, "cents is "
    print "Quarters:", quarters
    print "Dimes:", dimes
    print "Nickels:", nickels
    print "Pennies:", pennies


make_change(ask_change())
