---
name: tech_stack_audit
description: Audit tech debt, dépendances critiques, vendeurs, risques infra
metadata:
  type: checklist
  created: 2026-06-12
---

# Tech Stack Audit — Due Diligence Ready

**Pourquoi:** Acquéreur évalue:
- Code quality → maintenance cost post-acquisition
- Vendor lock-in → switching cost
- Scalability runway → technical risk
- Security posture → liability

Bad tech assessment = -20 to -40% valuation cut

---

## **Section 1 : Architecture Overview**

Créer un **architecture diagram** simple. Template:

```
Frontend:
├─ React 18 / Vue / Next.js? (Version?)
├─ Build tool: Webpack / Vite / Parcel
└─ State: Redux / Vuex / Context API / Zustand?

Backend:
├─ Language: Node.js / Python / Go / Java? (Version?)
├─ Framework: Express / Django / FastAPI / Spring?
├─ Database: PostgreSQL / MongoDB / DynamoDB?
└─ Queue: RabbitMQ / Kafka / Redis / SQS?

Infrastructure:
├─ Host: AWS / GCP / Azure / DigitalOcean / on-premise?
├─ Containerization: Docker / Kubernetes?
├─ CI/CD: GitHub Actions / GitLab CI / Jenkins / CircleCI?
└─ Monitoring: DataDog / New Relic / CloudWatch / Prometheus?

Third-party APIs:
├─ Stripe / PayPal (payments)
├─ Twilio (SMS/voice)
├─ SendGrid (email)
└─ [Your APIs...]
```

---

## **Section 2 : Tech Debt Assessment**

### **Code Quality Metrics**

| Metric | Current | Target | Risk |
|--------|---------|--------|------|
| Test Coverage | 45% | 70%+ | LOW (fixable) |
| Cyclomatic Complexity avg | 8.5 | <5 | MEDIUM (refactoring) |
| Duplicated Code % | 12% | <5% | LOW (tooling cleanup) |
| ESLint/Lint violations | 250 | 0 | MEDIUM (code quality) |
| TypeScript adoption | 30% | 100% | HIGH (type safety gap) |

**How to measure:**
```bash
# JavaScript/TypeScript
npm install --save-dev @types/node @types/jest
npm run lint
npm run test -- --coverage

# Python
pip install pytest coverage pylint
pytest --cov
pylint src/

# Go
go vet ./...
go test -cover ./...
```

### **Tech Debt Categories**

| Category | Severity | Examples | Remediation Time |
|---|---|---|---|
| Outdated dependencies | CRITICAL | Node 12 → 18 migration | 2-4 weeks |
| Legacy frameworks | HIGH | Rails 4 → 7, Vue 2 → 3 | 2-8 weeks |
| Monolithic vs microservices | HIGH | Splitting 50K LOC | 6-12 weeks |
| Database migrations | MEDIUM | SQL schema refactoring | 2-4 weeks |
| API versioning | MEDIUM | v1 deprecated, must migrate | 1-2 weeks |
| Code duplication | LOW | Consolidate similar modules | 1-2 weeks |
| Documentation gaps | LOW | Missing API docs, README | 1 week |

### **Debt Scoring:**

```
Tech Debt Score = (Severity × Impact × Days to Fix) / 1000

< 50: Acceptable
50-100: Monitor, plan refactor
100-200: Significant, should address pre-sale
> 200: Red flag, buyer will negotiate down 20-30%
```

---

## **Section 3 : Dependency & Vendor Lock-in**

### **Critical Vendor Dependencies**

| Vendor | Service | Alternative | Switching Cost | Data Portability |
|---|---|---|---|---|
| AWS | Hosting, RDS, S3 | GCP, Azure, DO | 1-2 months | HIGH (EC2→GCP) |
| Stripe | Payments | Square, PayPal | 2 weeks | MEDIUM (API rewrite) |
| Datadog | Monitoring | New Relic, CloudWatch | 1 week | HIGH (dashboards) |
| Auth0 | Authentication | Cognito, Firebase, custom | 2-3 weeks | HIGH (user migration) |

**Checklist:**
- [ ] Single cloud vendor (AWS, GCP)? → Risk if needs multi-cloud
- [ ] Can migrate data out? (Export, API access)
- [ ] Contracts negotiable or locked 3 years?
- [ ] Pricing locked or subject to increases?

**Red flag:** All infrastructure on Heroku with no way to export → buyer trapped

---

### **Internal Dependency Matrix**

| Service | Owner | Criticality | Backup | Disaster Recovery |
|---|---|---|---|---|
| Database server | Ops Engineer A | CRITICAL | Daily backup | RTO 1hr |
| API server | Engineer B | CRITICAL | Blue-green deployment | RTO 5min |
| Image processing | Worker service | HIGH | Queue-based retry | RTO 30min |
| Admin dashboard | Frontend C | LOW | Can rebuild in 1 day | RTO 24hrs |

**Checklist for each CRITICAL service:**
- [ ] Documented runbook? (How to restart, scale, backup?)
- [ ] Monitoring alerts? (Who gets paged?)
- [ ] Backup strategy? (Frequency, tested restore?)
- [ ] Owner documented? (What if Engineer A leaves?)
- [ ] Redundancy? (Active-active, active-passive, none?)

**Red flag:** "Only Engineer X knows how to restart database" = deal stalled 2 months

---

## **Section 4 : Scalability & Performance**

### **Current Performance Baselines**

| Metric | Current | Target for 10x Scale | Gap | Risk |
|---|---|---|---|---|
| API latency (p95) | 250ms | <100ms | MEDIUM | Growth bottleneck |
| Database query time | 2s (complex) | <500ms | HIGH | Indexing needed |
| Frontend bundle size | 450KB | <200KB | MEDIUM | Treeshaking opportunity |
| Infrastructure cost % revenue | 18% | <10% | LOW | Acceptable |

**How to measure:**
```bash
# API latency
curl -w "@curl-format.txt" https://api.example.com/endpoint

# Database query time
EXPLAIN ANALYZE SELECT ...;

# Bundle size
npm run build && ls -lh dist/bundle.js

# Cloud costs
# Check: AWS Cost Explorer, GCP Billing, Azure Cost Management
```

---

### **Scalability Assessment**

| Component | Current Limit | At 10x Scale | Action |
|---|---|---|---|
| Database connections | 100 | 1000 | Add connection pooling (PgBouncer) |
| API throughput | 500 req/s | 5000 req/s | Horizontal scaling ready? |
| Storage | 100GB | 1TB | Query optimization, archiving strategy |
| Cache (Redis) | 8GB | 80GB | Eviction policy defined? |

**Red flag:** "Our database will break at 2x scale" = growth ceiling, valuation down 30%

---

## **Section 5 : Security Posture**

### **Security Audit Checklist**

- [ ] SSL/TLS certificates valid? (HTTPS everywhere)
- [ ] Secrets management: no API keys in code/env files?
- [ ] Database encryption at rest?
- [ ] Encryption in transit (TLS 1.3)?
- [ ] WAF (Web Application Firewall) configured?
- [ ] SQL injection protections? (Parameterized queries)
- [ ] XSS prevention? (CSP headers)
- [ ] CSRF tokens on forms?
- [ ] Authentication: MFA enabled for critical accounts?
- [ ] Authorization: RBAC (role-based access control)?
- [ ] Audit logging: who did what, when?
- [ ] Regular penetration testing? (Last test date)
- [ ] Vulnerability scanning: dependency audits automated?
- [ ] Incident response plan? (Breach playbook)

**Security Tools:**
```bash
npm audit
pip audit
go list -json -m all | nancy sleuth
snyk test
OWASP Top 10 checklist
```

**Red flag:** No logging, no MFA, secrets in Git history = buyer requires security audit (-20%)

---

## **Section 6 : Infrastructure Health**

### **Uptime & Reliability**

| Period | Uptime % | Incidents | MTTR (Mean Time to Recover) | RTO/RPO |
|---|---|---|---|---|
| Last 12 months | 99.5% | 3 major | 45 min | 1 hr / 15 min |
| Last 3 months | 99.8% | 0 major | — | — |

**Target SLAs:**
- Consumer SaaS: 99.5% (acceptable)
- Enterprise SaaS: 99.9% (expected)
- Mission-critical: 99.99% (required)

**Checklist:**
- [ ] Status page (public) showing historical uptime?
- [ ] SLA commitments? (If yes, are you hitting them?)
- [ ] Incident postmortems documented?
- [ ] Automated alerting & escalation?
- [ ] Load testing done? (Max concurrent users?)
- [ ] Chaos engineering? (Netflix-style failure testing?)

---

## **Section 7 : Tech Stack Version Audit**

### **Dependency Freshness**

| Dependency | Current | Latest | Lag | Update Effort |
|---|---|---|---|---|
| React | 17.0.2 | 18.2.0 | 1 year old | 2 weeks |
| Node.js | 14 | 20 | 2 years old | 1 week |
| TypeScript | 4.2 | 5.1 | 1 year old | 1 day |
| Django | 3.2 | 5.0 | 2 years old | 3 weeks |

**Buyer concern:** If you're 2+ years behind, they assume maintenance hell

**Checklist:**
- [ ] All dependencies within 1 major version of latest?
- [ ] Security patches applied within 1 week of release?
- [ ] Deprecated/EOL versions? (Node 14 → 20 migration needed)

**Red flag:** "We use Node 12, haven't updated in 3 years" = -30% valuation cut

---

## **Section 8 : Documentation**

- [ ] README with setup instructions? (Can new hire get running in 2 hours?)
- [ ] Architecture documentation? (System design doc)
- [ ] API documentation? (OpenAPI/Swagger spec?)
- [ ] Database schema documentation?
- [ ] Deployment runbook? (How to deploy, rollback?)
- [ ] Disaster recovery plan?
- [ ] Security guidelines?
- [ ] Development workflow (Git branching, review process)?

**Score each 1-5:**
```
1 = Non-existent
2 = Minimal, outdated
3 = Basic, partially outdated
4 = Good, mostly current
5 = Excellent, automated, always current
```

**Red flag:** No documentation = buyer assumes 2 weeks to onboard new team

---

## **Section 9 : Tech Stack Summary Table**

Create this table for dataroom:

| Component | Technology | Version | Status | Debt? | Risk |
|---|---|---|---|---|---|
| **Frontend** | | | | | |
| | React | 18.2 | Current | No | LOW |
| | TypeScript | 5.0 | Current | No | LOW |
| | Tailwind | 3.3 | Current | No | LOW |
| **Backend** | | | | | |
| | Node.js | 18 LTS | Current | No | LOW |
| | Express | 4.18 | Current | No | LOW |
| | PostgreSQL | 14 | Current | No | LOW |
| **Infrastructure** | | | | | |
| | AWS | — | Current | No | MEDIUM (single vendor) |
| | Docker | Latest | Current | No | LOW |
| | Kubernetes | v1.26 | Current | No | LOW |
| **Third-party** | | | | | |
| | Stripe | API v3 | Current | No | LOW |
| | Auth0 | Latest | Current | No | MEDIUM (vendor lock) |
| **Monitoring** | | | | | |
| | DataDog | Latest | Current | No | MEDIUM (cost) |

---

## **Tech Health Score Calculation**

```
Tech Health = (Debt Score + Security Score + Performance Score) / 3

< 50: POOR (significant remediation needed)
50-70: FAIR (some debt, but manageable)
70-85: GOOD (well-maintained, minor issues)
85-95: EXCELLENT (best practices, minimal debt)
95+: WORLD-CLASS (rare)

Buyer expectation for acquisition-ready startup:
- Series A funded: 70+ (acceptable)
- Series B+: 75+ (expected)
- $10M+ ARR: 80+ (required)
```

---

## **Pre-Dataroom Checklist:**

- [ ] All critical systems documented (architecture, runbooks)
- [ ] No security vulnerabilities in dependency scan
- [ ] Tech debt scored and prioritized
- [ ] Scalability assessment completed
- [ ] Uptime metrics & incident reports 12-month history
- [ ] Vendor lock-in risks identified & mitigated
- [ ] All dependencies updated within 1 major version
- [ ] README & setup instructions tested by new team member

---

## **Dataroom Folder:**

```
Tech_Stack/
├── Architecture_Diagram.pdf
├── Tech_Stack_Inventory.xlsx
├── Dependency_Audit.txt (npm/pip output)
├── Security_Assessment.md
├── Performance_Baselines.xlsx
├── Uptime_Reports_12M.pdf
├── Incident_Log_12M.md
├── Tech_Debt_Assessment.md
├── Server_Runbooks/
│   ├── Database_Setup.md
│   ├── API_Deployment.md
│   └── Disaster_Recovery.md
└── Documentation_Index.md
```
## Related
