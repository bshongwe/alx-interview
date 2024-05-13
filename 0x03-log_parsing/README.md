# 0x03. Log Parsing 📊 💻 📜
`Algorithm` `Python`

For the `0x03. Log Parsing` project, you will need to apply your knowledge of
Python programming, focusing on parsing and processing data streams in
real-time. This project involves reading from standard input (stdin), handling
data in a specific format, and performing calculations based on the input data.
Here’s a list of concepts and resources that you might find useful:

## Concepts Needed:
### File I/O in Python 📄:
- Understand how to read from `sys.stdin` line by line.
- [Python Input and Output](https://docs.python.org/3/tutorial/inputoutput.html)
<br></br>
### Signal Handling in Python ⚠️:
- Handling keyboard interruption (CTRL + C) using signal handling in Python.
- [Python Signal Handling](https://docs.python.org/3/library/signal.html)
<br></br>
### Data Processing 🛠️:
- Parsing strings to extract specific data points.
- Aggregating data to compute summaries.
<br></br>
### Regular Expressions 🧵:
- Using regular expressions to validate the format of each line.
- [Python Regular Expressions](https://docs.python.org/3/library/re.html)
<br></br>
### Dictionaries in Python 📚:
- Using dictionaries to count occurrences of status codes and accumulate file
sizes.
- [Python Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
<br></br>
### Exception Handling ⚠️:
- Handling possible exceptions that may arise during file reading and data
processing.
- [Python Exceptions](https://docs.python.org/3/tutorial/errors.html)
<br></br>

By studying these concepts and utilizing the resources provided, you will be
well-prepared to tackle the log parsing project, effectively handling data
streams, parsing log entries, and computing metrics based on the processed
data.
<br></br>

## Additional Resources
- [Mock Technical Interview](https://www.hackerrank.com/interview/interview-preparation-kit)
<br></br>
## Requirements
### General
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using
`python3` (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the PEP 8 style (version 1.7.x)
- All your files must be executable
- The length of your files will be tested using `wc`
<br></br>

# Tasks📋
### Task 0. Log parsing
`mandatory` </br>
Write a script that reads stdin line by line and computes metrics:
-	Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size> (if the format is not this one, the line must be skipped)
-	After every 10 lines and/or a keyboard interruption (CTRL + C), print these statistics from the beginning:
	-	Total file size: File size: <total size>
	-	where <total size> is the sum of all previous <file size> (see input format above)
	-	Number of lines by status code:
		-	possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
		-	if a status code doesn’t appear or is not an integer, don’t print anything for this status code
		-	format: <status code>: <number>
		-	status codes should be printed in ascending order
<b>Warning:</b> In this sample, you will have random value - it’s normal to not have the same output as this one.
<br></br>

## Tests
### Edge Test File
```
0-generator.py
```
<br></br>
### Edge Test Command
```
./0-generator.py | ./0-stats.py
```
<br></br> 
Repo:
```
GitHub repository: alx-interview
Directory: 0x03-log_parsing
File: 0-stats.py
```



