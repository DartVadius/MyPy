from app import db


class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(255), index=True, unique=False)
    title = db.Column(db.String(255), index=True, unique=True)

    def __repr__(self):
        return '<Book %r>' % (self.author + self.title)
