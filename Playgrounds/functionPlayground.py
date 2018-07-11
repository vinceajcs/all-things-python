def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


student_info('Math', 'Art', name='John', age='22')

courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

student_info(courses, info)
print('')

student_info(*courses, **info)  # same as line 5
