if __name__ == '__main__':
    n = int(input())
    int_list = map(int, input().split())
    int_tuple = tuple(int_list)
    print(hash(int_tuple))
