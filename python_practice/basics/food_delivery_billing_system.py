"""
Example features:

GST calculation

Coupon: FLAT50, BUY1GET1

Delivery charge based on distance

Tip added
"""

class FoodDeliveryBillingSystem:

    def __init__(self, item_price, distance_km, tip=0, cupon_code=None):
        self.item_price = item_price
        self.distance_km = distance_km
        self.tip = tip
        self.coupon_code = cupon_code
        self.gst_rate = 0.05
        self.delivery_charges = self.calculate_delivery_charge()

    def calculate_delivery_charge(self):
        if self.distance_km <= 5:
            return 20
        elif self.distance_km > 5 and self.distance_km <= 15:
            return 50
        else:
            return 100

    def calculate_bill_without_gst(self):
        total_bill = self.item_price + self.tip + self.delivery_charges
        list_of_cupon_codes = ["FLAT50", "BUY1GET1"]
        if self.coupon_code in list_of_cupon_codes:
            total_bill = total_bill * 0.50
        return total_bill

    def calculate_gst_and_final_bill_price(self):
        total_bill = self.calculate_bill_without_gst()
        gst_amount = total_bill * (self.gst_rate/100)
        final_price = total_bill + gst_amount
        return int(final_price)


food_delivery_bill = FoodDeliveryBillingSystem(item_price=249, distance_km=10, tip=10, cupon_code="FLAT50")
print(food_delivery_bill.calculate_gst_and_final_bill_price())