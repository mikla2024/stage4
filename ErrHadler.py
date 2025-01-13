import yaml

def load_from_file(filename):
    try:
        with open (filename, 'r') as file:
            return yaml.safe_load(file)

    except FileNotFoundError:
        print(
            "File doesn't exist. "
            "File will be added"
        )
        with open(filename, 'x') as file:
            return None
    except:
        print('Программа выполнила недопустимую операцию и будет закрыта')
        return None

list_notes = load_from_file('IO_Amelkin_Mikhail.yaml')

if list_notes is not None:
    if type(list_notes) == list:
        for n in list_notes:
            if type(n) != dict:
                print('Ошибка при чтении файла или неверный формат')
                break

            print('\n************')
            for k,v in n.items():
                print (k,':',v)
        #print(list_notes)
    else:
        print('Ошибка при чтении файла или неверный формат')

else:
    print('File is empty. No data found')

