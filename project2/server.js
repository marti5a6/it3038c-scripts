const fs = require("fs");
const os = require("os");
const ip = require("ip");
const path = require("path");
const express = require("express");
const pug = require("pug");
const { uptime } = require("process");

// Create express and pug instance
const app = new express();
app.set("view engine", "pug");

// Add static /public endpoint for css, js, images, etc.
const dir = path.join(__dirname, "public");
app.use(express.static(dir));

// Map / endpoint
app.get("/", (req, res) => {
    res.render(__dirname + "/views/index", {
        title: "SysAdmin - Home ",
        header: "System Administration Hub"
    });
});

// Map /sysinfo endpoint
app.get("/sysinfo", (req, res) => {
    // Logic
    myHostname = os.hostname();
    totalMem = (os.totalmem() / (1024 * 1024)).toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
    freeMem = (os.freemem() / (1024 * 1024)).toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
    cpuCount = os.cpus().length;
    
    seconds = os.uptime();
    days = Math.floor(seconds / (3600 * 24));
    seconds -= (days * 3600 * 24);
    hours = Math.floor(seconds / 3600);
    seconds -= (hours * 3600);
    minutes = Math.floor(seconds / 60);
    seconds -= (minutes * 60);
    seconds = seconds.toFixed(2);

    // Passing variables to template
    res.render(__dirname + "/views/sysinfo", {
        title: "System Info",
        header: "System Information",
        hostname: `Hostname: ${myHostname}`,
        uptime: `Uptime: ${days} day(s), ${hours} hours(s), ${minutes} minute(s), and ${seconds} second(s).`,

        totalMemory: `Total Memory: ${totalMem} MB`,
        freeMemory: `Free Memory: ${freeMem} MB`,
        cpuTotal: `CPU Count: ${cpuCount} threads (${cpuCount / 2} cores).`
    });
});

// Map /netinfo endpoint
app.get("/netinfo", (req, res) => {
    // Logic
    myHostname = os.hostname();
    
    seconds = os.uptime();
    days = Math.floor(seconds / (3600 * 24));
    seconds -= (days * 3600 * 24);
    hours = Math.floor(seconds / 3600);
    seconds -= (hours * 3600);
    minutes = Math.floor(seconds / 60);
    seconds -= (minutes * 60);
    seconds = seconds.toFixed(2);

    app.set("trust proxy", true);
    sysIpAddr = ip.address();
    conIpAddr = req.ip;

    if (ip.isV4Format) {
        ipFormat = "IPV4";
    }
    else if (ip.isV6Format) {
        ipFormat = "IPV6";
    }

    // Passing variables to template
    res.render(__dirname + "/views/netinfo", {
        title: "Network Info",
        header: "Network Information",
        hostname: `Hostname: ${myHostname}`,
        uptime: `Uptime: ${days} day(s), ${hours} hours(s), ${minutes} minute(s), and ${seconds} second(s).`,
        
        sysIp: `Server Address: ${sysIpAddr}`,
        conIp: `Connected From: ${conIpAddr}`,
        format: `IP Format: ${ipFormat}`
    });
});

// Map 404 endpoint
app.get("*", (req, res) => {
    // Passing variables to template
    res.status(404).render(__dirname + "/views/404", {
        title: "Page Not Found",
        header: "Error 404",
        errorText: "These are not the droids you are looking for."
    });
});

// Start server
app.listen(3000, '0.0.0.0', function() {
    console.log("Server online at port 3000");
});