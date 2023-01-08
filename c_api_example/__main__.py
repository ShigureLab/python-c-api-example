from __future__ import annotations

import inspect


def spam_pybind():
    from c_api_example import spam

    print("Call spam.system:")
    status = spam.system("ls -l")
    print(status)
    print()

    print("Get spam.system.__doc__:")
    print(spam.system.__doc__)
    print()

    print("Get members of spam:")
    print(inspect.getmembers(spam))
    print()

    print("Get signature of spam.system:")
    print(inspect.signature(spam.system))
    print()


def main():
    spam_pybind()


if __name__ == "__main__":
    main()
