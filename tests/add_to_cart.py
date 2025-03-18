import asyncio
import os

from browser_use.agent.service import Agent
from browser_use.agent.views import ActionResult
from browser_use.browser.context import BrowserContext
from browser_use.controller.service import Controller
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
from pydantic import SecretStr, BaseModel

class ProductDetails(BaseModel):
    product_name: str
    product_price: str
    product_ram_size: str
    product_memory_size: str

controller = Controller(output_model=ProductDetails)

@controller.action('Get attribute and URL of the page')
async def get_attrib_url(browser: BrowserContext):
    page = browser.get_current_page()
    current_url = page.url
    attr = page.get_by_text('Shop Name').get_attribute('class')
    print(current_url)
    return ActionResult(extracted_content=f'Current URL is {current_url} and attr is {attr}')

async def test_validation():
    task = """
        1. Open the browser and go to the website "https://www.amazon.in/"
        2. Search for "iPhone 16"
        3. Get the product with product name "iPhone 16" (strictly match the name)
        4. Get the product details like product name, price, RAM size, and memory size from the product page
        """
    # Using Gemini GenAI
    api_key = os.environ["GEMINI_API_KEY"]
    llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash', api_key=SecretStr(api_key))
    # Using DeepSeek V1
    # api_key = os.environ["DEEPSEEK_API_KEY"]
    # llm = ChatOpenAI(base_url='https://api.deepseek.com/v1', model='deepseek-chat', api_key=SecretStr(api_key))
    # llm = ChatOllama(model='qwen2.5:latest',num_ctx=128000,)
    agent = Agent(task, llm=llm, controller=controller, use_vision=True)
    history = await agent.run()
    history.save_to_file('result.json')
    test_result = history.final_result()
    print(test_result)

if __name__ == "__main__":
    asyncio.run(test_validation())