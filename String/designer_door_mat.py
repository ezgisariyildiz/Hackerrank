def print_design(n, m):
    pattern = [('.|.' * (2 * i + 1)).center(m, '-') for i in range(n // 2)]
    welcome = 'WELCOME'.center(m, '-')
    print('\n'.join(pattern + [welcome] + pattern[::-1]))

if __name__ == '__main__':
    n, m = map(int, input().split())
    print_design(n, m)