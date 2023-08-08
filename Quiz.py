import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Application")

        self.questions = [
            {
                "question": "Which of the following is NOT a valid data type in Python?",
                "options": ["Integer", "String", "Dictionary", "Float"],
                "correct": 2
            },
            {
                "question": "What keyword is used to define a function in Python?",
                "options": ["define", "function", "def", "fun"],
                "correct": 2
            },
            {
                "question": "Which Python library is commonly used for data visualization?",
                "options": ["Matplotlib", "Numpy", "Pandas", "Sklearn"],
                "correct": 0
            }
        ]
        self.current_question = 0
        self.score = 0

        self.question_label = tk.Label(root, text="", font=("Helvetica", 14))
        self.question_label.pack(pady=10)

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(root, text="", font=("Helvetica", 12), command=lambda i=i: self.check_answer(i))
            button.pack(pady=5)
            self.option_buttons.append(button)

        self.next_button = tk.Button(root, text="Next Question", font=("Helvetica", 12), command=self.next_question)
        self.next_button.pack(pady=10)
        self.next_button.config(state=tk.DISABLED)

        self.update_question()

    def update_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            self.question_label.config(text=question_data["question"])

            for i, option in enumerate(question_data["options"]):
                self.option_buttons[i].config(text=option, state=tk.NORMAL)

    def check_answer(self, selected_option):
        question_data = self.questions[self.current_question]
        if selected_option == question_data["correct"]:
            self.score += 1
        self.option_buttons[selected_option].config(state=tk.DISABLED)
        self.next_button.config(state=tk.NORMAL)

    def next_question(self):
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.update_question()
            for button in self.option_buttons:
                button.config(state=tk.NORMAL)
            self.next_button.config(state=tk.DISABLED)
        else:
            messagebox.showinfo("Quiz Over", f"Your score: {self.score}/{len(self.questions)}")
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
