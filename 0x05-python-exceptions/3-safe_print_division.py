#!usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except:
        break
    finally:
        print("{}".foramt(result))
