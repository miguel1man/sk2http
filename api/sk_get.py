import os
import semantic_kernel as sk
import semantic_kernel.connectors.ai.open_ai as sk_oai
from semantic_kernel.core_plugins import HttpPlugin
from semantic_kernel.planners import ActionPlanner
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
org_id = os.getenv("OPENAI_ORG_ID")


async def sk_process(ask):
    # print(f"\nask processed:\n{ask}\n")
    kernel = sk.Kernel()
    kernel.import_plugin_from_object(HttpPlugin(), "http")

    service_id = "default"
    kernel.add_service(
        sk_oai.OpenAIChatCompletion(
            service_id=service_id,
            ai_model_id="gpt-3.5-turbo-1106",
            api_key=api_key,
            org_id=org_id,
        ),
    )

    planner = ActionPlanner(kernel, service_id)
    plan = await planner.create_plan(goal=ask)
    result = await plan.invoke(kernel)
    print(f"\nresult sk:\n{result}\n")
