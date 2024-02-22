if __name__ == '__main__':
    N = int(input())
    
    l = []
    for i in range(N):
        command = input().split()
        first_command = command[0]
        if first_command == 'insert':
            l.insert(int(command[1]), int(command[2]))
        elif first_command == 'print':
            print(l)
        elif first_command == 'remove':
            l.remove(int(command[1]))
        elif first_command == 'append':
            l.append(int(command[1]))
        elif first_command == 'sort':
            l.sort()
        elif first_command == 'pop':
            l.pop()
        elif first_command == 'reverse':
            l.reverse()
    