#!/usr/bin/env python3
"""Télécharge les PDFs des offres pour les 11 nouveaux dossiers TC Paris."""
import json
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path

BASE = "https://ow-offres-de-reprises.greffe-tae-paris.fr"
DOWNLOAD_URL = f"{BASE}/fr/download"
OUT_ROOT = Path("/Users/paul/Downloads/Dossiers Entreprises Nouveaux 2026-05-15")
OUT_ROOT.mkdir(exist_ok=True)

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15"

NEW_DOSSIERS = [
    (26, 159513, "SA MAISON MINELLI"),
    (32, 159816, "SARL SCOOT PARIS 16"),
    (40, 161149, "SAS FAIRSPACE"),
    (46, 161825, "SAS PETRUS"),
    (47, 161842, "SAS MGL"),
    (52, 162478, "SARL DES PLANCHES"),
    (57, 162985, "SAS ARANA FACILITIES"),
    (59, 163068, "SARL ARLO"),
    (61, 163093, "SAS DIGITAL COLLEGE"),
    (62, 163481, "SAS AXIOVAL"),
    (63, 163519, "SAS TEHTRI SECURITY"),
]


def http_get(url, referer=None):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Referer": referer or BASE})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()


def http_post(url, data, referer):
    body = urllib.parse.urlencode(data).encode()
    req = urllib.request.Request(
        url, data=body,
        headers={
            "User-Agent": UA,
            "X-Requested-With": "XMLHttpRequest",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json",
            "Referer": referer,
        }
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read())


def safe_filename(name):
    name = re.sub(r"[^\w\s.-]", "_", name)
    return re.sub(r"\s+", "_", name).strip("_")


def fetch_offers_for(co_id, position, nom):
    folder_name = f"{position:02d} - {nom}"
    out_dir = OUT_ROOT / folder_name
    out_dir.mkdir(exist_ok=True)
    detail_url = f"{BASE}/fr/societe/{co_id}"
    print(f"\n=== {folder_name} (ID {co_id}) ===")
    print(f"  → {detail_url}")
    html = http_get(detail_url).decode("utf-8", errors="ignore")
    # Extract gd values
    gds = re.findall(r'data-co="' + str(co_id) + r'"[^>]*data-gd="(\d+)"', html)
    # Also try reverse order
    gds += re.findall(r'data-gd="(\d+)"[^>]*data-co="' + str(co_id) + r'"', html)
    gds = list(dict.fromkeys(gds))  # dedup keep order
    print(f"  Offres détectées : {len(gds)}")
    if not gds:
        # Save the raw HTML for inspection
        (out_dir / "_page.html").write_bytes(html.encode("utf-8", errors="ignore"))
        print("  ⚠️ Aucune offre — HTML sauvegardé")
        return
    for i, gd in enumerate(gds, 1):
        try:
            resp = http_post(DOWNLOAD_URL, {"co": co_id, "gd": gd}, referer=detail_url)
            redirect = resp.get("redirect_to")
            if resp.get("msg_err") or not redirect:
                print(f"  [{i}] gd={gd} ERR: {resp.get('msg_err')}")
                continue
            pdf_bytes = http_get(redirect, referer=detail_url)
            fname = f"offre_{i:02d}_gd{gd}.pdf"
            (out_dir / fname).write_bytes(pdf_bytes)
            print(f"  [{i}] gd={gd} → {fname} ({len(pdf_bytes)//1024} KB)")
            time.sleep(0.3)
        except Exception as e:
            print(f"  [{i}] gd={gd} EXCEPTION: {e}")


if __name__ == "__main__":
    for pos, co_id, nom in NEW_DOSSIERS:
        try:
            fetch_offers_for(co_id, pos, nom)
        except Exception as e:
            print(f"  ⚠️ ERREUR {nom}: {e}")
        time.sleep(0.5)
    print(f"\n✓ Terminé. Folder : {OUT_ROOT}")
