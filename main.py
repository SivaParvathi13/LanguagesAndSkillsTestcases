from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

languages_skills = []

@app.route('/', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        language = request.form['language']
        skill = request.form['skill']
        languages_skills.append({'language': language, 'skill': skill})
        return redirect(url_for('profile'))
    return render_template('profile.html', languages_skills=languages_skills)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5003)