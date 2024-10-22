from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField

class RoleForm(FlaskForm):
    role = SelectField('Select Role', choices=[('student', 'Student'), ('admin', 'Admin')])
    submit = SubmitField('Submit')

class SearchForm(FlaskForm):
    search_by = SelectField('Search By', choices=[('name', 'Book Name'), ('author', 'Author Name')])
    query = StringField('Search Input')
    submit = SubmitField('Search')

class RequestForm(FlaskForm):
    book_id = StringField('Book ID')
    submit = SubmitField('Request Book')

class AdminForm(FlaskForm):
    book_id = StringField('Book ID')
    action = SelectField('Action', choices=[('Accepted', 'Accept'), ('Rejected', 'Reject')])
    submit = SubmitField('Update Status')
