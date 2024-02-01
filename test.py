# class RestaurantBill:
#     def _init_(self, table_no):
#         self.table_no = table_no
#         self.items = []

#     def add_item_to_bill(self, item_name, quantity, price_per_unit):
#         item_total = quantity * price_per_unit
#         self.items.append({"item_name": item_name, "quantity": quantity, "price_per_unit": price_per_unit, "item_total": item_total})

#     def calculate_total_bill(self):
#         total_bill = sum(item["item_total"] for item in self.items)
#         return total_bill

#     def apply_discount(self, discount_percentage):
#         total_bill = self.calculate_total_bill()
#         discount_amount = (discount_percentage / 100) * total_bill
#         discounted_total = total_bill - discount_amount
#         return discounted_total

#     def display_itemized_bill(self):
#         print(f"Itemized Bill for Table {self.table_no}:")
#         for item in self.items:
#             print(f"{item['item_name']} - {item['quantity']} x {item['price_per_unit']} = {item['item_total']}")
#         print("------------------------------")

# # Interactive usage:
# table_no = int(input("Enter table number: "))
# restaurant_bill = RestaurantBill(table_no)

# while True:
#     item_name = input("Enter item name (or 'done' to finish adding items): ")
#     if item_name.lower() == 'done':
#         break

#     quantity = int(input("Enter quantity: "))
#     price_per_unit = float(input("Enter price per unit: "))

#     restaurant_bill.add_item_to_bill(item_name, quantity, price_per_unit)

# discount_percentage = float(input("Enter discount percentage (0 for no discount): "))
# discounted_amount = restaurant_bill.apply_discount(discount_percentage)

# restaurant_bill.display_itemized_bill()
# print(f"Total Bill Amount: ₹{restaurant_bill.calculate_total_bill():.2f}")

# if discount_percentage > 0:
#     print(f"After {discount_percentage}% Discount: ₹{discounted_amount:.2f}")