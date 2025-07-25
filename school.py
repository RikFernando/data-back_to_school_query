# pylint:disable=C0111,C0103


def students_from_city(db, city):
    """return a list of students from a specific city"""
    query = '''SELECT students.first_name
    FROM students
    WHERE students.birth_city = ?
    '''
    db.execute(query, (city,))
    students = db.fetchall()
    students_list = [student[0] for student in students]
    return students_list




# To test your code, you can **run it** before running `make`
#   => Uncomment the following lines + run:
#   $ python school.py
#
# import sqlite3
# conn = sqlite3.connect('data/school.sqlite')
# db = conn.cursor()
# print(students_from_city(db, 'Paris'))
