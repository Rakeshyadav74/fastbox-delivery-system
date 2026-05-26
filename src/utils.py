import json
import math
import os


def load_json_file(file_path):
    """
    Load and validate JSON file.
    """

    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"File not found: {file_path}"
        )

    with open(file_path, "r") as file:
        data = json.load(file)

    validate_input_data(data)

    return data


def validate_input_data(data):
    """
    Validate required keys.
    """

    required_keys = [
        "warehouses",
        "agents",
        "packages"
    ]

    for key in required_keys:

        if key not in data:
            raise ValueError(
                f"Missing key: {key}"
            )


def calculate_distance(point1, point2):
    """
    Calculate Euclidean distance.
    """

    x1, y1 = point1
    x2, y2 = point2

    return round(
        math.hypot(x2 - x1, y2 - y1),
        2
    )


def normalize_warehouses(warehouses):
    """
    Support both warehouse formats.
    """

    if isinstance(warehouses, dict):
        return warehouses

    return {
        warehouse["id"]: warehouse["location"]
        for warehouse in warehouses
    }


def normalize_agents(agents):
    """
    Support both agent formats.
    """

    if isinstance(agents, dict):
        return agents

    return {
        agent["id"]: agent["location"]
        for agent in agents
    }