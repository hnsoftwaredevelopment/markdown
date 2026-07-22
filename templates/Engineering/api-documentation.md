# My Document

Base URL: `https://api.example.com/v1`

## Authentication

All requests require an API key in the header:

```
Authorization: Bearer YOUR_API_KEY
```

---

## Endpoints

### GET `/resource`

Retrieve a list of resources.

**Parameters:**

| Name   | Type   | Required | Description       |
|--------|--------|----------|-------------------|
| limit  | int    | No       | Max results (100) |
| offset | int    | No       | Pagination offset |

**Response:** `200 OK`

```json
{
  "data": [],
  "total": 0
}
```

### POST `/resource`

Create a new resource.

**Body:**

```json
{
  "name": "string",
  "value": "string"
}
```

**Response:** `201 Created`

## Error Codes

| Code | Description          |
|------|----------------------|
| 400  | Bad Request          |
| 401  | Unauthorized         |
| 404  | Not Found            |
| 500  | Internal Server Error|
