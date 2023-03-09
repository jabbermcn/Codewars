import os
import re
import pandas as pd
from chatgpt import ChatGPT

model = ChatGPT.load("models/model_name")


def analyze_reviews(reviews):
    result = []
    for review in reviews:
        # Получаем предсказания модели для конкретного отзыва
        predictions = model.predict(review)
        # Добавляем результаты в список
        result.append(predictions[0][1])
    # Сортируем список результатов по убыванию
    sorted_result = sorted(result, reverse=True)
    # Возвращаем отсортированный список результатов
    return sorted_result


reviews = ["Отличный сервис!", "Хорошо, но не очень удобно", "Не советую данный сервис"]
results = analyze_reviews(reviews)
print(results)
