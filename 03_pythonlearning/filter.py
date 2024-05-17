def filter_messages(messages):
    filtered_messages = []
    words_removed = [];

    for message in messages:
        words_removed_per_message = 0
        message_in_words = message.split()
        cleaned_message = []
        for word in message_in_words:
            if word == 'dang':
                words_removed_per_message += 1
            else:
                cleaned_message.append(word)

        words_removed.append(words_removed_per_message)
        filtered_messages.append(" ".join(cleaned_message))

    return filtered_messages, words_removed

