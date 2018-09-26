def main():
	while True:
		num = int(input())
		print(num * num)

try:
	main()
except (EOFError, ValueError):
	pass