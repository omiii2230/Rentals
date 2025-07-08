import frappe

def execute():
    vehicles = frappe.db.get_all("vehicle1", pluck="name")
    for v in vehicles:
        vehicle1 = frappe.get_doc("vehicle1",v)
        vehicle1.set_title()
        vehicle1.save()
    
    frappe.db.commit()

