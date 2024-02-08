import sys
import time


def main():
    print(eval(sys.argv[1]))
    for i in range(5, 0, -1):
        print(f"Close in {i}s...", end='\r')
        time.sleep(1)



if __name__ == "__main__":
    main()
