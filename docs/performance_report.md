# Performance Analysis Report

The performance of the FastAPI backend for the “A Dying Planet” project was evaluated by measuring response times for key API endpoints, including data retrieval and insertion. Testing was conducted locally using the built-in FastAPI server and Python tools to simulate requests.

The GET `/data` endpoint was tested to retrieve all climate records stored in the SQLite database. On average, the response time was under 50 milliseconds when returning several hundred records. Filtering operations, such as querying by country or year (e.g., `/data?country=United States`), showed slightly improved performance due to reduced dataset size, with response times averaging around 20–30 milliseconds.

The POST `/data` endpoint, used for inserting new records, consistently completed in under 30 milliseconds. This demonstrates efficient write performance within the SQLite database for the scale of this application.

Performance optimization techniques were applied to ensure responsiveness. An index was created on the `country` and `year` columns within the SQLite database to improve query efficiency, especially for filtered searches. Additionally, queries were structured dynamically to avoid unnecessary conditions, reducing overhead.

Although the application is currently operating on a moderate dataset size, the use of indexing ensures scalability as the dataset grows. Future improvements could include caching frequently requested queries and deploying the API to a cloud environment for further performance benchmarking.

Overall, the FastAPI backend demonstrates efficient performance, with low response times across all tested endpoints and effective optimization strategies in place to support future scalability.