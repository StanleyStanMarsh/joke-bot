from jokes.ai import get_words_joke


def delete_punctuation(s: str) -> str:
    new_s = ''
    marks = {'.', ',', ';', '!', '?', ':'}
    for c in s:
        if c not in marks:
            new_s += c
    return new_s


def try_to_generate_joke(words: str, length: str) -> str:
    words = delete_punctuation(words)
    words_set = set(map(str.lower, words.split()))

    for i in range(5):
        joke = get_words_joke(words_set, length)
        joke_set = set(map(str.lower, delete_punctuation(joke).split()))
        required_words = set(words_set)

        for word in joke_set:
            for req in required_words:
                if word.startswith(req):
                    required_words.discard(req)
                    break

        if len(required_words) == 0:
            return joke
    return "Не удалось сгенерировать анекдот"
