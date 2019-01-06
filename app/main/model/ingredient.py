from .. import db



class Ingredient(db.Model):

    __tablename__ = "ingredients"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    ingredient_id = db.Column(db.String(50),unique=True)

    def __repr__(self):
        return "<Ingredient '{}'>".format(self.name)

