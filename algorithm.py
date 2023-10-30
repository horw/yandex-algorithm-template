def main(file_name='input.txt'):
    with open(file_name) as f:
        n, m = map(int, f.readline().split(' '))
        for i in range(n, m):
            print(i)


if __name__ == '__main__':
    main()
