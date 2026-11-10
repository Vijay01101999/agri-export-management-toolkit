# Agri Export Management Toolkit

A beginner-friendly, open-source toolkit for organising agricultural export shipments.

## Current feature: Shipment Readiness Checker
- Record a shipment and destination market.
- Track common export-document and operational checkpoints.
- Identify pending items before dispatch.
- Download the checklist as a CSV file.

> Important: Requirements vary by product, destination country, buyer, contract, and current regulations. This tool is an organisational aid, not legal, customs, phytosanitary, or regulatory advice. Verify requirements with the relevant authorities and your freight forwarder.

## Run locally

1. Install Python 3.10 or newer.
2. Clone this repository:
   ```bash
   git clone https://github.com/YOUR-USERNAME/agri-export-management-toolkit.git
   cd agri-export-management-toolkit
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the app:
   ```bash
   streamlit run app.py
   ```

## Contributing
Contributions are welcome. Please open an issue before making large changes, describe the problem, and include steps to reproduce bugs.

## Roadmap
- [ ] Product- and destination-specific configurable checklists
- [ ] Shipment cost and margin calculator
- [ ] Supplier and buyer document tracker
- [ ] Multilingual interface
- [ ] Tests and user-contributed templates

## Disclaimer
This project is provided "as is", without warranty. Users are responsible for independently verifying all export requirements.
