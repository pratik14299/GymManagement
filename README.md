1. Membership Types
List Membership Types
URL: /membership-types/
Method: GET
Purpose: Retrieve a list of all membership types. This could be used by the frontend to display membership options to new users.

Retrieve a Specific Membership Type
URL: /membership-types/{pk}/
Method: GET
Purpose: Retrieve the details of a specific membership type by its primary key (pk). This could be used to display details when editing or viewing a specific membership type.

Format-Specific Endpoints
URLs ending with .{format}/ allow specifying response formats like JSON, XML, etc. For example, you might request /membership-types.json to get JSON output.

2. Members
List Members
URL: /members/
Method: GET
Purpose: Retrieve a list of all members. Admins can use this to manage or view member details.

Retrieve a Specific Member
URL: /members/{pk}/
Method: GET
Purpose: Retrieve details of a specific member by their primary key (pk). Useful for viewing individual member details in the admin portal.

Download Members
URL: /members/download_members/
Method: GET
Purpose: Download all member data, perhaps as a CSV file. Useful for generating reports or exporting member data.

3. Subscriptions
List Subscriptions
URL: /subscriptions/
Method: GET
Purpose: Retrieve a list of all subscriptions. Admins can use this to monitor subscription statuses or manage renewals.

Retrieve a Specific Subscription
URL: /subscriptions/{pk}/
Method: GET
Purpose: Retrieve details of a specific subscription by its primary key (pk). Useful for viewing or updating a specific subscription.

4. Payments
List Payments
URL: /payments/
Method: GET
Purpose: Retrieve a list of all payments. Admins can use this to view payment histories and manage financial records.

Retrieve a Specific Payment
URL: /payments/{pk}/
Method: GET
Purpose: Retrieve details of a specific payment by its primary key (pk). Useful for viewing payment details.

Download Payment Receipt
URL: /payments/{pk}/download_receipt/
Method: GET
Purpose: Download the receipt for a specific payment, potentially as a PDF. Members or admins can use this to get official receipts for payment records.
