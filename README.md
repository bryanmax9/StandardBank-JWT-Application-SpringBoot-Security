<img src="https://i.imgur.com/NLaRKVi.png" alt="MLH-banner" width="100%" height="500px">

# StandardBank-JWT-Application-SpringBoot-Security

🏦Spring Security on Banking API's🏦

# Data Model Used

<img src="https://i.imgur.com/vYZzD4j.png" alt="MLH-banner" width="650%" height="500px">

# Django Personalized Views with Face Authentication

This project integrates a SpringBoot application for face authentication, an AWS Lambda function for image processing, and a Django application for displaying personalized user dashboards.

## Overview

- The **SpringBoot application** prompts users to upload a facial image for authentication.
- The **AWS Lambda function** processes the uploaded image and uses Amazon Rekognition to authenticate the user.
- The **Django application** displays a personalized dashboard with user details and transaction records once the user is authenticated.

## Setup and Installation

### Prerequisites:

- Python (Version x.x.x recommended)
- Django (Version x.x.x recommended)
- Java (Version x.x.x recommended)
- SpringBoot (Version x.x.x recommended)
- AWS CLI and AWS SAM CLI

### Installation Steps:

1. **Django Setup**:
   - Navigate to the Django project directory.
   - Run `pip install -r requirements.txt` to install the necessary dependencies. (Note: Make sure you have a `requirements.txt` file).
   - Run migrations: `python manage.py migrate`
   - Start the server: `python manage.py runserver`

2. **SpringBoot Setup**:
   - Navigate to the SpringBoot directory.
   - Use Maven or Gradle commands to build and run the application, e.g., `./mvnw spring-boot:run`

3. **AWS Lambda**:
   - Deploy your AWS Lambda function using the AWS SAM CLI or via the AWS Console.

### Configuration:
Make sure to update the settings, application properties, and Lambda environment variables with your specific configurations, API keys, and endpoint URLs.

## Usage

1. Access the SpringBoot application and upload your face image for authentication.
2. If authentication is successful, you'll be redirected to the Django dashboard where you can view your details and transactions.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)



## Sources Used

https://spring.io/guides/gs/spring-boot/
https://start.spring.io/
https://jwt.io/introduction
https://docs.spring.io/spring-boot/docs/2.1.7.RELEASE/reference/html/getting-started-installing-spring-boot.html
https://docs.opencv.org/3.4/db/d27/tutorial_py_table_of_contents_feature2d.html
https://aws.amazon.com/lambda/
https://docs.aws.amazon.com/lambda/latest/dg/python-package.html
https://aws.amazon.com/s3/
https://www.teradata.com/
https://blog.hubspot.com/marketing/sql-tutorial-introduction
https://www.w3schools.com/sql/sql_join.asp
https://www.w3schools.com/sql/sql_groupby.asp
https://www.djangoproject.com/
https://docs.djangoproject.com/en/4.0/intro/tutorial01/
https://www.django-rest-framework.org/api-guide/permissions/
