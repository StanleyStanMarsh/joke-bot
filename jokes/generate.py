from jokes.ai import get_words_joke, words_check


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
        response = words_check(words, joke).lower()
        if 'да' in response or 'yes' in response:
            return joke
    return "Не удалось сгенерировать анекдот"
