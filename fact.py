import os
import asyncio
import semantic_kernel as sk
from dotenv import load_dotenv
import semantic_kernel.connectors.ai.open_ai as sk_oai
from semantic_kernel.planners.basic_planner import BasicPlanner

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
org_id = os.getenv("OPENAI_ORG_ID")


async def main():

    kernel = sk.Kernel()
    service_id = "default"
    kernel.add_service(
        sk_oai.OpenAIChatCompletion(
            service_id=service_id,
            ai_model_id="gpt-3.5-turbo-1106",
            api_key=api_key,
            org_id=org_id,
        ),
    )

    plugins_directory = "custom_plugins"
    kernel.import_plugin_from_prompt_directory(plugins_directory, "Organizer_Plugin")
    planner = BasicPlanner(service_id)
    ask = "Quiero agregar un producto a la lista."

    new_plan = await planner.create_plan(goal=ask, kernel=kernel)
    print(f"generated_plan:\n{new_plan.generated_plan}")
    results = await planner.execute_plan(new_plan, kernel)
    print(f"results:\n{results}")


asyncio.run(main())
