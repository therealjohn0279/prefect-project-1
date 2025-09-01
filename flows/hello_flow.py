from prefect import flow, get_run_logger, task


@task(log_prints=True)
def say_hello(name: str) -> str:
    logger = get_run_logger()
    logger.info(f"Hello, {name}!")
    print(f"Hello, {name}!")
    return f"Greeted {name}"


@task(log_prints=True)
def say_goodbye(name: str) -> str:
    logger = get_run_logger()
    logger.info(f"Goodbye, {name}!")
    print(f"Goodbye, {name}!")
    return f"Said goodbye to {name}"


@flow(name="hello-world-flow", log_prints=True)
def hello_world_flow(name: str = "World"):
    """A simple hello world flow"""
    logger = get_run_logger()
    logger.info(f"Flow started with name: {name}")

    hello_result = say_hello(name)
    goodbye_result = say_goodbye(name)

    return {"hello": hello_result, "goodbye": goodbye_result}


if __name__ == "__main__":
    hello_world_flow("Prefect")
