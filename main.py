from app.io import input, output


def main():
    input_text = input.input_text()
    file_content_builtin = input.read_file_builtin('data/input.txt')
    file_content_pandas = input.read_file_pandas('data/input.csv')

    output.output_console(input_text)
    output.output_console(file_content_builtin)
    output.output_console(file_content_pandas)

    output.write_file_builtin('data/output.txt', input_text)
    output.write_file_builtin('data/output_builtin.txt', file_content_builtin)


if __name__ == '__main__':
    main()
