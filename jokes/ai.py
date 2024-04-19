from gigachat import GigaChat
from dotenv import load_dotenv
import os

load_dotenv()

giga = GigaChat(credentials=os.getenv('GIGATOKEN'), scope='GIGACHAT_API_PERS', verify_ssl_certs=False)


def get_joke() -> str:
    response = giga.chat(f'Напиши несуществующий анекдот про Штирлица')
    return response.choices[0].message.content


def get_words_joke(words: set, length: str) -> str:
    required_words = ', '.join(words)
    response = giga.chat(f'Напиши {length} анекдот про Штирлица. Обязательно используй все эти слова: {required_words}')
    return response.choices[0].message.content
