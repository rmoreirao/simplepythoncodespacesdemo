import sys


def main():
    print("Current version: " + str(sys.version_info))
    if sys.version_info[:2] != (3,7): 
        # print red text to console
        print("\033[91m" + "Python 3.7 is required. Exiting..." + "\033[0m")
        sys.exit(1)
    else:
        # print green text to console
        print("\033[92m" + "Python 3.7 is installed. Continuing..." + "\033[0m")

if __name__ == "__main__":
    main()