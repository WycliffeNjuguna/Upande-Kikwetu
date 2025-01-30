import json
import frappe

@frappe.whitelist()
def create_stock_entry(stock_entry_data):
    stock_entry_data = json.loads(stock_entry_data)

    stock_entry = frappe.new_doc("Stock Entry")

    stock_entry_type = stock_entry_data["stock entry type"]
    variety = stock_entry_data["variety"]
    quantity = stock_entry_data["quantity"]
    breeder = stock_entry_data["breeder"]
    grower = stock_entry_data["grower"]
    location_data = stock_entry_data["location data"]
    
    stock_entry.stock_entry_type = stock_entry_type 

    stock_entry.append("items", {
        "item_code": variety,
        "qty": quantity,
        # Assumption is that the scanned item is a stem
        "custom_number_of_stems": quantity,
        "s_warehouse": location_data["source"],
        "t_warehouse": location_data["target"],
        "custom_breeder": breeder,
        "custom_grower": grower,
    })
    
    stock_entry.insert()
    
    # Submit the stock entry
    # stock_entry.submit()
    
    return stock_entry.name
