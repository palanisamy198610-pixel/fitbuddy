import random


def generate_skill_id():
    """Generate a unique skill ID."""
    return "SK-" + str(random.randint(10000, 99999))


def generate_wallet_id():
    """Generate a wallet ID."""
    return "WALLET-" + str(random.randint(100000, 999999))


def generate_certificate_id():
    """Generate a certificate ID."""
    return "CERT-" + str(random.randint(10000, 99999))


def generate_fidbuddy_response(message):
    """Generate a simple FidBuddy response."""

    message = message.lower().strip()

    responses = {
        "hello": "Hello! 👋 I am FidBuddy.",
        "hi": "Hi! How can I help you?",
        "help": "Sure! Tell me what you need help with.",
        "skill": "You can add, update and manage your skills in SkillWallet.",
        "wallet": "Your SkillWallet stores your skills and achievements.",
        "certificate": "You can generate and manage your skill certificates here."
    }

    for keyword, response in responses.items():
        if keyword in message:
            return response

    return "I'm FidBuddy 🤖. Please tell me more about your request."


if __name__ == "__main__":
    print("Skill ID:", generate_skill_id())
    print("Wallet ID:", generate_wallet_id())
    print("Certificate ID:", generate_certificate_id())

    message = input("You: ")
    print("FidBuddy:", generate_fidbuddy_response(message))
