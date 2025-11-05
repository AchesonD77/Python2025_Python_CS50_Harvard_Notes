# CS50P Notes & Exercises — 2025 Study Repo  
**Author:** AchesonD77 (Dan)  
**Course:** Harvard CS50’s Introduction to Programming with Python (CS50P)

> This repository is my bilingual (English + 中文) notebook for CS50P. It contains clean lecture notes, summaries, and my own practice projects organized by lecture.

---

## 🇬🇧 English Version

### Why this repo
- A concise, **hands-on companion** to CS50P with my solutions and takeaways.
- Two parallel note sets: **English** & **Chinese** so I can switch audiences easily.
- Reproducible scripts for each lecture’s practice problems.

### What’s inside
- **`EnglishVersion/`** — Lecture notes in English, one file per lecture.  
- **`ChineseVersion/`** — 对应的中文讲义与笔记，每讲一个文件。  
- **`PythonProjects/`** — My practice code organized by `lecture_00` … `lecture_08`.

Quick preview of the structure:
```
Python2025_Python_CS50_Harvard_Notes/
├── ChineseVersion/
│   ├── 课程_00_函数_变量.MD
│   ├── 课程_01_条件语句.MD
│   ├── 课程_02_循环.MD
│   ├── 课程_03_异常.MD
│   ├── 课程_04_库_包_模块.MD
│   ├── 课程_05_单元测试.MD
│   ├── 课程_06_文件_IO流.MD
│   ├── 课程_07_正则表达式.MD
│   └── 课程_08_面向对象编程.MD
├── EnglishVersion/
│   ├── LECTURE_00_FUNCTIONS_VARIABLES.MD
│   ├── LECTURE_01_CONDITIONALS.MD
│   ├── LECTURE_02_LOOPS.MD
│   ├── LECTURE_03_EXCEPTIONS.MD
│   ├── LECTURE_04_LIBRARIES.MD
│   ├── LECTURE_05_UNIT_TESTS.MD
│   ├── LECTURE_06_FILE_IO.MD
│   ├── LECTURE_07_REGULAR_EXPRESSIONS.MD
│   └── LECTURE_08_Object_Oriented_Programming.MD
└── PythonProjects/
    ├── lecture_00/
    ├── lecture_01/
    ├── lecture_02/
    ├── lecture_03/
    ├── lecture_04/
    ├── lecture_05/
    ├── lecture_06/
    ├── lecture_07/
    └── lecture_08/
```

### Course overview (topics I covered)
- **Functions & Variables**, input/output, style
- **Conditionals** and boolean logic
- **Loops** and iteration patterns
- **Exceptions** and error handling
- **Libraries, Packages, Modules** and imports
- **Unit Testing** (pytest-style thinking, testing mindset)
- **File I/O** and CSV/JSON basics
- **Regular Expressions**
- **Object-Oriented Programming** (class, static/class methods, inheritance)
- **Et cetera**: generators, iterators, and more

### Progress snapshot
I followed the weekly pace and finished Week 0 → Week 8 problem sets (e.g., **Indoor Voice, Camel Case, Grocery List, Bitcoin Price Index, Refueling, Scourgify, NUMB3RS, Cookie Jar, CS50 Shirtificate**, etc.). The project folders contain my runnable solutions and small utilities.

I used IDE PyCharm, python3.0, and then we can code.


### How to use / run
```bash
# 1) Clone
git clone https://github.com/<your-username>/Python2025_Python_CS50_Harvard_Notes.git
cd Python2025_Python_CS50_Harvard_Notes

# 2) (Optional) Create a virtual environment
python3 -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 3) Install optional tools for testing (if needed)
pip install -U pytest

# 4) Run any script
python PythonProjects/lecture_04/your_script.py

# 5) Run tests (when provided)
pytest -q
```

### Naming & navigation tips
- Each `lecture_xx/` folder mirrors CS50P’s order. Start from the lowest `xx` and go upward.
- Notes and code are intentionally simple and idiomatic to practice **readable Python**.

### Acknowledgements
- Course: **CS50P by Harvard University**. All trademarks belong to their respective owners.  
- This repo contains **my original notes and implementations** inspired by the course.

### License
Unless otherwise noted, all code and notes are for **personal study and educational sharing**. Please open an issue if you want to reuse a substantial portion.

---

## 🇨🇳 中文版本

### 这个仓库做什么
- 作为 CS50P 的**实践型学习笔记**，同步记录了我的解题思路与关键概念。
- **中英文双语**两套讲义，便于我在不同语境下复习与分享。
- 每一讲配套可运行的小脚本与练习代码。

### 仓库内容
- **`EnglishVersion/`** —— 英文讲义与笔记（每讲一个文件）。  
- **`ChineseVersion/`** —— 对应的**中文**讲义与总结。  
- **`PythonProjects/`** —— 按 `lecture_00 … lecture_08` 归档的练习与示例代码。

### 课程覆盖的主题
- **函数与变量**（输入/输出、风格）  
- **条件分支**与布尔逻辑  
- **循环**与迭代模式  
- **异常处理**与错误恢复  
- **库 / 包 / 模块**与 `import`  
- **单元测试**（以 pytest 思维为主）  
- **文件 I/O**（包含 CSV/JSON）  
- **正则表达式**  
- **面向对象编程**（类、静态/类方法、继承）  
- **扩展主题**：生成器、迭代器等

### 学习进度
我按周完成了 **Week 0 ~ Week 8** 的题目与项目（如：Indoor Voice、Camel Case、Grocery List、Bitcoin Price Index、Refueling、Scourgify、NUMB3RS、Cookie Jar、CS50 Shirtificate 等）。对应代码位于 `PythonProjects/` 各讲文件夹内。

### 如何使用 / 运行
```bash
git clone https://github.com/<your-username>/Python2025_Python_CS50_Harvard_Notes.git
cd Python2025_Python_CS50_Harvard_Notes
python3 -m venv .venv && source .venv/bin/activate   # Windows 使用 .venv\Scripts\activate
pip install -U pytest                                 # 可选：安装测试工具
python PythonProjects/lecture_04/your_script.py
pytest -q                                             # 可选：运行测试
```

### 说明
- `lecture_xx` 与课程顺序一致，**由低到高**逐讲练习。  
- 代码强调**可读性与规范性**，便于后续复盘。  

### 致谢与许可
- 课程来源：**Harvard CS50P**。本仓库仅为**学习与分享**用途。  
- 如需引用或改编大量内容，欢迎先提 Issue 讨论许可方式。

---

If this repo helped you, a ⭐️ would make my day!