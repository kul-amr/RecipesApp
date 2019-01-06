from flask import request
from flask_restplus import Resource

from ..util.dao import CourseDAO
from ..service.course_service import *
from ..util.decorator import *

api = CourseDAO.api
_course = CourseDAO.course


@api.route('/')
class CourseList(Resource):
    @api.doc('list_of_all_courses')
    @api.marshal_list_with(_course,envelope='data')
    # @token_required
    def get(self):
        return get_courses()

    @api.response(201,'course created successfully')
    @api.doc('create_new_course')
    @api.expect(_course,validate=True)
    def post(self):
        data =  request.json
        return create_course(data)


@api.route('/<course_id>')
@api.param('course_id')
@api.response(404,'course not found')
class Course(Resource):
    @api.doc('get_course_with_id')
    @api.marshal_with(_course)
    def get(self, course_id):
        course = get_course(course_id=course_id)

        if not course:
            api.abort(404)
        else:
            return course




@api.route('/<course_name>')
@api.param('course_name')
@api.response(404,'course not found')
class Ingredient(Resource):
    @api.doc('get_course_with_name')
    @api.marshal_with(_course)
    def get(self, course_name):
        course = get_course(course_name=course_name)

        if not course:
            api.abort(404)
        else:
            return course