# Resume Analyzer AI

## Project Overview

The Resume Analyzer AI is a web application designed to help job seekers optimize their resumes for Applicant Tracking Systems (ATS) and specific job roles. Leveraging the power of Google Gemini AI, this tool provides detailed analysis, assesses resume fit, suggests improvements, and identifies crucial keywords, significantly enhancing a candidate's chances of getting noticed by recruiters.

The project is built with a Django REST Framework backend and a React frontend, offering a modern, responsive, and powerful analysis solution.

## Features

* **Resume Upload:** Supports PDF and DOCX file formats.
* **Job Category & Role Selection:** Choose from predefined categories and specific roles for targeted analysis.
* **Custom Job Description Input:** Paste a specific job description for highly tailored and accurate resume matching.
* **AI-Powered Analysis:**
    * **Overall Fit Score:** A score (0-100) indicating how well the resume matches the target role.
    * **ATS Optimization Score:** A score (0-100) assessing resume scannability and keyword optimization for ATS.
    * **Detailed Assessments:** In-depth analysis of professional profile, skills, experience, and education sections.
    * **Keyword Analysis:** Identifies found and missing critical keywords based on the job description/role.
    * **Actionable Strengths & Improvements:** Specific, actionable feedback to enhance resume content.
    * **Suggested Professional Summary:** AI-generated summary tailored for the target role.
    * **Recommended Courses:** Suggestions for relevant courses to fill skill gaps.
    * **Potential Interview Questions:** AI-generated interview questions based on resume strengths and weaknesses.
* **Tabbed Report View:** Organizes the comprehensive analysis into easy-to-navigate tabs (ATS & Alignment, Profile & Skills, Experience & Education, Suggestions & Q&A).
* **Dark/Light Theme Toggle:** User-friendly interface with switchable themes.
* **Responsive Design:** Ensures usability across various devices.

## Technologies Used

### Backend (Django REST Framework)
* **Python 3.10**
* **Django REST Framework:** For building the RESTful API.
* **Google Generative AI (Gemini API):** For AI-powered resume analysis.
* **`python-decouple`:** For managing environment variables (API keys).
* **`PyPDF2`:** For extracting text from PDF files.
* **`python-docx`:** For extracting text from DOCX files.
* **`Pillow`:** (Often a dependency for other libraries, good to list if installed explicitly).

### Frontend (React)
* **React.js:** JavaScript library for building user interfaces.
* **HTML5, CSS3:** For structuring and styling the web application.
* **JavaScript (ES6+):** For frontend logic and interactivity.

## Setup Instructions

Follow these steps to set up and run the project locally.

### Prerequisites

* Python 3.10+
* Node.js and npm (or Yarn)
* Git

### 1. Clone the Repository

First, clone this repository to your local machine:
git clone [https://github.com/vishakh25/Resume-Analyzer-AI.git](https://github.com/vishakh25/Resume-Analyzer-AI.git)

### 2. Backend Setup

Navigate into the backend directory:

``Bash
cd resume-analyzer-backend``

a. Create a Virtual Environment (Recommended)

``Bash
python -m venv venv``

b. Activate the Virtual Environment
On Windows (Command Prompt):

``Bash
.\venv\Scripts\activate``

On macOS/Linux (or Git Bash/WSL on Windows):

``Bash
source venv/bin/activate``

c. Install Dependencies

``Bash
pip install -r requirements.txt``
Then, ensure this requirements.txt file is committed to your repository

d. Configure Environment Variables
Create a file named .env in the resume-analyzer-backend directory (the same level as manage.py).

Add your Google Gemini API key to this file:

``GOOGLE_API_KEY=your_gemini_api_key_here``

IMPORTANT: Replace your_gemini_api_key_here with your actual API key obtained from Google AI Studio. This .env file should NEVER be committed to Git or pushed to GitHub. It is included in the .gitignore to prevent this. If you accidentally committed it, you must remove it from your Git history and generate a new API key.

e. Run Django Migrations

``Bash
python manage.py migrate``

f. Start the Django Backend Server

``Bash
python manage.py runserver``

The backend server will run on http://127.0.0.1:8000/. Keep this terminal window open.

### 3. Frontend Setup
Open a new terminal/command prompt window and navigate into the frontend directory. First, go back to the project root, then into the frontend:

``Bash
cd .. # Go back to the root project directory (resume-analyzer/)
cd resume-analyzer-frontend``

a. Install Dependencies

``Bash
npm install
 OR (if you use Yarn)
 yarn install``

b. Start the React Development Server

``Bash
npm start
OR (if you use Yarn)
yarn start``

The frontend application will open in your browser, usually at http://localhost:3000/. Keep this terminal window open.

