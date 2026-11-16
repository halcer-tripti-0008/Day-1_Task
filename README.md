# AI Support Ticket Data Pipeline

## Project Overview
This project processes support ticket data using Python and Pandas. It loads, validates, cleans, and analyses support ticket datasets.

## Project Structure
- `tickets.csv` – Original support ticket dataset.
- `cleaned_tickets.csv` – Cleaned dataset.
- `ticket_processor.py` – Handles loading, validation, and cleaning.
- `ticket_analytics.py` – Performs ticket analytics.
- `main.py` – Runs the complete pipeline.
- `main.ipynb` – Notebook for experimentation.

## Technologies Used
- Python
- Pandas
- NumPy
- Git and GitHub
- Pytest (for automated testing)

## Features
1. CSV data loading.
2. Required column validation.
3. Duplicate ticket identification.
4. Missing and invalid value handling.
5. Data cleaning.
6. Ticket analytics:
   - Tickets by priority.
   - Average resolution time by category.
   - Average customer rating.
   - Unresolved ticket count.
   - Missing values and invalid records.

## How to Run

Install dependencies:

```bash
pip3 install pandas numpy pytest
```

Run the project:

```bash
python3 main.py
```

## Testing

Run automated tests using:

```bash
python3 -m pytest -v
```

## Data Cleaning Rules
The processor handles missing values, invalid numeric values, and duplicate ticket IDs according to the implemented cleaning rules. The original CSV is preserved.

## Project Status
Day 1 – Python Engineering and Ticket Data Pipeline.
