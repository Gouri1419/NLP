# ---------- TASK 3: SPAM DETECTOR ----------

def spam_detector(message, spam_words):
    message_lower = message.lower()
    found_spam_words = [word for word in spam_words if word in message_lower]
    is_spam = len(found_spam_words) > 0
    return is_spam, found_spam_words

# ---------- MAIN ----------
print("----- TASK 3: SPAM DETECTOR -----")

message = "you are wining a free price now!"
spam_words = ["win", "cash", "free"]

print("Message:", message)
print("Spam Words List:", spam_words)

is_spam, words = spam_detector(message, spam_words)

print("Is Spam:", is_spam)
print("Detected Spam Words:", words)
