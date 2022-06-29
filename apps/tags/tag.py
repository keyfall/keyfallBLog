from app import db


class Tag(db.Model):
    __tablename__ = 'tag'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False,unique=True)

    def auth_to_dict(self):
        auth_dict={
            "id":self.id,
            "name":self.name
        }
        return auth_dict