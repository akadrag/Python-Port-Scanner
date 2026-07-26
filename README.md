# Python Port Scanner

A beginner-friendly TCP Port Scanner built in Python using the built-in `socket` module and object-oriented programming.

## Features

- Scan TCP ports on an IP address or hostname
- Specify a custom port range
- Detect open ports
- Measure scan execution time
- Clean OOP-based implementation

## Technologies

- Python 3
- socket
- time

## Project Structure

```
main.py
scanner.py
requirements.txt
```

## How to Run

```bash
python main.py
```

Then enter:

- Target IP or hostname
- Start port
- End port

## Example

```
Target: scanme.nmap.org
Start Port: 20
End Port: 100
```

## Concepts Learned

- Python Classes & Objects
- Constructors (`__init__`)
- Methods
- TCP Networking
- Socket Programming
- Basic Port Scanning

## Future Improvements

- Multithreading
- Banner Grabbing
- Command-line arguments
- Export scan results
