import argparse

from create import create_main
from read import read_result
from update import update_main
from remove import remove_row


parser = argparse.ArgumentParser(description='CLI DB CRUD app')
parser.add_argument('--action', '-a', help='Commands: create, read, update, delete')
parser.add_argument('--model', '-m', help='use before the certain table for some changes')
# arguments of tables
parser.add_argument('--id')
# parser.add_argument('--group_name', help='name of a group')
parser.add_argument('--firstname', help='first name')
parser.add_argument('--lastname', help='last name')
parser.add_argument('--email')
parser.add_argument('--phone')
parser.add_argument('--address')
parser.add_argument('--start_date', help='Date of work starting')
parser.add_argument('--name')
parser.add_argument('--grade')
parser.add_argument('--stud_id')
parser.add_argument('--group_id')
parser.add_argument('--teach_id')
parser.add_argument('--subj_id')
parser.add_argument('--date')

arguments = parser.parse_args()
my_arg = vars(arguments)

# actions with tables
action = my_arg.get('action')
model = my_arg.get('model')
id_ = my_arg.get('id')
"""group_name = my_arg.get('group_name')
first_name = my_arg.get('firstname')
last_name = my_arg.get('lastname')
full_name = my_arg.get('fullname')
email = my_arg.get('email')
phone = my_arg.get('phone')
address = my_arg.get('address')
start_work = my_arg.get('start_work_date')
subject_name = my_arg.get('subject')
grade = my_arg.get('grade')
group_id = my_arg.get('group_id')
student_id = my_arg.get('stud_id')
lector_id = my_arg.get('lector_id')
subject_id = my_arg.get('subj_id')
lesson_date = my_arg.get('lesson_date')"""

# args = (model, id_, group_name, first_name, last_name, full_name, email, phone, )


def main():
    match action:
        case 'create':
            create_main(my_arg)
        case 'read':
            read_result(model, int(id_))
        case 'update':
            update_main(my_arg)
        case 'delete':
            result = remove_row(model, int(id_))
            if result > 0:
                print(f'Removed: {result}')
            else:
                print('Such a record was not found')
        case _:
            print('Nothing...')


if __name__ == '__main__':
    main()
