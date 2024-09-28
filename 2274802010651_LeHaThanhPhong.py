import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as msg

#create instance
win = tk.Tk()
win.title("Tinh Toan")

menu_bar = Menu(win)  
win.config(menu=menu_bar)

def _quit():
    win.quit()  
    win.destroy()  

def _msgBox():
    answer = msg.askyesnocancel("Python Message Multi Choice Box", "Are you sure you really wish to do this?")


class Calculator:
    def __init__(self, so_a, so_b):
        # Chuyển đổi sang số nguyên nếu có thể, nếu không thì giữ nguyên là số thực
        try:
            self.a = int(so_a)
        except ValueError:
            self.a = float(so_a)
            
        try:
            self.b = int(so_b)
        except ValueError:
            self.b = float(so_b)

    def cong(self):
        result = self.a + self.b
        # Kiểm tra nếu cả hai là số nguyên, thì trả về kết quả là số nguyên
        if isinstance(self.a, int) and isinstance(self.b, int):
            return int(result)
        return result

    def tru(self):
        return self.a - self.b

    def nhan(self):
        return self.a * self.b

    def chia(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Error: Division by zero"

    def chia_lay_du(self):
        if self.b != 0:
            return self.a % self.b
        else:
            return "Error: Division by zero"

# Hàm xử lý mỗi khi người dùng nhấn nút
def calculation(pheptinh):
    a = so_a.get()
    b = so_b.get()
    if a and b:
        try:
            # Khởi tạo đối tượng Calculator
            calc = Calculator(a, b)
            if pheptinh == "cong":
                result = calc.cong()
            elif pheptinh == "tru":
                result = calc.tru()
            elif pheptinh == "nhan":
                result = calc.nhan()
            elif pheptinh == "chia":
                result = calc.chia()
            elif pheptinh == "chia_lay_du":
                result = calc.chia_lay_du()

            # Hiển thị kết quả
            kq_output.delete(0, tk.END)
            kq_output.insert(0, str(result))
        except ValueError:
            msg.showerror("Input Error", "Please enter valid numbers for a and b")
    else:
        msg.showerror("Input Error", "Please enter values for both a and b")

# Create menu and add menu items
file_menu = Menu(menu_bar, tearoff=0)  
file_menu.add_command(label="New") 
file_menu.add_separator()
file_menu.add_command(label="Exit", command=_quit) 
menu_bar.add_cascade(label="File", menu=file_menu)

help_menu = Menu(menu_bar, tearoff=0)  
menu_bar.add_cascade(label="Help", menu=help_menu)  
help_menu.add_command(label="About", command=_msgBox)

tabControl = ttk.Notebook(win)
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Tab 1')

tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='Tab 2')

tabControl.pack(expand=1, fill='both')

trangtinh = tk.LabelFrame(tab1, text=' Trang tính', foreground="blue")
trangtinh.pack(padx=8, pady=4, fill="both")  

mighty2 = tk.LabelFrame(tab2, text=' Nothing Here ')
mighty2.pack(padx=8, pady=4, fill="both")  

# Phần nhập số a và b
ttk.Label(trangtinh, text="a:").grid(column=0, row=0, padx=5, pady=5, sticky=tk.E)
so_a = tk.StringVar()
so_a_entered = ttk.Entry(trangtinh, width=12, textvariable=so_a)
so_a_entered.grid(column=1, row=0, padx=5, pady=5)

ttk.Label(trangtinh, text="b:").grid(column=0, row=1, padx=5, pady=5, sticky=tk.E)
so_b = tk.StringVar()
so_b_entered = ttk.Entry(trangtinh, width=12, textvariable=so_b)
so_b_entered.grid(column=1, row=1, padx=5, pady=5)

# Ô hiển thị kết quả
ttk.Label(trangtinh, text="Kết quả:").grid(column=0, row=2, padx=5, pady=5, sticky=tk.E)
kq = tk.StringVar()
kq_output = ttk.Entry(trangtinh, width=30, textvariable=kq)
kq_output.grid(column=1, row=2, padx=5, pady=5)

# Bảng phép tính
buttons_frame = ttk.LabelFrame(trangtinh, text='Chọn phép tính')  
buttons_frame.grid(column=2, row=0, rowspan=3, padx=20, pady=10, sticky="n")

#lambda == hàm rỗng, dùng để thế chỗ
ttk.Button(buttons_frame, text="+", command=lambda: calculation("cong")).grid(column=0, row=0, padx=10, pady=10)
ttk.Button(buttons_frame, text="-", command=lambda: calculation("tru")).grid(column=1, row=0, padx=10, pady=10)
ttk.Button(buttons_frame, text="*", command=lambda: calculation("nhan")).grid(column=0, row=1, padx=10, pady=10)
ttk.Button(buttons_frame, text="/", command=lambda: calculation("chia")).grid(column=1, row=1, padx=10, pady=10)
ttk.Button(buttons_frame, text="%", command=lambda: calculation("chia_lay_du")).grid(column=0, row=2, padx=10, pady=10)

for child in buttons_frame.winfo_children():
    child.grid_configure(padx=8, pady=4)

so_a_entered.focus()

#Start GUI
win.mainloop()
