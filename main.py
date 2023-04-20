import sys


def main():
    print("Current version: " + str(sys.version_info))
    if sys.version_info[:2] != (3,7):
        print("Python 3.7 is required. Exiting...")
        sys.exit(1)
    else:
        print("Python 3.7 is installed. Continuing...")

if __name__ == "__main__":
    main()