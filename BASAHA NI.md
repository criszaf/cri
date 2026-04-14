## New Features

### 1. **Hardcoded Expiration Duration per Rule**
Each discount rule now has a **fixed expiration time** based on the discount percentage:

| Discount Rule | Discount % | Expiration Duration |
|---------------|-----------|-------------------|
| Rule 1 | 10% | 1 Day |
| Rule 2 | 20% | 2 Days |
| Rule 3 | 30% | 3 Days |
| Rule 4 | 40% | 4 Days |
| Rule 5 | 50% | 7 Days |

**No need to select expiration separately** - it's automatic based on the rule!

### 2. **Real-Time Countdown Timer (HH:MM:SS)**
- Displays remaining time in clear `HH:MM:SS` format
- Updates **every second** for live countdown
- Example: `02:15:45` = 2 hours, 15 minutes, 45 seconds remaining

### 3. **Auto-Expiration**
- Expired discounts are **automatically removed** from LocalStorage every second
- No manual deletion needed
- Real-time removal from UI

### 4. **Visual Alert - Expiring Soon**
- Rows **highlight in yellow** when discount expires in less than 1 hour
- Makes it easy to spot soon-to-expire discounts

### 5. **Persistent Storage**
- All discount data including expiration timestamp saved to **LocalStorage**
- Data persists across browser sessions
- No backend database needed

---

## Data Structure

### Old Discount Object
```javascript
{
  product_id: "101",
  discount_percent: 10,
  discounted_price: 500,
  created_at: "4/14/2026, 2:30:00 PM"
}
```

### New Discount Object (With Expiration)
```javascript
{
  product_id: "101",
  discount_percent: 10,
  discounted_price: 500,
  created_at: "4/14/2026, 2:30:00 PM",
  expiration_timestamp: 1744728600000  // Unix milliseconds
}
```
---

### Viewing Discounts
The discount table shows:
- Product ID
- Base Price
- Discount %
- Discounted Price
- **⏱️ Expires In** (HH:MM:SS countdown)
- Remove button

### Countdown Updates
- Updates **every 1 second**
- Yellow highlight appears when **< 1 hour remaining**
- Auto-removes when countdown reaches 00:00:00

---

## Technical Implementation

### Key Functions

#### `getExpirationHours(discountPercent)`
Maps discount percentage to expiration hours
```javascript
durationMap = {
  "10": 24,      // 1 day
  "20": 48,      // 2 days
  "30": 72,      // 3 days
  "40": 96,      // 4 days
  "50": 168      // 7 days
}
```

#### `formatTimeRemaining(hours)`
Converts hours to HH:MM:SS format
```javascript
// Input: 2.25 (hours)
// Output: "02:15:00"
```

#### `getTimeRemaining(expirationTimestamp)`
Calculates remaining time in hours
```javascript
// Compares current time with expiration timestamp
// Returns hours remaining as decimal
```

#### `removeExpiredDiscounts()`
Removes expired discounts from storage
```javascript
// Runs every 1 second
// Filters out discounts where expiration_timestamp < now
```

#### `renderDiscounts()`
Renders table with countdown timers
```javascript
// Called every second for live updates
// Checks if < 1 hour remaining → adds yellow highlight
// Displays HH:MM:SS format
```

---

## Files Modified

### `templates/admindiscountmanagement.html`

**HTML Changes:**
- Removed "Expires In" dropdown selector
- Updated table header to include "Expires In" column
- Rules now show duration in label (e.g., "10% - Rule 1 (1 day expiration)")

**CSS Changes:**
- Added `.expiring-soon` class for yellow highlight
- Added `.countdown` class for bold red timer text

**JavaScript Changes:**
- Added `getExpirationHours()` function
- Updated `formatTimeRemaining()` to return HH:MM:SS
- Added `expiration_timestamp` to discount data object
- Added `removeExpiredDiscounts()` function
- Changed timer update interval from none to every 1 second
- Updated table rendering to include countdown column

---

## LocalStorage Keys

| Key | Purpose | Format |
|-----|---------|--------|
| `pricing_products` | All products | JSON array |
| `pricing_discounts` | All discounts with expiration | JSON array |

---

### Understanding the Code

**localStorage:**
- Browser's built-in storage (like a small database)
- Data stored as JSON strings
- Persists across page reloads

**setInterval():**
```javascript
setInterval(function() {
  // This code runs every 1000 milliseconds (1 second)
}, 1000);
```

**Timestamps:**
- `new Date().getTime()` = current time in milliseconds
- Comparing timestamps tells us how much time has passed

**padStart():**
```javascript
"5".padStart(2, '0')  // Returns "05"
```
Used to format numbers with leading zeros