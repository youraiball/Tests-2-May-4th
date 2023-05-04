from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Game(db.Model):
    """Board game."""

    __tablename__ = "games"
    game_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    description = db.Column(db.String(100))


def connect_to_db(app, db_uri="postgresql:///games"):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.app = app
    db.init_app(app)


def example_data():
    """Create example data for the test database."""
    # a function that creates a Game instance and adds it to the database.

    game_1 = Game(name = "Duck Duck Goose", description = "steal each other's seats")
    game_2 = Game(name = "Chess", description = "Kill the King")
    game_3 = Game(name = "Musical Chairs", description = "kick people out")

    db.session.add_all([game_1, game_2, game_3])
    db.session.commit()




if __name__ == '__main__':
    from party import app

    connect_to_db(app)
    print("Connected to DB.")
