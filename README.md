# Proton-Therapy-QA
The project aims to deliver a modern SQL-based database with a web interface for Proton Beam Therapy (PBT) QA data management at UCLH, replacing an unsupported Microsoft Access system. The objective is to enable efficient data input, analysis, and long-term tracking to support clinical workflows and patient safety. 

Steps to run the project Locally:

- uv sync # Creates/updates .venv 
- uv run python manage.py runserver # Starts the Django development server

Server run on: http://127.0.0.1:8000/
Open SQl lite database from: https://sqlitebrowser.org/dl/