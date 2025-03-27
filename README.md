# Password Strength Checker & Generator

A Flask-based web application and CLI tool that checks password strength using the zxcvbn algorithm and generates secure passwords.

## Features

- **Password Strength Analysis**:
  - Real-time strength meter with color feedback
  - Crack time estimation
  - Detailed improvement suggestions
  - Common password detection

- **Password Generation**:
  - Custom length (8-64 characters)
  - Configurable character sets
  - One-click copy to clipboard

- **Multiple Interfaces**:
  - Web GUI with responsive design
  - Command Line Interface (CLI)

- **Additional Features**:
  - Export results to JSON
  - Security tips display
  - Performance optimized with LRU caching

## Installation

1. Clone the repository:
```
git clone https://github.com/DivyaMaryFrancis/PASSW0RD-Strength-checker.git
cd PASSW0RD-Strength-checker
```
2. Create and activate virtual environment:
```
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```
3. Install dependencies:
```
pip install -r requirements.txt
```
4. Run the Applicatiom
 Web Interface
```
python app.py
```
Then open http://localhost:5000 in your browser

 Command Line Interface

 # Check password strength
python app.py --check "yourpassword"

# Generate strong password
python app.py --generate --length 16

# Export results to file
python app.py --check "password" > results.json




## Usage

### GUI Mode

Run without arguments to launch the graphical interface:
```bash
python app.py
```

### CLI Mode

1. Interactive CLI:
```bash
python app.py --cli
```

2. Direct password check:
```bash
python app.py --check "your_password_here"
```

3. Generate password:
```bash
# Default length (16 characters)
python app.py --generate

# Custom length
python app.py --generate --length 20
```

### Command Line Arguments

- `--cli`: Launch interactive CLI mode
- `--check PASSWORD`: Check strength of a specific password
- `--generate`: Generate a strong password
- `--length N`: Specify length for generated password (default: 16)

## Features in Detail

### Password Strength Criteria

- Minimum length: 12 characters
- Character complexity:
  - Uppercase letters
  - Lowercase letters
  - Numbers
  - Special characters
- Checks against common weak passwords
- Checks against banned passwords
- Uses zxcvbn for advanced pattern matching

### GUI Features

- Password strength visualisation
- Password generation with clipboard support
- Export results to JSON
- Security tips display
- Interactive feedback

### CLI Features

- Interactive menu-driven interface
- Direct command execution
- Password generation with customisable length
- Detailed strength analysis output

## Logging

The application logs all password checks to `password_checker.log` with the following information:
- Timestamp
- Action performed
- Strength result

## Security Notes

- Passwords are never stored permanently
- All processing is done locally
- No external API calls for password checking
- Secure random generation for new passwords

## Dependencies

- Python 3.x
- flask
- zxcvbn
