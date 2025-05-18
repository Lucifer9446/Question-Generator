import random
import spacy

def generate_true_false(text, num_questions):
    # Load the English language model
    nlp = spacy.load('en_core_web_sm')

    # Analyze the text with spaCy
    doc = nlp(text)

    # Generate true/false questions
    true_false_questions = []
    used_questions = set()

    question_number = 1

    while len(true_false_questions) < num_questions:
        # Choose a random sentence from the analyzed document
        sentence = random.choice(list(doc.sents))

        # Check if the sentence has already been used in a question
        if sentence.text in used_questions:
            continue

        # Generate a true/false question based on different aspects of the sentence
        question_type = random.randint(1, 5)

        if question_type == 1:  # Named entities
            named_entities = [ent.text for ent in sentence.ents]
            if named_entities:
                question = f"True or False: The sentence '{sentence.text}' contains named entities."
                true_false_question = {
                    'question_number': question_number,
                    'question': question,
                    'answer': True,
                    'type': 'true_false'
                }
                true_false_questions.append(true_false_question)
            else:
                continue

        elif question_type == 2:  # Sentence length
            question = f"True or False: The sentence '{sentence.text}' is longer than 10 words."
            is_long = len(sentence) > 10
            true_false_question = {
                'question_number': question_number,
                'question': question,
                'answer': is_long,
                'type': 'true_false'
            }
            true_false_questions.append(true_false_question)

        elif question_type == 3:  # Part-of-speech pattern
            question = f"True or False: The sentence '{sentence.text}' follows a noun-verb-noun pattern."
            noun_verb_noun = False

            for i in range(len(sentence) - 2):
                if sentence[i].pos_ == 'NOUN' and sentence[i + 1].pos_ == 'VERB' and sentence[i + 2].pos_ == 'NOUN':
                    noun_verb_noun = True
                    break

            true_false_question = {
                'question_number': question_number,
                'question': question,
                'answer': noun_verb_noun,
                'type': 'true_false'
            }
            true_false_questions.append(true_false_question)

        elif question_type == 4:  # Starts with a verb
            question = f"True or False: The sentence '{sentence.text}' starts with a verb."
            starts_with_verb = sentence[0].pos_ == 'VERB'
            true_false_question = {
                'question_number': question_number,
                'question': question,
                'answer': starts_with_verb,
                'type': 'true_false'
            }
            true_false_questions.append(true_false_question)

        else:  # Contains a specific word
            target_word = random.choice([token.text for token in sentence if token.is_alpha])
            question = f"True or False: The sentence '{sentence.text}' contains the word '{target_word}'."
            contains_word = target_word in sentence.text
            true_false_question = {
                'question_number': question_number,
                'question': question,
                'answer': contains_word,
                'type': 'true_false'
            }
            true_false_questions.append(true_false_question)

        used_questions.add(sentence.text)

        question_number += 1

    return true_false_questions