# price-scraper

## Running on Windows

Follow these instructions to set up and run the price scraper on your Windows computer.

### 1. Create a Project Directory

First, create a dedicated folder for this project. You can do this using File Explorer. For this guide, we'll assume the folder is created at `C:\price-scraper`.

### 2. Download Project Files

Download `scraper.py` and `requirements.txt` from the project's source (e.g., GitHub) and place them inside the directory you just created (`C:\price-scraper`).

### 3. Open Command Prompt

Open the Windows Command Prompt. You can do this by searching for `cmd` in the Start Menu. Once open, use the `cd` (change directory) command to navigate to your project folder.

```shell
cd C:\price-scraper
```

### 4. Create a Python Virtual Environment

A virtual environment is an isolated Python environment that allows you to manage dependencies for a specific project without affecting other projects or your system's global Python installation. It's a best practice for Python development.

Create a virtual environment named `venv` by running the following command:

```shell
python -m venv venv
```

You will see a new `venv` folder appear in your project directory.

### 5. Activate the Virtual Environment

To use the virtual environment, you must "activate" it.

```shell
venv\Scripts\activate
```

Your command prompt line should now be prefixed with `(venv)`, indicating that the virtual environment is active.

### 6. Install Dependencies

Next, install the necessary Python libraries listed in `requirements.txt`. The `pip` command will read this file and install Playwright into your virtual environment.

```shell
pip install -r requirements.txt
```

Playwright also requires you to download browser binaries for automation. Run the following command to complete the setup:

```shell
playwright install
```

### 7. Run the Scraper

Now you are ready to run the script. Execute the following command in your terminal:

```shell
python scraper.py
```

The script will launch, navigate to the URLs specified within it, and print the scraped prices to your console.
