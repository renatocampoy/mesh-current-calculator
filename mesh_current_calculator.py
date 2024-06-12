import sympy as sp
import tkinter as tk
from tkinter import simpledialog, messagebox

class MalhasEletricasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Resolução de Malhas Elétricas")
        self.create_widgets()

    def create_widgets(self):
        self.header_label = tk.Label(self.root, text="Sistema de Resolução de Malhas Elétricas\nAutor: Eng. Renato Campoy <renato@campoy.eng.br>", font=("Helvetica", 16))
        self.header_label.pack(pady=10)

        self.loop_button = tk.Button(self.root, text="Adicionar Malha", command=self.get_loop_input)
        self.loop_button.pack(pady=5)

        self.solve_button = tk.Button(self.root, text="Resolver Malhas", command=self.solve_loops)
        self.solve_button.pack(pady=5)

        self.clear_button = tk.Button(self.root, text="Limpar", command=self.clear_screen)
        self.clear_button.pack(pady=5)

        self.output_text = tk.Text(self.root, height=20, width=80)
        self.output_text.pack(pady=10)

        self.loop_equations = {}
        self.known_values = {}

    def get_loop_input(self):
        loop_name = simpledialog.askstring("Input", "Digite o nome da malha:")
        if loop_name:
            defined_value = simpledialog.askstring("Input", f"A malha {loop_name} já tem um valor definido? (s/n):")
            if defined_value and defined_value.strip().lower() == 's':
                value = simpledialog.askfloat("Input", f"Digite o valor da malha {loop_name}:")
                self.loop_equations[loop_name] = value
                self.known_values[sp.Symbol(loop_name)] = value
                self.output_text.insert(tk.END, f"{loop_name}: {value}\n")
            else:
                equation = simpledialog.askstring("Input", f"Digite a equação da malha {loop_name} (ex: 20*(I2 - I1) + 40*(I2 - I3) + 50 = 0):")
                try:
                    sp.sympify(equation.replace('=', '- (') + ')')
                    self.loop_equations[loop_name] = equation
                    self.output_text.insert(tk.END, f"{loop_name}: {equation}\n")
                except (sp.SympifyError, SyntaxError):
                    messagebox.showerror("Erro", "Equação inválida. Tente novamente.")

    def substitute_known_values(self, equations, known_values):
        substituted_equations = []
        for eq in equations:
            for var, value in known_values.items():
                eq = eq.subs(var, value)
            substituted_equations.append(eq)
        return substituted_equations

    def solve_loops(self):
        self.clear_screen()
        variables = set()
        sympy_equations = []

        self.output_text.insert(tk.END, "Equações adicionadas:\n")
        for name, eq in self.loop_equations.items():
            self.output_text.insert(tk.END, f"{name}: {eq}\n")
            if isinstance(eq, float):
                self.known_values[sp.Symbol(name)] = eq
            else:
                sympy_equation = sp.sympify(eq.replace('=', '- (') + ')')
                sympy_equations.append(sympy_equation)
                variables.update(sympy_equation.free_symbols)

        sympy_equations = self.substitute_known_values(sympy_equations, self.known_values)

        self.output_text.insert(tk.END, "\nEquações simbólicas após substituição de valores conhecidos:\n")
        for eq in sympy_equations:
            self.output_text.insert(tk.END, f"{eq}\n")

        solutions = sp.linsolve(sympy_equations, list(variables))
        self.output_text.insert(tk.END, "\nSoluções:\n")
        self.output_text.insert(tk.END, f"{solutions}\n")

        if solutions:
            self.output_text.insert(tk.END, "\nValores das correntes nas malhas:\n")
            for solution in solutions:
                for var, value in zip(variables, solution):
                    self.output_text.insert(tk.END, f"{var}: {value.evalf()}\n")

    def clear_screen(self):
        self.output_text.delete('1.0', tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = MalhasEletricasApp(root)
    root.mainloop()
