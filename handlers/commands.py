from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from jokes.ai import get_joke, get_words_joke
from keyboards.length import make_row_keyboard

router = Router()

joke_length = ['Короткий', 'Средний', 'Длинный']


class JokeWithWords(StatesGroup):
    choosing_words = State()
    choosing_length = State()


@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "Привет! Я бот с анекдотами про Штирлица, работающий на базе GigaChat\n"
        "Доступные команды:\n"
        "/joke - команда для генерации случайного анекдота;\n"
        "/wordsjoke - команда для генерации анекдота с заданными словами.",
    )


@router.message(Command("joke"))
async def cmd_generate_joke(message: Message):
    await message.answer(
        get_joke()
    )


@router.message(StateFilter(None), Command("wordsjoke"))
async def cmd_words_joke(message: Message, state: FSMContext):
    await message.answer(
        "Введите через пробел слова, которые должны присутствовать в анекдоте"
    )
    await state.set_state(JokeWithWords.choosing_words)


@router.message(JokeWithWords.choosing_words, F.text.len() > 0)
async def choose_words_for_joke(message: Message, state: FSMContext):
    await state.update_data(words=message.text.lower())
    await message.answer(
        text="Интересный выбор. Теперь выбери длину анекдота",
        reply_markup=make_row_keyboard(joke_length)
    )
    await state.set_state(JokeWithWords.choosing_length)


@router.message(JokeWithWords.choosing_words)
async def incorrect_words(message: Message):
    await message.answer(
        text="Я тебя не понял. Попробуй ввести слова заново"
    )
