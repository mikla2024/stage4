import yaml

def load_from_file(filename):
    try:
        with open (filename, 'r') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        return "File with notes doesn't exist"

list_notes = load_from_file('IO_Amelkin_Mikhail.yaml')

if list_notes is not None:
    print(list_notes)
else:
    print('File is empty. No data found')

