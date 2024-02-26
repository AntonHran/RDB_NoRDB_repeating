import argparse

from create import *
from read import *
from update import *
from delete import *


parser = argparse.ArgumentParser(description='CLI DB CRUD app')
parser.add_argument('--action', '-a', help='Commands: create, read, update, delete')
parser.add_argument('--model', '-m', help='use before the certain table for some changes')
# arguments of tables
parser.add_argument('--id')
parser.add_argument('--grname', help='name of a group')
parser.add_argument('--fname', help='first name')
parser.add_argument('--lname', help='last name')
# parser.add_argument('--fullname', help='full name')
parser.add_argument('--email')
parser.add_argument('--phone')
parser.add_argument('--address')
parser.add_argument('--stw', help='Date of work staring')
parser.add_argument('--subject')
parser.add_argument('--grade')
parser.add_argument('--stid')
parser.add_argument('--groupid')
parser.add_argument('--lectorid')
parser.add_argument('--subid')
parser.add_argument('--lesdate')

arguments = parser.parse_args()
my_arg = vars(arguments)

# actions with tables
action = my_arg.get('action')
model = my_arg.get('model')
id_ = my_arg.get('id')
group_name = my_arg.get('grname')
first_name = my_arg.get('fname')
last_name = my_arg.get('lname')
full_name = my_arg.get('fullname')
email = my_arg.get('email')
phone = my_arg.get('phone')
address = my_arg.get('address')
start_work = my_arg.get('stw')
subject_name = my_arg.get('subject')
grade = my_arg.get('grade')
group_id = my_arg.get('groupid')
student_id = my_arg.get('stid')
lector_id = my_arg.get('lectorid')
subject_id = my_arg.get('subid')
lesson_date = my_arg.get('lesdate')


def main():
    match action:
        case 'create':
            if model == 'Group':
                create_group(group_name)
            elif model == 'Student':
                create_student(first_name, last_name, email, phone, address, group_id)
            elif model == 'Lector':
                create_lector(first_name, last_name, email, phone, address, start_work)
            elif model == 'Subject':
                create_subject(subject_name, lector_id)
            elif model == 'Mark':
                create_mark(grade, lesson_date, student_id, subject_id)
        case 'read':
            res = read_table(model, id_)
            return_read_res(res, model)
        case 'update':
            if model == 'Group':
                updated_row = update_group(id_, group_name)
                check_updated_row(model, updated_row)
            elif model == 'Student':
                updated_row = update_student(id_, first_name, last_name, email, phone, address, group_id)
                check_updated_row(model, updated_row)
            elif model == 'Lector':
                updated_row = update_lector(id_, first_name, last_name, email, phone, address, start_work)
                check_updated_row(model, updated_row)
            elif model == 'Subject':
                updated_row = update_subject(id_, subject_name, lector_id)
                check_updated_row(model, updated_row)
            elif model == 'Mark':
                updated_row = update_mark(id_, grade, lesson_date, student_id, subject_id)
                check_updated_row(model, updated_row)
        case 'delete':
            result = delete_table_row(id_, model)
            if result > 0:
                print(f'Removed: {result}')
            else:
                print('Not found such task')
        case _:
            print('Nothing...')


if __name__ == '__main__':
    main()
