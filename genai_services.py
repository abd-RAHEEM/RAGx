import os
import tiktoken
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("MODEL_API_KEY"),
)

def summarize_text(text):
    """
    Summarize the provided text using OpenAI's GPT model.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes text."},
                {"role": "user", "content": f"Summarize the following text:\n\n{text}"}
            ],
            max_tokens=500
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error occurred during summarization: {e}"

def chunk_text(text, chunk_size=500, chunk_overlap=50):
    """
    Split text into chunks based on token count.
    
    Args:
        text: The text to chunk.
        chunk_size: Maximum size of each chunk in tokens.
        chunk_overlap: Overlap between chunks in tokens.
        
    Returns:
        List of text chunks.
    """
    # Use tiktoken to count tokens (or fallback to splitting by length)
    enc = tiktoken.encoding_for_model("gpt-3.5-turbo")
    tokens = enc.encode(text)
    
    chunks = []
    i = 0
    while i < len(tokens):
        chunk_end = min(i + chunk_size, len(tokens))
        chunks.append(enc.decode(tokens[i:chunk_end]))
        i = chunk_end - chunk_overlap if chunk_end < len(tokens) else chunk_end
        
    return chunks

def answer_with_context(query, context_chunks):
    """
    Answer a user query using the provided context chunks.
    """
    context_text = "\n\n".join(context_chunks)
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant. Use the provided context to answer the user's question."},
                {"role": "user", "content": f"Context:\n{context_text}\n\nQuestion: {query}"}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error occurred during QnA: {e}"
