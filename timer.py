import functools, time

def timer(func_1): # Calculate runtime of decorated function
#    @functools.wraps(func_1) # To preserve info about the original function
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        func_1(*args, **kwargs)
#        value_1 = func_1(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Executed {func_1.__name__!r} in {run_time:.9f} seconds")
#        return value_1
    return wrapper_timer

@timer
def spend_time_func(n_1):
    for _ in range(n_1):
        sum([k**3 for k in range(10000)])

spend_time_func(100)
