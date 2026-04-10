def open_and_print_file_and_sort(path, output_path='sorted_songs.txt'):
	with open(path) as file:
		sorted_lines = sorted(file, key=str.casefold)
	
	with open(output_path, 'w') as output_file:
		for line in sorted_lines:
			output_file.write(line)


def main():
	open_and_print_file_and_sort('songs.txt', 'sorted_songs.txt') 


if __name__ == "__main__":
    main()