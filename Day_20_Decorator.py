# Decorator = A function that extends the behaviour of another 
#              function
#              w/o modifying the base function
#              Pass the base function as the argument  to the decorator


# Python Decorator Example :

# Step 1: Create a decorator
def my_decorator(func):

    # Step 2: Create a wrapper function
    # This function adds extra behavior before and after the original function.
    def wrapper():

        print("Before calling the function")

        # Call the original function
        func()

        print("After calling the function")

    # Step 3: Return the wrapper function
    return wrapper


# Step 4: Use the decorator
# This is the same as:
# show_message = my_decorator(show_message)
@my_decorator
def show_message():
    print("Hello! Welcome to Python Decorators.")


# Step 5: Call the function
show_message()