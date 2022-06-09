from flask import Blueprint,g,render_template
from ..tags.tag import Tag,db
from ..blogs.blog import Blog
from ..sorts.sort import sort
from settings import *


bug = Blueprint('bug', __name__,url_prefix="/bug/")


@bug.route('404/')
def g404():
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
    return render_template("bug/404.html", **context)