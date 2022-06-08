from flask import Blueprint,g,render_template
from .blog import Blog,db
from ..tags.tag import Tag
from ..sorts.sort import sort
from settings import *




blog = Blueprint('blog', __name__,url_prefix="/blog/")


@blog.route('aboutme/')
def aboutme():
    blogs = Blog.query
    pagination = blogs.order_by(Blog.create_time.desc()).paginate(1,pageSize,error_out=False)
    timeblogs=pagination.items
    starblogs = blogs.order_by(Blog.stars.desc()).all()
    tags = Tag.query.all()
    sorts = sort.query.all()
    context = {
        "starblogs":starblogs,
        'timeblogs':timeblogs,
        'tags':tags,
        'sorts':sorts
    }
    return render_template("about.html", **context)

@blog.route('add/')
def sss():
    return "ok"


@blog.route('update/')
def sss2():
    return "ok"


@blog.route('del/')
def sss4():
    return "ok"


@blog.route('query/<int:id>')
def queryone(id):
    blogs = Blog.query
    blog = blogs.get_or_404(id)
    starblogs = blogs.order_by(Blog.stars.desc()).all()
    timeblogs=blogs.order_by(Blog.create_time.desc()).paginate(1,4,error_out=False).items
    tags = Tag.query.all()
    sorts = sort.query.all()
    context = {
        "blog":blog,
        "timeblogs":timeblogs,
        "tags":tags,
        "sorts":sorts,
        "starblogs":starblogs
    }
    return render_template("blog.html", **context)

@blog.route('queryall/')
def queryall():
    blogs = Blog.query
    pagination = blogs.order_by(Blog.create_time.desc()).paginate(1,pageSize,error_out=False)
    timeblogs=pagination.items
    starblogs = blogs.order_by(Blog.stars.desc()).all()
    tags = Tag.query.all()
    sorts = sort.query.all()
    context = {
        "starblogs":starblogs,
        'timeblogs':timeblogs,
        'tags':tags,
        'sorts':sorts,
        "pagination":pagination
    }
    return render_template("index.html", **context)


@blog.route('queryall/<int:page>/')
def queryallpage(page=None):
    if(page==None):
        page=1
    blogs = Blog.query
    pagination = blogs.order_by(Blog.create_time.desc()).paginate(page,pageSize,error_out=False)
    timeblogs=pagination.items
    starblogs = blogs.order_by(Blog.stars.desc()).all()
    tags = Tag.query.all()
    sorts = sort.query.all()

    context = {
        "starblogs":starblogs,
        'timeblogs':timeblogs,
        'tags':tags,
        'sorts':sorts,
        "pagination":pagination
    }
    return render_template("index.html",**context)