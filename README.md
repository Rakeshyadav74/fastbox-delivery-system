# FastBox Delivery System

A logistics delivery simulation system built using Python 3.14.3.

## Features

- JSON file parsing
- Euclidean distance calculation
- Nearest agent assignment
- Delivery simulation
- Report generation
- CSV export support
- Multiple JSON structure support
- Dynamic test case execution

## Folder Structure

```bash
fastbox_delivery_system/
│
├── data/
├── src/
├── output/
├── README.md
├── requirements.txt
└── .gitignore
```

## How to Run

```bash
python src/main.py
```

## Assumptions

1. Nearest agent is selected using Euclidean distance.
2. Tie-breaking uses the first nearest agent found.
3. Agent return journey is not considered.
4. Efficiency is calculated as:

efficiency = total_distance / packages_delivered

## Testing

The system was tested using multiple
custom test cases to validate:

- Multiple warehouse scenarios
- Multiple agent scenarios
- Variable package counts
- Different JSON structures
- Edge case handling

## Technologies Used

- Python 3.14.3
- JSON
- CSV
- Git & GitHub