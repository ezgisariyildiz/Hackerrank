n = int(input())
for _ in range(n):
    a, b = input().split()
    try:
        print(int(a) // int(b))
    except Exception as e:
        print(f"Error Code: {e}")

########## OR ###########
        
for _ in range(int(input())):

    try:

        a, b = map(int, input().split())

        print(a // b)

    except ZeroDivisionError:

        print('Error Code: integer division or modulo by zero')

    except ValueError as e:

        print('Error Code:', e)