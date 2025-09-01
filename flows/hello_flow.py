from prefect import flow, task


@task
def say_hello(name: str) -> str:
    print(f"Hello, {name}!")
    return f"Greeted {name}"


@task
def say_goodbye(name: str) -> str:
    print(f"Goodbye, {name}!")
    return f"Said goodbye to {name}"


@flow(name="hello-world-flow")
def hello_world_flow(name: str = "World"):
    """A simple hello world flow"""
    hello_result = say_hello(name)
    goodbye_result = say_goodbye(name)
    return {"hello": hello_result, "goodbye": goodbye_result}


if __name__ == "__main__":
    # Run the flow locally for testing
    hello_world_flow("Prefect")
