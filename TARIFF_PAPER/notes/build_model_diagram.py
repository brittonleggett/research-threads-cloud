import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

fig, ax = plt.subplots(figsize=(14, 7.5))
ax.set_xlim(0, 14)
ax.set_ylim(0, 7.5)
ax.axis("off")


def box(x, y, w, h, text, fc="white"):
    b = FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.08,rounding_size=0.12",
        linewidth=1.6, edgecolor="black", facecolor=fc,
    )
    ax.add_patch(b)
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
             fontsize=10.5, wrap=True)
    return (x, y, w, h)


def center_right(bx):
    x, y, w, h = bx
    return (x + w, y + h / 2)


def center_left(bx):
    x, y, w, h = bx
    return (x, y + h / 2)


def center_top(bx):
    x, y, w, h = bx
    return (x + w / 2, y + h)


def center_bottom(bx):
    x, y, w, h = bx
    return (x + w / 2, y)


def arrow(p1, p2):
    a = FancyArrowPatch(p1, p2, arrowstyle="-|>", mutation_scale=16,
                         linewidth=1.4, color="black")
    ax.add_patch(a)


# Column 1: manipulated factors
attr = box(0.3, 5.3, 2.6, 1.4, "Attribution Frame\n(tariff-explicit /\ngeneral-cost-explicit /\nsilent)", fc="#eef4ff")
cost = box(0.3, 1.0, 2.6, 1.4, "Cost-Response\n(full pass-through /\nshared-burden)", fc="#eef4ff")

# Column 2: mediators
fair = box(4.0, 5.3, 2.6, 1.4, "Perceived\nPrice Fairness\n(Xia, Monroe & Cox 2004)", fc="#fff7e6")
oppo = box(4.0, 1.0, 2.6, 1.4, "Perceived\nOpportunism\n(Campbell 1999)", fc="#fff7e6")

# Column 3: trust
trust = box(7.7, 3.15, 2.4, 1.4, "Trust in the\nCompany\n(Chaudhuri &\nHolbrook 2001)", fc="#e9f9ee")

# Column 4: outcomes
pur = box(11.1, 4.6, 2.4, 1.3, "Purchase\nIntention\n(Dodds, Monroe\n& Grewal 1991)", fc="#f5eefc")
wom = box(11.1, 1.6, 2.4, 1.3, "Word-of-Mouth\nIntention\n(Maxham &\nNetemeyer 2002)", fc="#f5eefc")

# Arrows: factors -> mediators (full cross, matching the lean model)
for f in (attr, cost):
    for m in (fair, oppo):
        arrow(center_right(f), center_left(m))

# Mediators -> trust
for m in (fair, oppo):
    arrow(center_right(m), center_left(trust))

# Trust -> outcomes
arrow(center_right(trust), center_left(pur))
arrow(center_right(trust), center_left(wom))

# Section labels
ax.text(1.6, 6.9, "Manipulated (3×2 factorial)", fontsize=10, ha="center", style="italic")
ax.text(5.3, 6.9, "Mediators", fontsize=10, ha="center", style="italic")
ax.text(8.9, 6.9, "Mediator", fontsize=10, ha="center", style="italic")
ax.text(12.3, 6.9, "Outcomes", fontsize=10, ha="center", style="italic")

ax.text(7, 0.25,
        "Lean model, locked 2026-08-04 — Study 2/3, Journal of Consumer Marketing special issue \"Crafting Shape in a Fluid World\"",
        fontsize=9, ha="center", color="#444444")

plt.tight_layout()
plt.savefig("Tariff_Model_Lean_2026-08-04.png", dpi=200, bbox_inches="tight")
print("Saved diagram.")
