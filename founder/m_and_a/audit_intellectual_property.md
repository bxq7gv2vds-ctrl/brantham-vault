---
name: audit_intellectual_property
description: Inventaire complet IP (brevets, marques, licences, trade secrets)
metadata:
  type: checklist
  created: 2026-06-12
---

# Audit Intellectual Property — M&A Due Diligence

## **Why Buyers Care:**
- IP = core value in tech/SaaS deals
- Missing IP = deal killed, 40-70% valuation cut
- Unlicensed code = liability exposure (GPL, open-source compliance)

---

## **Section 1 : Patents**

### **Patents DÉPOSÉS (USA, EU, intl)**

| Patent Title | Filing Date | Issue Date | Inventor(s) | Patent # | Status | Coverage | Comment |
|---|---|---|---|---|---|---|---|
| Algorithm X for Y | 2022-03-15 | 2024-01-10 | Founder, Engineer A | US 11,234,567 | ISSUED | Claims 1-15 strong | Core tech, defensible |
| Method for Z optimization | 2021-09-01 | Pending | Founder | | PENDING | Non-provisional | Prosecution stage? |
| | | | | | | | |

### **Checklist Patents:**
- [ ] All inventors listed correctly (founder, employees, contractors?)
- [ ] Assignment agreements signed? (Inventor → Company)
- [ ] International filings (EU, China, Japan)? Cost/benefit?
- [ ] Prior art search done? (Freedom to operate?)
- [ ] Patent maintenance fees paid? (Not lapsed)
- [ ] Litigation history? (Infringement claims?)
- [ ] Provisional vs utility: strategy?

**Red flag:** Patent filed by founder but never assigned to company = company doesn't own it!

---

## **Section 2 : Trademarks**

### **Registered Marks**

| Mark | Type | Jurisdiction | Reg # | Issue Date | Renewal Date | Classes | Status |
|---|---|---|---|---|---|---|---|
| **ACME Coiffure** | Word | USA | 5,123,456 | 2020-05-01 | 2026-05-01 | 42 (Services) | ACTIVE |
| **ACME Logo** | Design | USA | 5,123,457 | 2020-05-01 | 2026-05-01 | 42 | ACTIVE |
| **ACME Coiffure** | Word | EU | 017123456 | 2019-03-15 | 2029-03-15 | 42 | ACTIVE |
| | | | | | | | |

### **Common Law Marks (Unregistered)**
- List any: brand names, taglines, logos used but not formally registered
- Risk: weak protection vs registered marks

### **Checklist Trademarks:**
- [ ] All brand names registered? (Core: product name, company name, tagline)
- [ ] Registrations active & not expired?
- [ ] Renewal dates upcoming? (Maintain before sale)
- [ ] Classes correct? (Class 42 for SaaS services, Class 9 for software)
- [ ] International coverage needed? (EU, Canada?)
- [ ] Cease & desist letters received? (Infringement?)
- [ ] Domain names owned? (.com, .io, etc.)
- [ ] Social handles (@company) controlled?

**Red flag:** Trademark expires in 6 months & buyer takes over = buyer's risk

---

## **Section 3 : Copyright**

### **Software & Works**

| Work | Type | Created | Registered | Copyright Notice | License |
|---|---|---|---|---|---|
| Core Product Codebase | Software | 2020-01-01 | NO (USA auto) | ©2020 Company Inc | Proprietary |
| Mobile App | Software | 2021-06-01 | YES (TX, reg#) | ©2021 Company Inc | Proprietary |
| Documentation | Documentation | 2020-01-01 | NO | ©2020 Company Inc | Creative Commons (internal) |
| | | | | | |

### **Checklist Copyright:**
- [ ] Copyright notices in code comments? (©YEAR Company)
- [ ] Registration certificates on file? (Recommended for litigation)
- [ ] Employee/contractor work-for-hire agreements signed?
- [ ] All code contributions assigned to company? (GitHub, GitLab?)
- [ ] No employee used personal GitHub account w/ company code?
- [ ] Third-party GPL/open-source properly attributed?

**Red flag:** Engineer leaves, claims they own the code = litigation risk

---

## **Section 4 : Open-Source License Compliance**

This is **critical** and often missed.

### **Dependencies & Licenses**

Run this scan:
```bash
# Node.js projects:
npm list | grep -E "GPL|AGPL|SSPL"

# Python projects:
pip show -f | grep -i license

# Java projects:
mvn license:add-third-party
```

| Package | Version | License | Compatibility | Risk | Action |
|---|---|---|---|---|---|
| lodash | 4.17.21 | MIT | ✅ Safe | None | OK |
| GPL-lib | 1.0.0 | GPLv3 | ⚠️ Viral | **CRITICAL** | Replace or release code open-source |
| mongoose | 5.11.0 | MIT | ✅ Safe | None | OK |

**License Categories:**
- **MIT, Apache 2.0, BSD:** Permissive, safe ✅
- **LGPL:** Linking allowed if proprietary, but redistribution requires license notice
- **GPLv2/v3:** **VIRAL** — your product must be open-source ⚠️
- **AGPL:** Most restrictive, network-use triggers viral ⚠️
- **SSPL:** Felicity-dubious, some courts reject
- **BUSL (Business Source License):** Commercial until date, then open

### **Compliance Checklist:**
- [ ] No unlicensed GPL code in proprietary product? **MANDATORY**
- [ ] NOTICE file created listing all dependencies + licenses?
- [ ] Developer aware of AGPL risk in SaaS (service = derivative work)?
- [ ] Dependencies pinned to vetted versions?
- [ ] No npm/pip packages installed via `--unsafe-perms` or from untrusted source?

**Red flag:** GPL library in proprietary SaaS = deal killer or 50% valuation cut

---

## **Section 5 : Trade Secrets & Confidential Info**

### **Checklist:**
- [ ] Algorithms documented in **non-code** form (secret value)?
- [ ] Process documentation kept confidential?
- [ ] Customer lists confidential? (Not published)
- [ ] Pricing models confidential?
- [ ] Nondisclosure agreements signed with:
  - [ ] All employees? (Exit package reminder)
  - [ ] Contractors? (Especially offshore)
  - [ ] Advisors?
- [ ] Source code on GitHub public? (If secret algo, move to private)
- [ ] Backups encrypted & access-controlled?
- [ ] Departing employee: IP transfer agreement signed?

**Red flag:** Algorithm in public GitHub since 2019 = not a trade secret

---

## **Section 6 : Third-Party IP Rights**

### **Do you use (and have rights to):**

- [ ] Third-party software libraries? (Licensed properly)
- [ ] Third-party APIs? (Terms allow resale/redistribution?)
- [ ] Third-party data (datasets, images, music)?
- [ ] Third-party brand assets? (Logo design, photography)

### **Example Red Flags:**
- Using Unsplash images commercially → check license
- Reselling data from Google Maps → need explicit license
- Using Adobe fonts in SaaS → need commercial license
- Recording software from Zoom → need explicit permission

**Template for each third-party resource:**
```
Resource: [Name]
Provider: [Company]
Agreement: [Link to terms]
Licensed for: [Use case]
Transferable to buyer? [YES/NO] - Explain
Risk if buyer takes over: [None / Need new license / Re-negotiation]
```

---

## **Section 7 : Domain Names & Web Assets**

| Domain | Registrar | Owner | Expires | Status | Critical? |
|---|---|---|---|---|---|
| mycompany.com | GoDaddy | Company name | 2027-03-15 | ACTIVE | YES |
| mycompany.io | Namecheap | Personal (founder) | 2025-09-01 | ACTIVE | **RED FLAG** |
| subdomain.mycompany.com | Cloudflare DNS | Company | Auto-renew | ACTIVE | NO |

### **Checklist:**
- [ ] All domains owned by **company** (not founder personally)?
- [ ] Auto-renew enabled on critical domains?
- [ ] WHOIS privacy to prevent competitor registration?
- [ ] SSL certificates (HTTPS) valid?
- [ ] Email MX records pointing to active mail server?

**Red flag:** Founder owns domain individually → deal stalls until transferred

---

## **Section 8 : Inventory Summary (Dataroom)**

Prepare these docs:
```
IP/
├── Patents/
│   ├── Patent_List.xlsx (all filed + issued)
│   ├── Patent_Assignments.pdf
│   └── Maintenance_Fee_Receipts.pdf
├── Trademarks/
│   ├── Trademark_Register.xlsx
│   └── Registration_Certificates.pdf
├── Copyrights/
│   ├── Copyright_Registrations.pdf
│   └── Work_For_Hire_Agreements.pdf
├── Open_Source/
│   ├── License_Scan_Report.txt (npm/pip/mvn output)
│   ├── NOTICE_File.txt
│   └── Open_Source_Policy.md
├── Agreements/
│   ├── NDAs_with_Employees.pdf
│   ├── Contractor_Work_for_Hire.pdf
│   └── Third_Party_Licenses.xlsx
└── Domains/
    ├── Domain_List.xlsx
    └── Registrar_Access_Creds.txt (buyer to verify)
```

---

## **Pre-Dataroom Checklist:**

- [ ] Patent assignment agreements signed & filed with USPTO (if USA patents)
- [ ] All trademarks renewed or renewal in progress
- [ ] Copyright notices updated (current year)
- [ ] Open-source compliance report zero-GPL confirmed
- [ ] All domains transferred to company ownership
- [ ] IP indemnification insurance quote obtained
- [ ] No pending litigation or cease & desist letters
- [ ] Employee IP assignments reviewed (old employees?)

---

## **What Buyer Will Do (Assume):**
1. Run `npm audit` / `pip safety` / `mvn license:check`
2. Check USPTO, WIPO, EUIPO databases for all registered IP
3. Review GitHub for accidental public commits
4. Ask for IP indemnification insurance
5. Reduce offer by 30% if GPL found in proprietary code

