# Flask App 3 – Simple Form API

This app accepts user-submitted names via form or JSON.

## POST Example

```bash
curl -X POST http://localhost:5000/ -H "Content-Type: application/json" -d '{"name": "Taye"}'

docker build -t flask-app-3 .
docker run --rm -p 5002:5000 --env-file .env flask-app-3
Then open: http://127.0.0.1:5002/



---

## 🧪 Test It Locally

```bash
docker build -t flask-app-3 .
docker run --rm -p 5002:5000 --env-file .env flask-app-3
# Flask App 3 – Simple Name Submission API

This app allows users to submit their name via:
- A basic HTML form (in the browser)
- Or a JSON `POST` request (via `curl`, Postman, etc.)

It returns a personalized greeting as JSON.

---

## 📦 Features

- Accepts POST requests via:
  - HTML form (for user-friendly input)
  - JSON API (for programmatic testing)
- Responds with:
  ```json
  {
    "message": "Hello, Taye! 🎉 You’ve just submitted your name."
  }
