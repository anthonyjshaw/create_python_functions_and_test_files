import sys
from create_functions import set_settings, make

def main():
	set_settings(sys.argv[1])
	make(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
	main()