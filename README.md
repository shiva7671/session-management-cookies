

# Django Session Cookies Project

This project demonstrates a **multi-step form submission workflow** using Django, where user data (name, age, course) is collected step-by-step using session cookies to maintain state between pages.  
It illustrates core Django concepts like views, cookies, forms, models, and templates in a clean, beginner-friendly architecture.

***

## Features

- 🚀 **Multi-step form handling**: Divided into name, age, and course input pages  
- 🍪 **Cookie management**: Stores user input in cookies to maintain session state  
- 🛠️ **Model-backed storage**: Saves final form data (`StudentModel`) into SQLite database for persistence  
- 🎨 **Template separation**: Clean UI with CSS styling for input and result pages  
- 🎯 **Validation & error handling**: Basic validation for required fields and user-friendly error feedback  
- 🔄 **Redirect & flow control**: Ensures proper navigation across form steps  

***

## Project Structure

- `models.py`: Defines `StudentModel` to store `name`, `age`, and `course`  
- `forms.py`: ModelForm `StudentForm` for validation & form rendering (optional in current flow)  
- `views.py`: Handles input, cookie setting, and saving student data to DB  
- `urls.py`: Routes requests to respective views for each step  
- `templates/`: HTML templates for each form page and result page  
- `static/`: CSS files `style.css` and `result.css` for UI styling  

***

## Installation & Setup

1. Clone the repository:  
   ```
   git clone https://github.com/yourusername/sessioncookies-django.git
   ```

2. Create and activate a virtual environment:  
   ```
   python -m venv env
   source env/bin/activate  # Windows: env\Scripts\activate
   ```

3. Install dependencies:  
   ```
   pip install django
   ```

4. Apply migrations to create DB schema:  
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Run the development server:  
   ```
   python manage.py runserver
   ```

6. Open your browser at `http://localhost:8000/home/` to start.

***

## Usage Flow

1. **Enter Name** on the home page → stored in cookie  
2. **Enter Age** on the age page → stored in cookie  
3. **Enter Course** on the course page → stored in database and cookie  
4. **View Result** page displaying all entered data  

***

## Screenshots

![Home Page](

  
*Name Input Page*

![Age Page](

  
*Age Input Page*

![Course Page](

  
*Course Input Page*

![Result Page](

  
*Result Display Page*

***

## Technologies Used

- Django 4.2  
- Python 3.13  
- SQLite Database  
- HTML5 / CSS3  
- Django Templates and Static Files Handling  

***

## Contributing

Contributions are welcome! Feel free to raise issues or submit pull requests for improvements.

***

## License

MIT License © 2025 vilasagaram shiva kumar

