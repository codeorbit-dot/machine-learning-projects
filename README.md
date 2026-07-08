# all4 Jupyter setup

This folder contains a minimal Jupyter notebook setup named "all4".

Quick start (Windows PowerShell):

1. Create virtual environment (already created by script):

   python -m venv .venv

2. Install dependencies and kernel (if not already installed):

   .venv\Scripts\pip.exe install -r requirements.txt
   .venv\Scripts\python.exe -m ipykernel install --user --name=all4 --display-name "Python (all4)"

3. Start Jupyter Notebook:

   .venv\Scripts\python.exe -m notebook

Notes:
- Kernel display name will be "Python (all4)".
- To reuse the environment in VS Code, select the `Python (all4)` kernel from the kernel picker.
