
abc = ['water', 'juice', 'beer']

choice = raw_input("get drink ")

def drink(choice):
    while choice in abc:
        print "good"
    else:
        choice not in abc
        raise RuntimeError("We don't have that drink ")

drink(choice)