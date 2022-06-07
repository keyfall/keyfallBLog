from app import db


class sort(db.Model):
    __tablename__ = "sort"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    blogs = db.relationship("Blog", backref='sorts', lazy="select")