# PocketWave — mobile phone store

**CodeAlpha Full Stack Development · Task 1**  
**Adapted and developed by Nunna Venkata Sai Manikanta**

PocketWave is a responsive, mobile-first shopping application focused entirely on smartphones. It has a fictional six-phone catalog with custom local vector illustrations, searchable product listings, detailed specifications, a session cart, account registration, and a complete demo order flow.

The phone names, specifications and prices in the sample catalog are fictional. Checkout records a demo order in the local database; it does **not** charge a customer or connect to a delivery provider.

## What you can do

- Browse the curated home page or search and filter the phone catalog by type.
- Sort by price or date and compare storage, display and battery on detail pages.
- Add phones to a bag, update quantities, and remove items.
- Create an account, sign in, place a demo order and view order history.
- Manage catalog items and order statuses in Django admin.
- Use an app-style bottom navigation on phones and a wide layout on larger screens.

## Stack

Python, Django 5.2, Django templates, HTML, CSS, JavaScript and SQLite. Product art is kept locally as SVG, so the demo catalog has no external image dependency. The local design uses Google Fonts when online and system fonts when offline.

## Quick start on Windows

Extract the ZIP and double-click **`START.bat`** inside the project folder. It creates `.venv`, installs packages, prepares the database, loads fictional demo content, and starts the server. Use one project at a time on port 8000.

To run the steps manually, open a terminal inside the project folder:

Extract the ZIP and open a terminal **inside `CodeAlpha_PocketWaveStore`**:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py seed_data
python manage.py runserver
```

Open <http://127.0.0.1:8000/>. If PowerShell prevents environment activation, use Command Prompt with `.venv\Scripts\activate.bat` or invoke `.\.venv\Scripts\python.exe` for each command.

Create a regular account on the Register page. For catalog and order management, run `python manage.py createsuperuser` and open <http://127.0.0.1:8000/admin/>.

Run automated checks:

```powershell
python manage.py check
python manage.py test
```

The sample catalog command is idempotent: rerunning it updates the six fictional demo phones by slug. Runtime database files and virtual environments are excluded from the ZIP/Git repository.

## Project layout

```text
CodeAlpha_PocketWaveStore/
├── pocketwave_core/             Django settings and root routes
├── store/                       Catalog, session bag, checkout, models, admin
│   ├── management/commands/seed_data.py
│   └── migrations/
├── templates/                   Shopping and account screens
├── static/css/                  Responsive visual system
├── static/img/products/         Original local phone illustrations
├── static/js/                   Small interface behavior
├── START.bat                    Windows one-click local setup
├── manage.py
├── requirements.txt
└── README.md
```

## Core data flow

`Product` holds price, stock, type, specifications and illustration path. A session bag stores product IDs and quantities; prices come from current product records. Checkout requires login, validates stock inside a database transaction, creates `Order` and `OrderItem` records, and reduces stock. Admin can change the order status. SQLite stores users, products and orders locally.

## Internship task coverage

| Task 1 requirement | PocketWave implementation |
| --- | --- |
| Product listings and details | Phone catalog, search/filter/sort, specifications |
| Shopping cart | Session bag with add, update, remove and totals |
| Order processing | Authenticated demo checkout and saved order history |
| Registration/login | Django account forms and sessions |
| Database | SQLite models for products and orders, Django users |

## Local development note

The default settings are for local development. Before hosting publicly, set `DJANGO_SECRET_KEY`, set `DJANGO_DEBUG=0`, configure `DJANGO_ALLOWED_HOSTS`, and provide production static/media hosting. This project does not include a real payment integration.

For a CodeAlpha submission, create a repository named `CodeAlpha_PocketWaveStore`, upload this source, and record your own walkthrough video. The supplied source archive does not include someone else's demo video, Git history, or database.
