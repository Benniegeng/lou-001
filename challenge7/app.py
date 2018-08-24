from flask import Flask, render_template, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/shiyanlou'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    created_time = db.Column(db.DateTime)
    category_id = db.Column(db.Integer,db.ForeignKey('category.id'))
    category = db.relationship('Category',backref=db.backref('posts', lazy='dynamic'))
    def __repr__(self):
        return '<File %r>' % self.title

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    def __repr__(self):
        return '<Category %r>' % self.name

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404

@app.route('/')
def index():
#    list_title = [i.title for i in File.query.all()]
#    for root, dirs, filenames in os.walk('/home/shiyanlou/files'):
#       for filename in filenames:
#            filepath = os.path.join(root, filename)
#            with open(filepath) as json_news:
#                dict_news = json.loads(json_news.read())
#                list_title.append(dict_news['title'])
    return render_template('index.html', files = File.query.all())
    
@app.route('/files/<file_id>')
def file(file_id):
#    filepath1 = os.path.join('/home/shiyanlou/files',filename+'.json')
#    if os.path.isfile(filepath1) :
#        with open(filepath1) as json_news_content:
#            dict_news_all = json.loads(json_news_content.read())
#            dict_news_content = dict_news_all['content']
#        return render_template('file.html', dict_news_content=dict_news_content)
#    else:
#        abort(404)
    f = File.query.filter_by(id=file_id).first()
    if not f:
        abort(404)
    return render_template('file.html', f=f)
