# Fast API Fundamentals

A small collection of practice API endpoints built with **FastAPI** (the file is named for the original Flask exercise it grew out of, but the code itself imports and runs on FastAPI).

## Requirements

- Python 3.8+
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/) (ASGI server)

Install dependencies:

```bash
pip install fastapi uvicorn
```

## Running

```bash
uvicorn fastAPIFundamentals:app --reload
```

The API will be available at `http://127.0.0.1:8000`, with interactive docs at `http://127.0.0.1:8000/docs`.

## Endpoints

| Method | Path | Description |
|---|---|---|
| GET | `/` | Welcome message |
| GET | `/student` | Returns a sample student record |
| GET | `/course` | Returns sample course details |
| GET | `/skills` | Returns a list of sample skills |
| GET | `/addition?a=&b=` | Adds two integers |
| GET | `/multipy?a=&b=` | Multiplies two integers |
| GET | `/square?n=` | Squares an integer |
| GET | `/check_even_odd?n=` | Checks whether a number is even or odd |
| GET | `/table?n=` | Returns the multiplication table (1–10) for `n` |
| GET | `/profile/{name}/{age}` | Returns a profile built from path parameters |
| GET | `/number/{num}` | Returns even/odd info, plus square and cube for odd numbers |

## License

Personal practice project — no license specified.
