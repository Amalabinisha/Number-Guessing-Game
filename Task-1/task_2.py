import random
import json
import os
from datetime import datetime

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    BOLD = '\033[1m'
    END = '\033[0m'

class NumberGuessGame:
    def __init__(self):
        self.high_score_file = 'guess_highscores.json'
        self.high_scores = self.load_scores()
        
    def load_scores(self):
        """Load high scores from file"""
        if os.path.exists(self.high_score_file):
            try:
                with open(self.high_score_file, 'r') as f:
                    return json.load(f)
            except:
                return {}
        return {}
    
    def save_score(self, difficulty, attempts, player_name):
        """Save high score if it's better than existing"""
        key = f"{difficulty}"
        if key not in self.high_scores or attempts < self.high_scores[key]['attempts']:
            self.high_scores[key] = {
                'name': player_name,
                'attempts': attempts,
                'date': datetime.now().strftime("%Y-%m-%d")
            }
            with open(self.high_score_file, 'w') as f:
                json.dump(self.high_scores, f, indent=2)
            return True
        return False
    
    def show_high_scores(self):
        """Display high scores table"""
        if not self.high_scores:
            print(f"{Colors.YELLOW}No high scores yet. Be the first!{Colors.END}")
            return
        
        print(f"\n{Colors.BOLD}{Colors.PURPLE}=== HIGH SCORES ==={Colors.END}")
        print(f"{'Difficulty':<12} {'Name':<15} {'Attempts':<10} {'Date'}{Colors.END}")
        print("-" * 50)
        for diff, data in self.high_scores.items():
            print(f"{diff:<12} {data['name']:<15} {data['attempts']:<10} {data['date']}")
    
    def get_difficulty(self):
        """Select difficulty level"""
        print(f"\n{Colors.BOLD}Select Difficulty:{Colors.END}")
        print(f"1. Easy (1-50, 10 attempts)")
        print(f"2. Medium (1-100, 7 attempts)")
        print(f"3. Hard (1-200, 5 attempts)")
        print(f"4. Insane (1-500, 8 attempts)")
        
        while True:
            choice = input("Enter choice (1-4): ").strip()
            if choice == '1':
                return "Easy", 1, 50, 10
            elif choice == '2':
                return "Medium", 1, 100, 7
            elif choice == '3':
                return "Hard", 1, 200, 5
            elif choice == '4':
                return "Insane", 1, 500, 8
            else:
                print(f"{Colors.RED}Invalid choice!{Colors.END}")
    
    def get_smart_hint(self, guess, target):
        """Give smart hints based on distance"""
        diff = abs(guess - target)
        if diff >= 50:
            return "You're freezing cold!"
        elif diff >= 25:
            return "Cold"
        elif diff >= 15:
            return "Warm"
        elif diff >= 10:
            return "Hot!"
        elif diff >= 5:
            return "Very hot!"
        else:
            return "Burning hot! Almost there!"
    
    def play_game(self):
        """Main game logic"""
        print(f"\n{Colors.BOLD}{Colors.BLUE}=== NUMBER GUESSING GAME PRO ==={Colors.END}")
        player_name = input("Enter your name: ").strip() or "Player"
        
        difficulty, min_num, max_num, max_attempts = self.get_difficulty()
        target = random.randint(min_num, max_num)
        attempts = 0
        
        print(f"\n{Colors.GREEN}I'm thinking of a number between {min_num} and {max_num}{Colors.END}")
        print(f"You have {max_attempts} attempts. Difficulty: {difficulty}")
        print(f"Type 'hint' for a special hint (costs 1 attempt)")
        
        while attempts < max_attempts:
            try:
                guess_input = input(f"\n{Colors.BOLD}Attempt {attempts + 1}/{max_attempts} - Enter guess: {Colors.END}").strip().lower()
                
                if guess_input == 'hint':
                    attempts += 1
                    if target % 2 == 0:
                        print(f"{Colors.YELLOW}Hint: The number is EVEN{Colors.END}")
                    else:
                        print(f"{Colors.YELLOW}Hint: The number is ODD{Colors.END}")
                    continue
                
                guess = int(guess_input)
                
                if guess < min_num or guess > max_num:
                    print(f"{Colors.RED}Please guess between {min_num} and {max_num}{Colors.END}")
                    continue
                
                attempts += 1
                
                if guess == target:
                    print(f"\n{Colors.GREEN}{Colors.BOLD}🎉 CORRECT! You won! 🎉{Colors.END}")
                    print(f"The number was {target}")
                    print(f"You got it in {attempts} attempts")
                    
                    if self.save_score(difficulty, attempts, player_name):
                        print(f"{Colors.PURPLE}🏆 NEW HIGH SCORE for {difficulty}! 🏆{Colors.END}")
                    break
                    
                elif guess < target:
                    hint = self.get_smart_hint(guess, target)
                    print(f"{Colors.BLUE}Too low! {hint}{Colors.END}")
                else:
                    hint = self.get_smart_hint(guess, target)
                    print(f"{Colors.RED}Too high! {hint}{Colors.END}")
                
                remaining = max_attempts - attempts
                if remaining > 0:
                    print(f"{Colors.YELLOW}{remaining} attempts left{Colors.END}")
                    
            except ValueError:
                print(f"{Colors.RED}Please enter a valid number or 'hint'{Colors.END}")
        
        else:
            print(f"\n{Colors.RED}{Colors.BOLD}Game Over! You're out of attempts{Colors.END}")
            print(f"The number was: {target}")
    
    def run(self):
        """Main menu loop"""
        while True:
            print(f"\n{Colors.BOLD}=== MAIN MENU ==={Colors.END}")
            print("1. Play Game")
            print("2. View High Scores")
            print("3. Rules")
            print("4. Exit")
            
            choice = input("Select option: ").strip()
            
            if choice == '1':
                self.play_game()
            elif choice == '2':
                self.show_high_scores()
            elif choice == '3':
                self.show_rules()
            elif choice == '4':
                print(f"{Colors.GREEN}Thanks for playing!{Colors.END}")
                break
            else:
                print(f"{Colors.RED}Invalid option!{Colors.END}")
    
    def show_rules(self):
        print(f"\n{Colors.BOLD}=== GAME RULES ==={Colors.END}")
        print("1. Computer picks a random number")
        print("2. You guess until you get it or run out of attempts")
        print("3. 'Too high' / 'Too low' hints after each guess")
        print("4. Smart hints tell you how close you are: Cold to Burning hot")
        print("5. Type 'hint' to know if number is odd/even (costs 1 attempt)")
        print("6. Beat the high score for each difficulty level")

if __name__ == "__main__":
    game = NumberGuessGame()
    game.run()