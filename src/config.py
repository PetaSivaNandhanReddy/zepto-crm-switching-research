"""Central configuration: paths, column map, constructs, pre-specified hypotheses.

All paths are relative to the project root so the project runs on any machine.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW_CSV = ROOT / "data" / "raw" / "Quick-Commerce_Survey.csv"
CLEAN_DIR = ROOT / "data" / "cleaned"
PROC_DIR = ROOT / "data" / "processed"
TABLES = ROOT / "outputs" / "tables"
FIGS = ROOT / "outputs" / "figures"
STATS = ROOT / "outputs" / "statistical_results"
REPORTS = ROOT / "outputs" / "reports"
DOCS = ROOT / "documentation"
LIT = ROOT / "literature"
SEC = ROOT / "secondary_data"

SEED = 20260929
ALPHA = 0.05
BOOT = 5000

# position (0-based) of each raw column -> clean name, role
COLS = [
    ("timestamp", "Timestamp"),
    ("platforms_used", "Which quick-commerce platforms have you used?"),
    ("qc_frequency", "How frequently do you use quick-commerce platforms?"),
    ("choice_factor", "What factor most influences your choice of a quick-commerce platform?"),
    ("ever_used_zepto", "Have you ever used Zepto?"),
    ("SAT1", "Overall, I am satisfied with my experience using Zepto."),
    ("SAT2", "My experience using Zepto generally meets my expectations."),
    ("PUSH_consider", "Some aspects of my Zepto experience make me consider using another quick-commerce platform."),
    ("ALT1", "Other quick-commerce platforms can better meet some of my needs than Zepto."),
    ("ALT2", "I find some competing quick-commerce platforms more attractive than Zepto."),
    ("VAR1", "Competing quick-commerce platforms offer product choices that better meet my needs."),
    ("VAR2", "Competing platforms provide a wider range of brands or product variants that are relevant to me."),
    ("PROMO1", "Deals and promotional offers on competing quick-commerce platforms are more attractive to me than those on Zepto."),
    ("SC1", "Switching from Zepto to another quick-commerce platform would require additional time and effort."),
    ("FAM1", "My familiarity with Zepto makes me less likely to switch to another platform."),
    ("SC2", "The effort involved in changing to another quick-commerce platform makes me less likely to switch."),
    ("INT1", "I am considering switching from Zepto to another quick-commerce platform."),
    ("INT2", "I am likely to choose another quick-commerce platform instead of Zepto in the future."),
    ("INT3", "I intend to reduce my use of Zepto and use competing platforms more often."),
    ("shifted_any", "Have you shifted any of your regular quick-commerce purchases from Zepto to another platform?"),
    ("INERT1", "I would continue using Zepto even when other quick-commerce platforms are available."),
    ("fu_reasons", "Why did you stop using Zepto regularly?"),
    ("fu_destination", "Which platform did you primarily shift to after using Zepto?"),
    ("fu_main_reason", "What was the single most important reason for your shift from Zepto?"),
    ("fu_increased_other", "After moving away from Zepto, did you increase your use of another quick-commerce platform?"),
    ("fu_alt_variants", "Did the alternative platform offer products or variants that you could not easily find on Zepto?"),
    ("fu_return", "Would you consider returning to Zepto in the future?"),
    ("nu_reason", "What is the main reason you have never used Zepto?"),
    ("nu_platform", "Which quick-commerce platform do you use most often?"),
    ("nu_pref_reason", "What is the main reason you prefer your current platform over Zepto?"),
    ("nu_current_better", "The quick-commerce platform I currently use better meets my needs than Zepto would."),
    ("nu_consider_trying", "I would consider trying Zepto if it offered benefits that better matched my needs."),
    ("nu_what_would", "What could make you consider trying Zepto?"),
    ("age_group", "What is your age group?"),
    ("occupation", "What is your occupation?"),
    ("location_type", "Location type"),
    ("monthly_spend", "Approximate monthly spending on quick-commerce"),
]
CLEAN_NAMES = [c for c, _ in COLS]

CURRENT_LIKERT = ["SAT1", "SAT2", "PUSH_consider", "ALT1", "ALT2", "VAR1", "VAR2",
                  "PROMO1", "SC1", "FAM1", "SC2", "INT1", "INT2", "INT3", "INERT1"]
FORMER_BLOCK = ["fu_reasons", "fu_destination", "fu_main_reason", "fu_increased_other"]
FORMER_BLOCK_EXT = FORMER_BLOCK + ["fu_alt_variants", "fu_return"]
NEVER_BLOCK = ["nu_reason", "nu_platform", "nu_pref_reason", "nu_current_better",
               "nu_consider_trying", "nu_what_would"]
COMMON_NEW_LATER = ["VAR2", "INERT1", "fu_alt_variants", "fu_return", "location_type", "monthly_spend"]

GROUP_MAP = {
    "Yes, I currently use Zepto": "Current",
    "Yes, I used Zepto previously but do not currently use it": "Former",
    "No, I have never used Zepto": "Never",
}
RETURN_MAP = {"Definitely No": 1, "Probably no": 2, "Not Sure": 3, "Probably Yes": 4, "Definitely Yes": 5}
AGE_ORDER = ["18–24", "25–34", "35–44", "45 and above"]
SPEND_ORDER = ["Less than ₹500", "₹500–₹1,000", "₹1,001–₹2,000", "₹2,001–₹5,000", "More than ₹5,000"]
FREQ_ORDER = ["I don't currently use quick-commerce platforms", "Rarely", "2–3 times a month",
              "About once a week", "Several times a week", "Daily"]

# Questionnaire versions by response number (1-based row order = chronological order): V1 = 1-16, V1.5 = 17-22, V2 = 23-184
def version_of(resp_id: int) -> str:
    if resp_id <= 16:
        return "V1"
    if resp_id <= 22:
        return "V1.5"
    return "V2"

# ---------------------------------------------------------------------------
# Construct definitions (current users). Items are averaged over available items.
# ---------------------------------------------------------------------------
CONSTRUCTS = {
    "SAT":      dict(items=["SAT1", "SAT2"], ppm="Push", label="Satisfaction / expectation fulfilment"),
    "ALT":      dict(items=["ALT1", "ALT2"], ppm="Pull", label="Alternative attractiveness"),
    "VAR":      dict(items=["VAR1", "VAR2"], ppm="Pull", label="Competitor product choice/variety"),
    "PROMO":    dict(items=["PROMO1"], ppm="Pull", label="Competitor promotional attractiveness"),
    "SWEFFORT": dict(items=["SC1", "SC2"], ppm="Mooring", label="Switching effort (cost)"),
    "FAM":      dict(items=["FAM1"], ppm="Mooring", label="Familiarity"),
    "INERT":    dict(items=["INERT1"], ppm="Mooring", label="Inertia / continued-use tendency"),
    "PULL":     dict(items=["ALT1", "ALT2", "VAR1", "VAR2", "PROMO1"], ppm="Pull", label="Pull composite (5 items)"),
    "INT":      dict(items=["INT1", "INT2", "INT3"], ppm="Outcome", label="Switching intention"),
}

# ---------------------------------------------------------------------------
# PRE-SPECIFIED HYPOTHESES (written before any test result was inspected).
# Decision rule: Supported iff direction as expected AND Holm-adjusted p < .05
# within the family H1-H7; otherwise "Not supported / insufficient evidence".
# ---------------------------------------------------------------------------
HYPOTHESES = [
    dict(id="H1", construct="SAT", ppm="Push", expected="-", outcome="INT",
         text="Satisfaction/expectation fulfilment is negatively associated with switching intention.",
         literature="Bansal et al. 2005 (dissatisfaction as push); Hsieh et al. 2012",
         items="SAT1, SAT2"),
    dict(id="H2", construct="ALT", ppm="Pull", expected="+", outcome="INT",
         text="Alternative attractiveness is positively associated with switching intention.",
         literature="Bansal et al. 2005; Hsieh et al. 2012; Chang et al. 2023 (pull significant)",
         items="ALT1, ALT2"),
    dict(id="H3", construct="VAR", ppm="Pull", expected="+", outcome="INT",
         text="Perceived competitor product choice/variety is positively associated with switching intention.",
         literature="Pull/alternative-attractiveness tradition; fresh-food e-commerce PPM (WHICEB 2025)",
         items="VAR1, VAR2"),
    dict(id="H4", construct="PROMO", ppm="Pull", expected="+", outcome="INT",
         text="Perceived competitor promotional attractiveness is positively associated with switching intention.",
         literature="Pull factors in platform switching (Chang et al. 2023; e-grocery PPM 2023)",
         items="PROMO1"),
    dict(id="H5", construct="SWEFFORT", ppm="Mooring", expected="-", outcome="INT",
         text="Perceived switching effort is negatively associated with switching intention.",
         literature="Burnham et al. 2003; Bansal et al. 2005; Chang et al. 2023 (mooring significant)",
         items="SC1, SC2"),
    dict(id="H6", construct="FAM", ppm="Mooring", expected="-", outcome="INT",
         text="Familiarity with Zepto is negatively associated with switching intention.",
         literature="Habit/familiarity as mooring (Bansal et al. 2005; Cui et al. 2026 on inertia)",
         items="FAM1"),
    dict(id="H7", construct="INERT", ppm="Mooring", expected="-", outcome="INT",
         text="Inertia (continued-use tendency) is negatively associated with switching intention.",
         literature="Inertia as mooring (Cui et al. 2026)", items="INERT1"),
]
EXTENSION_HYPOTHESES = [
    dict(id="H8", text="Push, Pull and Mooring composites jointly explain variance in switching intention (multiple regression, model F-test)."),
    dict(id="H9", text="Current users who report having shifted some purchases (Q19=Yes) have higher switching intention than those who have not."),
    dict(id="H10", text="Former users whose most important reason was area/coverage have higher willingness to return than former users whose most important reason was voluntary (platform-choice)."),
]
