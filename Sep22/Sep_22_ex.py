filename = 'file_jamaica.txt'
try:
    with open(filename) as file_obj:
        file_contents = file_obj.read()
except FileNotFoundError:
    err_msg = "file does not exist."
    print(err_msg)



