import tkinter as tk

questions = [
    {"question": "What does CPU stand for?", "answer": "central processing unit"},
    {"question": "What does GPU stand for?", "answer": "graphics processing unit"},
    {"question": "What does RAM stand for?", "answer": "random access memory"},
    {"question": "What does PSU stand for?", "answer": "power supply unit"},
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.score = 0
        self.q_index = 0

        self.question_label = tk.Label(root, text="", font=("Arial", 16))
        self.question_label.pack(pady=20)

        self.answer_entry = tk.Entry(root, font=("Arial", 14))
        self.answer_entry.pack()

        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

        self.next_question()

    def next_question(self):
        if self.q_index < len(questions):
            self.question_label.config(text=questions[self.q_index]["question"])
            self.answer_entry.delete(0, tk.END)
        else:
            self.question_label.config(text=f"Quiz Over! Your score: {self.score}/{len(questions)}")
            self.answer_entry.pack_forget()
            self.submit_button.pack_forget()

    def check_answer(self):
        user_answer = self.answer_entry.get().lower().strip()
        correct_answer = questions[self.q_index]["answer"]
        if user_answer == correct_answer:
            self.result_label.config(text="Correct!", fg="green")
            self.score += 1
        else:
            self.result_label.config(text=f"Wrong! Correct: {correct_answer}", fg="red")
        self.q_index += 1
        self.root.after(1000, self.next_question)

root = tk.Tk()
app = QuizApp(root)
root.mainloop()
