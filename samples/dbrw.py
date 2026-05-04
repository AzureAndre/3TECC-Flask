from flask import Flask, render_template as RenderTemplate, request, redirect       # Import the Flask class from the flask module


@app.route('/allposts', methods=['GET','POST'])                 # Define a route for the URL "/allposts" and specify that it accepts GET and POST requests
def posts():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        new_post = Post(title=title, content=content, author='Andre')
        db.session.add(new_post)
        db.session.commit()
        return redirect('/allposts')
    else:
        dbposts = Post.query.all()
        #dbposts = Post.query.filter_by(author='Author 1').all()
        #dbposts = Post.query.order_by(Post.title.desc()).all()
        #dbposts = Post.query.order_by(Post.date_posted.asc()).all()
        return RenderTemplate('allposts.html', posts=dbposts)


# Read DB by ID

dbpost = Post.query.get(2)
if dbpost == None:
    print('Post not found!')
else:   
    print(dbpost.title)

# Delete a post by ID
@app.route('/posts/delete/<int:id>')
def delete_post(id):
    post = Post.query.get(id)
    db.session.delete(post)
    db.session.commit()
    return redirect('/allposts')


# Edit a post by ID
@app.route('/posts/edit/<int:id>', methods=['GET','POST'])
def edit_post(id):
    dbpost = Post.query.get(id)
    if request.method == 'POST':
        dbpost.title = request.form['title']
        dbpost.content = request.form['content']
        db.session.commit()
        return redirect('/allposts')
    else:
        return RenderTemplate('editpost.html', post=dbpost)
