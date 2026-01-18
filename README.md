# Todo Full-Stack Web Application - Phase II

This is a complete full-stack Todo application with a Next.js frontend and FastAPI backend, featuring JWT authentication and Neon PostgreSQL database.

## Architecture Overview

- **Frontend**: Next.js 14 with App Router
- **Backend**: FastAPI with SQLModel ORM
- **Database**: Neon Serverless PostgreSQL
- **Authentication**: Better Auth (JWT-based)

## Features

- Create, read, update, and delete todos
- Toggle completion status
- JWT-based authentication and authorization
- User isolation (users can only access their own todos)
- Responsive UI

## Tech Stack

### Frontend
- Next.js 14 (App Router)
- React 18
- TypeScript
- Tailwind CSS

### Backend
- Python 3.13+
- FastAPI
- SQLModel
- Pydantic
- JWT for authentication

### Database
- Neon Serverless PostgreSQL
- SQLModel ORM

## Environment Variables

Create a `.env.local` file in the root directory with the following variables:

```env
NEXT_PUBLIC_API_URL=http://localhost:8000/api
BETTER_AUTH_URL=http://localhost:3000
```

For the backend, create a `.env` file in the `backend` directory:

```env
NEON_DB_URL=postgresql://username:password@ep-xxx.us-east-1.aws.neon.tech/dbname?sslmode=require
BETTER_AUTH_SECRET=your-better-auth-secret-here
BETTER_AUTH_URL=http://localhost:3000
FRONTEND_URL=http://localhost:3000
```

## Setup Instructions

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables in `.env` file

4. Initialize the database:
```bash
python -m backend.database_init
```

5. Start the backend server:
```bash
uvicorn backend.main:app --reload
```

The backend will be available at `http://localhost:8000`

### Frontend Setup

1. Install dependencies:
```bash
npm install
```

2. Set up environment variables in `.env.local` file

3. Start the development server:
```bash
npm run dev
```

The frontend will be available at `http://localhost:3000`

## API Endpoints

All API endpoints require a valid JWT token in the Authorization header.

### GET `/api/{user_id}/tasks`
Get all tasks belonging to the authenticated user

### POST `/api/{user_id}/tasks`
Create a new task for the authenticated user

### GET `/api/{user_id}/tasks/{task_id}`
Get a specific task by ID

### PUT `/api/{user_id}/tasks/{task_id}`
Update a specific task

### PATCH `/api/{user_id}/tasks/{task_id}/complete`
Toggle the completion status of a task

### DELETE `/api/{user_id}/tasks/{task_id}`
Delete a specific task

## Authentication

The application uses JWT tokens issued by Better Auth. The backend verifies these tokens using the shared secret.

## Database Schema

### Todo Table
- `id`: UUID (Primary Key)
- `title`: String (Non-empty)
- `completed`: Boolean (Default: false)
- `user_id`: String (Indexed, Foreign-key-like behavior)
- `created_at`: Timestamp

## Development

### Running Tests

Backend tests:
```bash
python -m pytest backend/
```

### Project Structure

```
backend/
├── auth/                 # JWT authentication
├── config/              # Configuration and database setup
├── models/              # Database models
├── repositories/        # Database operations
├── routes/              # API endpoints
├── services/            # Business logic
├── main.py              # FastAPI application
├── database_init.py     # Database initialization
└── requirements.txt     # Dependencies
```

## Deployment

### Backend Deployment
- Deploy to a cloud platform that supports Python (Heroku, Railway, etc.)
- Ensure environment variables are set in deployment environment
- Run database migrations on deploy

### Frontend Deployment
- Deploy to Vercel, Netlify, or similar platform
- Set environment variables in deployment environment

## Security Considerations

- JWT tokens are validated using a shared secret
- Users can only access their own todos
- Input validation is performed at the service layer
- SQL injection is prevented by using SQLModel ORM

## Troubleshooting

1. **Backend won't start**: Ensure all environment variables are set correctly
2. **Database connection fails**: Verify NEON_DB_URL is correct
3. **Authentication fails**: Check that BETTER_AUTH_SECRET matches between frontend and backend
4. **CORS errors**: Ensure FRONTEND_URL is set correctly in backend environment

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request