# Session Analysis (Unnesting Parameters)

This provides examples for kc_enrich_sample_data.ga_events table.

## Overview

In GA4, a "session" is not a dedicated row; instead, every event contains a nested parameter called ga_session_id. To count total sessions, you must isolate the session_start event and "unnest" its parameters to extract the unique session ID.

```sql
SELECT 
  COUNT(DISTINCT value.int_value) AS total_sessions
FROM 
  `kc_enrich_sample_data.ga_events`, 
  UNNEST(event_params) 
WHERE 
  event_name = 'session_start' 
  AND key = 'ga_session_id'
```
