class MovieTicket:

    def __init__(self, age, ticket_price, show_time):
        self.age = age
        self.ticket_price = ticket_price
        self.show_time = show_time

    # 50% off for children (5 to 12)
    def children_discount(self):
        if 5 <= self.age <= 12:
            return self.ticket_price * 0.50
        return 0

    # 30% off for seniors (60+)
    def senior_discount(self):
        if self.age >= 60:
            return self.ticket_price * 0.30
        return 0

    # 20% off for special show timings
    def show_time_discount(self):
        discount_timings = ["12:00 PM", "3:00 PM"]
        if self.show_time in discount_timings:
            return self.ticket_price * 0.20
        return 0

    # calculate final price
    def final_ticket_price(self):
        # calculate discounts
        discount_child = self.children_discount()
        discount_senior = self.senior_discount()
        discount_show = self.show_time_discount()

        total_discount = discount_child + discount_senior + discount_show
        final_price = self.ticket_price - total_discount

        # if age between 13 and 59 → no age discount
        if 13 <= self.age <= 59 and discount_show == 0:
            return self.ticket_price  # no discount at all

        return final_price




# Testing
movie_ticket = MovieTicket(age=14, ticket_price=200, show_time="12:00 PM")
print("Final Ticket Price:", movie_ticket.final_ticket_price())
