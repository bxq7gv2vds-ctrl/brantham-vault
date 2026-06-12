---
name: ma-tech-due-diligence-framework
description: Framework de due diligence technique rapide pour acquisitions SaaS
type: pattern
created: 2026-06-12
---

# Framework de Due Diligence Technique Rapide (48h)

## Objectif
Évaluer la viabilité technique et les coûts d'intégration d'une cible SaaS en 48h maximum pour décision d'acquisition.

---

## Phase 1 : Audit Architectural (4h)

### 🔍 Stack Technology
- **Frontend** : Framework, version, état de maintenance
- **Backend** : Language, framework, architecture (monolith/microservices)
- **Database** : Type, scaling, complexité des schémas
- **Infrastructure** : Cloud provider, auto-scaling, CI/CD

### 📊 Architecture Scorecard
| Catégorie | Critère | Score (0-5) | Notes |
|-----------|---------|-------------|-------|
| **Modularité** | High coupling | | |
| **Scalabilité** | Horizontal scaling | | |
| **Documentation** | API docs, architecture | | |
| **Tests** | Coverage >70% | | |
| **Maintenabilité** | Technical debt | | |

**Indicateur rouge** : Score <12/25

---

## Phase 2 : Security Review (6h)

### 🔐 Sécurité de base
- **HTTPS/TLS** : Certificats valides, HSTS
- **Authentification** : OAuth2/JWT, refresh tokens
- **Autorisation** : RBAC, granularité
- **Données sensibles** : Encryption at rest/transit
- **Vulnérabilités** : CVE récentes, patching <30j

### 🛡️ Checklist Sécurité
- [ ] OWASP Top 10 audit récent
- [ ] GDPR compliance documentée
- [ ] Incidents de sécurité <6 mois
- [ ] Pen test annuel validé
- [ ] Backup/testing recovery

**Indicateur rouge** : 3+ items non conformes

---

## Phase 3 : Performance & Scalability (6h)

### ⚡ Performance critique
- **API latency** : P95 <200ms
- **Database queries** : Slow queries >1%
- **Cache strategy** : Redis/Memcached efficace
- **CDN usage** : Static assets optimisés
- **Error rates** : <0.1% 30j

### 📈 Scalabilité test
- **Load testing** : 10x current load
- **Database scaling** : Read/write replicas
- **Auto-scaling** : Horizontal scaling testé
- **Cost efficiency** : Cost per user <€5/mois

---

## Phase 4 : Integration Assessment (8h)

### 🔄 Integration points
| Service | Cible | Brantham | Complexité | Impact |
|---------|-------|----------|------------|--------|
| **Auth** | SSO | Okta/Clerk | | |
| **Payment** | Stripe | Adyen | | |
| **API** | REST/GraphQL | Standard | | |
| **Analytics** | Mixpanel | Amplitude | | |
| **Storage** | AWS S3 | Backblaze | | |

### 💰 Coûts d'intégration estimés
- **Development** : Jours-homme nécessaires
- **Infrastructure** : Coûts mensuels additionnels
- **Licenses** : Logiciens supplémentaires
- **Downtime** : Perte de revenus estimée

**Seuil acceptable** : <6 mois de revenue target

---

## Phase 5 : Risk Matrix (4h)

### 🎯 Technical Risk Assessment

| Risque | Probabilité | Impact | Mitigation |
|--------|-------------|--------|------------|
| **Data migration** | M | H | API layer abstraction |
| **API breaking changes** | L | H | Versioning strategy |
| **Performance degradation** | M | M | Load testing + CDN |
| **Security gaps** | L | H | Security review team |
| **Team retention** | H | H | Integration bonus |

### 🚨 Risk Triggers
- **High risk** : >2 high-impact items
- **Medium risk** : >3 medium-impact items  
- **Low risk** : <2 medium-impact items

---

## Phase 6 : Business Case (6h)

### 📊 Technical Value Proposition
- **Revenue impact** : Upsell/cross-sell potential
- **Cost savings** : Infrastructure optimization
- **Speed to market** : Feature acceleration
- **Talent acquisition** : Key engineers retained

### 💼 Deal Structure Impact
- **Earn-out** : Technical milestones
- **Payment terms** : Integration-dependent
- **Warranties** : Technical representations

---

## Red Flags - Deal Breakers

### ❌ Non-négociables
- Technical debt >30%
- Security incident <3 mois
- Single vendor dependency >50%
- No documentation
- Team turnover >25%

### ⚠️ High Risk (>6 mois integration)
- Legacy monolith without modernization plan
- Complex data migration (>10TB)
- High operational complexity
- No automated testing

---

## Success Metrics Post-Acquisition

| KPI | D+30 | D+90 | D+180 |
|-----|------|------|-------|
| **Uptime** | >99% | >99.5% | >99.9% |
| **API latency** | <250ms | <200ms | <150ms |
| **Integration cost** | <20% budget | <15% budget | <10% budget |
| **Feature delivery** | 1/mois | 2/mois | 3/mois |

---

## Related
[[_system/MOC-patterns]]
[[brantham/_MOC]]
[[ma-analysis-template]]