import sys
import os

# Добавляем папку 'app' в путь поиска модулей
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

import pytest
from fastapi.testclient import TestClient
from app.main import app  # Теперь модуль 'app' должен быть найден

@pytest.fixture
def client():
    # Создаем клиент для тестирования
    return TestClient(app)