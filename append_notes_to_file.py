import yaml
import uuid
from datetime import datetime as dt, timedelta


def save_to_file(my_notes,filename):
    with open (filename, 'a') as file:
        yaml.dump(my_notes,file)


note1 = {
    'username':'mikla',
    'note_id':str(uuid.uuid4()),
    'content':'shopping list',
    'status':'in progress',
    'created_date':dt.strftime(dt.today(),'%d %b'),
    'issue_date':dt.strftime((dt.today() + timedelta(days=7)),'%d %b'),
    'titles': ['milk','bread','sugar']
}

note2 = {
    'username':'mikla',
    'note_id':str(uuid.uuid4()),
    'content':'to do list',
    'status':'in progress',
    'created_date':dt.strftime(dt.today(),'%d %b'),
    'issue_date':dt.strftime((dt.today() + timedelta(days=7)),'%d %b'),
    'titles': ['gym','coding']
}


my_list_notes = [note1,note2]

save_to_file(my_list_notes,'IO_Amelkin_Mikhail.yaml')