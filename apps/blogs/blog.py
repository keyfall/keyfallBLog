from app import db
from ..secondary.secondary_tables import article_tag

class Blog(db.Model):
    __tablename__ = 'blog'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    blogname = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(5000), nullable=False)
    create_time = db.Column(db.Date, nullable=False)
    update_time = db.Column(db.Date, nullable=False)
    image_url = db.Column(db.String(200), nullable=True)
    tags = db.relationship('Tag', secondary=article_tag, lazy="select",backref=db.backref("blogs"))
    stars = db.Column(db.Integer, nullable=False, default=0)
    sort_id = db.Column(db.Integer,db.ForeignKey("sort.id"))





    def auth_to_dict(self):
        tagsdict = {}
        for index,tag in enumerate(self.tags):
            tagsdict[index] = tag.auth_to_dict
        auth_dict = {
            "id" : self.id,
            "blogname" : self.blogname,
            "content" : self.content,
            "create_time" : self.create_time,
            "update_time" : self.update_time,
            "image_url" : self.image_url,
            "stars" : self.stars,
            "tags" : tagsdict,
            "sort" : self.sorts.auth_dict() if self.sort_id is not None else "默认"
        }
        return auth_dict

    def auth_dict(self):


        auth_dict = {
            "id" : self.id,
            "blogname" : self.blogname,
            "content" : self.content,
            "create_time" : self.create_time,
            "update_time" : self.update_time,
            "image_url" : self.image_url,
            "stars" : self.stars,
            "sort": self.sorts.auth_dict() if self.sort_id is not None else "默认"
        }
        return auth_dict