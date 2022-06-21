from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

class sortForm(FlaskForm):
    name = StringField(label="名称",validators=[DataRequired()],
                        render_kw={'class':'span6 typeahead',
                                   "id":"typeahead"}
                                  )
    submit = SubmitField("提交")