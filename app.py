from flask import Flask, request, send_from_directory
import csv
import os

app = Flask(__name__)

# Ensure the data directory exists
if not os.path.exists('data'):
    os.makedirs('data')


@app.route('/')
def index():
    return send_from_directory('public', 'index.html')

@app.route('/form')
def form():
    return send_from_directory('public', 'form.html')

@app.route('/submit-form', methods=['POST'])
def submit_form():
    favorite_language = request.form.get('favorite-language')
    bug_fix = request.form.get('bug-fix')
    motivation = request.form.get('motivation')
    approach = request.form.get('approach')
    struggle = request.form.get('struggle')
    experience = request.form.get('experience')
    project_type = request.form.get('project-type')

    # Log the form data to the console
    print(f"Favorite Language: {favorite_language}")
    print(f"Bug Fix: {bug_fix}")
    print(f"Motivation: {motivation}")
    print(f"Approach: {approach}")
    print(f"Struggle: {struggle}")
    print(f"Experience: {experience}")
    print(f"Project Type: {project_type}")

    # Write the form data to a CSV file
    with open('data/form_responses.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([favorite_language, bug_fix, motivation, approach, struggle, experience, project_type])

    # Send a response back to the user
    return f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Survey Submitted</title>
      <link rel="stylesheet" href="styles/form.css">
    </head>
    <body>
      <div class="container">
        <h1>thank you for filling out the form</h1>
        <p>i hope to eventually use this data to create a mlm model that will predict users favorite programming language</p>
        <ul>
          <li><strong>favorite Language:</strong> {favorite_language}</li>
          <li><strong>bug Fix:</strong> {bug_fix}</li>
          <li><strong>motivation:</strong> {motivation}</li>
          <li><strong>approach:</strong> {approach}</li>
          <li><strong>struggle:</strong> {struggle}</li>
          <li><strong>experience:</strong> {experience}</li>
          <li><strong>project Type:</strong> {project_type}</li>
        </ul>
        <a href="/">take me back home</a>
      </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)