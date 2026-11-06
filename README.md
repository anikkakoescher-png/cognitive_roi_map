# Cognitive ROI Map: dataset

The current count is in `summary.json`. One data point is one value, for one country (or the euro area), one indicator, one occupation group and one month, from one cited source.

## Contents

| Indicator | What it measures | Countries | Months | Data points |
|---|---|---|---|---|
| `ai_share_postings` | Share of job postings mentioning AI keywords (e.g. "machine learning", "artificial intelligence"), % | AU, CA, DE, FR, GB, IE, IT, NL, US | Jan 2019 to Sep 2026 | 837 |
| `postings_index_total` | Job postings index, all occupations (1 Feb 2020 = 100; seasonally adjusted where available) | AU, CA, DE, EA (euro area), ES, FR, GB, IE, IT, NL, US | Feb 2020 to Oct 2026 | 891 |
| `postings_index_group` | Job postings index for 47 occupation groups (1 Feb 2020 = 100) | AU, CA, DE, FR, GB, US | Feb 2020 to Oct 2026 | 21,789 |

## Method

- Source files give daily values. Each monthly value is the mean of that month's daily values; `n_days` records how many days went into it.
- For occupation groups, only the "total postings" series is used.
- No values were estimated, filled in or modelled.

## Sources and licence

- Indeed Hiring Lab, AI Tracker: https://github.com/hiring-lab/ai-tracker. Licence: CC BY 4.0.
- Indeed Hiring Lab, Job Postings Tracker: https://github.com/hiring-lab/job_postings_tracker. Licence: CC BY 4.0.

Required credit: "Source: Indeed Hiring Lab". Anna Ernst has aggregated the daily data into monthly means.

## Limits

- Job postings on Indeed are not all hiring, and their mix differs by country.
- China, the Middle East and Africa are not covered by these sources.
- Falling postings since late 2022 have many causes (the post-pandemic peak, interest rates). These data alone do not show that AI caused any change.
