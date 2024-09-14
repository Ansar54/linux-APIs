# FastAPI CRUD Application

This repository contains a simple FastAPI application that implements basic CRUD (Create, Read, Update, Delete) operations. Developed using WSL2 on a Linux environment, this project showcases how to build a RESTful API with FastAPI.

## Project Structure

- `main.py`: Contains the FastAPI application with CRUD operations.

## Setup Instructions

### Prerequisites

- Python 3.x
- `pip` (Python package installer)
- `virtualenv` (optional, for creating virtual environments)
- Git


**## **Steps of Execution and linux Commands used**

```bash
**Create and activate Virtual environment(Optional)**
python3 -m venv env
source env/bin/activate

**Clone the Repository**
```bash
   git clone https://github.com/yourusername/linux-APIs.git
   cd linux-APIs

**Install Dependencies**
```bash
pip install -r requirements.txt

**Run the FastAPI Application**
```bash
uvicorn main:app --reload**

## **Linux Commands Used**
**Git Commands**
**Initialize a Git Repository**

```bash
git init

**Add Files to Staging Area**
```bash
git add .

**Commit Changes**

```bash
git commit -m "Initial commit"

**Add a Remote Origin**
```bash
git remote add origin https://github.com/yourusername/linux-APIs.git

**Push Changes to GitHub**
```bash
git push -u origin main

**Delete a Remote Origin**
```bash
git remote remove origin

**Rename a Branch**
bash
git branch -M main

**Check Git Status**

```bash
git status

**Check Git Remote**

```bash
git remote -v
## **File Operations**

**Remove Files**
```bash
rm path/to/file

**Generate requirements.txt**
bash
pip freeze > requirements.txt

