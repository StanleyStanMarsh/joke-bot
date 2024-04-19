from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from jokes.generate import try_to_generate_joke
from utils.length_keyboard import make_row_keyboard

router = Router()

joke_length = ['Короткий', 'Средний', 'Длинный']


class JokeWithWords(StatesGroup):
    choosing_words = State()
    choosing_length = State()


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


@router.message(JokeWithWords.choosing_length, F.text.in_(joke_length))
async def choose_joke_length(message: Message, state: FSMContext):
    user_data = await state.get_data()
    await message.answer(
        text=try_to_generate_joke(user_data['words'], message.text.lower()),
        reply_markup=ReplyKeyboardRemove()
    )
    await state.clear()


@router.message(JokeWithWords.choosing_length)
async def incorrect_length(message: Message):
    await message.answer(
        text="Я не знаю такую длину, введи длину заново",
        reply_markup=make_row_keyboard(joke_length)
    )
