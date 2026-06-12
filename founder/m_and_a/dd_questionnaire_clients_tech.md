---
title: Due Diligence Questionnaires (Clients & Tech)
created: 2026-06-12
category: diligence
status: active
---

# Due Diligence Questionnaires — Clients & Tech

**Usage** : Envoyer aux targets pendant LOI phase. Réponses = décision go/no-go.

---

## PARTIE A : Questionnaire Clients (pour vendor calls)

### A1. Revenue & Concentration
```
1. Nombre total de clients actifs (dernier 30j)?
2. Top 10 clients = X% du revenu? (red flag si >50%)
3. Churn mensuel (%) sur derniers 12 mois (moyen & volatilité)?
4. Customers acquired via: a) Organic b) Sales c) Resellers (%)
5. Customers perdue dans les 12 derniers mois (liste noms + raisons)?
6. Customer acquisition cost (CAC payback period en mois)?
7. Customers contractuel > 12 mois (%) vs month-to-month (%)?
```

### A2. Expansion & Upsell
```
8. Net revenue retention (NRR) sur T-1 year? (ex: 118%)
9. Gross revenue retention (GRR)? (ex: 94%)
10. Expansion revenu (%) = NRR - 100 (ex: 18%)?
11. Customers avec multiple products (%) ou seat expansion?
12. ASP (average selling price) par tier (Basic, Pro, Enterprise)?
13. Enterprise deals (définition?): nombre & pipeline?
```

### A3. Satisfaction & Product
```
14. NPS (Net Promoter Score) actuel & trend 12 mois?
15. Customer satisfaction (CSAT) ou Customer effort score?
16. Support ticket volume / month? Moyenne response time?
17. Feature requests top 10 (customer-facing roadmap)?
18. Integration partners (Slack, Zapier, native APIs)?
```

---

## PARTIE B : Questionnaire Technique (pour CTO/VP Eng)

### B1. Architecture & Scale
```
1. Langage(s) principal(aux) (versions: Python 3.11? Node 20? Old Rails 4?)
2. Frameworks & dépendances clés (Django, FastAPI, Next.js, etc)?
3. Primary database(s) (PostgreSQL version? MySQL? MongoDB? Multi-region?)
4. Current infrastructure:
   a) Cloud provider(s) (AWS/GCP/Azure? Multi-cloud?)
   b) Regions deployed (US-only? EU for GDPR?)
   c) Estimated monthly cloud bill?
   d) On-premise systems (si applicable)?
5. Load:
   a) Current monthly API calls / requests?
   b) Peak concurrent users?
   c) Database size (GB)?
   d) Expected growth rate (3x/year? 10x?)?
6. Can it scale?
   a) Load tested @ what multiplier (2x? 5x? 10x peak)?
   b) Auto-scaling configured (Kubernetes? AWS ASG?)?
   c) Database replication / failover tested?
```

### B2. Security & Compliance (critical!)
```
7. Security audit in last 12 months? (type: internal/external? Results?)
8. Penetration testing? When? Findings resolved?
9. OWASP Top 10: how many are mitigated?
10. ISO 27001? SOC 2? HIPAA? GDPR compliance status?
    a) Certifications completed (%)?
    b) Timeline to full compliance?
11. Data encryption:
    a) In-transit (TLS version)?
    b) At-rest (AES-256? Database encryption?)?
    c) Customer data separation (multi-tenancy)?
12. Identity & access:
    a) IAM system (AWS IAM, Okta, custom)?
    b) MFA enabled for all admins?
    c) SSH key management (rotation policy)?
    d) Service account credentials (how managed)?
13. Vendor/supplier data sharing (APIs to 3rd parties?)
14. Known CVEs or unresolved vulnerabilities?
15. Data retention policy (how long? Customer deletion honored?)
```

### B3. Code Quality & Tech Debt
```
16. Test coverage:
    a) Unit tests (%)? Coverage tool?
    b) Integration tests (%)? E2E tests?
    c) Test execution time (full suite in X minutes)?
17. Code review process (pre-merge? Standards?)?
18. Tech debt backlog (estimated story points)?
19. Deprecated technologies (Flash, Java 8, Python 2, etc)?
20. Documentation:
    a) Architecture diagrams (current & up-to-date)?
    b) API documentation (Swagger/OpenAPI)?
    c) Runbooks for common operations?
    d) Deployment procedures documented?
21. Open source dependencies:
    a) Total number of dependencies?
    b) Any GPL/AGPL (viral licenses)?
    c) Dependency audit tool (Snyk, FOSSA)?
    d) EOL/unmaintained packages?
```

### B4. Operations & Monitoring
```
22. Monitoring & observability:
    a) Logging (ELK, Datadog, Splunk)?
    b) Metrics (Prometheus, Datadog)?
    c) Tracing (Jaeger, Datadog)?
    d) Alerting rules (automated pages)?
23. Incident response:
    a) On-call rotation (who? Hours covered?)?
    b) SLA uptime targets (%)?
    c) Last major incident (what, when, RCA done?)?
24. Disaster recovery:
    a) RPO (recovery point objective) target?
    b) RTO (recovery time objective) target?
    c) Backup strategy (daily? Encrypted? Off-site)?
    d) Recovery drill last performed (when)?
25. CI/CD pipeline:
    a) Tool (GitHub Actions, GitLab, Jenkins)?
    b) Deployment frequency (daily? Weekly?)?
    c) Automated testing in pipeline?
    d) Rollback procedure (how fast?)?
```

### B5. Vendor/Integration Risk
```
26. Critical 3rd-party dependencies:
    a) List all APIs called in production (Stripe, Twilio, SendGrid, etc)
    b) Fallback if vendor goes down?
    c) License terms (do they allow usage transfer post-M&A)?
27. Data residency:
    a) Customer data stored where (EU, US, etc)?
    b) GDPR DPA in place?
    c) Data localization requirements for customers?
28. Future platform migration:
    a) Difficult to migrate away from current stack?
    b) Custom infrastructure ("cattle" vs "pets")?
```

---

## PARTIE C : Quick scoring template

| Dimension | Score (1-5) | Risky if <4 |
|-----------|-------------|------------|
| **Clients** | | |
| Revenue concentration | ? | Top 10 >60% |
| Churn stability | ? | >10% monthly |
| NRR positive | ? | <100% |
| Product-market fit | ? | NPS <30 |
| **Tech** | | |
| Security baseline | ? | No audit, CVEs open |
| Scalability | ? | Can't 5x |
| Code quality | ? | <50% test coverage |
| Tech debt | ? | >20% story pts debt |
| Monitoring | ? | No alerting |

---

## PARTIE D : Sending & Follow-up

**Timeline** :
- **Day 1 (LOI signed)** : Send questionnaires
- **Day 5-7** : First drafts due
- **Day 10-14** : Deep dives (call with CTO, customer calls)
- **Day 21** : Final answers + remediation plan (if red flags)

**Pro tip** : Don't accept vague answers. "Good" = not acceptable. Want specifics.
- ❌ "We scale well"
- ✅ "Tested up to 5x peak load. Horizontal scaling on Kubernetes. RDS Multi-AZ."

---

## Key decision triggers (go/no-go)

**Automatic NO-GO** :
- [ ] Top customer = >60% revenue (customer concentration risk)
- [ ] Churn >15% month-over-month (trending worse?)
- [ ] Known critical CVE unpatched (security risk)
- [ ] No tests, no monitoring (operational risk)
- [ ] Key engineer leaving post-deal (talent risk)
- [ ] Illegal licensing (GPL code in proprietary product)

**Automatic YELLOW FLAG** (proceed with caution):
- [ ] NRR 100-110% (flat growth)
- [ ] Tech debt >25% of capacity
- [ ] Scaling tested only to 2x (risky)
- [ ] No backup/DR tested in 12+ months
- [ ] Customer satisfaction declining

**Green light if**:
- ✅ NRR >115%, churn <5%, NPS >40
- ✅ Security audit clean or clear remediation plan
- ✅ Scales to 5x+
- ✅ Test coverage >70%
- ✅ Key team stays (earn-outs signed)
## Related
## Related
## Related
