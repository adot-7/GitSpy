# GitSpy

![Logo](https://cdn-icons-png.freepik.com/512/16104/16104848.png) <!-- Optional: Add your project's logo -->

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup](#setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

GitSpy is a web application that leverages the GitHub API to provide insights into users' repositories. It allows users to view their top repositories, profile information, and contributions.
Developed with Django, GitSpy aims to enhance the way users interact with their GitHub profiles by offering a centralized dashboard.

## Features

- **User Profile**: Displays user avatar, name, and join date.
- **Top Repositories**: Lists the user's top 5 repositories with details such as last updated date and description.
- **Responsive Design**: Fully responsive UI that works well on both desktop and mobile devices.
- **Dynamic Data**: Fetches real-time data from the GitHub API.

## Technologies Used

- **Frontend**: HTML, CSS, Bootstrap
- **Backend**: Django (Python)
- **Hosting**: Vercel
- **APIs**: GitHub REST API

## Setup

To set up GitSpy locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/gitspy.git
2. Navigate to the project directory:
   ```bash
   cd gitspy
3. Create a virtual environment and activate it:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
4. Install the required packages:
   ```bash
   pip install -r requirements.txt
5. Set up your database and update the settings in **settings.py** with your database configuration.
6. Run migrations:
   ```bash
   python manage.py migrate
7. Start the development server:
   ```bash
   python manage.py runserver
8. Access the application in your browser at **http://127.0.0.1:8000/**.

## Usage
1. Visit the application in your browser.
2. Enter the GitHub username to view the profile and repositories.
3. Navigate through the dashboard to explore user data and repository insights.
