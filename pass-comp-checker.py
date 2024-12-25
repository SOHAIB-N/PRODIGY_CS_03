import string
import pyfiglet

class PasswordStrengthChecker:
    def __init__(self, password):
        self.password = password
        self.criteria = {
            'length': False,
            'uppercase': False,
            'lowercase': False,
            'digit': False,
            'special_char': False
        }
        self.feedback = []

    def check_length(self):
        """Ensure password has a minimum length of 8 characters."""
        if len(self.password) >= 8:
            self.criteria['length'] = True
        else:
            self.feedback.append("Password must be at least 8 characters long.")

    def check_uppercase(self):
        """Check if password contains at least one uppercase letter."""
        if any(char.isupper() for char in self.password):
            self.criteria['uppercase'] = True
        else:
            self.feedback.append("Password must contain at least one uppercase letter.")

    def check_lowercase(self):
        """Check if password contains at least one lowercase letter."""
        if any(char.islower() for char in self.password):
            self.criteria['lowercase'] = True
        else:
            self.feedback.append("Password must contain at least one lowercase letter.")

    def check_digit(self):
        """Check if password contains at least one digit."""
        if any(char.isdigit() for char in self.password):
            self.criteria['digit'] = True
        else:
            self.feedback.append("Password must contain at least one digit.")

    def check_special_character(self):
        """Check if password contains at least one special character."""
        special_characters = string.punctuation
        if any(char in special_characters for char in self.password):
            self.criteria['special_char'] = True
        else:
            self.feedback.append("Password must contain at least one special character.")

    def analyze_password(self):
        """Run all checks and analyze password strength."""
        self.check_length()
        self.check_uppercase()
        self.check_lowercase()
        self.check_digit()
        self.check_special_character()

        if all(self.criteria.values()):
            return "Your password is strong."
        else:
            return self.generate_feedback()

    def generate_feedback(self):
        """Generate a detailed feedback based on the password's weaknesses."""
        missing_criteria = [key for key, value in self.criteria.items() if not value]
        feedback_message = "Password strength is insufficient due to the following reasons:\n"
        for criterion in missing_criteria:
            if criterion == 'length':
                feedback_message += "- Password must be at least 8 characters long.\n"
            elif criterion == 'uppercase':
                feedback_message += "- Password must contain at least one uppercase letter.\n"
            elif criterion == 'lowercase':
                feedback_message += "- Password must contain at least one lowercase letter.\n"
            elif criterion == 'digit':
                feedback_message += "- Password must contain at least one digit.\n"
            elif criterion == 'special_char':
                feedback_message += "- Password must contain at least one special character.\n"
        return feedback_message

def main():
    ascii_art = pyfiglet.figlet_format("Password Checker")
    print(ascii_art)
    
    print("Welcome to the Password Strength Checker!\n")
    user_password = input("Please enter your password: ")
    checker = PasswordStrengthChecker(user_password)
    result = checker.analyze_password()
    print(result)

if __name__ == "__main__":
    main()
