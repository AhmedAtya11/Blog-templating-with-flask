from flask import Flask, render_template
import requests


response=requests.get("https://api.npoint.io/ab425fdf58b1703d48a0")
data=response.json()


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html",post_data=data)


@app.route('/post/<int:index>')
def show_post(index):
    for post in data:
        if post['id']==index:
            return render_template ("post.html",title=post['title'],post_body=post['more_details'])


if __name__ == "__main__":
    app.run(debug=True)
