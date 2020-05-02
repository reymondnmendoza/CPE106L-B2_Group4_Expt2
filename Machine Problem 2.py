
import random


class Doctor(object):
    history = []
    hedges = ("Please tell me more.",
            "Don't worry. You're not the only one.",
            "Please coninue.")
    qualifiers = ("Why do you say that you ",
            "You seem to think that you ",
            "Can you explain why you ")
    replacements = {"I": "you", "me": "you", "my": "your",
            "we": "you", "us": "you", "mine": "yours",
            "you": "I", "your": "my", "yours": "mine"}
    def __init__(self):
        pass
    def reply(self, sentence):
        """Implements three different reply strategies."""
        probability = random.randint(1, 5)
        if probability in (1, 2):
            # Just hedge
            answer = random.choice(Doctor.hedges)
        elif probability == 3 and len(Doctor.history) > 3:
            # Go back to an earlier topic
            answer = "Earlier you said that " + \
            self.changePerson(random.choice(Doctor.history))
        else:
            # Transform the current input
            answer = random.choice(Doctor.qualifiers) + \
            self.changePerson(sentence)
            Doctor.history.append(sentence)
            return answer
    def changePerson(self, sentence):
        words = sentence.split()
        replyWords = []
        for word in words:
            replyWords.append(Doctor.replacements.get(word, word))
        return " ".join(replyWords)
    def greeting(self):
        return "Hi, Let's get started"
    def farewell(self):
        return "Time's up, Let's pick up here next week"
def main():
    d = Doctor()
    print(d.greeting())
    while True:
        sentence = input("\n>> ")
        if sentence.upper() == "QUIT":
            print(d.farewell())
            break
        print(d.reply(sentence))
if __name__ == "__main__":
    main()
