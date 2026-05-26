from utils import load_json_file

from simulator import (
    DeliverySimulator
)

from report_service import (
    ReportService
)


def validate_delivery_count(
    simulation_result,
    total_packages
):
    """
    Validate total delivered packages.
    """

    delivered_count = sum(
        details["packages_delivered"]
        for details in simulation_result.values()
    )

    print(
        f"\nValidation: "
        f"{delivered_count}/"
        f"{total_packages} "
        f"packages delivered"
    )


def main():

    print(
        "\n========== "
        "FASTBOX DELIVERY SYSTEM "
        "==========\n"
    )

    file_name = input(
        "Enter JSON file name: "
    )

    file_path = f"data/{file_name}"

    data = load_json_file(file_path)

    simulator = DeliverySimulator(data)

    simulation_result = (
        simulator.simulate_deliveries()
    )

    validate_delivery_count(
        simulation_result,
        len(data["packages"])
    )

    final_report = (
        ReportService.generate_report(
            simulation_result
        )
    )

    ReportService.save_report(
        final_report
    )

    ReportService.export_top_performer_csv(
        final_report
    )

    print(
        "\n========== "
        "FINAL REPORT "
        "==========\n"
    )

    for agent, details in final_report.items():

        print(f"{agent}: {details}")


if __name__ == "__main__":

    try:
        main()

    except Exception as error:

        print(f"\n[ERROR] {error}")