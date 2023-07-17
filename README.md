# Book Querying Project

The Book Querying Project is an querying system that allows users to ask questions related to a given book, and it responds with accurate and naturally sounding answers. This intelligent querying capability is achieved through prompt engineering using the Langchain library.

## Key Features

- **Prompt Engineering**: The project leverages the power of prompt engineering techniques to formulate effective queries and obtain relevant answers from the text data.

- **Vectorization with OpenAI's Embedding**: The document contents are vectorized using OpenAI's embedding, a technique that converts the text data into high-dimensional vectors with 1536 dimensions. This helps in capturing intricate semantic relationships between words and sentences.

- **Chroma DB for Similarity Search**: The vectorized documents are stored in a Chroma DB, enabling efficient similarity searches. This allows the system to find the most relevant documents related to a user's query quickly.

- **Natural Language Response with OpenAI's Davinci Model**: To generate natural and human-like responses, the project employs OpenAI's powerful language model, Davinci. The top-k similar documents retrieved from the Chroma DB are fed into the Davinci model to produce more contextually appropriate responses.

- ** API with FastAPI**: The book submission and querying response are handled through API built using FastAPI. This allows for easy integration with other applications and services, making the querying process seamless and accessible from various platforms.

## How it Works

1. The Book Querying Project reads the input book or a collection of books.

2. The content of the books is vectorized into high-dimensional representations using OpenAI's embedding.

3. These vectorized representations are stored in a Chroma DB, which enables fast and efficient similarity searches.

4. When a user submits a query, the system performs a similarity search in the Chroma DB to find the most relevant documents.

5. The top-k similar documents are then passed to OpenAI's Davinci model, which generates natural and coherent responses to the user's queries.

## Getting Started

To get started with the Book Querying Project, follow these steps:

1. Clone the repository to your local machine.

2. Install the required dependencies specified in the `requirements.txt` file.

3. Prepare your book data or use the provided example data.

4. Run the project, and you are ready to start querying the books using the provided FastAPI-based API.

## Contributing

If you have any questions or feedback, please don't hesitate to open an issue or reach out to me. Feel free to submit bug reports, feature requests, or pull requests.
