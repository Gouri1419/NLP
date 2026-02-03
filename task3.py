import re

def spam_detector(message, spam_words):
    message_lower = message.lower()
    found_spam_words = [word for word in spam_words if word in message_lower]
    is_spam = len(found_spam_words) > 0
    return is_spam, found_spam_words
