const http = require("http");
const fs = require("fs");
const os = require("os");
const ip = require("ip");
const path = require("path");
const express = require("express");

// Add /public directory to static webpage
const dir = path.join(__dirname, 'public');
const app = new express();

// Start server using above settings
app.use(express.static(dir));
app.listen(3000, function() {
    console.log("Server listening on port 3000");
});
