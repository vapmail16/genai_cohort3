# GenAI Cohort 3 Projects

This repository contains projects developed during the GenAI Cohort 3 program.

## Projects

### 1. Login System (`/login/`)
A complete authentication system with React frontend and Node.js backend.

**Features:**
- User registration and login
- JWT token authentication
- PostgreSQL database
- Protected routes
- Profile management
- Responsive design

**Tech Stack:**
- Frontend: React, React Router, Formik, Axios
- Backend: Node.js, Express, PostgreSQL, JWT
- Database: PostgreSQL with migrations

**Quick Start:**
```bash
# Backend
cd login/backend
npm install
npm run migrate
npm run dev

# Frontend
cd login/frontend
npm install
npm start
```

### 2. Project Scaffolding (`/scaffolding/`)
Basic project scaffolding for web applications with separated frontend and backend services.

**Structure:**
- Frontend folder with React setup
- Backend folder with Node.js/Express setup
- Shared configuration files
- Docker setup
- GitHub workflows

## Getting Started

1. Clone the repository:
```bash
git clone https://github.com/vapmail16/genai_cohort3.git
cd genai_cohort3
```

2. Navigate to the project you want to work with
3. Follow the specific setup instructions in each project's README

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License.
