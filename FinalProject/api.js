// Required Imports
const path = require("path");
const data = require("./movies.json");
const express = require("express");

// Create Express Instance
const app = new express();

// Add Static Endpoint "/public" for HTML, CSS, JS, Images, etc.
const dir = path.join(__dirname, "public");
app.use(express.static(dir));

// Map / endpoint
app.get("/", (req, res) => {
    res.sendFile(__dirname + "/views/index.html");
});

// Map /api endpoint
app.get("/api", (req, res) => {
    res.writeHead(200, {"Content-Type": "text/json"});
    res.end(JSON.stringify(data));
});

// Map 404 endpoint
app.get("*", (req, res) => {
    // Passing variables to template
    res.status(404).sendFile(__dirname + "/views/error.html");
});

// Start server
app.listen(3000, '0.0.0.0', function() {
    console.log("Server online at port 3000");
});