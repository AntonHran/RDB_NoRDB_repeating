import argparse

from create import *
from read import read_result
from update import update_table
from remove import remove_row


parser = argparse.ArgumentParser(description='CLI DB CRUD app')
parser.add_argument('--action', '-a', help='Commands: create, read, update, delete')
parser.add_argument('--model', '-m', help='use before the certain table for some changes')
# arguments of tables
parser.add_argument('--id')
parser.add_argument('--group_name', help='name of a group')
parser.add_argument('--firstname', help='first name')
parser.add_argument('--lastname', help='last name')
parser.add_argument('--email')
parser.add_argument('--phone')
parser.add_argument('--address')
parser.add_argument('--start_w', help='Date of work starting')
parser.add_argument('--subject')
parser.add_argument('--grade')
parser.add_argument('--stud_id')
parser.add_argument('--group_id')
parser.add_argument('--lector_id')
parser.add_argument('--subj_id')
parser.add_argument('--lesson_date')

arguments = parser.parse_args()
my_arg = vars(arguments)

# actions with tables
action = my_arg.get('action')
model = my_arg.get('model')
id_ = my_arg.get('id')
group_name = my_arg.get('group_name')
first_name = my_arg.get('firstname')
last_name = my_arg.get('lastname')
full_name = my_arg.get('fullname')
email = my_arg.get('email')
phone = my_arg.get('phone')
address = my_arg.get('address')
start_work = my_arg.get('start_work')
subject_name = my_arg.get('subject')
grade = my_arg.get('grade')
group_id = my_arg.get('group_id')
student_id = my_arg.get('stud_id')
lector_id = my_arg.get('lector_id')
subject_id = my_arg.get('subj_id')
lesson_date = my_arg.get('lesson_date')

args = (model, id_, group_name, first_name, last_name, full_name, email, phone, )


def main():
    match action:
        case 'create':
            if model == 'Group':
                create_record("Group", {"name": group_name})
            elif model == 'Student':
                create_student(first_name, last_name, int(group_id))
            elif model == 'Lector':
                create_lector(first_name, last_name, start_work)
            elif model == 'Subject':
                create_subject(subject_name)
            elif model == 'Grade':
                create_grade(grade, lesson_date, student_id, subject_id)
        case 'read':
            read_result(model, int(id_))
        case 'update':
            update_table(my_arg)
        case 'delete':
            result = remove_row(model, int(id_))
            if result > 0:
                print(f'Removed: {result}')
            else:
                print('Not found such task')
        case _:
            print('Nothing...')


if __name__ == '__main__':
    main()
