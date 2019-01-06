from .. import db



class RecipeIngredient(db.Model):

    __tablename__ = "recipe_ingredients"

    # id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), primary_key=True)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredients.id'), primary_key=True)
    quantity = db.Column(db.String(100))
    recipe = db.relationship('Recipe',backref="recipes")
    ingredient = db.relationship('Ingredient',backref="ingredients")

    def __repr__(self):
        return "<RecipeIngred '{}'>".format(self.recipe.title,self.ingredient.name)

