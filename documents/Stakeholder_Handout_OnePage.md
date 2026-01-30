# SharePoint Migration - Quick Reference Handout

## Why Are We Moving to SharePoint?

| Current Problem | SharePoint Solution |
|-----------------|-------------------|
| Can't access files remotely | Access from anywhere, any device |
| "Final_v3_FINAL.docx" confusion | Automatic version history |
| Files get lost in folders | Powerful search finds anything |
| Email attachments back & forth | Real-time collaboration |
| Manual backups | Automatic cloud protection |

---

## The Big Change: Folders → Metadata

### OLD WAY: Navigate 7 folders to find one file
```
\\Server\Finance\Invoices\2024\Q1\January\Vendor_ABC\Paid\INV-001.pdf
        ↓       ↓       ↓    ↓    ↓         ↓       ↓
     Click   Click  Click Click Click    Click   Click  = 45 seconds
```

### NEW WAY: Search or filter with 2-3 clicks
```
SharePoint → Finance → Invoices Library → Filter: Vendor=ABC, Year=2024

OR simply search: "ABC invoice 2024" = 10 seconds
```

---

## How Metadata Works

**One file can have multiple tags (unlike folders where it can only be in one place):**

```
┌─────────────────────────────────┐
│  Contract_ABC.pdf               │
│                                 │
│  Year:     [2024           ▼]  │
│  Vendor:   [ABC Corp       ▼]  │
│  Project:  [Alpha          ▼]  │
│  Status:   [Active         ▼]  │
└─────────────────────────────────┘

This ONE file now appears in:
✓ 2024 Documents view
✓ ABC Corp vendor view
✓ Project Alpha view
✓ Active contracts view
```

**Same file, found 4 different ways!**

---

## Our Recommended Approach

| Use Folders For | Use Metadata For |
|-----------------|------------------|
| Major categories (1-2 levels) | Year, Month, Quarter |
| Document types (Contracts, Invoices) | Vendor/Client |
| | Status (Draft, Approved, Final) |
| | Project name |
| | Department |

**Simple structure + Rich metadata = Best of both worlds**

---

## What Changes for You

| Today | After Migration |
|-------|-----------------|
| Navigate folders to find files | Search or filter |
| Save to specific folder path | Save + add 2-3 tags |
| Email file as attachment | Share link (always current) |
| "Is this the latest version?" | Version history shows all |
| Office-only access | Access from home/mobile |

---

## Key Numbers

| Item | Recommendation |
|------|----------------|
| Max folder depth | **2 levels** |
| Metadata columns | **5-7 per library** |
| Required fields | **2-3 only** |
| Training provided | **Yes, before your migration** |

---

## Your Role

- [ ] Complete the discovery questionnaire
- [ ] Identify a department champion
- [ ] Attend training session
- [ ] Provide feedback during pilot
- [ ] Adopt the new system

---

## Questions?

**Project Contact:** _________________ | **Email:** _________________

---

*Remember: Search first, browse second. Your files will be easier to find than ever!*
