def do_something(times: int) -> str:
    if times < 0:
        raise ValueError("times must be >= 0")
    for _ in range(times):
        print("Do something")
    return f"Something has been done {times} times"


if __name__ == "__main__":
    print(do_something(3))
