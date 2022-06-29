from flask import Blueprint,g,render_template,jsonify,request,redirect,url_for
from .blog import Blog,db
from ..tags.tag import Tag
from ..sorts.sort import sort
from settings import *
from .blogForm import blogForm
import datetime
import os


blog = Blueprint('blog', __name__,url_prefix="/blog/")



@blog.before_request
def before_request():

    engine = db.get_engine()
    conn = engine.connect()
    g.conn = conn
    print("starting connection")


@blog.after_request
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





@blog.route('back/')
def back():
    return render_template("back/blogtables.html")



@blog.route('create/',methods=['get','post'])
def create():
    form = blogForm()
    if request.method == 'GET':
        tags = Tag.query.all()
        sorts = sort.query.all()
        return render_template("back/newblog.html",form=form,tags=tags,sorts=sorts)
    if request.method == 'POST':
        if form.validate_on_submit():
            title = form.title.data
            content = form.content.data
            create_time=update_time=datetime.date.today()
            tags = form.tags.data
            taglist = tags.split(',')
            alltag = Tag.query.with_entities(Tag.name).all()
            ts = []
            for tag in taglist:
                if str(alltag).find(tag)==-1:
                    ts.append(Tag(name=tag))
                else:
                    t = Tag.query.filter_by(name=tag).first()
                    ts.append(t)
            s=None
            if form.sort.data!=0:
                s = form.sort.data
            img_url=None
            if form.fileimg.data:
                if not os.path.exists(upload_dir+str(create_time)):
                    os.makedirs(upload_dir+str(create_time))
                img_url = ori_img+"/"+str(create_time)+"/"+form.fileimg.data.filename
                form.fileimg.data.save(upload_dir+str(create_time)+"/"+form.fileimg.data.filename)
            blog = Blog(blogname=title,content=content,create_time=create_time,update_time=update_time,image_url=img_url,sort_id=s)
            blog.tags = ts
            db.session.add(blog)
            db.session.commit()
        else:
            print("报错了")
        return redirect(url_for('blog.backqueryall',page=1))



@blog.route('backqueryall/<int:page>')
def backqueryall(page):
    if(page==None):
        page=1
    blogs = Blog.query
    pagination = blogs.order_by(Blog.create_time.desc()).paginate(page,10,error_out=False)
    timeblogs=pagination.items
    context = {
        'timeblogs':timeblogs,
        "pagination":pagination
    }
    return render_template("back/blogtables.html", **context)

@blog.route('ss',methods=['GET','POST'])
def ss():
    return render_template("mm.html")

@blog.route('qqq/',methods=['GET','POST'])
def qqq():
    blogs = Blog.query.all()
    # pagination = blogs.order_by(Blog.create_time.desc()).paginate(1,pageSize,error_out=False)
    # timeblogs=pagination.items
    # starblogs = blogs.order_by(Blog.stars.desc()).all()
    # tags = Tag.query.all()
    # sorts = sort.query.all()
    starblogsdict=[]
    for index,blog in enumerate(blogs):
        starblogsdict.append(blog.auth_dict())
    context = {
        "starblogs":starblogsdict

    }

    return jsonify(context)



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


@blog.route('update/<int:id>',methods=['GET','POST'])
def update(id):
    form = blogForm()
    blogs = Blog.query
    blog = blogs.get_or_404(id)
    if request.method == 'GET':
        tags = Tag.query.all()
        sorts = sort.query.all()
        return render_template("back/editblog.html",form=form,blog=blog,id=id,tags=tags,sorts=sorts)
    if request.method == 'POST':
        if form.validate_on_submit():
            blog.blogname=form.title.data
            blog.content=form.content.data
            blog.update_time=update_time=datetime.date.today()
            tags = form.tags.data
            taglist = tags.split(',')
            alltag = Tag.query.with_entities(Tag.name).all()
            ts = []
            for tag in taglist:
                if str(alltag).find(tag) == -1:
                    ts.append(Tag(name=tag))
                else:
                    t = Tag.query.filter_by(name=tag).first()
                    ts.append(t)
            if form.sort.data!=0:
                blog.sort_id = form.sort.data
            img_url=None
            if form.fileimg.data:
                if not os.path.exists(upload_dir+str(update_time)):
                    os.makedirs(upload_dir+str(update_time))
                img_url = ori_img+"/"+str(update_time)+"/"+form.fileimg.data.filename
                form.fileimg.data.save(upload_dir+str(update_time)+"/"+form.fileimg.data.filename)
            blog.image_url=img_url
            blog.tags=ts
            db.session.commit()
        else:
            print("报错了")
        return redirect(url_for('blog.backqueryall',page=1))


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

@blog.route('del/<int:id>/page/<int:page>')
def dele(id,page):
    blogs = Blog.query
    blog = blogs.get_or_404(id)
    if blog:
        db.session.delete(blog)
    pagination = blogs.order_by(Blog.create_time.desc()).paginate(page, 10, error_out=False)
    timeblogs = pagination.items
    context = {
        'timeblogs': timeblogs,
        "pagination": pagination
    }
    return render_template("back/blogtables.html", **context)

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


@blog.route('queryallarticles/<int:page>/')
def queryallarticles(page=None):
    if(page==None):
        page=1
    blogs = Blog.query
    pagination = blogs.order_by(Blog.create_time.desc()).paginate(page,20,error_out=False)
    timeblogs=pagination.items
    starblogs = blogs.order_by(Blog.stars.desc()).all()
    tags = Tag.query.all()
    sorts = sort.query.all()

    context = {
        "starblogs":starblogs,
        'timeblogs':timeblogs,
        'tags':tags,
        'sorts':sorts,
        "pagination":pagination,
        "title":"文章"
    }
    return render_template("blogs.html",**context)