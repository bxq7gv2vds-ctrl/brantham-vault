from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt


OUT = Path(__file__).with_name("INFRA-teaser-client.pptx")

INK = RGBColor(0x0F, 0x0F, 0x0E)
T2 = RGBColor(0x4A, 0x4A, 0x47)
T3 = RGBColor(0x8A, 0x8A, 0x86)
BORDER = RGBColor(0xD8, 0xD7, 0xD4)
OFF = RGBColor(0xF5, 0xF4, 0xF2)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)

FONT = "Cambria"
FONT_BODY = "Cambria"


def set_run(run, size=10, bold=False, italic=False, color=INK):
    run.font.name = FONT_BODY
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = color


def add_textbox(slide, x, y, w, h, text="", size=10, bold=False, italic=False, color=INK, align=PP_ALIGN.LEFT):
    box = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = box.text_frame
    tf.clear()
    tf.margin_left = Inches(0)
    tf.margin_right = Inches(0)
    tf.margin_top = Inches(0)
    tf.margin_bottom = Inches(0)
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.alignment = align
    p.space_after = Pt(0)
    run = p.add_run()
    run.text = text
    set_run(run, size=size, bold=bold, italic=italic, color=color)
    return box


def add_title(slide, number, title, subtitle=None):
    add_textbox(slide, 0.55, 0.32, 8.8, 0.34, f"{number}. {title}", size=15, bold=True)
    if subtitle:
        add_textbox(slide, 0.55, 0.70, 8.9, 0.25, subtitle, size=8.5, color=T2)
    line = slide.shapes.add_shape(1, Inches(0.55), Inches(0.98), Inches(8.9), Pt(0.8))
    line.fill.solid()
    line.fill.fore_color.rgb = INK
    line.line.color.rgb = INK


def add_footer(slide, page):
    add_textbox(slide, 0.55, 7.08, 4.0, 0.18, "Brantham Partners — document confidentiel pre-NDA", size=6.5, color=T3)
    add_textbox(slide, 9.0, 7.08, 0.45, 0.18, str(page), size=6.5, color=T3, align=PP_ALIGN.RIGHT)


def add_table(slide, x, y, w, h, headers, rows, font_size=7.1, header_size=7.2, col_widths=None):
    table_shape = slide.shapes.add_table(len(rows) + 1, len(headers), Inches(x), Inches(y), Inches(w), Inches(h))
    table = table_shape.table
    if col_widths:
        total = sum(col_widths)
        for i, cw in enumerate(col_widths):
            table.columns[i].width = Inches(w * cw / total)
    for i, header in enumerate(headers):
        cell = table.cell(0, i)
        cell.fill.solid()
        cell.fill.fore_color.rgb = WHITE
        cell.margin_left = Inches(0.04)
        cell.margin_right = Inches(0.04)
        cell.margin_top = Inches(0.02)
        cell.margin_bottom = Inches(0.02)
        p = cell.text_frame.paragraphs[0]
        p.text = header
        p.alignment = PP_ALIGN.LEFT
        for run in p.runs:
            set_run(run, size=header_size, bold=True)
    for r, row in enumerate(rows, start=1):
        for c, value in enumerate(row):
            cell = table.cell(r, c)
            cell.fill.solid()
            cell.fill.fore_color.rgb = WHITE if r % 2 else OFF
            cell.margin_left = Inches(0.04)
            cell.margin_right = Inches(0.04)
            cell.margin_top = Inches(0.015)
            cell.margin_bottom = Inches(0.015)
            p = cell.text_frame.paragraphs[0]
            p.text = str(value)
            p.alignment = PP_ALIGN.RIGHT if c > 0 and str(value).startswith(("~", "+", "-", "1", "2", "3", "4", "5", "6", "7", "8", "9")) else PP_ALIGN.LEFT
            for run in p.runs:
                set_run(run, size=font_size, bold=False, color=INK)
    for row in table.rows:
        for cell in row.cells:
            cell.vertical_anchor = MSO_ANCHOR.TOP
            for side in ("top", "bottom", "left", "right"):
                getattr(cell, side).color.rgb = BORDER
                getattr(cell, side).width = Pt(0.35)
    return table_shape


def add_lead_para(slide, x, y, w, h, lead, body, size=8.6):
    box = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = box.text_frame
    tf.clear()
    tf.margin_left = Inches(0)
    tf.margin_right = Inches(0)
    tf.margin_top = Inches(0)
    tf.margin_bottom = Inches(0)
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.space_after = Pt(0)
    r1 = p.add_run()
    r1.text = lead
    set_run(r1, size=size, bold=True)
    r2 = p.add_run()
    r2.text = " " + body
    set_run(r2, size=size, color=INK)
    return box


prs = Presentation()
prs.slide_width = Inches(10)
prs.slide_height = Inches(7.5)
blank = prs.slide_layouts[6]

# Slide 1
s = prs.slides.add_slide(blank)
s.background.fill.solid()
s.background.fill.fore_color.rgb = WHITE
add_textbox(s, 0.9, 2.20, 8.2, 0.42, "Opportunite de reprise", size=20, bold=True, align=PP_ALIGN.CENTER)
line = s.shapes.add_shape(1, Inches(3.35), Inches(2.74), Inches(3.3), Pt(0.8))
line.fill.solid()
line.fill.fore_color.rgb = INK
line.line.color.rgb = INK
add_textbox(
    s,
    1.35,
    2.98,
    7.3,
    0.92,
    "Agence francaise de communication et de production visuelle\nMarque historique du Grand Est — pres de 50 ans d'existence\nProcedure collective — fenetre de reprise a clarifier",
    size=11,
    align=PP_ALIGN.CENTER,
)
add_textbox(s, 2.8, 4.55, 4.4, 0.24, "Brantham Partners — Conseil M&A distressed", size=9.5, align=PP_ALIGN.CENTER)
add_textbox(s, 4.25, 4.92, 1.5, 0.2, "2026-05-20", size=9, align=PP_ALIGN.CENTER)
add_textbox(s, 2.8, 5.35, 4.4, 0.2, "Document confidentiel — diffusion pre-NDA", size=8.5, italic=True, color=T2, align=PP_ALIGN.CENTER)

# Slide 2
s = prs.slides.add_slide(blank)
add_title(s, "1", "L'opportunite en bref", "Profil synthetique et donnees de cadrage")
add_lead_para(
    s,
    0.55,
    1.18,
    8.9,
    0.55,
    "En une phrase.",
    "Agence-conseil integree combinant strategie de marque, production photo/video, edition print, contenu, marque employeur et digital responsable, avec une capacite historique proche de 3 M€ de chiffre d'affaires.",
    size=8.4,
)
rows = [
    ("Anciennete", "pres de 50 ans", "Marque installee, historique commercial reel"),
    ("CA pic recent", "~3,0 M€", "Niveau d'activite prouve avant decrochage"),
    ("CA dernier exercice plein", "~2,3 M€", "Activite encore significative"),
    ("CA annualise recent", "~1,8 M€", "Baisse d'environ 22% vs dernier exercice"),
    ("Effectif actuel", "18-19 salaries", "Base deja resserree vs plaquette historique"),
    ("Point mort estime", "2,4-2,6 M€ CA", "Cap operationnel clair pour le repreneur"),
]
add_table(s, 0.55, 1.95, 8.9, 2.05, ("Indicateur", "Donnee teaser", "Lecture"), rows, font_size=7.4, col_widths=(1.3, 1.15, 3.0))
add_lead_para(
    s,
    0.55,
    4.35,
    4.25,
    0.85,
    "Ce que l'on achete.",
    "Une marque ancienne, un outil de production, un portefeuille B2B probable, des savoir-faire photo/video/print/digital et une equipe deja resserree.",
    size=8.2,
)
add_lead_para(
    s,
    5.1,
    4.35,
    4.35,
    0.85,
    "These.",
    "Le dossier devient interessant si le repreneur relance le commercial, securise les contrats transferables et repositionne l'offre sur contenu, video, marque employeur et IA.",
    size=8.2,
)
add_textbox(s, 0.55, 6.15, 8.9, 0.38, "Message cle : l'actif n'est pas financierement propre, mais il dispose d'une base exploitable et d'un historique commercial rare dans son bassin.", size=8.2, italic=True, color=T2, align=PP_ALIGN.CENTER)
add_footer(s, 2)

# Slide 3
s = prs.slides.add_slide(blank)
add_title(s, "2", "Trajectoire financiere et causes DCP", "Pourquoi la societe a decroche")
finance_rows = [
    ("CA", "2 993", "2 427", "2 216", "2 312", "1 357"),
    ("EBE", "+227", "+36", "+22", "+79", "-284"),
    ("Resultat net", "+97", "-77", "-73", "-1", "-345"),
]
add_table(s, 0.55, 1.22, 8.9, 1.25, ("K€", "03/2022", "03/2023", "03/2024", "03/2025", "12/2025 9m"), finance_rows, font_size=7.7, col_widths=(1.2, 1, 1, 1, 1, 1))
cause_rows = [
    ("Dette de LBO INTRA", "Rachat 2016 via holding INTRA", "Pression financiere durable"),
    ("Budgets communication", "Conjoncture defavorable", "Contraction du CA"),
    ("Choc IA generative", "Clients pensant produire eux-memes", "Pression sur prestations simples"),
    ("Absence commerciale", "Fonction affaiblie plus d'un an", "Pipeline insuffisant"),
    ("Couts fixes rigides", "Masse salariale elevee face au CA", "EBE negatif malgre marge brute"),
    ("Tresorerie consommee", "VMP mobilisees, cash reduit", "Sauvegarde avant cessation complete"),
]
add_table(s, 0.55, 2.82, 8.9, 2.65, ("Cause DCP", "Fait constate", "Impact economique"), cause_rows, font_size=6.65, col_widths=(1.45, 2.15, 2.25))
add_lead_para(
    s,
    0.55,
    5.85,
    8.9,
    0.55,
    "Lecture.",
    "Le retournement resulte d'un effet ciseaux : baisse rapide du chiffre d'affaires, structure de couts calibree pour un niveau superieur, dette de LBO portee par la holding et choc IA sur les prestations simples.",
    size=8.0,
)
add_footer(s, 3)

# Slide 4
s = prs.slides.add_slide(blank)
add_title(s, "3", "Atouts strategiques", "Ce qui peut etre repris et reactive")
atout_rows = [
    ("Anciennete de marque", "Pres de 50 ans d'existence, credibilite locale difficile a reconstruire"),
    ("Ancrage Grand Est", "Proximite avec PME, ETI industrielles et institutions regionales"),
    ("Production integree", "Photo, video, redaction, print, digital ; capacite a produire sans tout sous-traiter"),
    ("Positionnement responsable", "Print eco-responsable, digital frugal, Green UX ; differenciation agences generalistes"),
    ("Portefeuille clients installe", "Cas clients B2B recrutement, produit, salon, institutionnel ; valeur a confirmer par contrats"),
    ("Equipe resserree", "18-19 salaries, base operationnelle deja ajustee"),
    ("Actifs incorporels", "Marque, methodologie, phototheque/videotheque, noms de domaine, fichier clients"),
    ("Cadre distressed", "Possibilite de repartir avec une structure de couts redimensionnee"),
]
add_table(s, 0.55, 1.20, 8.9, 3.25, ("Atout", "Pourquoi il a de la valeur"), atout_rows, font_size=6.8, col_widths=(1.45, 4.5))
add_lead_para(
    s,
    0.55,
    4.82,
    4.25,
    0.92,
    "Un actif historique.",
    "La valeur ne vient pas uniquement du CA actuel, mais de l'anciennete commerciale, du capital relationnel et de la capacite a reactiver une marque regionale connue.",
    size=8.0,
)
add_lead_para(
    s,
    5.1,
    4.82,
    4.35,
    0.92,
    "Un outil a repositionner.",
    "L'IA attaque les productions simples, mais ouvre une opportunite : industrialiser les contenus et vendre conseil, video, social content, marque employeur et workflows IA.",
    size=8.0,
)
add_footer(s, 4)

# Slide 5
s = prs.slides.add_slide(blank)
add_title(s, "4", "These de reprise et points de confirmation", "Levier repreneur, donnees a securiser et disclaimer")
levier_rows = [
    ("Retour vers point mort", "CA cible 2,4-2,6 M€", "Retour EBE positif"),
    ("Relance commerciale", "CA historique ~3,0 M€", "Recuperation partielle du volume"),
    ("Recalibrage social", "18-19 salaries actuels", "Reduction du cout fixe repris"),
    ("Dette historique", "PGE ~850 K€ non repris", "Bilan de reprise allege"),
    ("Charges transmises", "L.642-12 ~9,8 K€", "Faible friction bancaire directe"),
    ("Materiel revendique", "10-15 K€ remplacement", "Sujet negociable, non bloquant"),
    ("BFR redemarrage", "100-200 K€", "Besoin a anticiper dans l'offre"),
]
add_table(s, 0.55, 1.18, 8.9, 2.35, ("Levier", "Base chiffree", "Effet attendu"), levier_rows, font_size=6.9, col_widths=(1.65, 1.6, 2.25))
add_lead_para(
    s,
    0.55,
    3.85,
    8.9,
    0.56,
    "Points a confirmer avant offre.",
    "Statut procedural exact et possibilite effective de cession ; contrats clients transferables ; bail du site actuel ; etat du passif ; liste d'effectif actualisee ; actifs incorporels disponibles ; materiel revendique et contrats de leasing.",
    size=7.7,
)
add_lead_para(
    s,
    0.55,
    4.70,
    8.9,
    0.72,
    "Disclaimer.",
    "Ce document constitue une presentation preliminaire et confidentielle d'une opportunite de reprise. Il ne constitue ni une offre, ni un memorandum d'information, ni une recommandation d'investissement. Certaines informations d'identification sont volontairement omises a ce stade. Toute diffusion est interdite sans accord ecrit prealable.",
    size=7.3,
)
add_textbox(s, 0.55, 6.12, 3.8, 0.18, "Paul Roulleau — Brantham Partners", size=8.2, bold=True)
add_textbox(s, 0.55, 6.40, 4.2, 0.18, "paul.roulleau@branthampartners.fr — 07 68 36 25 63", size=7.6, color=T2)
add_footer(s, 5)

prs.save(OUT)
print(OUT)
