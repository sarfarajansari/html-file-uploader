

# HTML File Uploader

This repository contains a Django-based application that allows users to upload HTML files. Each uploaded file results in its own individual website, which can be accessed via a unique URL. The app simplifies the process of quickly viewing and sharing HTML files hosted on a Django backend.

## Features

- **HTML File Upload**: Users can upload their HTML files through an intuitive interface.
- **Unique URL for Each File**: After a file is uploaded, a unique URL is generated for the file, allowing users to access the file as a standalone website.
- **Django Backend**: The app is built using Django, leveraging its powerful backend capabilities to manage file uploads and URL routing.
- **Simple UI**: A clean, user-friendly frontend allows for easy file uploads and browsing of uploaded HTML files.

## Technologies Used

- **Django**: The web framework used to handle the backend, manage file uploads, and generate unique URLs.
- **HTML/CSS**: Used for rendering the frontend interface and serving the uploaded HTML content.
- **SQLite**: The default database used by Django to store information about the uploaded files.

## How It Works

1. **Upload HTML File**: Users visit the application and upload their HTML files via the web interface.
2. **File Processing**: Once a file is uploaded, the server stores the file and generates a unique URL based on the file’s identifier.
3. **Access the File**: The user can visit the generated URL to view the uploaded HTML file as a separate website.
4. **Standalone Websites**: Each uploaded HTML file is displayed on its own page, providing a quick way to share and access static HTML content.

