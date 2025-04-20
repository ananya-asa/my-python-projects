import string 
import colorama
from colorama import Fore,Style
import getpass
colorama.init(autoreset=True)

def password_srength(password):
    score=0
    remarks=""

    if len(password)>=8:
        score+=1
    if any(c.islower() for c in password):
        score+=1
    if any(c.isupper() for c in password):
        score+=1
    if any(c.isdigit() for c in password):
        score+=1
    if any(c in string.punctuation for c in password):
        score+=1
    
    return score
def feedback(score):
    if score <=2:
        return Fore.RED + "❌ Very Weak Password"
    elif score==3:
        return Fore.YELLOW + "⚠️ Moderate Password"
    elif score==4:
        return Fore.CYAN + "✅ Good Password"
    else:
        return Fore.GREEN + "💪 Strong Password"

def password_art():
    art = r'''
 ____                                  _     
  |  _ \ __ _ ___ _____      _____  _ __| | __ 
  | |_) / _` / __/ __\ \ /\ / / _ \| '__| |/ / 
  |  __/ (_| \__ \__ \\ V  V / (_) | |  |   <  
  |_|   \__,_|___/___/ \_/\_/ \___/|_|  |_|\_\ 

'''  
    print(Fore.MAGENTA + art + Style.RESET_ALL)


def main():

    password_art()
    print("🔒 Enter your password (input hidden):")
    password=getpass.getpass(">> ")

    score=password_srength(password)
    print("\nStrength Score:", score, "/ 5")
    print("Feedback:", feedback(score))

    suggestions = [
        "🔸 Use a mix of uppercase and lowercase letters.",
        "🔸 Add numbers and symbols.",
        "🔸 Make it longer than 12 characters.",
        "🔸 Avoid common words or sequences."
    ]

    if score < 5:
        print(Fore.LIGHTBLUE_EX + "\n✨ Suggestions to improve your password:")
        for tip in suggestions:
            print("  ", tip)

if __name__ == "__main__":
    main()

    

