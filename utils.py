def read_text_file(text_file):
    with open(text_file) as read_file:
        data = read_file.read().splitlines()
    return data
