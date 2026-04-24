# Secure Full-Stack Application - Experiment 9

This experiment demonstrates secure backend with Spring Security, OAuth, RBAC, JPA optimization, and React frontend integration.

## Backend Setup

1. Navigate to `backend` folder.
2. Update `application.properties` with your Google OAuth client ID/secret.
3. Run `mvn spring-boot:run` to start the backend on port 8080.

## Frontend Setup

1. Navigate to `frontend` folder.
2. Run `npm install`.
3. Run `npm run dev` to start the frontend on port 5173.

## Features

- Spring Security with OAuth2 Google Login
- Role-Based Access Control (USER/ADMIN)
- JPA with caching for performance optimization
- CORS enabled for frontend-backend communication
- User management with database persistence

## Performance Optimizations

- Ehcache for second-level caching on user queries
- Indexed database columns
- Optimized JPA queries

## Next Steps

- Test authentication and authorization
- Monitor cache performance
- Add more entities and optimize queries