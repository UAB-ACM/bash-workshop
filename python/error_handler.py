# usage: <other_command> 3>&1 1>&2 2>&3 | python error_handler.py

def main():
	while True:
		error = input()
		handle_error(error)


def handle_error(error):
	print("Handled: {}".format(error))


try:
	main()
except EOFError:
	pass
