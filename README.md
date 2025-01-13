# HealthSync-Django App

MediConnect is a Django-based healthcare management web application designed to connect patients and doctors seamlessly. This platform allows doctors to manage their profiles, and patients to access healthcare services efficiently.

## Features

- **User Registration & Authentication**: Secure sign-up and login for doctors and patients.
- **Doctor Dashboard**: Doctors can manage their profiles, including personal details and address.
- **Patient Dashboard**: Patients can view their profile and connect with doctors.
- **Profile Picture Upload**: Both patients and doctors can upload and update their profile pictures.
- **Responsive Design**: Optimized for both desktop and mobile devices.

## Technologies Used

- **Django**: Python-based web framework for building robust backend functionality.
- **Bootstrap**: Frontend framework for a responsive design.
- **SQLite**: Default database for local development and testing.
- **HTML, CSS, JavaScript**: Core technologies for the frontend.

## Installation

To run the project locally, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/your-username/MediConnect.git
cd MediConnect
```

2. Set up a virtual environment:

```bash
python -m venv venv
```

3. Activate the virtual environment:
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On MacOS/Linux:
      ```bash
      source venv/bin/activate
      ```

4. Install the required dependencies:

```bash
pip install -r requirements.txt
```

5. Run database migrations:

```bash
python manage.py migrate
```

6. Create a superuser for admin access:

```bash
python manage.py createsuperuser
```

7. Start the development server:

```bash
python manage.py runserver
```

8. Visit the application at `http://127.0.0.1:8000/` in your web browser.

## Video Demo

Watch the demo video of the application below:

[![Watch the video](https://www.loom.com/share/d22560b00dc24bab8d96fca2678549c4?sid=90d976f6-a6ed-4277-b4e4-7fdd94e1f3a5)](https://www.youtube.com/watch?v=YOUR_VIDEO_ID)

## Contributing

Feel free to fork the repository and submit pull requests. Please make sure to follow the contribution guidelines and maintain the code quality.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---