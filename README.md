# Jupyter Notebook Project

## 📌 Project Setup Guide
Follow these steps to set up and run this project on your local machine.

---

## 📂 1. Extract the ZIP File
After downloading the zip file:
1. Extract it to your preferred directory.
2. Navigate to the extracted folder.

```sh
cd your-project-folder
```

---

## 🏗 2. Create a Virtual Environment (Recommended)
To keep dependencies isolated, create a virtual environment.

```sh
python -m venv venv
```

#### **Activate the Virtual Environment:**
- **Windows (Command Prompt):**  
  ```sh
  venv\Scripts\activate
  ```
- **Windows (PowerShell):**  
  ```sh
  venv\Scripts\Activate.ps1
  ```
- **Mac/Linux:**  
  ```sh
  source venv/bin/activate
  ```

---

## 📦 3. Install Dependencies
Once the virtual environment is activated, install all required packages:

```sh
pip install -r requirements.txt
```

This will install necessary libraries such as `pandas`, `matplotlib`, `numpy`, and any other dependencies used in the notebook.

---

## 📚 4. Add Virtual Environment to Jupyter
Ensure Jupyter recognizes the new environment:

```sh
pip install ipykernel
python -m ipykernel install --user --name=venv --display-name "Python (venv)"
```

---

## 🚀 5. Start Jupyter Notebook
To run the Jupyter Notebook, execute:

```sh
jupyter notebook
```

This will open Jupyter in your default web browser. Navigate to the `.ipynb` file and start working!

---

## 🔄 6. Deactivate the Virtual Environment (After Work)
When you're done, deactivate the virtual environment:

```sh
deactivate
```

---

## ❗ Additional Notes
- Ensure you have **Python 3.8+** installed before running the commands.
- If `jupyter` is not installed, install it manually:

  ```sh
  pip install jupyter
  ```

- If you face **kernel issues**, restart Jupyter Notebook and select **Kernel > Change Kernel > Python (venv)**.

---

## 🔄 (Optional) Update `requirements.txt`
If you add new packages and want to update `requirements.txt`, run:

```sh
pip freeze > requirements.txt
```

---

**🎉 Now you're ready to run the project! Happy coding!** 🚀

