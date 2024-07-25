# School Forum

School Forum is a web application for discussing and sharing information about schools. Users can view school information, read discussions, and create their own discussions and comments.

## Requirements

- Python 3.7+
- Django 3.2+
- Pillow (for image handling)

## Installation

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/yourusername/schoolforum.git
    cd schoolforum
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply database migrations:
    ```bash
    python manage.py migrate
    ```

5. Create a superuser account:
    ```bash
    python manage.py createsuperuser
    ```

6. Collect static files:
    ```bash
    python manage.py collectstatic
    ```

7. Run the development server:
    ```bash
    python manage.py runserver
    ```

8. Open your web browser and navigate to `http://127.0.0.1:8000` to see the application.

## Features

- View detailed information about schools.
- Users can create, read, update, and delete discussions.
- Users can comment on discussions.
- User authentication and profile management.

## Models

- **School**: Stores information about schools.
- **Discussion**: Represents discussions related to a school.
- **Comment**: Represents comments made on discussions.
- **Rating**: Allows users to upvote or downvote discussions.
- **Image**: Stores images related to schools, discussions, and comments.

## Forms

- **DiscussionForm**: Form for creating and updating discussions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## Contact

For any questions or suggestions, please open an issue or contact the repository owner.

---

Thank you for using School Forum!
