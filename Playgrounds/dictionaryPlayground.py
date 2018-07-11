# like hash maps

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CS']}

student.update({'name': 'Jane', 'age': 26, 'phone': '555-5555'})

print(student.get('pet', 'dog'))  # if key doesn't exist, return 'dog'

print(student)

age = student.pop('age')
# del student['age'] #deletes key value pair with specified key
print(age)
print(student)

print(len(student))  # returns number of keys

print(student.keys())

print(student.values())

print(student.items())

for key in student:
    print(key)

for key, value in student.items():
    print(key, value)

print(list(student.values()))

student['name'] += 'Hey'

print(student)

print(7 / 4)

j = 123
print(str(j))

nums = [1, 3, 5, 6]
target = 2

for i, j in enumerate(nums):
    if target < nums[i + 1]:
        print(target)
        print(nums[i + 1])
        print(i)
        break
