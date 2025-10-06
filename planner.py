#!/usr/bin/env python3
# planner.py
# Простой планировщик дня. Сохраняет задачи в файл tasks.json.

import json
from datetime import datetime
from dataclasses import dataclass, asdict
from typing import List
import os

# Имя файла, где хранятся задачи
DATA_FILE = "tasks.json"

@dataclass
class Task:
    id: int
    time: str
    title: str
    note: str = ""
    priority: int = 3
    done: bool = False
    created_at: str = ""

    def __post_init__(self):
        if not self.created_at:
            self.created_at = datetime.now().isoformat(timespec="seconds")

def load_tasks() -> List[Task]:
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    return [Task(**t) for t in data]

def save_tasks(tasks: List[Task]):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump([asdict(t) for t in tasks], f, ensure_ascii=False, indent=2)

def next_id(tasks: List[Task]) -> int:
    return max((t.id for t in tasks), default=0) + 1

def validate_time(s: str) -> bool:
    try:
        datetime.strptime(s, "%H:%M")
        return True
    except ValueError:
        return False

def add_task(tasks: List[Task], time: str, title: str, note: str = "", priority: int = 3) -> Task:
    if not validate_time(time):
        raise ValueError("Неверный формат времени. Используй HH:MM, например 09:30")
    t = Task(id=next_id(tasks), time=time, title=title.strip(), note=note.strip(), priority=priority)
    tasks.append(t)
    tasks.sort(key=lambda x: (x.time, x.priority))
    save_tasks(tasks)
    return t

def list_tasks(tasks: List[Task]):
    if not tasks:
        print("Задачи не найдены.")
        return
    print("\n=== План на день ===")
    for t in tasks:
        status = "✓" if t.done else " "
        print(f"[{status}] ID:{t.id} {t.time} | {t.title} (prio:{t.priority})")
        if t.note:
            print(f"     → {t.note}")
    print("====================\n")

def mark_done(tasks: List[Task], task_id: int) -> bool:
    for t in tasks:
        if t.id == task_id:
            t.done = True
            save_tasks(tasks)
            return True
    return False

def delete_task(tasks: List[Task], task_id: int) -> bool:
    for i, t in enumerate(tasks):
        if t.id == task_id:
            tasks.pop(i)
            save_tasks(tasks)
            return True
    return False

def prompt_loop():
    tasks = load_tasks()
    print("=== Планировщик дня ===")
    while True:
        print("\nКоманды: add / list / done / del / exit / help")
        cmd = input("Команда: ").strip().lower()
        if cmd == "add":
            time = input("Время (HH:MM): ").strip()
            title = input("Заголовок: ").strip()
            note = input("Заметка (опц): ").strip()
            pr = input("Приоритет 1-high,2-medium,3-low [3]: ").strip()
            pr_val = int(pr) if pr.isdigit() else 3
            try:
                t = add_task(tasks, time, title, note, pr_val)
                print(f"Добавлено: ID {t.id} {t.time} {t.title}")
            except ValueError as e:
                print("Ошибка:", e)
        elif cmd == "list":
            list_tasks(tasks)
        elif cmd == "done":
            tid = input("ID задачи: ").strip()
            if tid.isdigit() and mark_done(tasks, int(tid)):
                print("Отмечено выполненным.")
            else:
                print("Задача не найдена.")
        elif cmd == "del":
            tid = input("ID задачи: ").strip()
            if tid.isdigit() and delete_task(tasks, int(tid)):
                print("Удалено.")
            else:
                print("Задача не найдена.")
        elif cmd == "help":
            print("add - добавить задачу\n list - показать задачи\n done - отметить как выполненную\n del - удалить задачу\n exit - выйти")
        elif cmd == "exit":
            print("Выход. Данные сохранены.")
            break
        else:
            print("Неизвестная команда.")

if __name__ == "__main__":
    prompt_loop()
