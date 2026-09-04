package main

import (
    "database/sql"
    "os/exec"
)

func runCommand(userInput string) {
    exec.Command("echo", userInput).Run()
}

func getUserData(db *sql.DB, username string) {
    db.Query("SELECT * FROM users WHERE username = ?", username)
}
