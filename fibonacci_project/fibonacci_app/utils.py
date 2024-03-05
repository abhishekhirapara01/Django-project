import time

def timing_decorator(func):
  def wrapper(*args, **kwargs):
    start_time= time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    execution_time = end_time - start_time
    result['execution_time'] = f"{execution_time:.6f} seconds"
    return result
  return wrapper

def fibonacci_generator(n):
  a, b = 0, 1
  for _ in range(n):
    yield a
    a, b = b, a + b