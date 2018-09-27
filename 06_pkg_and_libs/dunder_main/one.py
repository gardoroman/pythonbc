def func():
    print("in one")


print("top level in one.py")

if __name__ == '__main__':
    print("running one.py directly")
else:
    print("one.py has been imported")
