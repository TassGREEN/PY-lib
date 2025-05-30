import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os


class PyToExeConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Python 转 EXE 打包工具")
        self.root.geometry("600x400")  # 设置默认窗口大小
        self.root.resizable(False, False)  # 禁止改变窗口大小

        # 存储文件和输出路径
        self.script_path = tk.StringVar()
        self.output_path = tk.StringVar()

        # 创建界面组件
        self.create_widgets()

    def create_widgets(self):
        # 标题标签
        title_label = tk.Label(self.root, text="Python 转 EXE 打包工具", font=("Arial", 16))
        title_label.pack(pady=20)

        # 选择脚本路径
        script_frame = tk.Frame(self.root)
        script_frame.pack(pady=10, fill=tk.X, padx=20)

        tk.Label(script_frame, text="Python 脚本路径:", width=15).pack(side=tk.LEFT)

        tk.Entry(script_frame, textvariable=self.script_path, width=40).pack(side=tk.LEFT, expand=True, fill=tk.X)
        tk.Button(script_frame, text="浏览", command=self.browse_script).pack(side=tk.LEFT, padx=5)

        # 选择输出路径
        output_frame = tk.Frame(self.root)
        output_frame.pack(pady=10, fill=tk.X, padx=20)

        tk.Label(output_frame, text="输出目录:", width=15).pack(side=tk.LEFT)

        tk.Entry(output_frame, textvariable=self.output_path, width=40).pack(side=tk.LEFT, expand=True, fill=tk.X)
        tk.Button(output_frame, text="浏览", command=self.browse_output).pack(side=tk.LEFT, padx=5)

        # 按钮区域
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=30)

        tk.Button(button_frame, text="开始打包", width=15, command=self.convert_to_exe).pack(side=tk.LEFT, padx=10)
        tk.Button(button_frame, text="退出", width=10, command=self.root.quit).pack(side=tk.LEFT)

    def browse_script(self):
        file_path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
        if file_path:
            self.script_path.set(file_path)

    def browse_output(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.output_path.set(folder_path)

    def convert_to_exe(self):
        script = self.script_path.get()
        output_dir = self.output_path.get()

        if not script or not os.path.isfile(script):
            messagebox.showerror("错误", "请选择有效的 Python 脚本文件。")
            return

        if not output_dir or not os.path.isdir(output_dir):
            messagebox.showerror("错误", "请选择有效的输出目录。")
            return

        try:
            # 构造 PyInstaller 命令
            cmd = [
                'pyinstaller',
                '--onefile',  # 单个 exe
                '--noconfirm',  # 不提示覆盖
                f'--distpath={output_dir}',  # 输出路径
                script
            ]

            # 执行命令
            subprocess.run(cmd, check=True)
            messagebox.showinfo("成功", f"打包完成！EXE 文件位于: {output_dir}")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("错误", f"打包失败: {str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = PyToExeConverter(root)
    root.mainloop()