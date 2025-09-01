import asyncio

from prefect import get_client


async def trigger_flow(name_parameter="therealjohn0279"):
    async with get_client() as client:
        print("Connected to Prefect client")

        # First, verify the deployment exists
        try:
            deployment = await client.read_deployment("6ad8fdfe-389d-44c5-97dd-252ed5f7035f")
            print(f"Found deployment: {deployment.name}")
            print(f"   Flow: {deployment.flow_id}")
            print(f"   Work pool: {deployment.work_pool_name}")
            print(f"   Default parameters: {deployment.parameters}")
        except Exception as e:
            print(f"Error reading deployment: {e}")
            return None

        # Trigger the flow run with custom parameter
        try:
            print("Creating flow run...")
            print(f"Using parameter: name = '{name_parameter}'")

            flow_run = await client.create_flow_run_from_deployment(
                deployment_id="6ad8fdfe-389d-44c5-97dd-252ed5f7035f", parameters={"name": name_parameter}
            )
            print("Flow run created!")
            print(f"   ID: {flow_run.id}")
            print(f"   State: {flow_run.state}")
            print(f"   URL: https://app.prefect.cloud/flow-runs/flow-run/{flow_run.id}")

            return flow_run.id

        except Exception as e:
            print(f"Error creating flow run: {e}")
            return None


# Actually run the function
if __name__ == "__main__":
    print("Starting flow trigger...")

    # You can change the parameter here
    custom_name = "John from API"  # Change this to whatever you want
    flow_run_id = asyncio.run(trigger_flow(custom_name))

    if flow_run_id:
        print(f"\nSuccess! Flow run ID: {flow_run_id}")
        print("Check your Prefect Cloud dashboard to see the run!")
    else:
        print("\nFailed to trigger flow")
