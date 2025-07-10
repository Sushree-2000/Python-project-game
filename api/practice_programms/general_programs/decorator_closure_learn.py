# Closure: A closure is a function that remembers the variables from its enclosing scope, even is that scope is no longer available.
# Ex:
def outer(msg):
    def inner():
        print(f"Given outer variable's value is: {msg}")
    return inner

res = outer('Testing Closure')
res()
