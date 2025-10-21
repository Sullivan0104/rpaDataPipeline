from src.fetch_swapi import fetch_data
from src.automation import transform_data
from src.report import generate_report
from src.emailer import send_report

def main():
    print("Starting RPA data pipeline...")

    data = fetch_data("people")
    processed_data = transform_data(data)
    report_path = generate_report(processed_data)
    send_report(report_path)

    print("Pipeline completed successfully.")

if __name__ == "__main__":
    main()

