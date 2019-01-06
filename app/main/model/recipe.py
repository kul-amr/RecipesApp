from .. import db



class Recipe(db.Model):

    __tablename__ = "recipes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), unique=True, nullable=False)
    recipe_id = db.Column(db.String(50), unique=True)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'),nullable=False)

    def __repr__(self):
        return "<Recipe '{}'>".format(self.title)

