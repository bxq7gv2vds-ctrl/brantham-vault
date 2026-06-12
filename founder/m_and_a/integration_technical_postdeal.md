---
title: Checklist Intégration Technique Post-Acquisition
created: 2026-06-12
category: post-deal
status: active
---

# Checklist Intégration Technique Post-Acquisition

**Usage** : Planifier l'intégration tech sur 90-180 jours. À remplir PENDANT diligence (pas après closing).

---

## Phase 1 : Pré-closing (30 jours avant signature)

### Infrastructure & DevOps
- [ ] Mapping complet infra cible (clouds: AWS/GCP/Azure? Regions? Data centers?)
- [ ] Coûts mensuels infrastructure (serveurs, DB, CDN, backups)
- [ ] Scaling capacity : peut supporter 2x/5x/10x trafic?
- [ ] Disaster recovery / backup strategy documentée?
- [ ] Monitoring & alerting en place (Datadog/New Relic/Prometheus)?
- [ ] CI/CD pipeline (GitHub Actions/GitLab/Jenkins)? Frequency? Tests?

### Sécurité & Compliance (critiques!)
- [ ] Audit de sécurité réalisé (pen test, vulnérabilités connues)?
- [ ] ISO 27001 / SOC 2 / GDPR compliance status?
- [ ] Data encryption (in transit, at rest)? Standards (TLS 1.3, AES-256)?
- [ ] Access control (IAM, MFA, SSH keys management)?
- [ ] Dependency scanning (npm/pip audit, software composition)? Known CVEs?
- [ ] GDPR Data Processing Agreement en place?
- [ ] Customer data location & residency requirements?

### Codebase & Debt
- [ ] Langage principal(s) + frameworks (Python 3.x? Node.js 20? Old Rails 4?)
- [ ] Code review standard + test coverage (unit tests: %, integration tests?)
- [ ] Tech debt inventory (legacy systems, EOL frameworks, hardcoded config)
- [ ] Documentation quality (README, architecture diagrams, runbooks?)
- [ ] Open source dependencies : aucune AGPL/GPL surprises?

### Databases & Data
- [ ] Primary DB(s) (PostgreSQL, MongoDB, MySQL version?)
- [ ] Replication / failover strategy (master-slave? Multi-region?)
- [ ] Backup schedule & recovery test (RPO/RTO documented?)
- [ ] Data migration tools ready (CDC, ETL)?
- [ ] Customer data separation / multi-tenancy architecture?

---

## Phase 2 : Days 1-30 Post-Closing

### Immediate security lockdown
- [ ] Change all secrets/API keys (GitHub, AWS, Stripe, etc)
- [ ] Rotate database credentials
- [ ] Review VPN/SSH access logs (alert on anomalies)
- [ ] Revoke contractor/vendor access (except retained employees)
- [ ] Enable MFA on all admin accounts

### Snapshot baseline
- [ ] Git clone all repositories (archive to S3)
- [ ] Database backups (separate off-site)
- [ ] Code dependencies frozen (requirements.txt, package-lock.json, Gemfile.lock)
- [ ] Docker images tagged & stored
- [ ] Full system configuration export (Terraform, CloudFormation, etc)

### Team onboarding
- [ ] Tech lead assigned (single throat to choke)
- [ ] Engineering team integrations (Slack, GitHub, Jira, wiki access)
- [ ] Architecture walkthrough session(s)
- [ ] Production runbook review (who on-call? Alert procedures?)
- [ ] Disaster recovery drill (can you restore from backup?)

---

## Phase 3 : Days 30-90 (Migration prep)

### Merge pipelines (if consolidating platforms)
- [ ] Feature parity assessment (what does target do that acquirer doesn't?)
- [ ] API compatibility layer planned (wrap old API to new? Migrate customers?)
- [ ] Data model alignment (schema diff, ETL process if different DBs)
- [ ] Authentication/identity merge (single sign-on planned?)

### Performance & observability
- [ ] Baseline metrics captured (latency p50/p95/p99, error rate, throughput)
- [ ] Logging standardized (log format, centralized log storage)
- [ ] Metrics & alerting ported to acquirer's stack
- [ ] SLA goals defined (target uptime, response time)

### Scaling plan
- [ ] Load testing completed (target system @ 5x peak load)
- [ ] Database query optimization identified (slow queries logged)
- [ ] Caching strategy (Redis, CloudFlare, application-level?)
- [ ] Auto-scaling rules configured (CPU/memory thresholds)

### Vendor integrations
- [ ] List all 3rd-party APIs used (Stripe, Twilio, SendGrid, etc)
- [ ] API keys/creds inventory & rotation plan
- [ ] License audit (paid services; do contracts allow transfer?)
- [ ] Duplicate service elimination (e.g., two email providers? Keep one.)

---

## Phase 4 : Days 90-180 (Execution)

### Platform consolidation (if required)
- [ ] Decide: keep separate systems or merge immediately?
- [ ] If merging: data migration test on copies first (rollback plan)
- [ ] Customer notification 4 weeks before migration
- [ ] Feature flag strategy (dark launch new combined system)
- [ ] Rollback plan documented (if migration fails, revert in <2 hours)

### Modernization (optional but useful)
- [ ] Dependencies updated (security patches at minimum)
- [ ] Tech debt backlog prioritized (what kills future velocity?)
- [ ] Documentation filled (architecture diagrams, runbooks for common tasks)
- [ ] Test coverage improved (target: >80% unit test coverage)

### Operational readiness
- [ ] On-call rotation established (who handles 3am pages?)
- [ ] Incident response playbook (post-mortems, blameless culture)
- [ ] Cost optimization reviewed (are we overpaying on infra?)
- [ ] Backup & DR tested again (2+ full recoveries from backup)

---

## Phase 5 : Day 180+ (Steady state)

### Decommission redundancy
- [ ] Old infrastructure retired (save $$)
- [ ] Duplicate databases consolidated
- [ ] Redundant tools/licenses cancelled
- [ ] Legacy code removed (if safe)

### Team structure
- [ ] Clear ownership (who owns each service/team?)
- [ ] Promotion pathways (talent retention)
- [ ] Training/onboarding documented (for future hires)

---

## Red flags caught during integration

🚩 **If you discover**:
- Critical unpatched CVEs in dependencies
- No automated tests (manual QA only)
- Customer data in plaintext or unencrypted
- Undocumented integrations (black box systems)
- Key engineer planning to leave post-deal

**Action**: Escalate to leadership, adjust timeline/risk tolerance.

---

## Template: Integration timeline Gantt

```
Week 1-2    [=] Security lockdown
Week 2-4    [=====] Baseline snapshot & team onboarding
Week 4-8    [=========] Architecture walkthrough, dev env setup
Week 8-12   [=====] Load testing, performance baseline
Week 12-16  [=====] Data migration prep (if consolidating)
Week 16-26  [===========] Platform consolidation OR parallel running
Week 26+    [=====] Decommission old systems, optimize costs
```

---

## Ownership & Handoff

| Role | Responsibility | Deadline |
|------|-----------------|----------|
| **CTO/VP Eng** | Technical roadmap, architecture decisions | Day 30 |
| **DevOps/Infra** | Infrastructure consolidation | Day 90 |
| **Security** | Vulnerability assessment, compliance | Day 30 |
| **Data/Analytics** | Data migration, ETL pipelines | Day 90 |
| **Product** | Feature parity assessment | Day 14 |

---

## Key insight

**Don't automate integration before understanding**. Spend 30-60 days in "read mode" (observe, document), then consolidate with high confidence.
