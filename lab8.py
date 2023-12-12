from flask import Blueprint, render_template, request, abort, jsonify
from datetime import datetime

lab8 = Blueprint('lab8', __name__)

@lab8.route('/lab8/')
def main():
    return render_template('lab8/index.html')

courses = [
    {"name": "c++", "videos": 3, "price": 3000},
    {"name": "basic", "videos": 30, "price": 0},
    {"name": "c#", "videos": 8}
]

@lab8.route('/lab8/api/courses/', methods=['GET'])
def get_courses():
    return jsonify(courses)

@lab8.route('/lab8/api/courses/<int:course_num>', methods=['GET'])
def get_course(course_num):
    if 0 <= course_num < len(courses):
        return jsonify(courses[course_num])
    else:
        abort(404)

@lab8.route('/lab8/api/courses/<int:course_num>', methods=['DELETE'])
def del_course(course_num):
    if 0 <= course_num < len(courses):
        del courses[course_num]
        return '', 204

@lab8.route('/lab8/api/courses/<int:course_num>', methods=['PUT'])
def put_course(course_num):
    if 0 <= course_num < len(courses):
        course = request.get_json()
        courses[course_num]['name'] = course.get('name', courses[course_num]['name'])
        courses[course_num]['videos'] = course.get('videos', courses[course_num]['videos'])
        courses[course_num]['price'] = course.get('price', None)  # Set price to None if not provided
        return jsonify(courses[course_num])
    else:
        abort(404)

@lab8.route('/lab8/api/courses/', methods=['POST'])
def add_course():
    course = request.get_json()
    course['createdAt'] = datetime.now()
    course['price'] = course.get('price', None)  # Set price to None if not provided
    courses.append(course)
    return {"num": len(courses)-1}
