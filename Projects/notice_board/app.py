from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models import db, Admin, Notice
from config import Config
from datetime import datetime

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

@login_manager.user_loader
def load_user(user_id):
    return Admin.query.get(int(user_id))

# --- Routes ---

@app.route('/')
def index():
    # User View Logic
    search_query = request.args.get('q', '')
    category_filter = request.args.get('category', 'All')
    sort_order = request.args.get('sort', 'newest')

    query = Notice.query

    # Search
    if search_query:
        query = query.filter(Notice.title.ilike(f'%{search_query}%'))

    # Filter
    if category_filter != 'All':
        query = query.filter_by(category=category_filter)

    # Sort
    if sort_order == 'oldest':
        query = query.order_by(Notice.created_at.asc())
    else:
        query = query.order_by(Notice.created_at.desc())

    notices = query.paginate(page=1, per_page=6, error_out=False)
    
    # Get unique categories for filter dropdown
    categories = [r.category for r in db.session.query(Notice.category).distinct()]

    return render_template('index.html', notices=notices, categories=categories)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = Admin.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            login_user(user)
            next_page = request.args.get('next')
            flash('Login successful!', 'success')
            return redirect(next_page) if next_page else redirect(url_for('dashboard'))
        else:
            flash('Login Unsuccessful. Check username and password', 'danger')
            
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

# --- Admin Dashboard Routes ---

@app.route('/dashboard')
@login_required
def dashboard():
    notices = Notice.query.order_by(Notice.created_at.desc()).all()
    return render_template('dashboard.html', notices=notices)

@app.route('/dashboard/add', methods=['POST'])
@login_required
def add_notice():
    title = request.form.get('title')
    content = request.form.get('content')
    category = request.form.get('category')
    
    if title and content:
        new_notice = Notice(title=title, content=content, category=category)
        db.session.add(new_notice)
        db.session.commit()
        flash('Notice added successfully!', 'success')
    else:
        flash('Title and Content are required!', 'danger')
        
    return redirect(url_for('dashboard'))

@app.route('/dashboard/edit/<int:id>', methods=['POST'])
@login_required
def edit_notice(id):
    notice = Notice.query.get_or_404(id)
    notice.title = request.form.get('title')
    notice.content = request.form.get('content')
    notice.category = request.form.get('category')
    
    db.session.commit()
    flash('Notice updated successfully!', 'success')
    return redirect(url_for('dashboard'))

@app.route('/dashboard/delete/<int:id>')
@login_required
def delete_notice(id):
    notice = Notice.query.get_or_404(id)
    db.session.delete(notice)
    db.session.commit()
    flash('Notice deleted.', 'warning')
    return redirect(url_for('dashboard'))

def create_default_admin():
    """Create default admin user if not exists"""
    admin = Admin.query.filter_by(username='admin').first()
    if not admin:
        admin = Admin(username='admin')
        admin.set_password('admin123')
        db.session.add(admin)
        db.session.commit()
        print("Default admin user created: username='admin', password='admin123'")
    else:
        print("Admin user already exists")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        create_default_admin()
    app.run(debug=True)
