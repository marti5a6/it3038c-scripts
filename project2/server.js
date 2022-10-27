const http = require("http");
const fs = require("fs");
const os = require("os");
const ip = require("ip");

http.createServer((req, res) => {
    if (req.url === "/") {
        fs.readFile("./public/index.html", "UTF-8", (err, body) => {
            res.writeHead(200, {"Content-Type": "text/html"});
            res.end(body);
        });
    }
    else if(req.url === "/sysinfo") {
        myHostname = os.hostname();
        ipAddr = ip.address();
        totalMem = (os.totalmem() / (1024 * 1024)).toFixed(2);
        freeMem = (os.freemem() / (1024 * 1024)).toFixed(2);
        cpuCount = os.cpus().length;
        
        seconds = os.uptime();
        days = Math.floor(seconds / (3600 * 24));
        seconds -= (days * 3600 * 24);
        hours = Math.floor(seconds / 3600);
        seconds -= (hours * 3600);
        minutes = Math.floor(seconds / 60);
        seconds -= (minutes * 60);
        seconds = seconds.toFixed(2);

        html = `
        <!DOCTYPE HTML>
        <html>
            <head>
                <title>Node JS Response</title>
            </head>
            <body>
                <p>Hostname: ${myHostname}</p>
                <p>IP: ${ipAddr}</p>
                <p>Server Uptime: ${days} day(s), ${hours} hours(s), ${minutes} minute(s), and ${seconds} second(s).</p>
                <p>Total Memory: ${totalMem} MB</p>
                <p>Free Memory: ${freeMem} MB</p>
                <p>Number of CPUs: ${cpuCount}</p>
            </body>
        </html>
        `
        res.writeHead(200, {"Content-Type": "text/html"});
        res.end(html);
    }
    else {
        res.writeHead(404, {"Content-Type": "text/plain"});
        res.end(`404 File Not Found at ${req.url}`);
    }
}).listen(3000);

console.log("Server listening on port 3000");
