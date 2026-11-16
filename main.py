
from ticket_processor import TicketDataProcessor
from ticket_analytics import TicketAnalytics


processor = TicketDataProcessor("tickets.csv")

processor.load_data()

processor.validate_columns()

cleaned_data = processor.clean_data()

print("\nCleaned Dataset:")
print(cleaned_data)

processor.show_report()

cleaned_data.to_csv("cleaned_tickets.csv", index=False)

print("\nCleaned dataset saved successfully!")

analytics = TicketAnalytics(cleaned_data)
report = analytics.analyze()

print("\nTicket Analytics Report:")
print(report)
