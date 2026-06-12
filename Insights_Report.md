# Amazon Sales 2025 — Insights Report

## Executive Summary

| KPI | Value |
|---|---|
| Total Net Revenue (valid orders) | ₹3,28,16,753 (~₹3.28 Cr) |
| Total Valid Orders | 11,268 |
| Average Order Value (AOV) | ₹2,912.38 |
| Return Rate | 7.09% |
| Cancellation Rate | 6.10% |
| Average Discount Given | 18.4% |
| Average Customer Rating | 4.04 / 5 |

---

## 1. Monthly Revenue & Seasonality

| Month | Net Revenue (₹) | MoM Growth |
|---|---|---|
| Jan | 31,78,182 | — (New Year sale spike) |
| Feb | 21,51,644 | -32.3% |
| Mar | 23,34,981 | +8.5% |
| Apr | 20,92,846 | -10.4% |
| May | 24,15,893 | +15.4% |
| Jun | 25,28,638 | +4.7% |
| Jul | 25,30,247 | +0.1% |
| Aug | 26,45,361 | +4.5% |
| Sep | 27,89,042 | +5.4% |
| Oct | 33,27,283 | +19.3% |
| Nov | 37,06,720 | +11.4% |
| Dec | 31,15,917 | -15.9% |

**Insight:** Revenue follows a clear seasonal curve — a January sale spike, a mid-year dip (Feb/Apr), and a strong **festive-season ramp from September through November** (Diwali/Big Billion Days style events), peaking in November at ₹37.07L, the highest month of the year. December tapers off post-festive.

**Recommendation:** Concentrate inventory build-up, ad spend, and seller incentives in the Sep–Nov window. The Feb/Apr dips are good windows for "mid-season sale" promotions to smooth demand.

---

## 2. Category & Product Performance

**Revenue by Category (valid orders):**

| Category | Net Revenue (₹) | % of Total |
|---|---|---|
| Electronics | 1,14,98,024 | 35.0% |
| Home & Kitchen | 65,56,171 | 20.0% |
| Office Products | 51,71,931 | 15.8% |
| Clothing | 31,40,052 | 9.6% |
| Sports & Fitness | 29,73,397 | 9.1% |
| Beauty & Personal Care | 20,36,221 | 6.2% |
| Toys & Games | 10,55,431 | 3.2% |
| Books | 3,85,528 | 1.2% |

**Insight:** Electronics alone drives over a third of total revenue. Combined with Home & Kitchen and Office Products, the top 3 categories account for ~71% of revenue — a classic Pareto pattern.

**Top 5 Products by Revenue:** Laptop Stand (₹15.6L), USB-C Cable (₹15.4L), Smartwatch (₹15.2L), Smartphone Case (₹15.0L), Power Bank (₹14.1L) — all Electronics accessories, indicating strong demand for affordable, high-frequency tech add-ons rather than big-ticket items alone.

**Recommendation:** Double down on Electronics accessory bundling (e.g., "buy a Smartwatch, get 20% off a Power Bank") and prioritize Books/Toys for clearance-style promotions given their low revenue share.

---

## 3. Geographic Performance

**Top 5 Cities by Revenue:** Hyderabad (₹28.9L), Lucknow (₹28.6L), Mumbai (₹28.2L), Kochi (₹28.1L), Delhi (₹27.9L).

**Insight:** Revenue is fairly evenly distributed across metro and tier-2 cities — no single city dominates, suggesting demand is geographically diversified rather than concentrated in traditional metros alone (Lucknow and Kochi rank alongside Mumbai and Delhi).

**Delivery speed (avg days):** Chennai (3.37), Surat (3.37), Hyderabad (3.36), Lucknow (3.36), Mumbai (3.34) are the slowest; fastest cities are closer to ~2.9–3.0 days.

**Recommendation:** Investigate fulfillment center capacity near Chennai/Surat — these cities combine solid revenue with slower delivery, a risk for customer satisfaction and return rates.

---

## 4. Customer Segment (Prime vs Non-Prime)

| Segment | Orders | Revenue (₹) | AOV (₹) |
|---|---|---|---|
| Prime | 6,093 | 1,77,67,929 | 2,916.12 |
| Non-Prime | 5,175 | 1,50,48,824 | 2,907.99 |

**Insight:** Prime customers place ~18% more orders and contribute ~18% more revenue than Non-Prime, but **AOV is virtually identical** (₹2,916 vs ₹2,908). This was statistically tested in R using a two-sample t-test (`r/amazon_sales_analysis.R`) — the difference in AOV is **not** practically meaningful; Prime's value lies in order *frequency*, not basket size.

**Recommendation:** Prime membership campaigns should be framed around increasing purchase frequency (subscribe & save, faster delivery perks) rather than expecting Prime members to spend more per order.

---

## 5. Sales Channel Performance

| Channel | Orders | Revenue (₹) |
|---|---|---|
| Amazon App | 6,723 | 1,94,47,496 |
| Amazon Web | 3,630 | 1,05,44,551 |
| Alexa Voice Order | 915 | 28,24,707 |

**Insight:** The mobile app drives ~59% of revenue — by far the dominant channel. Alexa voice ordering remains a small niche (~8.6% of revenue) but represents a frictionless reorder channel worth nurturing for repeat/staple purchases.

---

## 6. Payment Method vs Order Outcomes

| Payment Method | Return Rate % | Cancel Rate % |
|---|---|---|
| Prepaid - Wallet | 7.75 | 7.06 |
| Prepaid - UPI | 7.54 | 5.70 |
| Prepaid - Card | 6.97 | 6.20 |
| Cash on Delivery | 6.53 | 6.15 |
| Prepaid - Net Banking | 6.49 | 6.40 |

**Insight:** Contrary to common assumption, **Cash on Delivery does *not* have the highest return/cancellation rate** — Wallet and UPI payments show marginally higher return rates. This was tested with a chi-square independence test in R (`amazon_sales_analysis.R`) — differences across payment methods are small and likely not strongly dependent.

**Recommendation:** Don't over-restrict COD eligibility based on return-rate assumptions; focus return-reduction efforts on Wallet/UPI checkout flows (e.g., clearer product images/sizing info before payment).

---

## 7. Discount Strategy Analysis

| Discount Band | Orders | Revenue (₹) | AOV (₹) |
|---|---|---|---|
| 0% | 1,449 | 52,24,601 | 3,605.66 |
| 1–10% | 2,717 | 90,21,919 | 3,320.54 |
| 11–20% | 3,340 | 97,55,005 | 2,920.66 |
| 21–30% | 2,406 | 61,56,175 | 2,558.68 |
| 31–50% | 1,281 | 25,50,556 | 1,991.07 |
| 50%+ | 75 | 1,08,498 | 1,446.64 |

**Insight:** The **11–20% discount band generates the highest absolute revenue** (₹97.6L) and a healthy order count (3,340). AOV declines steadily as discount % increases — deep discounts (30%+) attract fewer, lower-value orders and erode margin without a proportional volume offset.

**Correlation check:** Discount % vs. Rating correlation = **-0.014** (essentially zero) — higher discounts do **not** meaningfully hurt customer satisfaction, so promotional discounting in the 10–20% range is safe from a CSAT perspective.

**Recommendation:** Standardize promotional campaigns around **10–20% discounts** as the revenue-maximizing sweet spot; reserve 30%+ discounts for clearance/dead stock only.

---

## 8. Returns Analysis

| Category | Return Rate % |
|---|---|
| Books | 7.77 |
| Toys & Games | 7.75 |
| Clothing | 7.65 |
| Sports & Fitness | 7.26 |
| Beauty & Personal Care | 7.10 |
| Electronics | 7.03 |
| Office Products | 6.59 |
| Home & Kitchen | 6.05 |

**Insight:** Return rates are relatively tight (6.1%–7.8%) across categories, with **Clothing and Toys & Games** showing the highest rates — consistent with real-world fit/sizing and gift-mismatch issues. Home & Kitchen has the lowest return rate, suggesting higher purchase-decision confidence for functional household items.

**Recommendation:** Improve size charts / fit-prediction tools for Clothing, and clearer age/feature descriptions for Toys & Games to reduce returns.

---

## 9. Weekday vs Weekend

| Day Type | Orders | Revenue (₹) | AOV (₹) |
|---|---|---|---|
| Weekday | 8,003 | 2,31,66,689 | 2,894.75 |
| Weekend | 3,265 | 96,50,064 | 2,955.61 |

**Insight:** Weekends generate a slightly higher AOV (₹2,956 vs ₹2,895) despite fewer total orders — customers may be making more considered, higher-value purchases when they have more browsing time.

---

## 10. Summary of Recommendations

1. **Seasonality:** Plan inventory and marketing spend around the Sep–Nov festive surge; use Feb/Apr dips for mid-season promos.
2. **Category focus:** Prioritize Electronics accessories (highest revenue density); use bundling to lift AOV.
3. **Discounting:** Hold standard promos at 10–20% — this band maximizes revenue without materially hurting ratings.
4. **Logistics:** Audit delivery performance in Chennai/Surat/Hyderabad — slower delivery in high-revenue cities is a risk.
5. **Returns:** Target Clothing and Toys & Games with better product information to cut the highest return rates.
6. **Prime strategy:** Frame Prime benefits around increasing order *frequency*, not basket size (AOV is statistically similar across segments).
7. **Channel:** Continue investing in the mobile app (59% of revenue) while nurturing Alexa voice ordering for repeat/staple SKUs.

---

## Methodology Note

- All "valid orders" exclude `Order_Status = 'Cancelled'`.
- Currency figures are in INR (₹), simulated data, rounded to nearest rupee in this report (exact values available in source files).
- Statistical tests (t-test, chi-square, correlation, linear regression) are implemented in `r/amazon_sales_analysis.R` with full output in `r/regression_summary.txt` (generated on run).
