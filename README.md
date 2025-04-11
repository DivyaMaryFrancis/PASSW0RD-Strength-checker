# Password Strength Checker & Generator

A Flask-based web application that checks password strength using the zxcvbn algorithm and generates secure passwords.

## 🌐 Deployed Website

🔗 **Live Demo**: [passsafely](https://passsafely.pythonanywhere.com/)

##  Features

###  Password Strength Analysis
- Real-time strength meter with color-coded feedback
- Crack time estimation
- Detailed improvement suggestions
- Common and banned password detection

###  Password Generation
- Custom length (8–64 characters)
- Configurable character sets
- One-click copy to clipboard

###  Web Interface
- Responsive and user-friendly design
- Password strength visualization
- Secure password generation with export to JSON
- Useful security tips display


##  Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/DivyaMaryFrancis/PASSW0RD-Strength-checker.git
   cd PASSW0RD-Strength-checker
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # Mac/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application:**
   ```bash
   python app.py
   ```
   Then open your browser and go to [http://localhost:5000](http://localhost:5000)

##  Password Strength Criteria

- Minimum recommended length: 12 characters
- Must include:
  - Uppercase and lowercase letters
  - Numbers
  - Special characters
- Detects common and banned passwords
- Uses **zxcvbn** for pattern-based analysis


##  Dependencies

- Python 3.x
- Flask
- zxcvbn

---


Referenced implementation logic from [Sharma-IT/password-strength-checker](https://github.com/Sharma-IT/password-strength-checker).
