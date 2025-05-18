import random
from nltk.tokenize import sent_tokenize, word_tokenize

def generate_mcq_questions(text, num_questions):
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)

    mcq_questions = []
    used_sentences = set()

    question_number = 1

    while len(mcq_questions) < min(num_questions, len(sentences)):
        # Choose a random sentence that hasn't been used before
        unused_sentences = [sentence for sentence in sentences if sentence not in used_sentences]
        if not unused_sentences:
            break
        sentence = random.choice(unused_sentences)

        # Mark the sentence as used
        used_sentences.add(sentence)

        # Tokenize the sentence into words
        words = word_tokenize(sentence)

        # Generate fill-in-the-blank question for the sentence
        word = random.choice(words)
        blank_sentence = sentence.replace(word, "_____")

        # Create a question with options
        question = f"{blank_sentence}"
        answer = word

        # Get the options by shuffling the words in the sentence (excluding the answer)
        options = [w for w in words if w != answer]
        options = options[:3]
        options.append(answer)
        random.shuffle(options)

        # Format the options as separate lines
        formatted_options = "\n".join(f"{i + 1}. {option}" for i, option in enumerate(options))

        # Format the complete MCQ question
        mcq_question = {
            'question_number': question_number,
            'question': question,
            'options': formatted_options,
            'answer': answer,
            'type': 'mcq'
        }
        mcq_questions.append(mcq_question)

        question_number += 1

    return mcq_questions
