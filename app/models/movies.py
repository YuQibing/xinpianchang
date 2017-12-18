from app.extensions import db


class Movies(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    image_url = db.Column(db.String(length=300))
    title = db.Column(db.String(length=100))
    views = db.Column(db.String(length=10))
    good = db.Column(db.Integer())
    auth = db.Column(db.String(length=30))
    vocation = db.Column(db.String(length=30))
    video_url = db.Column(db.String(length=300), default='')
