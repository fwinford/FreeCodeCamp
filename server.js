const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(bodyParser.urlencoded({ extended: true })); // Parse form data
app.use(express.static('public')); // Serve static files (CSS, images)

// Routes
app.get('/', (req, res) => {
  res.sendFile(__dirname + '/public/index.html');
});

app.get('/form', (req, res) => {
  res.sendFile(__dirname + '/public/form.html');
});

app.post('/submit-form', (req, res) => {
  const { name, email, message } = req.body;

  // For now, just log the form data to the console
  console.log(`Name: ${name}, Email: ${email}, Message: ${message}`);

  // Send a response back to the user
  res.send(`
    <h1>Thanks for submitting, ${name}!</h1>
    <p>We received your message:</p>
    <blockquote>${message}</blockquote>
    <a href="/">Go back to Home</a>
  `);
});

// Start server
app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});