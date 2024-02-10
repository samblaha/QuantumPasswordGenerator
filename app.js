const express = require('express');
const { spawn } = require('child_process');
const path = require('path');
const app = express();
const port = 3000;

// Middleware to serve static files from the 'public' directory
app.use(express.static('public'));

// Route to run Python script
app.get('/run-python', (req, res) => {
  // Extract the length parameter from the query string
  const length = req.query.length ? req.query.length : 12; // Default to 12 if not provided

  // Adjust the path to your Python script as necessary
  const pythonProcess = spawn('python3', ['/Users/sam/Documents/QPGweb/QuantumPasswordGenerator/QPG.py', length]);

  let outputData = '';
  pythonProcess.stdout.on('data', (data) => {
    outputData += data.toString();
  });

  pythonProcess.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`);
  });

  pythonProcess.on('close', (code) => {
    console.log(`child process exited with code ${code}`);
    if(code === 0) {
      res.send(outputData); // Send the successful data response back to the client
    } else {
      res.status(500).send('Error executing Python script');
    }
  });
});

// Listen on the specified port
app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
