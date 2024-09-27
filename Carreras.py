import tkinter as tk
from tkinter import messagebox
import random
import json
import os

# Ruta del archivo para almacenar los datos del usuario
DATA_FILE = "user_data.json"


# Clase para el juego
class MathGame:
    def __init__(self):
        self.score = 0
        self.level = 1
        self.user_data = self.load_user_data()

    def load_user_data(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r') as file:
                return json.load(file)
        return {}

    def save_user_data(self):
        with open(DATA_FILE, 'w') as file:
            json.dump(self.user_data, file)

    def new_game(self):
        self.score = 0
        self.level = 1
        self.user_data = {}
        self.save_user_data()

    def next_level(self):
        self.level += 1

    def add_score(self, points):
        self.score += points

    def get_score(self):
        return self.score


# Funciones para la interfaz
def start_game():
    game.new_game()
    show_question()


def show_question():
    operation, result = generate_question(game.level)
    question_label.config(text=f"Nivel {game.level}: ¿Cuánto es {operation}?")
    answer_entry.delete(0, tk.END)
    answer_entry.focus()
    global correct_answer
    correct_answer = result


def check_answer():
    answer = answer_entry.get()
    if answer.isdigit() and int(answer) == correct_answer:
        game.add_score(10)  # Añadir 10 puntos por respuesta correcta
        messagebox.showinfo("Correcto", "¡Respuesta correcta!")
        game.next_level()
        show_question()
    else:
        messagebox.showerror("Incorrecto", "Respuesta incorrecta. Intenta de nuevo.")


def show_instructions():
    instructions = (
        "Instrucciones:\n"
        "1. Comienza un nuevo juego.\n"
        "2. Responde correctamente las preguntas matemáticas para avanzar.\n"
        "3. Obtén puntos por cada respuesta correcta.\n"
        "4. Tu puntaje total se mostrará después de cada nivel."
    )
    messagebox.showinfo("Instrucciones", instructions)


def generate_question(level):
    # Genera una operación aleatoria (suma, resta, multiplicación, división)
    operators = ['+', '-', '*', '/']
    op = random.choice(operators)

    if op == '+':
        a, b = random.randint(1, 10 * level), random.randint(1, 10 * level)
        result = a + b
    elif op == '-':
        a, b = random.randint(1, 10 * level), random.randint(1, 10 * level)
        result = a - b
    elif op == '*':
        a, b = random.randint(1, 10 * level), random.randint(1, 10 * level)
        result = a * b
    else:  # Division
        b = random.randint(1, 10 * level)
        a = b * random.randint(1, 10 * level)  # Asegura que sea divisible
        result = a // b

    return f"{a} {op} {b}", result


# Configuración de la ventana principal
root = tk.Tk()
root.title("Juego de Matemáticas")

game = MathGame()

# Elementos de la interfaz
question_label = tk.Label(root, text="", font=("Helvetica", 14))
question_label.pack(pady=20)

answer_entry = tk.Entry(root, font=("Helvetica", 14))
answer_entry.pack(pady=10)

check_button = tk.Button(root, text="Comprobar respuesta", command=check_answer)
check_button.pack(pady=10)

start_button = tk.Button(root, text="Nuevo Juego", command=start_game)
start_button.pack(pady=5)

instructions_button = tk.Button(root, text="Instrucciones", command=show_instructions)
instructions_button.pack(pady=5)

# Ejecutar la aplicación
root.mainloop()
