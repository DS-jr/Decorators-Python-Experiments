import functools, time

def delay(func_2): # Decorator for a two-second delay before calling another function
    # functools.wraps(func_2) # To preserve info about the original function
    def wrapper_delay(*args):
        time.sleep(2)
        return func_2(*args)
    return wrapper_delay

@delay
def countdown(start_sec):
    if start_sec < 1:
        print("start_sec now is < 1")
    else:
        # time.sleep(2)
        print(start_sec)
        countdown(start_sec - 1)

countdown(7)
