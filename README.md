# InventoryPro


InventoryPro is a warehouse inventory system that helps businesses track inventory without relying on paper records or spreadsheets.

## Project Goal

The goal of InventoryPro is to make inventory tracking faster, easier, and more accurate.

The main users are warehouse employees and managers.

## User Roles

### Employees

Employees will be able to:

- Log in to the system
- Search for products
- Add incoming inventory
- Remove inventory when products are shipped
- View inventory information

### Managers

Managers will have all employee permissions, along with the ability to:

- Add new products
- View inventory reports
- Check low-stock products
- Manage product information

## Main Features

- User login
- Employee and manager accounts
- Add new products
- Search for products
- Update inventory quantities
- Track incoming and outgoing inventory
- Low-stock alerts
- Inventory dashboard
- Inventory transaction history
- Role-based permissions
- Inventory validation

## Database Design

### Users

| Field | Description |
|---|---|
| UserID | Unique user identifier |
| Username | User login name |
| PasswordHash | Securely stored password |
| FullName | User's full name |
| Role | Employee or manager |

### Products

| Field | Description |
|---|---|
| ProductID | Unique product identifier |
| SKU | Product stock-keeping unit |
| ProductName | Name of the product |
| Category | Product category |
| QuantityOnHand | Current inventory quantity |
| ReorderLevel | Quantity that triggers a low-stock alert |
| WarehouseLocation | Product storage location |
| UnitCost | Cost of one unit |

### InventoryTransactions

| Field | Description |
|---|---|
| TransactionID | Unique transaction identifier |
| ProductID | Product involved in the transaction |
| UserID | User who completed the transaction |
| TransactionType | Inventory coming in or going out |
| Quantity | Number of items changed |
| TransactionDate | Date and time of the transaction |

## Planned Screens

- Login screen
- Dashboard
- Product search page
- Add product page
- Update inventory page
- Low-stock page

## Dashboard

The dashboard will display:

- Total number of products
- Recent inventory transactions
- Products that are running low
- General inventory summaries

## Inventory Process

1. A user logs in.
2. The user is taken to the dashboard.
3. The user searches for or selects a product.
4. The user adds or removes inventory.
5. The product quantity is updated.
6. A transaction record is automatically created.

The system will prevent users from entering negative quantities or removing more inventory than is currently available.

## Project Status

InventoryPro is currently in the planning and design stage.

The next steps are:

- Build the database
- Design the application screens
- Implement user login
- Add employee and manager permissions
- Implement product management
- Implement inventory transactions
- Test the system

## Proposed Technology

- Python
- Flask
- SQLite
- HTML
- CSS
- Bootstrap

## Author

Joe Del Torto Jr.
## Project Backlog

### Sprint 1 (Completed)
- ✅ Created GitHub repository.
- ✅ Wrote the project README.
- ✅ Set up the initial project structure.
- ✅ Began designing the inventory management application.
- ✅ Planned core features for the MVP.

### Sprint 2 (Current Backlog)
- ⏳ Complete the Add Inventory feature.
- ⏳ Implement Edit Inventory functionality.
- ⏳ Implement Delete Inventory functionality.
- ⏳ Add search and filtering capabilities.
- ⏳ Improve the user interface.
- ⏳ Add input validation and error handling.
- ⏳ Test the application and fix bugs.
## Project Backlog
## Sprint 2 Progress

During Sprint 2, I continued developing InventoryPro by improving the project structure and making progress on the core inventory management features. I also updated the project backlog, fixed issues found during development, and continued testing to ensure the application functions correctly.
## Sprint 2 Backlog (Completed)

- ✅ Continued development of the InventoryPro application.
- ✅ Improved the project structure and organization.
- ✅ Updated the README documentation.
- ✅ Fixed bugs found during testing.
- ✅ Updated the project backlog.

## Sprint 3 Backlog

- ⏳ Finish the Add Inventory feature.
- ⏳ Complete the Edit Inventory feature.
- ⏳ Complete the Delete Inventory feature.
- ⏳ Improve the user interface.
- ⏳ Continue testing and bug fixes.
git push
