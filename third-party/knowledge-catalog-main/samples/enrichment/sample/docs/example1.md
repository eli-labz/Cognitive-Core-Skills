# High-Level Event and User Volume

This provides examples for kc_enrich_sample_data.ga_events table.

## Overview

Before diving into deep analysis, it is best practice to understand the scale of your dataset. This query counts the total number of events, the total number of unique users (based on device cookies), and the number of days present in the dataset.

```sql
SELECT 
  COUNT(*) AS total_events, 
  COUNT(DISTINCT user_pseudo_id) AS total_unique_users, 
  COUNT(DISTINCT event_date) AS total_days
FROM 
  `kc_enrich_sample_data.ga_events`
```
