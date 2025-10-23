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
