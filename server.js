const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static('public')); // Serve static files from the public directory

// Routes
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.get('/form', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'form.html'));
});

app.get('/src/CatPhotoApp', (req, res) => {
  res.sendFile(path.join(__dirname, 'src', 'CatPhotoApp', 'index.html'));
});

app.get('/src/Cafe-Menu', (req, res) => {
  res.sendFile(path.join(__dirname, 'src', 'Cafe-Menu', 'index.html'));
});

app.get('/src/Crayons', (req, res) => {
  res.sendFile(path.join(__dirname, 'src', 'Crayons', 'index.html'));
});

app.get('/src/Registration-Form', (req, res) => {
  res.sendFile(path.join(__dirname, 'src', 'Registration-Form', 'index.html'));
});

app.post('/submit-form', (req, res) => {
  const { favoriteLanguage, bugFix, motivation, approach, struggle } = req.body;

  // Log the form data to the console
  console.log(`Favorite Language: ${favoriteLanguage}`);
  console.log(`Bug Fix: ${bugFix}`);
  console.log(`Motivation: ${motivation}`);
  console.log(`Approach: ${approach}`);
  console.log(`Struggle: ${struggle}`);

  // Send a response back to the user
  res.send(`
    <h1>Thanks for submitting the survey!</h1>
    <p>We received your responses:</p>
    <ul>
      <li><strong>Favorite Language:</strong> ${favoriteLanguage}</li>
      <li><strong>Bug Fix:</strong> ${bugFix}</li>
      <li><strong>Motivation:</strong> ${motivation}</li>
      <li><strong>Approach:</strong> ${approach}</li>
      <li><strong>Struggle:</strong> ${struggle}</li>
    </ul>
    <a href="/">Go back to Home</a>
  `);
});

// Start server
app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});