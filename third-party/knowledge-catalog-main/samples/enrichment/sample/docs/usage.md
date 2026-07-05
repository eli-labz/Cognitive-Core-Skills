# Using Google Analytics 4 BigQuery Public Dataset

This provides usage information for kc_enrich_sample_data.ga_events table.

## How the Data Can Be Used

This dataset is incredibly valuable for analysts, data scientists, and developers who want to learn how to query GA4 data in BigQuery without needing their own fully populated e-commerce site or GA4 export.

## Getting Started

To interact with the dataset, you need:

A Google Cloud Project with the BigQuery API enabled.

You can use the BigQuery Sandbox, which provides a generous free tier of up to 1 TB of querying per month, allowing you to explore the data without needing to attach a credit card.

## Primary Applications

Schema Familiarization: GA4 exports data in a highly nested format (using arrays and structs for event_params, user_properties, and items). This dataset allows you to practice the UNNEST() function to flatten data.

Testing Queries & Data Models: Build and test advanced SQL data models for user retention, funnel analysis, or marketing attribution before applying them to your production data.

Dashboard Prototyping: Connect this public BigQuery dataset to visualization tools like Looker Studio or Tableau to practice building e-commerce and web performance dashboards.
