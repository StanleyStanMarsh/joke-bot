from langchain.chat_models.gigachat import GigaChat
from langchain.schema import HumanMessage, SystemMessage
from dotenv import load_dotenv
import os

load_dotenv()

sys_msg = SystemMessage(
    content="Ты бот, генерирующий анекдоты про Штирлица"
)

giga = GigaChat(credentials=os.getenv('GIGATOKEN'), scope='GIGACHAT_API_PERS', verify_ssl_certs=False)


def get_joke() -> str:
    msg = [
        sys_msg,
        HumanMessage("Сгенерируй анекдот про Штирлица, не повторяйся, делай каждый раз новый")
    ]
    response = giga(msg)
    return response.content


def get_words_joke(words: set, length: str) -> str:
    required_words = ', '.join(words)
    msg = [
        sys_msg,
        HumanMessage(f"Сгенерируй {length} анекдот про Штирлица, не повторяйся, делай каждый раз новый. "
                     f"Обязательно используй все эти слова: {required_words}")
    ]
    response = giga(msg)
    return response.content


def words_check(words: str, joke: str) -> str:
    response = giga([HumanMessage(f"Есть ли данные слова: {words} - в следующем сообщении: {joke}\n"
                                  f"Ответь одним словом: да/нет")])
    # print(response)
    return response.content
