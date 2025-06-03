# Dealership Loaner Management Platform
> ⚠️ This project is actively in development.

A full-stack, paperless loaner car management system for auto dealerships. 
Digitizes insurance verification, check-in workflows, vehicle inspections, digital agreements, and fleet tracking — with zero paid APIs or vendor lock-in.

---

## Why This Matters

Dealerships waste **thousands of dollars per month** verifying insurance manually:

- **$1.37 per phone call** in labor cost (man hours)
- Most stores keep verification logs in **Excel** with typos and incomplete records
- Systems like **Axle** cost ~$2.00 per verification
- Axle can only verify **~8.1% of customers** via API logins

This platform eliminates all of that:

- ✔️ No vendor lock-in
- ✔️ Works from photos/screenshots of cards
- ✔️ Tracks all data with audit trail and PDF records
- ✔️ Pays for itself in reduced friction, labor, and liability

---

## Stack & Dependencies

**Frontend**
- React + TypeScript
- TailwindCSS (Axle-style UI)
- react-hook-form, react-signature-canvas, react-dropzone

**Backend**
- FastAPI (Python 3.10+)
- PostgreSQL or Supabase
- Tesseract OCR or EasyOCR
- spaCy (PII/Entity redaction)
- WeasyPrint (PDF generation)

**Dev Tools**
- Docker + Docker Compose
- GitHub Actions CI/CD

---

## Folder Map

```markdown
dealership_loaner_platform/
├── backend/                      # FastAPI backend
│   ├── main.py                   # Entry point
│   ├── api/                      # API route definitions
│   │   ├── insurance.py
│   │   ├── agreement.py
│   │   ├── customer.py
│   │   └── vehicle.py
│   ├── services/                 # Core business logic modules
│   │   ├── ocr_engine.py         # Tesseract OCR logic for screenshots
│   │   ├── validation.py         # Insurance rule validation logic
│   │   ├── pdf_generator.py      # Create loaner agreements as PDF
│   │   └── walkaround.py         # Handle image upload + tagging
│   ├── models/                   # Pydantic + DB models
│   │   ├── insurance.py
│   │   ├── customer.py
│   │   ├── vehicle.py
│   │   ├── agreement.py
│   │   └── subsidy.py
│   ├── db/                       # DB setup (PostgreSQL)
│   │   ├── session.py
│   │   └── base.py
│   ├── utils/                    # Helper functions
│   │   ├── redact.py
│   │   ├── date_parser.py
│   │   └── file_utils.py
│   ├── config.py
│   ├── .env
│   └── requirements.txt
│
├── frontend/                     # React + TypeScript frontend
│   ├── public/
│   └── src/
│       ├── components/
│       │   ├── UploadForm.tsx    # Upload and preview insurance card screenshot
│       │   ├── SignaturePad.tsx  # react-signature-canvas
│       │   ├── WalkaroundForm.tsx
│       │   ├── AgreementReview.tsx
│       │   └── ui/
│       │       └── Button.tsx
│       ├── pages/
│       │   ├── CheckIn.tsx       # Customer self-check-in UI
│       │   ├── FleetDashboard.tsx
│       │   └── Agreement.tsx
│       ├── services/             # API interface layer
│       │   ├── insurance.ts
│       │   ├── agreement.ts
│       │   └── customer.ts
│       ├── App.tsx
│       └── index.tsx
│   ├── package.json
│   └── tsconfig.json
│
├── scripts/
│   ├── seed_vehicles.py
│   └── test_ocr_flow.py
│
├── tests/                        # Unit + integration tests
│   ├── test_insurance.py
│   ├── test_validation.py
│   └── test_pdf_contract.py
│
├── docker/
│   ├── backend.Dockerfile
│   ├── frontend.Dockerfile
│   └── docker-compose.yml
│
├── .github/workflows/deploy.yml
├── README.md
└── LICENSE
```

---

## Setup (Local)

```bash
# 1. Clone the repo
cd ~/Desktop
git clone [this repo] dealership_loaner_platform
cd dealership_loaner_platform

# 2. Set up Python env
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 3. Run backend
uvicorn main:app --reload

# 4. Run frontend
cd ../frontend
npm install
npm run dev
```

---

## 🐋 Setup with Docker

```bash
cd docker
mv nginx.conf.txt nginx.conf  # if needed
cd ..
docker-compose up --build
```

Access:
- Frontend: [http://localhost:3000](http://localhost:3000)
- Backend API: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## Scripts & Testing

```bash
# Seed demo vehicles
python scripts/seed_vehicles.py

# Test OCR extraction
python scripts/test_ocr_flow.py
```

---

## Dev Notes

- Sample insurance cards for OCR testing live in `/tests/sample_insurance_card.png`
- Generated rental agreements are saved to `/generated_pdfs`
- Uploaded DL/insurance screenshots stored under `/uploaded_files`
- OCR pipeline is 100% open source — no third-party API costs required

---

## Future Roadmap

- Fleet geofencing
- Optional insurance login fallback (e.g., MeasureOne) if OCR fails
  → Cheaper than Axle, better fallback coverage
  → Not required for primary workflow
- Repair order sync with Xtime
- Subsidy tracking (BMW, etc.)

---

MIT License 
