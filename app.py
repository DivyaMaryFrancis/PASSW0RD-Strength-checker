from flask import Flask, render_template, request, jsonify, send_file
import re
import random
import string
import logging
import json
import io
from functools import lru_cache
from zxcvbn import zxcvbn


from datetime import datetime


app = Flask(__name__)

# Configure logging
logging.basicConfig(filename='password_checker.log', level=logging.INFO,



                   format='%(asctime)s - %(levelname)s - %(message)s')

class PasswordStrength:
    """Enhanced password strength checker with all requested features."""
    
    def __init__(self):
        self.min_password_length = 12
        self.strength_mapping = {
            0: "Very Weak",
            1: "Weak",
            2: "Moderate",
            3: "Strong",
            4: "Very Strong"
        }
        self.security_tips = [
            "Use at least 12 characters",
            "Combine uppercase and lowercase letters",
            "Include numbers and special characters",
            "Avoid personal information or common words",
            "Use unique passwords for each account",
            "Consider using a password manager",
            "Change passwords every 3-6 months",
            "Never share your passwords with anyone",
            "Enable two-factor authentication where available",
            "Be cautious of phishing attempts"
        ]

    @lru_cache(maxsize=1000)
    def check_password_strength(self, password: str) -> dict:
        """Check password strength with detailed feedback."""
        if len(password) < 8:
            return {
                "strength": "Too short",
                "score": 0,
                "message": "Password should be at least 8 characters long.",
                "suggestions": ["Increase length to at least 12 characters"],
                "crack_time": "instantly",
                "visual_feedback": self._get_visual_feedback(0)
            }

        result = zxcvbn(password)
        score = result["score"]
        strength = self.strength_mapping[score]
        
        complexity_issues = []
        if not re.search(r'[A-Z]', password):
            complexity_issues.append("Add uppercase letters")
        if not re.search(r'[a-z]', password):
            complexity_issues.append("Add lowercase letters")
        if not re.search(r'\d', password):
            complexity_issues.append("Add numbers")
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            complexity_issues.append("Add special characters")

        feedback = {
            "strength": strength,
            "score": score,
            "message": result["feedback"]["warning"] or "Password meets basic requirements",
            "suggestions": (result["feedback"]["suggestions"] + complexity_issues)[:5],
            "crack_time": result["crack_times_display"]["online_no_throttling_10_per_second"],
            "visual_feedback": self._get_visual_feedback(score),
            "security_tips": random.sample(self.security_tips, 3)
        }
        
        return feedback

    def _get_visual_feedback(self, score: int) -> dict:
        """Generate visual feedback data for the password meter."""
        colors = ["#dc3545", "#fd7e14", "#ffc107", "#28a745", "#20c997"]
        widths = ["20%", "40%", "60%", "80%", "100%"]
        labels = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
        return {
            "color": colors[score],
            "width": widths[score],
            "label": labels[score]
        }

    def generate_password(self, length=16, include_special=True) -> str:
        """Generate a secure random password with customizable options."""
        chars = string.ascii_letters + string.digits
        if include_special:
            chars += string.punctuation
            
        while True:
            password = ''.join(random.choice(chars) for _ in range(length))
            if self.check_password_strength(password)["score"] >= 3:
                return password

    def export_results(self, data: dict) -> io.BytesIO:
        """Export results to a JSON file download."""
        export_data = {
            "password_analysis": data,
            "timestamp": datetime.now().isoformat(),
            "application": "Password Strength Checker"
        }
        file = io.BytesIO()
        file.write(json.dumps(export_data, indent=2).encode('utf-8'))
        file.seek(0)
        return file

password_checker = PasswordStrength()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        action = request.form.get('action')
        
        if action == 'check':
            password = request.form.get('password', '')
            result = password_checker.check_password_strength(password)
            return jsonify(result)
            
        elif action == 'generate':
            length = int(request.form.get('length', 16))
            include_special = request.form.get('include_special', 'true') == 'true'
            password = password_checker.generate_password(length, include_special)
            result = password_checker.check_password_strength(password)
            result['password'] = password
            return jsonify(result)
        
        elif action == 'export':
            data = json.loads(request.form.get('data', '{}'))
            file = password_checker.export_results(data)
            return send_file(
                file,
                as_attachment=True,
                download_name=f"password_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                mimetype='application/json'
            )
    
    return render_template('index.html')

@app.route('/get_tips', methods=['GET'])

def get_tips():
    return jsonify({"tips": random.sample(password_checker.security_tips, 3)})

if __name__ == '__main__':
    app.run(debug=True)
    
