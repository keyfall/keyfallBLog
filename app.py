from flask import Flask


from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

#账号:密码@数据库ip地址:端口号/数据库名
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@localhost:3306/keyfallblog"


# 数据库修改跟踪操作
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#请求结束后会自动提交数据库中的变动
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True

# 开启输出底层执行的sql语句
app.config["SQLALCHEMY_ECHO"] = True
# 秘钥，前端form表单时CSRF需要
app.config['SECRET_KEY'] = "54683ASDASXCVDSQ8646"
db = SQLAlchemy(app)


from apps.blogs.view import blog
from apps.tags.view import tag
from apps.sorts.view import Sort
from apps.bug.view import bug

app.register_blueprint(blog)
app.register_blueprint(tag)
app.register_blueprint(Sort)
app.register_blueprint(bug)







# SQLALCHEMY_NATIVE_UNICODE    # 可以用于显式禁用原生 unicode 支持
# SQLALCHEMY_POOL_SIZE         # 数据库连接池的大小，默认是引擎默认值（5）
# SQLALCHEMY_POOL_TIMEOUT      # 设定连接池的连接超时时间，默认是 10
# SQLALCHEMY_POOL_RECYCLE      # 多少秒后自动回收连接，mysql默认为2小时
# SQLALCHEMY_RECORD_QUERIES    # 可以用于显式地禁用或启用查询记录
# SQLALCHEMY_ECHO              # 为Ture时用于调试，显示错误信息
# SQLALCHEMY_BINDS             # 一个映射 binds 到连接 URI 的字典




@app.route('/')
def hello():
    return "hello world"



