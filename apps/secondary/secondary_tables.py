from app import db

article_tag = db.Table('article_tag',
                       db.Column("blog_id", db.Integer, db.ForeignKey('blog.id'), primary_key=True),
                       db.Column("tag.id", db.Integer, db.ForeignKey('tag.id'), primary_key=True)
                       )