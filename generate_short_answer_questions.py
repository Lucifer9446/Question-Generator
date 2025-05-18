import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.tag import pos_tag
from nltk.stem import WordNetLemmatizer
import random

def generate_short_answer_questions(text, num_questions):
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)

    # Initialize variables
    questions = []
    question_answers = set()
    used_verbs = set()

    # Counter for question numbering
    question_number = 1

    # Question templates
    question_templates = [
        "What does '{verb}' mean in the given context?",
        "How would you define '{verb}' in this context?",
        "Can you explain the implication of '{verb}'?",
        "Describe the action denoted by '{verb}' in the provided information.",
        "In the given context, what is the significance of '{verb}'?"
    ]

    # Iterate through each sentence
    for sentence in sentences:
        # Tokenize the sentence into words
        words = nltk.word_tokenize(sentence)

        # Remove stopwords and lemmatize the words
        stop_words = set(stopwords.words('english'))
        words = [WordNetLemmatizer().lemmatize(word.lower()) for word in words if word.lower() not in stop_words]

        # Perform part-of-speech tagging on the words
        tagged_words = pos_tag(words)

        # Generate questions based on sentence structure
        for word, pos in tagged_words:
            if pos.startswith('VB') and len(word) > 2 and word not in used_verbs:
                # Select a random question template
                question_template = random.choice(question_templates)
                question = f"{question_number}. {question_template.replace('{verb}', word)}"

                questions.append({
                    'question_number': question_number,
                    'question': question,
                    'type': 'short_answer'
                })

                question_number += 1

                used_verbs.add(word)

                if len(questions) == num_questions:
                    return questions, list(question_answers)

    return questions, list(question_answers)
