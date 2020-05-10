from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        works = requests.get(
            'https://api.codemao.cn/web/works/subjects/211/works?&offset=0&limit=16&sort=-audited_at,-id')
        works.encoding = 'utf-8'
        works = works.text
        works = json.loads(works)
        return render_template('index.html', works=works["items"])
    else:
        g = request.form.get("g")
        works = requests.get(
            u'https://api.codemao.cn/web/works/subjects/211/works?&offset=0&limit=%s&sort=-audited_at,-id' % g)
        works.encoding = 'utf-8'
        works = works.text
        works = json.loads(works)
        return render_template('index.html', works=works["items"])


@app.route('/forum', methods=['GET', 'POST'])
def forum():
    if request.method == 'GET':
        forums = requests.get(
            'https://api.codemao.cn/web/works/subjects/labels/424/posts?limit=30&offset=0')
        forums.encoding = 'utf-8'
        forums = forums.text
        forums = json.loads(forums)
        return render_template('forum.html', forums=forums)
    else:
        g = request.form.get("g")
        forums = requests.get(
            u'https://api.codemao.cn/web/works/subjects/labels/424/posts?limit=%s&offset=0'%g)
        forums.encoding = 'utf-8'
        forums = forums.text
        forums = json.loads(forums)
        return render_template('forum.html', forums=forums)


@app.route('/member')
def member():
    members = requests.get(
        'https://api.codemao.cn/web/shops/211/users?limit=40&offset=0')
    members.encoding = 'utf-8'
    members = members.text
    members = json.loads(members)
    return render_template('member.html', members=members["items"])


@app.route('/work/<id>')
def work(id):
    w = requests.get(u'https://api.codemao.cn/web/works/%s' % id)
    w.encoding = 'utf-8'
    w = w.text
    w = json.loads(w)
    wc = requests.get(
        u'https://api.codemao.cn/web/discussions/%s/comments?source=WORK&sort=-created_at&limit=15&offset=0' % id)
    wc.encoding = 'utf-8'
    wc = wc.text
    wc = json.loads(wc)
    return render_template('work.html', work=w, wc=wc["items"])


@app.route('/post/<id>')
def post(id):
    p = requests.get(
        u'https://api.codemao.cn/web/forums/posts/%s/details' % id)
    p.encoding = 'utf-8'
    p = p.text
    p = json.loads(p)
    pc = requests.get(
        u'https://api.codemao.cn/web/forums/posts/%s/replies?page=1&limit=10&sort=-created_at' % id)
    pc.encoding = 'utf-8'
    pc = pc.text
    pc = json.loads(pc)
    return render_template('post.html', post=p, pc=pc["items"])


if __name__ == '__main__':
    app.run()
