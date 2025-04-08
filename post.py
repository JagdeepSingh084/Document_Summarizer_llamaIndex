#Creating a post.py file to send the input query from the user to the RAG.py file and pprint the response fetching form the RAG.py file
import requests
import json
from typing import Dict, Any
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# URL for the FastAPI backend API
# Configuration
CONFIG = {
    "api_url": "http://localhost:8000/job_search",
    "sample_queries": [
        "What startups match my skills and experience?",
        "Find me jobs based on my resume",
        "Which startup would be the best fit for me?",
        "bye"
    ]
}

def send_query(query: str) -> Dict[str, Any]:
    """
    Send query to job search API with proper error handling
    
    Args:
        query: The user's search query
        
    Returns:
        Dictionary containing response or error information
    """
    try:
        response = requests.post(
            CONFIG["api_url"],
            json={"query": query},
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"API request failed: {str(e)}")
        return {"error": str(e)}
    except json.JSONDecodeError as e:
        logger.error(f"Failed to decode response: {str(e)}")
        return {"error": "Invalid response from server"}
    


def interactive_session():
    """Run an interactive session with the job search API"""
    print("Startup project Assistant (type 'exit' to quit)")
    print("Some example queries you can try:")
    for i, query in enumerate(CONFIG["sample_queries"], 1):
        print(f"{i}. {query}")
    
    while True:
        try:
            user_input = input("\nYou: ").strip()
            if not user_input:
                continue
                
            if user_input.lower() in ['exit', 'quit', 'q']:
                print("Goodbye!")
                break
                
            # Send query and handle response
            result = send_query(user_input)
            
            if "error" in result:
                print(f"Error: {result['error']}")
            else:
                print(f"\nAssistant: {result.get('response', 'No response received')}")
                
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            logger.error(f"Unexpected error: {str(e)}")
            print("An unexpected error occurred. Please try again.")

if __name__ == "__main__":
    # Run in interactive mode by default
    interactive_session()