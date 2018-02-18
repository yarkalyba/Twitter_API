from flask import Flask, render_template, session, request, redirect, url_for
from web_map import cr_map
from twitter2 import make_js
from params import info1

app = Flask(__name__)
app.secret_key = "arman"


@app.route('/')
def main():
    """
    return: a start page where the user name should be entered
    """
    return render_template('startpage.html')


@app.route('/process', methods=['POST'])
def process():
    """
    return: depending on user choice returns wep map or next page
    """
    session['username'] = request.form.get('username')
    if "build a map" in request.form:
        acct = session.get('username')
        cr_map(acct)
        return render_template('rybka_twitter3.html')
    else:
        return redirect(url_for('params'))


@app.route('/params')
def params():
    """
    return: page where a parameter can be chosen
    """
    username = session.get('username')
    return render_template('params_choose.html', username=username)


@app.route('/info', methods=['POST'])
def info():
    """
    return: page with info about a requested data
    """
    # get parameter from user
    par = request.form.get('info')
    username = session.get('username')
    js = make_js(username)
    result = info1(par, js)
    return render_template('results.html', name=result)


if __name__ == '__main__':
    app.run(debug=True)
