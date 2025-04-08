def Main():
    x = account_maybe
    if is_account:
        return Login
    else:
        return Register

def account_maybe():
    while True:
        s = input("Do you have an account? ").strip().title()
        if is_account:
            break
    return s

def is_account(n):
    return True if Log == Yes or No else False

def Register():
    pass

def Login():
    pass

Main()
account_maybe()