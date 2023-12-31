# Pygeon: A Cheap Alternative to EvilGinx
![PYGEON](https://github.com/analyserdmz/Pygeon/assets/61113942/0ab948da-f3bf-4ac9-8337-221f9f387078)

## Description

Pygeon is a Python-based reverse proxy application designed to manipulate traffic for auditing and debugging purposes. Built on top of Flask, it allows seamless proxying of requests while enabling easy header and content modifications. It still needs a lot of work, but hey, it works so far.

![ezgif-2-b3d496f4eb](https://github.com/analyserdmz/Pygeon/assets/61113942/d666549e-337c-4278-88ef-72f875efe3de)

![image](https://github.com/analyserdmz/Pygeon/assets/61113942/f749ba30-0040-428b-ae24-6fae1a5fc73b)


## Features

- Uses Flask as the web server to route traffic.
- Header modification including 'User-Agent' and 'Referer'.
- Content manipulation to replace URLs.
- Customizable final endpoint and reverse proxy URL.
- Thread-safe logging with color-coded outputs.
- Cookie and Form Data tracking for POST requests in clear-text.
- No need for templates whatsoever (and it'll probably stay that way).
- Client identification with Client<->Proxy isolated cookie.
- Cookie-based session storage to allow the user browse the target website further. (Needs to be tested)
- Debug mode.

## Prerequisites

Make sure you have Python installed on your system. Then, you can install the required packages using pip:

```bash
pip install Flask
pip install requests
pip install beautifulsoup4
pip install colorama
```

## Installation

1. Clone this repository or download the source code.
2. Navigate to the directory containing the `PyGeon.py` script.
3. Run the script:

```bash
python PyGeon.py
```

The application will start and listen on port `8887` where you can navigate with your browser to and try to log into an account right away to test it.

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

## Pull Requests

For pull requests use the following template.

```https://github.com/analyserdmz/Pygeon/pulls?template=pull_request_template.md```

## Author

- Konstantinos Karakatsoulis ([analyserdmz](https://github.com/analyserdmz)) - Proud author of Lecpetex

[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-Donate-orange.svg)](https://www.buymeacoffee.com/analyserdmz)

## Disclaimer

This software is for educational and debugging purposes only. Use responsibly and ensure you have permission before manipulating any real-world traffic.

## Future plans & TODO

- It should become modular.
- SSL support (Let's Encrypt).
- Seamless support for any target domain with minimum configuration.
- Implement a clever way to also proxy other domains/subdomains included in page links or form posts (eg. when the login form has another subdomain in its action).

## Why the name "Pygeon"

It comes from the combination of Python and Pigeon. Historically, pigeons have been used as messengers capable of reliably carrying important information across great distances. In covert operations, they acted as unassuming spies, bridging gaps and breaking barriers. This mirrors the software's core functionality to act as a middleman, ferrying data discreetly between a client and a server, much like a pigeon would carry messages.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
