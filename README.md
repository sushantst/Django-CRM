# CRM (Customer Relationship Management) App

Welcome to the CRM (Customer Relationship Management) App! This project is a powerful and user-friendly customer management solution built using Django, Python, and MySQL. Whether you're a business owner looking to enhance your customer relationships or a recruiter seeking a standout project, you've come to the right place.

## Features

Our CRM App offers a range of essential features designed to streamline your customer management processes:

- **User Authentication:** Users can easily register, log in, and log out to access their personalized CRM dashboard.

- **Data Management:** With MySQL as the backend database, you can efficiently add, view, update, and delete customer records.

## Getting Started

To get the CRM App up and running locally, follow these simple steps:

1. **Clone the Repository:** Start by cloning this repository to your local machine:

   ```
   git clone https://github.com/your-username/crm-app.git
   ```

2. **Create a Virtual Environment:** Set up a virtual environment to isolate your project's dependencies:

   ```
   python -m venv venv
   ```

3. **Activate the Virtual Environment:** Activate the virtual environment:

   - On Windows:

     ```
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```
     source venv/bin/activate
     ```

4. **Install Dependencies:** Install the required Python packages using pip:

   ```
   pip install -r requirements.txt
   ```

5. **Database Configuration:** Configure the MySQL database settings in the `settings.py` file:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'crm_db',
           'USER': 'your_db_username',
           'PASSWORD': 'your_db_password',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```

6. **Migrate Database:** Apply migrations to set up the database schema:

   ```
   python manage.py migrate
   ```

7. **Create Superuser:** Create a superuser account for accessing the Django admin panel:

   ```
   python manage.py createsuperuser
   ```

8. **Run the Development Server:** Start the development server:

   ```
   python manage.py runserver
   ```

9. **Access the CRM:** Open your web browser and go to `http://localhost:8000` to access the CRM App. Use the superuser credentials you created earlier to log in.

## Usage

Once you've set up the CRM App, you can start managing your customer relationships efficiently. Log in, add customer records, view and update existing records, and delete records when necessary.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions, suggestions, or inquiries, please feel free to contact us:

- Email: [rmessona@gmail.com]
- GitHub: [https://github.com/sushantst]

Thank you for checking out the CRM App project! We hope you find it impressive and valuable.
