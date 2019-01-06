from .. import db



class Course(db.Model):

    __tablename__ = "courses"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    course_title = db.Column(db.String(255), unique=True, nullable=False)
    course_id = db.Column(db.String(50),unique=True)

    def __repr__(self):
        return "<Course '{}'>".format(self.course_title)

