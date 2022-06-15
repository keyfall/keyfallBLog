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


@Sort.route('backqueryall/<int:page>')
def backqueryall(page):
    if(page==None):
        page=1
    sorts = sort.query
    pagination = sorts.paginate(page,10,error_out=False)
    sortss=pagination.items
    context = {
        'sorts':sortss,
        "pagination":pagination
    }
    return render_template("back/sorttables.html", **context)



@Sort.route('create/')
def create():
    return render_template("back/newsort.html")

@Sort.route('add/')
def sss2():
    return "ok"


@Sort.route('update/')
def sss():
    return "ok"


@Sort.route('del/')
def sss4():
    return "ok"


@Sort.route('query/<int:id>/<int:page>')
def queryone(id=None,page=None):
    if(page==None):
        page=1
    if(id==None):
        id=1
    blogs = Blog.query
    pagination = blogs.filter(Blog.sort_id==id).order_by(Blog.create_time.desc()).paginate(page,20,error_out=False)
    timeblogs=pagination.items
    starblogs = blogs.order_by(Blog.stars.desc()).all()
    title = sort.query.get_or_404(id).name
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
    return render_template("sort.html",**context)


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

