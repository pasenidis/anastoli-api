# anastoli-api

Let's see how many schools are closing in Greece due to the pandemic.

## Local Server

```sh
poetry install
poetry run hypercorn run:app
```

## Brief Documentation

### `/schools`

Returns an array (list) with schools in JSON

### `/schools/search/$name`

Searches for the right school and returns the results

### `/health`

Check if the API works, should return the following:

```json
{
  "message": "hi"
}
```
