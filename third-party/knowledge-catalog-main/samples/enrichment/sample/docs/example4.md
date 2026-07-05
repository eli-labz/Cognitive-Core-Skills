# E-Commerce Product Interest

This provides examples for kc_enrich_sample_data.ga_events table.

## Overview

For an e-commerce store, understanding which items are frequently added to the cart is crucial. E-commerce data is stored in a nested array called items. This query flattens the items array and aggregates the top 10 products based on the add_to_cart event.

```sql
SELECT 
  items.item_name, 
  COUNT(*) AS added_to_cart_count 
FROM 
  `kc_enrich_sample_data.ga_events`, 
  UNNEST(items) AS items
WHERE 
  event_name = 'add_to_cart' 
GROUP BY 
  items.item_name 
ORDER BY 
  added_to_cart_count DESC 
LIMIT 10
```
