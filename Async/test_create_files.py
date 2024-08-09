import pytest
import asyncio
import aiofiles
import os

from file_creation import create_file, main

@pytest.mark.asyncio
async def test_create_file():
    index = 1
    filename = f"file_{index}.txt"

    if os.path.exists(filename):
        os.remove(filename)

    await create_file(index)

    assert os.path.exists(filename), f"{filename} не был создан."

    async with aiofiles.open(filename, 'r') as f:
        content = await f.read()
        assert content == f"This is file number {index}", "Содержимое файла не совпадает с ожидаемым."

    # Удаление файла после теста
    #os.remove(filename)

@pytest.mark.asyncio
async def test_main():
    # Запуск функции main
    await main()

    # Проверка, что все файлы созданы
    for i in range(1, 11):
        filename = f"file_{i}.txt"
        assert os.path.exists(filename), f"{filename} не был создан."

        # Проверка содержимого файла
        async with aiofiles.open(filename, 'r') as f:
            content = await f.read()
            assert content == f"This is file number {i}", f"Содержимое {filename} не совпадает с ожидаемым."

        # Удаление файла после теста
        #os.remove(filename)
