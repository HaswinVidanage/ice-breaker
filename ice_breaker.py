from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
from third_parties.linkedin import scrape_linkedin_profile


if __name__ == "__main__":
    load_dotenv()
    print("Hello LangChain!")
    print(os.environ['OPENAI_API_KEY'])

    summary_template = """
        given the imformation {information} about a person from I want you to create:
        1. a short summary
        2. two interesting facts about them
    """


    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)

    llm = ChatOpenAI(temperature=0,model_name="gpt-3.5-turbo")

    chain = summary_prompt_template | llm

    linkedin_data = scrape_linkedin_profile(linkedin_profile_url="", mock=True)
    res = chain.invoke(input={"information": linkedin_data})

    print(res)