# AI-Lawyer Template & Knowledge Index

> Master index of all document templates, knowledge references, and resources

## Template Categories

### 📋 Family Law Templates (`templates/family/`)
| Template ID | Name (ID) | Name (EN) | Complexity |
|---|---|---|---|
| surat-gugatan-cerai | Surat Gugatan Cerai | Divorce Petition (Wife) | Moderate |
| surat-permohonan-cerai-talak | Surat Permohonan Cerai Talak | Divorce Petition (Husband) | Moderate |
| perjanjian-pranikah | Perjanjian Pranikah | Prenuptial Agreement | Complex |
| surat-keterangan-waris | Surat Keterangan Waris | Inheritance Declaration | Moderate |
| surat-wasiat | Surat Wasiat (Testament) | Last Will and Testament | Complex |

### 🏢 Business Law Templates (`templates/business/`)
| Template ID | Name (ID) | Name (EN) | Complexity |
|---|---|---|---|
| akta-pendirian-pt | Akta Pendirian PT | Company Incorporation Deed | Complex |
| perjanjian-kerjasama | Perjanjian Kerjasama | Partnership Agreement | Moderate |
| surat-kuasa | Surat Kuasa | Power of Attorney | Simple |
| perjanjian-jual-beli | Perjanjian Jual Beli | Sale & Purchase Agreement | Moderate |
| non-disclosure-agreement | NDA / Kerahasiaan | Non-Disclosure Agreement | Moderate |

### 👷 Employment Law Templates (`templates/employment/`)
| Template ID | Name (ID) | Name (EN) | Complexity |
|---|---|---|---|
| kontrak-kerja-pkwt | Kontrak Kerja PKWT | Fixed-Term Employment Contract | Moderate |
| kontrak-kerja-pkwtt | Kontrak Kerja PKWTT | Permanent Employment Contract | Moderate |
| surat-pengunduran-diri | Surat Pengunduran Diri | Resignation Letter | Simple |
| surat-peringatan | Surat Peringatan (SP) | Warning Letter | Simple |
| surat-phk | Surat PHK | Termination Letter | Complex |

### 🏠 Property Law Templates (`templates/property/`)
| Template ID | Name (ID) | Name (EN) | Complexity |
|---|---|---|---|
| perjanjian-sewa-menyewa | Perjanjian Sewa Menyewa | Rental/Lease Agreement | Moderate |
| perjanjian-jual-beli-tanah | Perjanjian Jual Beli Tanah | Land Sale Agreement (PPJB) | Complex |
| surat-kuasa-jual-tanah | Surat Kuasa Jual Tanah | Power of Attorney - Land Sale | Moderate |

### ⚖️ General Templates (`templates/general/`)
| Template ID | Name (ID) | Name (EN) | Complexity |
|---|---|---|---|
| surat-somasi | Surat Somasi | Demand/Warning Letter | Moderate |
| surat-pernyataan | Surat Pernyataan | Sworn Statement/Affidavit | Simple |
| surat-pengaduan-polisi | Surat Pengaduan Polisi | Police Complaint Letter | Moderate |
| surat-pengaduan-konsumen | Surat Pengaduan Konsumen | Consumer Complaint | Simple |
| perjanjian-perdamaian | Perjanjian Perdamaian | Settlement Agreement | Moderate |

---

## Knowledge Base

### 📚 Law References (`laws/`)
| File | Coverage |
|---|---|
| INDEX.md | Master index of all Indonesian laws |
| family-law.md | UU 1/1974, KHI, divorce, custody, inheritance |
| labor-law.md | UU 13/2003, Cipta Kerja, PKWT/PKWTT, PHK, severance |
| company-law.md | UU 40/2007, PT formation, CV, OSS/NIB |
| criminal-law.md | KUHP Baru, KUHAP, offenses, criminal process |
| consumer-protection.md | UU 8/1999, BPSK, e-commerce |
| data-privacy.md | UU PDP 27/2022, data protection |
| property-law.md | UUPA, land rights, AJB, taxes |

### 📖 Step-by-Step Procedures (`procedures/`)
| File | Description |
|---|---|
| divorce-procedure.md | Complete divorce process guide |
| company-formation.md | PT formation step-by-step |
| employment-dispute.md | Industrial dispute resolution |
| consumer-complaint.md | Consumer complaint process |
| property-transaction.md | Property buy/sell procedure |

### 📝 Glossary (`glossary/`)
| File | Description |
|---|---|
| legal-glossary.md | 200+ bilingual Indonesian-English legal terms |

### ❓ FAQ (`faq/`)
| File | Description |
|---|---|
| family-faq.md | 22 family law Q&As |
| business-faq.md | 17 business law Q&As |
| general-faq.md | 18 general legal Q&As |

---

## Template Engine

### Schema
- `templates/schema.json` — JSON Schema for template validation and form generation

### How Templates Work

```
User Query → AI Classification → Template Selection → Form Generation → Document Output
     ↓              ↓                    ↓                  ↓              ↓
  "Saya mau     Category:          surat-gugatan-     Fields from      PDF/DOCX
   cerai"       family              cerai              schema.json      output
```

### Integration Points

1. **RAG Pipeline**: Law references + FAQ + Glossary → Vector embeddings → Qdrant
2. **Document Generation**: Template schema → Form UI → Populated .md template → PDF/DOCX
3. **AI Chat**: User questions → Semantic search → Relevant knowledge → GPT-4o response
4. **Procedure Guidance**: Step-by-step guides → Interactive checklist UI

### File Structure
```
knowledge/
├── README.md                    # Repository overview
├── INDEX.md                     # This file - master index
├── laws/                        # Legal reference materials
│   ├── INDEX.md
│   ├── family-law.md
│   ├── labor-law.md
│   ├── company-law.md
│   ├── criminal-law.md
│   ├── consumer-protection.md
│   ├── data-privacy.md
│   └── property-law.md
├── templates/                   # Document templates
│   ├── schema.json              # Unified template schema
│   ├── family/
│   │   ├── templates.json
│   │   └── surat-gugatan-cerai.md
│   ├── business/
│   │   ├── templates.json
│   │   ├── akta-pendirian-pt.md
│   │   └── surat-kuasa.md
│   ├── employment/
│   │   ├── templates.json
│   │   ├── kontrak-kerja-pkwt.md
│   │   └── surat-peringatan.md
│   ├── property/
│   │   ├── templates.json
│   │   └── perjanjian-sewa-menyewa.md
│   └── general/
│       ├── templates.json
│       ├── surat-somasi.md
│       └── surat-pengaduan-polisi.md
├── procedures/                  # Step-by-step guides
│   ├── divorce-procedure.md
│   ├── company-formation.md
│   ├── employment-dispute.md
│   ├── consumer-complaint.md
│   └── property-transaction.md
├── glossary/
│   └── legal-glossary.md        # 200+ bilingual terms
└── faq/
    ├── family-faq.md
    ├── business-faq.md
    └── general-faq.md
```

---

## Statistics

| Metric | Count |
|---|---|
| Total Templates | 23 |
| Template Categories | 5 |
| Law Reference Files | 8 |
| Procedure Guides | 5 |
| Glossary Terms | 200+ |
| FAQ Questions | 57+ |
| Legal Bases Referenced | 30+ laws |

---

## Future Additions (Planned)
- [ ] Tax law templates (SPT, keberatan pajak, banding)
- [ ] Immigration templates (KITAS, KITAP applications)
- [ ] IP law templates (trademark, patent, copyright)
- [ ] Bankruptcy/PKPU templates
- [ ] Environmental law templates
- [ ] Administrative law templates (PTUN)
- [ ] Syariah finance templates
- [ ] Mediation/arbitration templates
- [ ] Legal opinion templates
- [ ] Due diligence checklists
