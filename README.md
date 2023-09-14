# Pygeon: A Cheap Alternative to EvilGinx

## Description

Pygeon is a Python-based reverse proxy application designed to manipulate traffic for auditing and debugging purposes. Built on top of Flask, it allows seamless proxying of requests while enabling easy header and content modifications.

## Features

- Uses Flask as the web server to route traffic.
- Header modification including 'User-Agent' and 'Referer'.
- Content manipulation to replace URLs.
- Customizable final endpoint and reverse proxy URL.
- Thread-safe logging with color-coded outputs.
- Cookie and Form Data tracking for POST requests.

## Prerequisites

Make sure you have Python installed on your system. Then, you can install the required packages using pip:

\`\`\`bash
pip install Flask
pip install requests
pip install beautifulsoup4
pip install colorama
\`\`\`

## Installation

1. Clone this repository or download the source code.
2. Navigate to the directory containing the `PyGeon.py` script.
3. Run the script:

\`\`\`bash
python PyGeon.py
\`\`\`

The application will start and listen on port `8887`.

## Configuration

You can configure the application via constants inside the code:

- `FINAL_ENDPOINT`: The final URL to which the requests should be proxied.
- `REVERSE_PROXY_URL`: The URL of the reverse proxy itself.

## How It Works

The application listens to incoming HTTP requests and forwards them to a predefined `FINAL_ENDPOINT`. While proxying, it allows for a range of modifications including:

- Replacing the 'Referer' header.
- Modifying the content to replace URLs.
- Logging form data from POST requests.
- Displaying cookies set or changed by the remote host.

## Author

- Konstantinos Karakatsoulis - Proud author of Lecpetex

## Disclaimer

This software is for educational and debugging purposes only. Use responsibly and ensure you have permission before manipulating any real-world traffic.


