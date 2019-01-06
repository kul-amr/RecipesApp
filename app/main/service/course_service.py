import uuid
from app.main import db
from app.main.model.course import Course


def create_course(data):

    course = Course.query.filter_by(course_title=data['course_title']).first()

    if not course:
        new_course = Course(course_id=str(uuid.uuid4())[:8],
                            course_title=data['course_title'])

        db.session.add(new_course)
        db.session.commit()

        resp_obj = {'status':'success',
                    'message':'course created successfully'}

        return resp_obj, 200
    else:
        resp_obj = {'status': 'fail',
                    'message': 'course already exists'}

        return resp_obj, 400


def get_course(course_id=None,course_name=None):

    if course_id is not None:
        return Course.query.filter_by(course_id=course_id).first()
    elif course_name is not None:
        return Course.query.filter_by(course_title=course_name).first()
    else:
        return None


def get_courses():

    return Course.query.all()