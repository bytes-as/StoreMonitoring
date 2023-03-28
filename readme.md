# Live Store Monitoring System

The code base initializes the Flask application, sets up logging, creates the database tables, and registers the blueprints for the three API routes. The fetch_report() and generate_report() functions are API endpoint functions that handle GET requests to /get_report/<report_id> and /trigger_report, respectively. The Report, StoreStatus, StoreTimezone, and WorkingHours classes define the database models that are used by the application. The generate_report_task() function is used to generate a report asynchronously using Celery.

Note: Logic for report generation is yet to be implemented yet.