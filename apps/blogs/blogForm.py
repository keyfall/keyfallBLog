from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField, TextAreaField, validators, IntegerField
from wtforms.validators import regexp,DataRequired


class blogForm(FlaskForm):
    title = StringField(label="标题",validators=[DataRequired()],
                        render_kw={'class':'span6 typeahead'}
                                  )
    fileimg = FileField(label="图片",
                        render_kw={'class':'input-file uniform_on',
                                   'id':"fileimg",
                                   'onchange':"change(this)"})
    content = TextAreaField(label="内容",
                            render_kw={'id':'mytextarea',
                                       'class':'cleditor'})
    sort = IntegerField(label="分类")

    tags = StringField(label="标签")

    submit = SubmitField("提交")