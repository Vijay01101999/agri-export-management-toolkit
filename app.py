import csv
import io
from datetime import date

import streamlit as st

st.set_page_config(page_title="Agri Export Management Toolkit", page_icon="🌾", layout="wide")

DEFAULT_ITEMS = [
    ("Commercial invoice", "Commercial"),
    ("Packing list", "Commercial"),
    ("Purchase order / sales contract checked", "Commercial"),
    ("Certificate of origin (if required)", "Trade / customs"),
    ("Phytosanitary certificate (if required)", "Plant health"),
    ("Fumigation certificate (if required)", "Plant health"),
    ("Quality / inspection certificate (if required)", "Quality"),
    ("Import permit requirements checked with buyer", "Destination checks"),
    ("HS code and customs requirements verified", "Customs"),
    ("Shipping booking confirmed", "Logistics"),
    ("Insurance arranged (as agreed)", "Logistics"),
    ("Labels and packaging checked against buyer requirements", "Packaging"),
    ("Container / vehicle condition checked", "Logistics"),
    ("Dispatch documents shared with buyer / forwarder", "Dispatch"),
]

st.title("🌾 Agri Export Management Toolkit")
st.caption("A practical shipment checklist for agricultural exporters. Verify all requirements for each product and destination.")

with st.sidebar:
    st.header("Shipment details")
    shipment_ref = st.text_input("Shipment reference", placeholder="e.g. EXP-2026-001")
    product = st.text_input("Product", placeholder="e.g. Fresh onions")
    destination = st.text_input("Destination country", placeholder="e.g. UAE")
    buyer = st.text_input("Buyer / importer")
    planned_dispatch = st.date_input("Planned dispatch date", value=date.today())
    st.info("This checklist is a starting point. It is not a definitive list of mandatory documents.")

st.subheader("Readiness checklist")
st.write("Tick each item only after it has been checked for this specific shipment.")

completed = []
for index, (item, category) in enumerate(DEFAULT_ITEMS):
    done = st.checkbox(f"{item}  ·  {category}", key=f"item_{index}")
    completed.append({"Item": item, "Category": category, "Status": "Complete" if done else "Pending"})

done_count = sum(row["Status"] == "Complete" for row in completed)
total = len(completed)
progress = done_count / total
col1, col2, col3 = st.columns(3)
col1.metric("Completed", f"{done_count}/{total}")
col2.metric("Pending", total - done_count)
col3.metric("Checklist progress", f"{progress:.0%}")
st.progress(progress)

if done_count == total:
    st.success("All checklist items are marked complete. Independently verify that each item is applicable and valid before dispatch.")
else:
    st.warning(f"{total - done_count} item(s) are still pending. Review them before dispatch.")

if st.button("Prepare CSV export"):
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=["Shipment reference", "Product", "Destination", "Buyer", "Planned dispatch", "Item", "Category", "Status"])
    writer.writeheader()
    for row in completed:
        writer.writerow({
            "Shipment reference": shipment_ref,
            "Product": product,
            "Destination": destination,
            "Buyer": buyer,
            "Planned dispatch": planned_dispatch.isoformat(),
            **row,
        })
    st.download_button(
        "Download shipment checklist (CSV)",
        data=output.getvalue().encode("utf-8"),
        file_name=f"{shipment_ref or 'shipment'}_checklist.csv",
        mime="text/csv",
    )

st.divider()
st.caption("Open-source starter project. Contributions, corrections, and destination-specific templates should be reviewed before use.")
