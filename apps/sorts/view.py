from flask import Blueprint,g,render_template
from ..blogs.blog import Blog
from ..tags.tag import Tag
from .sort import sort,db
from settings import *

Sort = Blueprint('sort', __name__,url_prefix="/sort/")


@Sort.before_request
def before_request():

    engine = db.get_engine()
    conn = engine.connect()
    g.conn = conn
    print("starting connection")


@Sort.after_request
def after_request(response):
    """
    这里如果有两个连接分别进入，先完成的给后完成的conn关了怎么办
    :param response:
    :return:
    """
    if g.conn is not None:
        print("closing connection")
        g.conn.close()
    return response

@Sort.route('add/')
def sss2():
    return "ok"


@Sort.route('update/')
def sss():
    return "ok"


@Sort.route('del/')
def sss4():
    return "ok"


@Sort.route('query/')
def queryone():
    return "ok"


@Sort.route('queryall/')
def queryall():
    blogs = Blog.query
    pagination = blogs.order_by(Blog.create_time.desc()).paginate(1,pageSize,error_out=False)
    timeblogs=pagination.items
    starblogs = blogs.order_by(Blog.stars.desc()).all()
    blogslength = blogs.filter(Blog.sort_id!=0).count()
    tags = Tag.query.all()
    sorts = sort.query.all()
    context = {
        "starblogs":starblogs,
        'timeblogs':timeblogs,
        'tags':tags,
        'sorts':sorts,
        "pagination":pagination,
        "blogslength":blogslength
    }

    return render_template("sorts.html",**context)