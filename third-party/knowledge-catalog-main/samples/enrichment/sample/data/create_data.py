# Creates sample data in BigQuery to demonsrtate enrichment agent.
#

import subprocess

import google.cloud.bigquery as bigquery


SAMPLE_DATASET_ID = 'kc_enrich_sample_data'
SAMPLE_TABLE_NAME = 'ga_events'


def create_dataset(bq: bigquery.Client, project_id: str):
  bq.create_dataset(f'{project_id}.{SAMPLE_DATASET_ID}', exists_ok=True)


def create_table(bq: bigquery.Client, project_id: str):
  sql_script = f'''
    CREATE TABLE IF NOT EXISTS `{project_id}.{SAMPLE_DATASET_ID}.{SAMPLE_TABLE_NAME}`
    PARTITION BY event_date_dt
    AS
    SELECT
      *,
      PARSE_DATE('%Y%m%d', event_date) AS event_date_dt
    FROM
      `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_*`
  '''

  ddl_job = bq.query(sql_script)
  ddl_job.result()
  print(f"Created table {project_id}.{SAMPLE_DATASET_ID}.{SAMPLE_TABLE_NAME}")


def main():
  process = subprocess.run(
      'gcloud -q config get-value project'.split(),
      check=True,
      text=True,
      capture_output=True,
  )
  project_id = process.stdout.strip()

  bq = bigquery.Client(project=project_id)
  create_dataset(bq, project_id)
  create_table(bq, project_id)


if __name__ == "__main__":
  main()
