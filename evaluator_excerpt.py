"""Archived evaluator excerpt — retained for audit, not for reuse.

Original source location removed from this public release.
SHA-256:
  629a4236cbbe6850dedcd65198defc0f2ddbaca8e3fd948debc0a37b3071f397

Defect: self-similarity is set to -inf, but the query remains in `order` and
therefore in `rel.sum()`. With three pages per writer it becomes a third
relevant item at the final rank.
"""


def archived_core(fp, yp, torch):
    """Literal operative logic; dependency injection keeps this an excerpt."""
    fp = torch.nn.functional.normalize(fp.float(), dim=1)
    sim = fp @ fp.T
    sim.fill_diagonal_(float("-inf"))
    n = fp.shape[0]
    ar = torch.arange(1, n + 1).float()
    aps = []
    for i in range(n):
        order = sim[i].argsort(descending=True)
        rel = (yp[order] == yp[i]).float()  # self-query is still relevant
        prec = torch.cumsum(rel, 0) / ar
        aps.append(float((prec * rel).sum() / rel.sum()))
    return aps
