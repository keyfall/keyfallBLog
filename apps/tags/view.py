from flask import Blueprint,g,render_template
from ..blogs.blog import Blog
from .tag import Tag,db
from ..sorts.sort import sort
from settings import *


tag = Blueprint('tag', __name__,url_prefix="/tag/")


@tag.before_request
def before_request():

    engine = db.get_engine()
    conn = engine.connect()
    g.conn = conn
    print("starting connection")


@tag.after_request
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

@tag.route('add/')
def sss():
    return "ok"


@tag.route('update/')
def sss2():
    return "ok"


@tag.route('del/')
def sss3():
    return "ok"


@tag.route('query/<int:id>/<int:page>')
def queryone(id=None,page=None):
    if(page==None):
        page=1
    if(id==None):
        id=1
    blogs = Blog.query
    pagination = blogs.filter(Blog.sort_id==id).order_by(Blog.create_time.desc()).paginate(page,20,error_out=False)
    timeblogs=pagination.items
    starblogs = blogs.order_by(Blog.stars.desc()).all()
    title = Tag.query.get_or_404(id).name
    tags = Tag.query.all()
    sorts = sort.query.all()

    context = {
        "starblogs":starblogs,
        'timeblogs':timeblogs,
        'tags':tags,
        'sorts':sorts,
        "pagination":pagination,
        "title":title,
        "id":id
    }
    return render_template("tag.html",**context)


@tag.route('queryall/')
def queryall():
    blogs = Blog.query
    pagination = blogs.order_by(Blog.create_time.desc()).paginate(1,pageSize,error_out=False)
    timeblogs=pagination.items
    starblogs = blogs.order_by(Blog.stars.desc()).all()
    tags = Tag.query.all()
    blogslength = 0
    for tag in tags:
        blogslength += len(tag.blogs)
    sorts = sort.query.all()
    context = {
        "starblogs":starblogs,
        'timeblogs':timeblogs,
        'tags':tags,
        'sorts':sorts,
        "pagination":pagination,
        "blogslenth":blogslength
    }

    return render_template("tags.html",**context)