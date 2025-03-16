import asyncio
import os

from browser_use.agent.service import Agent
from browser_use.agent.views import ActionResult
from browser_use.browser.context import BrowserContext
from browser_use.controller.service import Controller
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import SecretStr, BaseModel

class ProductDetails(BaseModel):
    search_result: str
    product_description: str

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
        I am an Automation Engineer performing automation tasks.
        1. Open https://rahulshettyacademy.com/loginpagePractise/ and maximize the browser window.
        2. Get the username and password from the webpage.
        3. Enter the username and password.
        4. Click on the login button.
        5. Get the search result of the first product.
        6. Get attribute and URL of the page.
        7. Get the product description of the first product.
        """

    api_key = os.environ["GEMINI_API_KEY"]
    llm = ChatGoogleGenerativeAI(model='gemini-2.0-pro-exp-02-05', api_key=SecretStr(api_key))
    agent = Agent(task, llm=llm, controller=controller, use_vision=True)
    history = await agent.run()
    history.save_to_file('result.json')
    test_result = history.final_result()
    print(test_result)

if __name__ == "__main__":
    asyncio.run(test_validation())