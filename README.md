# Flask Application with Database Migrations

## Setup Instructions

### 1. Configure Environment Variables
Create a `.env` file in the root directory of your project and add the `DATABASE_URL`:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/your_database_name


---

### Summary of Changes
1. **`flask db init`** initializes the migration folder.
2. **`flask db migrate`** generates migration scripts for schema changes.
3. **`flask db upgrade`** applies migrations to the database.
4. **`flask db current`** shows the current migration version.
5. **`flask db downgrade`** rolls back the last migration.
6. Added instructions for handling schema changes and generating new migrations as needed.

Let me know if you need further modifications! 😊
