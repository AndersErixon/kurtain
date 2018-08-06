cd C:\Users\kurt\Python\Kurtain
set FLASK_APP=kurtain.py
python
from app import app, db
from app.models import User, Post
u = User(username='susan', email='susan@example.com')
u.set_password('cat')
db.session.add(u)
db.session.commit()
@pause