from flask import Flask, request, send_from_directory, render_template_string
import csv
import os

app = Flask(__name__)
app.static_folder = 'public'

@app.route('/')
def index():
    return send_from_directory('public', 'index.html')

@app.route('/form')
def form():
    return send_from_directory('public', 'form.html')

@app.route('/src/<path:filename>')
def serve_src(filename):
    # Handle nested paths within src directory
    parts = filename.split('/')
    if len(parts) > 1:
        # For nested paths like CatPhotoApp/index.html
        return send_from_directory(os.path.join('src', *parts[:-1]), parts[-1])
    # For files directly in src
    return send_from_directory('src', filename)

@app.route('/styles/<path:path>')
def serve_styles(path):
    return send_from_directory('public/styles', path)

@app.route('/images/<path:path>')
def serve_images(path):
    return send_from_directory('public/images', path)

@app.route('/submit-form', methods=['POST'])
def submit_form():
    favorite_language = request.form.get('favorite-language')
    bug_fix = request.form.get('bug-fix')
    motivation = request.form.get('motivation')
    approach = request.form.get('approach')
    struggle = request.form.get('struggle')
    experience = request.form.get('experience')
    project_type = request.form.get('project-type')

    # Write to CSV
    if not os.path.exists('data'):
        os.makedirs('data')
    with open('data/form_responses.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([favorite_language, bug_fix, motivation, approach, struggle, experience, project_type])

    # Return HTML response using the same CSS
    return f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Survey Submitted</title>
        <link rel="stylesheet" href="/styles/form.css">
    </head>
    <body>
        <div class="container">
            <h1>thank you for filling out the form!</h1>
            <p>i hope to eventually use this data to create an ml model that will predict users' favorite programming language</p>
            <div class="response-list">
                <p>your responses:</p>
                <ul>
                    <li><strong>favorite language:</strong> {favorite_language}</li>
                    <li><strong>bug fix:</strong> {bug_fix}</li>
                    <li><strong>motivation:</strong> {motivation}</li>
                    <li><strong>approach:</strong> {approach}</li>
                    <li><strong>struggle:</strong> {struggle}</li>
                    <li><strong>experience:</strong> {experience}</li>
                    <li><strong>project type:</strong> {project_type}</li>
                </ul>
            </div>
            <a href="/" class="home-button">go back to home</a>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)