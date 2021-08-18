<<<<<<< HEAD
from app import app
=======
from app import app, db
from app.models import User, Post



@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'User': User,
        'Post': Post
    }
>>>>>>> 8a71b3c31ee095cfe68dfefe165f39e20ad67bbd
