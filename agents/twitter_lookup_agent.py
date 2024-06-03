
from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.tools import Tool
from langchain.agents import (
    create_react_agent,
    AgentExecutor,
)
from langchain import hub
import sys

import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tools.tools import get_profile_url_tavily

load_dotenv()

def lookup(name: str) -> str:
    llm = ChatOpenAI(
        temperature=0,
        model_name ="gpt-3.5-turbo",
    )

    template = """given the name {name_of_person} I want you to find a link to their Twitter profile page, and extract from their twitter handle from it. Your final answer should only contain the person's username"""

    prompt_template = PromptTemplate(
        template=template,
        input_variables=["name_of_person"]
    )

    tools_for_agent = [
        Tool(
            name="Crawl Google 4 Twitter profile page",
            func=get_profile_url_tavily,
            description="Useful for when you need to get the Twitter Page URL"
        )
    ]

    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt) 
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True) # runtime of the agent

    result = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(name_of_person=name)}

    )

    twitter_profile_url = result["output"]
    return twitter_profile_url

if __name__ == "__main__":
    twitter_url = lookup(name="Elon Musk")
    print(twitter_url)