# import pymongo
#
# uri="mongodb://127.0.0.1:27017"
# client=pymongo.MongoClient(uri)
# database=client['fullstack']
# collection=database['students']
# #cursor object
# students=collection.find({})
# #list object
# # student_list=[]
# # for student in students:
# #     student_list.append(student)
# #     print(student)
#
# # for student in students:
# #     print(student)
# #List Comprehensions
# #students=[student for student in collection.find({})]
# # students=[student['mark'] for student in collection.find({})]
# students=[student['mark'] for student in collection.find({}) if student['mark']==90]
# print(students)
from database import Database
from models.post import Post
# post=Post()
# post2=Post()
Database.initialize()
post=Post(
    blog_id="123",
    title="Another great post",
    content="This is some sample content",
    author="Jose"
)
post.save_to_mongo()
#post2.content="Different conetnt"

