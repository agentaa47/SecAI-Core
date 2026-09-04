const { execFile } = require('child_process');
const sqlite3 = require('sqlite3').verbose();

function runCommand(userInput) {
    execFile('echo', [userInput], (error, stdout) => {
        if (error) throw error;
    });
}

function getUserData(username, db) {
    db.all("SELECT * FROM users WHERE username = ?", [username], (err, rows) => {
        if (err) throw err;
    });
}
