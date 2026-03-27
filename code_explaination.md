# Code Explanation Guide

Kini nga file focused lang sa pinaka important nga changes sa project:

- routing
- pricing tab
- pricing logic

Dili na ni apil ang taas nga explanation sa tanang pages para mas direct ug mas related sa actual changes nga imong gihimo.

## 1. Routing changes sa `app.py`

Ang [app.py](app.py) mao ang main Flask file nga nagbuot kung unsang page ang i-open.

Sa recent changes, ang pinaka important nga part kay ang user routing.

### Main user route

```python
@app.route('/userdashboard')
def userdashboard():
    return render_template('userdashboard.html', username='User', role='user')
```

Meaning:
- if mo adto ang user sa `/userdashboard`
- ang mo open kay [userdashboard.html](templates/userdashboard.html)

Kini mao ang main dashboard page sa user.

### Section route

```python
@app.route('/userdashboard/<section>')
def userdashboard_section(section):
```

Kini nga route importante kaayo kay mao ni ang nag allow nga naay separate pages ang user tabs.

Instead nga usa ra ka file tanan, ang route mo decide unsang HTML ang i-render depending sa `section`.

### If section is `pricing`

```python
if section == 'pricing':
    return render_template(
        'pricingdashboard.html',
        username='User',
        role='user'
    )
```

Meaning:
- if ang gi open kay `/userdashboard/pricing`
- ang mo gawas kay [pricingdashboard.html](templates/pricingdashboard.html)

### If section is `discount`

```python
elif section == 'discount':
    return render_template(
        'discountdashboard.html',
        username='User',
        role='user'
    )
```

Meaning:
- ang `Discount Management` naa nay route
- pero placeholder pa lang ang page

### If section is `settings`

```python
elif section == 'settings':
    return render_template(
        'settingsdashboard.html',
        username='User',
        role='user'
    )
```

Meaning:
- ang `Settings` tab naa pud own route and own page

### Why important ni nga routing?

Kini nga change importante kay:
- each tab naa nay own route
- each tab naa nay own HTML file
- mas limpyo ang structure
- dali ma manage ang per-page content

So instead nga usa ka file nga daghan conditional parts, ang setup karon kay:
- dashboard page
- pricing page
- discount page
- settings page

## 2. Pricing tab overview

Ang [pricingdashboard.html](templates/pricingdashboard.html) mao ang pinaka working feature sa project karon.

Kini nga page ang responsible sa:
- pag save sa product base price
- pag update sa product price
- pag display sa saved products
- pag display sa price history

## 3. Structure sa pricing tab

Ang pricing tab kay naay 3 ka parts:

- HTML
- CSS
- JavaScript

### HTML part

Ang HTML mao ang visible structure sa page.

Important parts:

```html
<form id="pricingForm">
```

Meaning:
- mao ni ang form para sa user input
- diri i-enter ang `Product ID`
- diri i-enter ang `Price`

Naa pud ni:

```html
<tbody id="pricingTableBody"></tbody>
```

Meaning:
- diri i-display ang product list
- empty ni sa sugod
- JavaScript ang mo fill sa rows

### CSS part

Ang CSS sa pricing tab kay para sa layout ug styling.

Usa sa pinaka useful nga change kay ang scrollable table body:

```css
tbody {
    display: block;
    max-height: 320px;
    overflow-y: auto;
}
```

Meaning:
- if daghan na ug saved products
- ang table body na lang ang mo scroll
- dili na motaas ang whole page

## 4. Pricing logic sa JavaScript

Ang JavaScript mao gyud ang nagdala sa main functionality sa pricing tab.

Diri nahitabo ang:
- save product
- update product
- display products
- display history
- load data from browser

## 5. Why `localStorage`?

Before, naay hardcoded products sa Python.

Karon, gitangtang na sila ug gibalhin ang data ngadto sa browser pinaagi sa `localStorage`.

Meaning:
- ang products dili na hardcoded sa backend
- ang products ma save sa browser
- if mo refresh ka, naa gihapon ang data

Pero limitation:
- browser-only ra siya
- dili shared sa laing browser or device

## 6. Important functions sa pricing logic

### `getProducts()`

Purpose:
- mo kuha sa saved products gikan sa `localStorage`

```javascript
function getProducts() {
    const savedProducts = localStorage.getItem(storageKey);
    return savedProducts ? JSON.parse(savedProducts) : [];
}
```

If naay saved products:
- i-load sila

If wala:
- empty array lang

### `saveProducts(products)`

Purpose:
- mo save sa products balik sa browser

```javascript
function saveProducts(products) {
    localStorage.setItem(storageKey, JSON.stringify(products));
}
```

### `renderProductOptions()`

Purpose:
- mo show ug suggestions sa `Product ID` field

Meaning:
- if naa nay saved products
- makita nimo ilang IDs when you click or type

Kini nga feature useful para:
- dali maka pili sa existing product
- dali maka update ug price

### `renderProducts()`

Purpose:
- mo display sa tanan saved products sa table

Ang ipakita niya:
- Product ID
- Base Price
- Price History

If walay products:
- mo show ug `No products saved yet.`

## 7. Form submit logic

Kini ang pinaka important part sa pricing tab:

```javascript
pricingForm.addEventListener("submit", function (event) {
```

Meaning:
- once mo click ang user sa `Save Price`
- JavaScript ang mo handle sa process

### Actual flow

1. kuhaon ang `Product ID`
2. kuhaon ang `Price`
3. check if empty ang fields
4. check if valid ang price
5. load ang current products gikan sa `localStorage`
6. tan-awon if existing na ba ang product ID

### If existing ang product ID

Kung existing na:
- dili na siya mag create ug new product
- ang buhaton kay update sa `base_price`
- then mag append ug new entry sa `price_history`

Meaning:
- na preserve ang old history
- nadungagan lang ug bagong record

### If new ang product ID

Kung wala pa ang product ID:
- mag create ug new product object
- magbutang ug first history entry

Meaning:
- ang first saved price mahimong base price
- mao pud na ang first record sa history

### After saving

After ma save or ma update:
- i-save balik ang products sa `localStorage`
- i-refresh ang Product ID suggestions
- i-refresh ang table
- i-reset ang form

## 8. Summary sa changes

Sa short version:

Ang main code changes sa project kay duha:

### Routing
- ang user tabs naa nay separate routes
- ang user tabs naa nay separate HTML files

### Pricing logic
- gitangtang ang hardcoded products sa Python
- gigamit ang `localStorage`
- pwede na mag save ug `Product ID` plus `Price`
- pwede na mag update sa existing product
- naa nay price history
- naa nay product suggestions
- naa nay scrollable table

Mao ni ang pinaka important nga technical changes sa current version sa project.
