---
date: 2026-03-20
status: resolved
tags: [dns, email, google-workspace, dkim, mx]
---

# Fix DNS email branthampartners.fr

## Probleme
- MX record pointait vers `smtp.google.com` (serveur SMTP sortant, pas de reception)
- DKIM absent — mails sortants risquaient le spam
- DMARC rua pointait vers `tonemail@brantham-partners.fr` (domaine inexistant)
- Note: le domaine est `branthampartners.fr` (sans tiret), pas `brantham-partners.fr`

## Fix applique
1. Remplace MX `smtp.google.com` par les 5 MX Google Workspace corrects (ASPMX.L.GOOGLE.COM etc.)
2. Ajoute record DKIM `google._domainkey` TXT genere depuis Google Admin Console
3. Active l'authentification DKIM dans Google Admin
4. Corrige DMARC rua vers `paul@branthampartners.fr`

## Boites mail sur le domaine
- paul@branthampartners.fr
- soren.mendy@branthampartners.fr

## Records DNS finaux
- A: 76.76.21.21 (Vercel)
- CNAME www: cname.vercel-dns.com
- MX: 5 records Google Workspace (priorite 1/5/5/10/10)
- TXT SPF: `v=spf1 include:_spf.google.com ~all`
- TXT DKIM: `google._domainkey` (RSA 2048)
- TXT DMARC: `v=DMARC1; p=none; rua=mailto:paul@branthampartners.fr`
- TXT: google-site-verification

## Related
- [[brantham/_MOC]]
- [[remember/2026-03-20]]
