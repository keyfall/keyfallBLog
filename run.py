from app import app
from apps.blogs import blog
# from apps.tags import tag
# from apps.sorts import sort

if __name__ == '__main__':
    # db.drop_all()
    # db.create_all()
    app.run(host="127.0.0.1",port=8000)