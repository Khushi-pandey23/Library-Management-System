from flask import Flask, render_template, request, redirect, url_for
from books import Books
from forms import RoleForm, SearchForm, RequestForm, AdminForm

app = Flask(__name__)
app.secret_key = "supersecretkey"

@app.route('/', methods=['GET', 'POST'])
def home():
    form = RoleForm()
    if form.validate_on_submit():
        role = form.role.data
        if role == 'student':
            return redirect(url_for('student'))
        elif role == 'admin':
            return redirect(url_for('admin'))
    return render_template('home.html', form=form)

# Route for student role
@app.route('/student', methods=['GET', 'POST'])
def student():
    request_form = RequestForm()
    
    if request_form.validate_on_submit():
        book_id = int(request_form.book_id.data)
        for book in Books:
            if book['id'] == book_id:
                book["Status"] = "Requested"
        return redirect(url_for('student'))
    
    return render_template('student.html', request_form=request_form)


# Route for admin role
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        book_id = int(request.form.get('book_id'))
        action = request.form.get('action')
        for book in Books:
            if book['id'] == book_id and book['Status'] == 'Requested':
                book['Status'] = action
                break
        return redirect(url_for('admin'))

    requested_books = [book for book in Books if book['Status'] in ['Requested', 'Accepted', 'Rejected']]
    return render_template('admin.html', requested_books=requested_books)



@app.route('/request_status', methods=['GET', 'POST'])
def request_status():
    requested_books = [book for book in Books if book['Status'] in ['Requested', 'Accepted', 'Rejected']]
    request_form = RequestForm()

    if request_form.validate_on_submit():
        book_id = request_form.book_id.data
        for book in Books:
            if book['id'] == int(book_id):
                book["Status"] = "Requested"
                break
        return redirect(url_for('request_status'))

    return render_template('request_status.html', requested_books=requested_books, request_form=request_form)



@app.route('/search', methods=['GET', 'POST'])
def search():
    search_form = SearchForm()
    result = []

    if search_form.validate_on_submit():
        search_by = search_form.search_by.data
        query = search_form.query.data

        if search_by == 'name':
            result = [book for book in Books if book['Name'].lower() == query.lower()]
        else:
            result = [book for book in Books if book['Author'].lower() == query.lower()]

        return render_template('search.html', search_form=search_form, result=result)

    return render_template('search.html', search_form=search_form, result=result)


if __name__ == "__main__":
    app.run(debug=True)
