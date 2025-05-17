Here’s an updated and refined version of your README that includes the details about the SQL database integration and the login flow you described:

---

# AMES Demo Website

This is a simple demo website created as part of the AMES Club recruitment assignment. It showcases a minimal login system and an events page — with a **FastAPI backend** and a **basic HTML/CSS/JavaScript frontend**.

---

## 🧠 Focus Areas

* The main focus of this project is **backend development**.
* I implemented **API routes using FastAPI** for:

  * User login functionality.
  * Displaying the current server time.
* I used a **SQL database** (from a larger personal FastAPI project I’m developing) and integrated it here for user authentication.
* The backend handles user validation and redirects users to the events page upon successful login.

---

## 🔐 Example Login

* **User ID:** `xyz1@gmail.com`
* **Password:** `abcd`
* Logging in with these credentials will grant access to the events page showing upcoming activities.

---

## 💻 Frontend

* The frontend includes:

  * A simple **login page**.
  * An **events page** that displays a list of upcoming events.
* Built with **HTML, CSS, and JavaScript**.
* I intentionally kept the frontend clean and minimal. Since I’m still learning, I used **AI tools (like ChatGPT)** for guidance and support.

---

## ⚙️ Tech Stack

* **Backend:** FastAPI (Python)
* **Database:** SQL (via a shared DB setup from my other FastAPI projects)
* **Frontend:** HTML, CSS, JavaScript
* **Version Control:** Git + GitHub

---

## 🚀 How to Run (Locally)

1. Clone the repo.
2. Run the FastAPI backend (e.g., using `uvicorn main:app --reload`).
3. Open the `ames.html` file in your browser to access the frontend.

---

## 🔒 Security Note

* Sensitive files (e.g., database configuration and credentials) are excluded using `.gitignore`.
* Only example credentials are shown; real users and passwords are stored securely in the SQL backend.

---

