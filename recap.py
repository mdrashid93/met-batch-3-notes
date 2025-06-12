name = "Joy"
age = 14
is_married = False
fruits = ["banana","kiwi", "dragon"]
colors = ('white', 'black', 'blue')
users = {'Alex', 'Anny', 'Ria'}
person = {
    "name": "Chen",
    "age": 30
}



# 1. lists inside lists
 
# fruits = [["jack", "apple"], ["orange", "kiwi"], ["dragon", "grape"]]
 
# print(fruits[-1][-2])
 
 
# 2. tuple inside tuple
# coordinates = ((0, 1), (2, 3), (4, 5))
# print(coordinates[2][1])
 
 
# 3. tuple inside a list
# students = [("Alice", 23), ("Bob", 21)]
# print(students[1][1])
 
# 4. List inside a tuple
# groups = ([10, 20], [30, 40])
# print(groups[1][1])
 
# 5. list of dictionaries
# students = [{
#     "name": "Alice",
#     "age": 23
# }, {
#     "name": "Bob",
#     "age": 27
# }]
 
# print(students[0]["name"])
 
 
# 6. List inside a dictionary
# subject_marks = {
#     "Math": [30, 67, 80]
# }
# print(subject_marks["Math"][1])
 
 
# 7. Dictionary inside a Dictionary
# user_profile = {
#     "alice": {
#         "name": "Alice",
#         "age": 23
#     }
# }
 
# print(user_profile)
 
 
# 8. Dictionary inside a list
 
# billing_history = [{
#     "amount": "200",
#     "status": "failed"
# },
# {
#     "amount": "832",
#     "status": "success"
# }
# ]
 
# for i in billing_history:
#     print(f'Payment Rs.{i["amount"]} was {i["status"]}')
 
# 9. dictionary inside a tuple
# billing_history = ({
#     "amount": "200",
#     "status": "failed"
# },
# {
#     "amount": "832",
#     "status": "success"
# }
# )
 
# for i in billing_history:
#     print(f'Payment Rs.{i["amount"]} was {i["status"]}')
 
 
# students = [
#    {"name": "Alice", "marks": [80, 85, 90]},
#    {"name": "Bob", "marks": [70, 75, 68]},
#    {"name": "Charlie", "marks": [90, 92, 88]}
# ]
# # Task:
# # Write a function that calculates average marks for each student,
# # then sorts and prints
