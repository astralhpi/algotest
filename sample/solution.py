
def add(a, b):
    return a + b

def main():
    count = int(raw_input())
    for i in xrange(count):
        a, b = map(int, raw_input().split(' '))
        print(add(a, b))

if __name__ == "__main__":
    main()
