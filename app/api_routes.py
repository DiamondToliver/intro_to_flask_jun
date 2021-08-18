from app import app, db
from flask import jsonify, request
from app.models import User, Post


@app.route('/api/users')
def users():
    """
    [GET] /api/users
    """
    users = [u.to_dict() for u in User.query.all()]
    return jsonify(users=users)


@app.route('/api/create-user', methods=['POST'])
def create_user():
    """
    [POST] /api/create-user
    """
    data = request.get_json()

    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    # Sad path - request body is missing key
    if not username or not email or not password:
        return jsonify({'error': 'You need a username, email, and password'}), 400

    # Create a new user
    new_user = User(username, email, password)

    # Add new user to the database
    db.session.add(new_user)
    db.session.commit()

    return jsonify(new_user.to_dict())


@app.route('/api/posts')
def posts():
    posts= [p.to_dict() for p in Post.query.all()]
    return jsonify(posts=posts)

@app.route('/api/create-post', methods=['POST'])
def create_post():
    data = request.get_json()
    print(data)
    title = data.get('title')
    user_id =data.get('user_name')
    body = data.get('body')
    
    if not title or not body or not user_id:
        return jsonify({'error': 'You need a username, email, and password'})
        
    print(title, body, user_id)
    new_post = Post(title,body,user_id)

    db.session.add(new_post)
    db.session.commit()

    return jsonify(new_post.to_dict())
