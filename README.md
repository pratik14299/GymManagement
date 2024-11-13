# GymManagement

Members Endpoints
Get list of members (default format)

GET /api/members/
Get list of members (specific format)

GET /api/members.json
GET /api/members.xml
Export members to Excel (default format)

GET /api/members/export_to_excel/
Export members to Excel (specific format)

GET /api/members/export_to_excel.json
GET /api/members/export_to_excel.xml
Get list of pending payments (default format)

GET /api/members/pending_payments/
Get list of pending payments (specific format)

GET /api/members/pending_payments.json
GET /api/members/pending_payments.xml
Get details of a specific member by ID (default format)

GET /api/members/123/
Get details of a specific member by ID (specific format)

GET /api/members/123.json
GET /api/members/123.xml
Payments Endpoints
Get list of payments (default format)

GET /api/payments/
Get list of payments (specific format)

GET /api/payments.json
GET /api/payments.xml
Get details of a specific payment by ID (default format)

GET /api/payments/456/
Get details of a specific payment by ID (specific format)

GET /api/payments/456.json
GET /api/payments/456.xml
Generate a receipt for a specific payment (default format)

POST /api/payments/456/generate_receipt/
Generate a receipt for a specific payment (specific format)

POST /api/payments/456/generate_receipt.json
POST /api/payments/456/generate_receipt.xml
