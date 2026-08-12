# My Document

**Database:** Database Name
**Engine:** PostgreSQL / MySQL / SQLite
**Last Updated:** YYYY-MM-DD

---

## Entity Relationship Diagram

```mermaid
erDiagram
    USERS ||--o{ POSTS : writes
    USERS ||--o{ COMMENTS : authors
    POSTS ||--o{ COMMENTS : has
    POSTS ||--o{ TAGS : tagged
    USERS {
        int id PK
        string email
        string name
        timestamp created_at
    }
    POSTS {
        int id PK
        int user_id FK
        string title
        text content
        timestamp published_at
    }
    COMMENTS {
        int id PK
        int post_id FK
        int user_id FK
        text body
        timestamp created_at
    }
    TAGS {
        int id PK
        string name
    }
```

## Tables

### users

| Column     | Type       | Nullable | Default | Notes        |
|------------|------------|----------|---------|--------------|
| id         | INT        | NO       | AUTO    | Primary key  |
| email      | VARCHAR    | NO       |         | Unique index |
| name       | VARCHAR    | YES      |         |              |
| created_at | TIMESTAMP  | NO       | NOW()   |              |

## Indexes

| Table | Index Name       | Columns | Type   |
|-------|------------------|---------|--------|
| users | idx_users_email  | email   | UNIQUE |
| posts | idx_posts_user   | user_id | BTREE  |

## Migration Notes

- [ ] Create tables
- [ ] Add indexes
- [ ] Seed initial data
- [ ] Backfill existing records
