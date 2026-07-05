# Querying a Specific Date Range

This provides examples for kc_enrich_sample_data.ga_events table.

## Overview

Because the GA4 export creates a new partition for every day, you should use the predicate on the partition timestamp column to limit the data scanned. This improves performance and drastically reduces query costs. This query finds the daily count of active users for December 2020.

```sql
SELECT 
  event_date, 
  COUNT(DISTINCT user_pseudo_id) as active_users 
FROM 
  `kc_enrich_sample_data.ga_events` 
WHERE 
  event_date_dt BETWEEN PARSE_DATE('%Y%m%d', '20201201') AND PARSE_DATE('%Y%m%d', '20201231') 
GROUP BY 
  event_date 
ORDER BY 
  event_date ASC
```
