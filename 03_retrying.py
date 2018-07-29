from retrying import retry

@retry(stop_max_attempt_number=3)
def fun1():
    print("this is func1")
    raise ValueError("this is test error")


