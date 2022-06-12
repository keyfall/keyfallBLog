from app import db
import json

class sort(db.Model):
    __tablename__ = "sort"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    blogs = db.relationship("Blog", backref='sorts', lazy="select")

    def auth_to_dict(self):
        blogdict = {}
        for index,blog in enumerate(self.blogs):
            blogdict[index] = blog.auth_dict()
        auth_dict={
            "id" : self.id,
            "name" : self.name,
            "blogs" : blogdict
        }
        return auth_dict

    def auth_dict(self):
        auth_dict={
            "id" : self.id,
            "name" : self.name
        }
        return auth_dict