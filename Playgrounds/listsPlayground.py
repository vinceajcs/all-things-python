courses = ['History', 'Math', 'Physics', 'CS']
print(courses)
print(len(courses))
print(courses[-1] == courses[len(courses) - 1])
# index -1 will always be the last item

print(courses[::-1])
print(courses[:2])  # same as [0:2]
print(courses[2:])


courses.append('Art')
print(courses)
courses.append(1)

courses.insert(0, 'Art')
print(courses)

courses_2 = ['Bio', 'Nursing']

courses.insert(0, courses_2)
print(courses)
print(courses[0])

# add actual items
courses.extend(courses_2)
print(courses)

courses.remove('Math')
print(courses)
print(courses.pop())

courses.reverse()
print(courses)

# courses.sort()
print(courses)

# courses.sort(reverse=True)
print(courses)

# if we don't wanna change the actual list

# sortedCourses = sorted(courses)
# print(sortedCourses)

nums = [1, 2, 3, 5, 92, 8, 100]
print(max(nums))
print(min(nums))
print(sum(nums))

print(courses.index(1))
# print(courses.index('Engineering')) returns error

print('Engineering' in courses)
print('Art' in courses)

courses.remove(courses_2)
print(courses)
courses.remove('Art')
courses.remove(1)
print(courses)

for course in courses:
    print(course)


for index, course in enumerate(courses):
    print(index, course)

print('')

for i, course in enumerate(courses, start=2):
    print(i, course)

joined = ' '.join(courses)
print("hey" + joined)

joined = ', '.join(courses)
print(joined)

joined = ' - '.join(courses)
print(joined)

newList = joined.split(' - ')
print(newList)


# lists mutable, tuples are immutable

# mutable
list1 = [1, 2, 3]
list2 = list1

print(list1)
print(list2)

list1[0] = 4

print(list1)
print(list2)

# immutable (can't append, remove, etc)
tuple1 = (1, 2, 3)
tuple2 = tuple1

print(tuple1)
print(tuple2)

# tuple1[0] = 4 (can't do this)

# sets
set1 = {'History', 'Math', 'Physics', 'CS', 'Math'}
print(set1)
# gets rid of duplicates

print('Math' in set1)

set2 = {'History', 'Math', 'Art', 'Design'}

print(set1.intersection(set2))  # determine same elements
print(set1.difference(set2))  # determine different elements

print(set1.union(set2))  # combine sets


# creating lists, tuples, and sets

emptyList = []
emptyList = list()

emptyTuple = ()
emptyTuple = tuple()

emptySet = {}  # can't do this! this is a dictionary
emptySet = set()  # this is the correct way
