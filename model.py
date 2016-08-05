from flask.ext.sqlalchemy import SQLAlchemy

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
    
    # In case this is run more than once, empty out existing data
    Game.query.delete()

    # Add sample game data
    twister = Game(name='twister', description='grid of dots to get twisted up on')
    scrabble = Game(name='scrabble', description='fit words on grid')


    db.session.add_all([twister, scrabble])
    db.session.commit()


if __name__ == '__main__':
    from server import app

    connect_to_db(app)
    print "Connected to DB."
