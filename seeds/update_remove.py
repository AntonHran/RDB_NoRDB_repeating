from conf.db_connection import session
from conf.models import Teacher, Student, Contact, TeacherStudent


def update_student(st_id: int, teachers: list):
    student = session.query(Student).filter(Student.id == st_id).first()
    student.teachers = teachers
    session.commit()
    return student


if __name__ == '__main__':
    teachers_ = session.query(Teacher).filter(Teacher.id.in_([1, 2, 3])).all()
    update_student(2, teachers_)
