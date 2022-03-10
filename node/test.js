var path = require("path");

var hello = "Hello from Node JS variable!";
console.log(hello);

var fn = path.basename(__filename)
var args = process.argv

console.log("Using PATH module:");
console.log("Hello from file " + fn);

console.log("Process args: " + args);
