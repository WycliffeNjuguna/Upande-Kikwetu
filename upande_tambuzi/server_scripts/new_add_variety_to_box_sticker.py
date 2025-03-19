import frappe

@frappe.whitelist()
def add_variety_to_sticker(box_label_sticker_name, variety, uom, qty, scan_doc_id):
    box_sticker_doc = frappe.get_doc("Box Label", box_label_sticker_name)
    scan_doc = frappe.get_doc("Scan", scan_doc_id)
    
    quantity = qty
    initPackrate = box_sticker_doc.pack_rate
    packrate = 0

    box_sticker_doc.append("box_item", {
        "variety": variety,
        "uom": uom,
        "qty": quantity
    })

    scan_doc.append("scanned_items", {
        "variety": variety,
        "bunch_size": uom,
        "number_of_bunches": quantity
    })

    uom_conversion_factor = {
        "Bunch (5)": 5,
        "Bunch (6)": 6,
        "Bunch (10)": 10,
        "Bunch (12)": 12,
        "Bunch (25)": 25
    }

    packrate = uom_conversion_factor.get(uom, 0) * int(quantity)

    box_sticker_doc.pack_rate = initPackrate + packrate

    box_sticker_doc.save()


