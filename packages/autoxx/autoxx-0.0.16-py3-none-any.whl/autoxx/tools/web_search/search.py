from typing import Dict, List, Optional
import json
from pathlib import Path
from autogpt.config import Config

from autogpt.commands.web_selenium import scrape_text_with_selenium
from selenium.webdriver.remote.webdriver import WebDriver
from autogpt.commands.google_search import google_search, google_official_search
from autogpt import token_counter
from autogpt.llm_utils import create_chat_completion
from autogpt.processing.text import split_text

FILE_DIR = Path(__file__).parent
CFG = Config()

def create_message(chunk: str, question: str) -> Dict[str, str]:
    """Create a message for the chat completion

    Args:
        chunk (str): The chunk of text to summarize
        question (str): The question to answer

    Returns:
        Dict[str, str]: The message to send to the chat completion
    """
    return {
        "role": "user",
        "content": f'"""{chunk}""" Analyze the above text and extract all information in detail relevant to '
        f'question: "{question}" -- if there is no relevant information, summarize the text in detail.'
    }
    

def scroll_to_percentage(driver: WebDriver, ratio: float) -> None:
    """Scroll to a percentage of the page

    Args:
        driver (WebDriver): The webdriver to use
        ratio (float): The percentage to scroll to

    Raises:
        ValueError: If the ratio is not between 0 and 1
    """
    if ratio < 0 or ratio > 1:
        raise ValueError("Percentage should be between 0 and 1")
    driver.execute_script(f"window.scrollTo(0, document.body.scrollHeight * {ratio});")

def summarize_chunks(text:str, question: str, url: str, driver: Optional[WebDriver] = None) -> List[str]:
    """Summarize a list of chunks

    Args:
        chunks (list[str]): The chunks to summarize
        question (str): The question to answer

    Returns:
        str: The summary of the chunks
    """
    model = CFG.fast_llm_model
    text_length = len(text)
    print(f"Text length: {text_length} characters")

    chunks = list(
        split_text(text=text, max_length=CFG.browse_chunk_max_length, question=question)
    )
    summaries = []

    scroll_ratio = 1 / len(chunks)
    for i, chunk in enumerate(chunks):
        if driver:
            scroll_to_percentage(driver, scroll_ratio * i)

        messages = [create_message(chunk, question)]
        tokens_for_chunk = token_counter.count_message_tokens(messages, model)
        print(
            f"Summarizing {url} chunk {i + 1} / {len(chunks)} of length {len(chunk)} characters, or {tokens_for_chunk} tokens"
        )

        summary = create_chat_completion(
            model=CFG.fast_llm_model,
            messages=messages,
        )
        summaries.append(summary)

    return summaries

def add_header(driver: WebDriver) -> None:
    """Add a header to the website

    Args:
        driver (WebDriver): The webdriver to use to add the header

    Returns:
        None
    """
    try:
        with open(f"{FILE_DIR}/js/overlay.js", "r") as overlay_file:
            overlay_script = overlay_file.read()
        driver.execute_script(overlay_script)
    except Exception as e:
        print(f"Error executing overlay.js: {e}")

def close_browser(driver: WebDriver) -> None:
    """Close the browser

    Args:
        driver (WebDriver): The webdriver to close

    Returns:
        None
    """
    driver.quit()


def browse_website(url: str, question: str) -> str:
    """Browse a website and summarize it

    Args:
        url (str): The url to browse
        question (str): The question to answer

    Returns:
        str: The summary of the website
    """
    driver, text = scrape_text_with_selenium(url=url)
    add_header(driver)
    summaries = summarize_chunks(text=text, question=question, url=url, driver=driver)
    close_browser(driver)
    return '\n'.join(summaries)

def web_search(question:str, search_num:Optional[int]=2) -> List[Dict]:
    search_result = google_search(query=question, num_results=search_num)
    search_search_json = json.loads(search_result)
    search_summaries = []

    if isinstance(search_search_json, list):
        for res in search_search_json:
            print(f"{res['title']} x {res['href']}\n")
            summary = browse_website(url=res['href'], question=question)

            search_summaries.append({
                "relevant_content": summary,
                "title": res['title'],
                "url": res['href']
            })

            print(f"{res['title']} x {res['href']} summary: {summary}\n")
    else:
        print(f"{search_search_json['title']} x {search_search_json['href']}")
        summary = browse_website(url=search_search_json['href'], question=question)
        search_summaries.append({
            "content": summary,
            "title": res['title'],
            "url": res['href']
        })
        print(f"{search_search_json['title']} x {search_search_json['href']} summary: {summary}\n")

    return search_summaries