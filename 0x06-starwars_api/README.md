# 0x06. Star Wars API 🌟
`Algorithm` `API` `JavaScript`
<br></br>
## Overview
The **Star Wars Characters** project requires interaction with the Star Wars API to fetch and display information about characters from a specified movie. This is accomplished through the use of HTTP requests and asynchronous programming in JavaScript.
<br></br>
## Key Concepts
### HTTP Requests in JavaScript 🌐
- Making HTTP requests to external services using modules like `request` or `fetch` in Node.js.
- **Resource:** [A Complete Guide to Making HTTP Requests in Node.js](https://nodejs.dev/learn/making-http-requests-with-nodejs)

### Working with APIs 🛠️
- Understanding RESTful APIs and interacting with them.
- Parsing JSON data returned by APIs.
- **Resource:** [Working with APIs in JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Introduction)

### Asynchronous Programming ⏳
- Managing asynchronous operations with callbacks, promises, and async/await syntax.
- Handling API response data asynchronously.
- **Resource:** [Asynchronous Programming in JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous)

### Command Line Arguments in Node.js 💻
- Using `process.argv` to access command-line arguments.
- **Resource:** [How to Parse Command Line Arguments in Node.js](https://nodejs.dev/learn/nodejs-command-line-arguments)

### Array Manipulation and Iteration 🔄
- Iterating over arrays and manipulating data structures to format and display character names.
- **Resource:** [JavaScript Array Methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
<br></br>
## Requirements
### General ⚙️
- **Editors:** `vi`, `vim`, `emacs`
- **Environment:** Ubuntu 20.04 LTS using Node.js (version 10.14.x)
- **File Endings:** All files must end with a new line.
- **First Line:** The first line of all files should be `#!/usr/bin/node`.
- **README.md:** A mandatory README file at the root of the project.
- **Coding Style:** Semistandard compliant. Rules of Standard + semicolons on top. Reference: AirBnB style.
- **Executables:** All files must be executable.
- **File Length:** Will be tested using `wc`.
- **No `var` Usage:** Use `let` and `const` instead of `var`.

### Setup 🛠️
#### Install Node 10
```bash
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

#### Install Semi-Standard
```bash
$ sudo npm install semistandard --global
```

#### Install Request Module
```bash
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```
<br></br>
## Task
### 0. Star Wars Characters 🌠
- **Objective:** Write a script that prints all characters of a specified Star Wars movie.
- **Usage:** The first positional argument is the Movie ID (e.g., `3` for "Return of the Jedi").
- **Output:** One character name per line, in the same order as the `characters` list in the `/films/` endpoint.
- **Requirements:**
  - Use the Star Wars API.
  - Use the `request` module.

**Example:**
$ ./0-starwars_characters.js 3

## Repository

- **GitHub Repository:** [alx-interview](https://github.com/bshongwe/alx-interview)
- **Directory:** `0x06-starwars_api`
- **File:** `0-starwars_characters.js`
