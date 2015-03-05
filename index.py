#access at http://localhost:8080/main

from bottle import route, run, request
import markdown

page='\
<a href="http://localhost:8080/main">Home</a><br>\
<a href="http://localhost:8080/new">New Post</a><br>\
<a href="http://localhost:8080/posts">Past Posts</a><br>'

form='<form action="/newpost" method="post">\
    Title: <input name="title" type="text" /><br>\
    <textarea name="content" rows="10"/></textarea><br>\
    <input value="Post" type="submit" />\
</form>'

posts=[]
numPosts=-1

@route('/main')
def main():
    return page
    
@route('/new')
def new():
	return page+form
	
@route('/newpost', method='POST')
def newpost():
	global posts
	global numPosts
	
	numPosts=numPosts+1
	title = request.forms.get('title')
	content = request.forms.get('content')
	content = markdown.markdown(content)
	temp = [title,content]
	posts.append(temp)

	return page+"<br>Post Created"
	
@route('/posts')
def pastPosts():
	global posts
	global numPosts

	show = ""
	if numPosts>-1:
		for i in posts:
			show=show+"<h1>"+i[0]+"</h1><br>"
			show=show+i[1]+"<br>"
			
	return page+show
			

run(host='localhost', port=8080)