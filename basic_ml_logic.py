<<<<<<< HEAD
# app/basic_ml_logic.py


def process_data(input_data):
    """Пример функции, имитирующей обработку данных."""
    # Получение значений из Словаря
    income = input_data["income"]
    age = input_data["age"]

    # Имитация простой "ML-логики"
    score = income / age

    # Возврат результата в виде Словаря
    return {"calculated_score": score, "status": "processed"}


# Пример использования
data_to_process = {"income": 50000.0, "age": 30}
result = process_data(data_to_process)
# print(result) # Должно вывести: {'calculated_score': 1666.666..., 'status': 'processed'}
print(result)
=======
# app/basic_ml_logic.py (Финальная версия дня 1)

from typing import Dict, Union


def process_data_typed(input_data: Dict[str, Union[float, int]]) -> Dict[str, Union[float, str]]:
    """ 
    Имитирует обработку данных с использованием строгих аннотаций типов.
    """
    if 'income' not in input_data or 'age' not in input_data:
        return {"error": "Missing required fields."}

    income = float(input_data['income'])
    age = float(input_data['age'])

    if age == 0:
        return {"error": "Age cannot be zero."}

    score = income / age

    return {
        "calculated_score": round(score, 2),
        "status": "processed_cleanly"
    }
>>>>>>> 7928892 (Adds type-annotated utility modules for ML and math)
