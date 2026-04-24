# Smart Resume Builder

A project that allows users to build their resume dynamically.

## Project Structure

```
smart-resume-builder/
├── templates/
│   ├── resume_template.html
│   └── cover_letter_template.html
├── src/
│   ├── main.py
│   ├── resume.py
│   └── cover_letter.py
├── tests/
│   ├── test_resume.py
│   └── test_cover_letter.py
└── README.md
```

## Features
- Create resumes and cover letters.
- Dynamic data input from users.
- Export to PDF and DOCX formats.
- Template customization.

## Requirements
- Python 3.x
- Flask
- Jinja2
- WeasyPrint

## Getting Started
1. Clone the repository: `git clone https://github.com/Kalpana-Prabha/smart-resume-builder.git`
2. Navigate to the project directory.
3. Install the required packages: `pip install -r requirements.txt`
4. Run the application: `python src/main.py`