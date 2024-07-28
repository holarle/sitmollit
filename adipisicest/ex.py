def joke(update, context):
    jokes = [
        "Why don't skeletons fight each other? They don't have the guts.",
        "I told my wife she should embrace her mistakes. She gave me a hug.",
        "I'm reading a book on anti-gravity. It's impossible to put down!",
        "Why couldn't the bicycle stand up by itself? It was two tired."
    ]
    
    random_joke = random.choice(jokes)
    update.message.reply_text(random_joke)
