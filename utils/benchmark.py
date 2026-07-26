import time
import functools


def benchmark(func):
    """
    A decorator that prints the time a function takes to execute.

    This decorator is useful for profiling and understanding the performance
    of your code.
    """

    # functools.wraps() is a very important part of a well-behaved decorator.
    # It ensures that the wrapper function retains the original function's
    # name, docstring, and other metadata. This is crucial for debugging and
    # for tools that inspect functions.
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """
        The wrapper function that executes the timing logic.

        It takes arbitrary arguments (*args) and keyword arguments (**kwargs)
        to handle any function signature.
        """
        # Get the start time before the function call
        start_time = time.perf_counter()

        # Call the original function with its arguments and store the result
        result = func(*args, **kwargs)

        # Get the end time after the function has completed
        end_time = time.perf_counter()

        # Calculate the elapsed time
        elapsed_time = end_time - start_time

        # Print the benchmark result in a readable format
        print(f"Function '{func.__name__}' took {elapsed_time:.4f} seconds to execute.")

        # Return the result of the original function call
        return result

    # Return the new, decorated function
    return wrapper
