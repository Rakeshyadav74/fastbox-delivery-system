import json
import csv
import os


class ReportService:

    OUTPUT_FOLDER = "output"

    @staticmethod
    def generate_report(agent_report):

        best_agent = None
        best_efficiency = float("inf")

        for agent_id, details in agent_report.items():

            delivered = details[
                "packages_delivered"
            ]

            total_distance = round(
                details["total_distance"],
                2
            )

            efficiency = (
                round(
                    total_distance / delivered,
                    2
                )
                if delivered > 0
                else 0
            )

            details["total_distance"] = (
                total_distance
            )

            details["efficiency"] = (
                efficiency
            )

            if (
                delivered > 0 and
                efficiency < best_efficiency
            ):

                best_efficiency = efficiency
                best_agent = agent_id

        agent_report["best_agent"] = best_agent

        return agent_report

    @classmethod
    def save_report(
        cls,
        report_data
    ):

        os.makedirs(
            cls.OUTPUT_FOLDER,
            exist_ok=True
        )

        report_path = (
            f"{cls.OUTPUT_FOLDER}/report.json"
        )

        with open(report_path, "w") as file:

            json.dump(
                report_data,
                file,
                indent=4
            )

        print(
            f"[INFO] Report saved: "
            f"{report_path}"
        )

    @classmethod
    def export_top_performer_csv(
        cls,
        report_data
    ):

        best_agent = report_data[
            "best_agent"
        ]

        csv_path = (
            f"{cls.OUTPUT_FOLDER}/"
            f"top_performer.csv"
        )

        with open(
            csv_path,
            "w",
            newline=""
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                "Agent ID",
                "Packages Delivered",
                "Total Distance",
                "Efficiency"
            ])

            writer.writerow([
                best_agent,
                report_data[best_agent][
                    "packages_delivered"
                ],
                report_data[best_agent][
                    "total_distance"
                ],
                report_data[best_agent][
                    "efficiency"
                ]
            ])

        print(
            f"[INFO] CSV exported: "
            f"{csv_path}"
        )