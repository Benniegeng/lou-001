# -*- coding:utf-8 -*-

from flask import Flask, render_template, abort
import os, json


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404

@app.route('/')
def index():
    list_title = []
    for root, dirs, filenames in os.walk('/home/shiyanlou/files'):
        for filename in filenames:
            filepath = os.path.join(root, filename)
            with open(filepath) as json_news:
                dict_news = json.loads(json_news.read())
                list_title.append(dict_news['title'])
    return render_template('index.html', list_title=list_title)
    
@app.route('/files/<filename>')
def file(filename):
    filepath1 = os.path.join('/home/shiyanlou/files',filename+'.json')
    if os.path.isfile(filepath1) :
        with open(filepath1) as json_news_content:
            dict_news_all = json.loads(json_news_content.read())
            dict_news_content = dict_news_all['content']
        return render_template('file.html', dict_news_content=dict_news_content)
    else:
        abort(404)

