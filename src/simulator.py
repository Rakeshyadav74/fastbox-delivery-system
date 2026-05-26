import random

from utils import (
    calculate_distance,
    normalize_warehouses,
    normalize_agents
)


class DeliverySimulator:

    def __init__(self, data):

        self.warehouses = normalize_warehouses(
            data["warehouses"]
        )

        self.agents = normalize_agents(
            data["agents"]
        )

        self.packages = data["packages"]

        self.agent_report = {
            agent_id: {
                "packages_delivered": 0,
                "total_distance": 0.0
            }
            for agent_id in self.agents
        }

    def find_nearest_agent(
        self,
        warehouse_location
    ):
        """
        Find nearest available agent.
        """

        nearest_agent = min(
            self.agents,
            key=lambda agent_id:
            calculate_distance(
                self.agents[agent_id],
                warehouse_location
            )
        )

        return nearest_agent

    def simulate_deliveries(self):
        """
        Run delivery simulation.
        """

        for package in self.packages:

            package_id = package["id"]

            warehouse_id = package.get(
                "warehouse",
                package.get("warehouse_id")
            )

            destination = package["destination"]

            if warehouse_id not in self.warehouses:

                print(
                    f"[WARNING] Invalid warehouse "
                    f"for package {package_id}"
                )

                continue

            warehouse_location = self.warehouses[
                warehouse_id
            ]

            nearest_agent = self.find_nearest_agent(
                warehouse_location
            )

            agent_location = self.agents[
                nearest_agent
            ]

            pickup_distance = calculate_distance(
                agent_location,
                warehouse_location
            )

            delivery_distance = calculate_distance(
                warehouse_location,
                destination
            )

            total_distance = (
                pickup_distance +
                delivery_distance
            )

            # Random delivery delay bonus feature
            delay = random.randint(1, 5)

            self.agent_report[nearest_agent][
                "packages_delivered"
            ] += 1

            self.agent_report[nearest_agent][
                "total_distance"
            ] += total_distance

            print(
                f"[INFO] "
                f"Package {package_id} "
                f"assigned to {nearest_agent}"
            )

            print(
                f"[INFO] Delivery delayed "
                f"by {delay} minutes."
            )

            print(
                f"Route: "
                f"{nearest_agent} -> "
                f"{warehouse_id} -> "
                f"{destination}"
            )

        return self.agent_report