# Taks

A python application that shows weather conditions using the OpenWeatherMap API

---

## Table of Contents

- [Prerequesites](#prerequesites)
- [How to run](#how-to-run)
- [Screenshot](#screenshot)
- [Contributing](#contributing)
- [Issues](#issues)
- [License](#license)

---

## Prerequesites

- Python 3.10+
  - Python Libararies:
    - Requests
    - Rich

- A terminal that supports true color to show the colors of the text (can be ignored)

---

## How to run

1. Clone the repositery

```bash
git clone https://github.com/nothingfr87/Taks.git
cd Taks
```

2. Install the required libararies in a `venv`
   - Mac & Linux

     ```bash
     # Create the venv
     python3 -m venv .venv

     # Activate the venv
     source .venv/bin/activate

     # if you are using the fish shell
     # source .venv/bin/activate.fish

     # Install all packages
     pip install -r requirements.txt

     # Alterntavely, you can install all the packages by yourself
     pip install rich requests
     ```

   - Windows

     ```bash
     # Create the ven
     py -m venv .venv

     # Activate the venv
     .\\venv\\Scripts\\activate.bat

     # Install all packages
     pip install -r requirements.txt

     # Alterntavely, you can install all the packages by yourself
     pip install rich requests
     ```

3. Add API Key

To make sure the application works you need to get your own API key from `openweathermap.org`

- Go to [OpenWeatherMap](https://home.openweathermap.org/users/sign_in) and sign in with your account, if you don't have one, create a new one

- Go to API Keys tab and create an API key

- Copy your API key to `.env` file and write the following

```env
API_KEY=<YOUR-API-KEY>
```

And That's it.

After that you can run the application with python

```bash
python3 src/main.py
```

in the repositery direcotry, then run the application normally

---

## Screenshot

![screenshot](assets/screenshot.png)
![screenshot](assets/screenshot2.png)
![screenshot](assets/screenshot3.png)

---

## Contributing

Contributions are welcome whether they are improving code, or adding a new feature

simply, fork the repositery, add your changes, push them, and make a pull request

---

## Issues

if you find any issues in the application, you can report in the [Issues Tab](https://github.com/nothingfr87/Taks/issues)

---

## License

This application is licensed under the [GPLv3 License](LICENSE)
