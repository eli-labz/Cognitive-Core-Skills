# Google Analytics 4 BigQuery Public Dataset

This provides an overview of kc_enrich_sample_data.ga_events table.

## High-Level Information and Data Source

The Google Analytics 4 (GA4) sample ecommerce dataset is a publicly available dataset hosted within the Google Cloud BigQuery Public Datasets program. It provides raw, event-level data exported directly from Google Analytics 4.

## The Source

The data originates from the Google Merchandise Store, an actual online e-commerce website that sells Google-branded apparel, accessories, and other items. The website implements a standard GA4 web e-commerce setup alongside enhanced measurement events.

## Key Characteristics

Dataset Name: bigquery-public-data.ga4_obfuscated_sample_ecommerce

Table Format: events_YYYYMMDD (Daily partitioned tables, totaling 92 tables).

Time Range: The dataset covers a three-month period from November 1, 2020, to January 31, 2021.

Obfuscation: To protect user privacy and business metrics, the data is deliberately obfuscated. You will encounter placeholder values such as <Other>, NULL, and empty strings ''. Because of this, internal consistency might be limited, and the metrics cannot be directly compared to the live GA4 Demo Account for the Google Merchandise Store.
