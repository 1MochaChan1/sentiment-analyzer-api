# sentiment-analyzer-api
>[!NOTE]
>API that's used to analyze blog content given a link to the blog or text content using BERT model from HuggingFace (Max limit is 512 token i.e. 2500 characters)

# Sentiment Analysis API

This API checks the sentiment (like positive or negative) of a webpage or some text you provide.


# Setup Guide

## Step 1: Create a Virtual Environment

A virtual environment keeps your project’s dependencies separate from other Python projects on your system.

1. Open your terminal or command prompt.
2. Run the following command to create a virtual environment:

   ```bash
   python -m venv venv
   ```

   This will create a folder named `venv` in your project directory.

## Step 2: Activate the Virtual Environment

Once the virtual environment is created, you need to activate it.

- On Windows:

  ```bash
  venv\Scripts\activate
  ```

- On macOS/Linux:

  ```bash
  source venv/bin/activate
  ```

You’ll know it’s activated if you see `(venv)` at the beginning of your terminal prompt.

## Step 3: Install Requirements

With the virtual environment activated, install the necessary packages.

1. Run the following command to install the packages:

   ```bash
   pip install -r requirements.txt
   ```

This will install the requirement packages and libraries.

---

## How to Use

You can send requests to the following endpoints:

### 1. **Analyze a Link (`/l`)**

**What it Does**: Checks the sentiment of a webpage by its URL.

**How to Use**: Add the `link` to the URL as a query parameter.

**Request Example**:

```http
GET /l?link=https://example.com
```

**Response Example**:

```json
{
  "sentiment": "positive"
}
```

### 2. **Analyze Text Content (`/c`)**

**What it Does**: Checks the sentiment of some text you provide.

**How to Use**: Add the `content` to the URL as a query parameter.

**Request Example**:

```http
GET /c?content=This+is+awesome!
```

**Response Example**:

```json
{
  "sentiment": "positive"
}
```

## Possible Errors

- If you forget to include `link` or `content`, you’ll get an error saying the request is invalid.

---
