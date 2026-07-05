if [ ! -d ".venv" ]; then
  python3 -m venv .venv
fi

source .venv/bin/activate

if [ "$1" == "--install" ]; then
  pip install -r requirements.txt
fi

export PYTHONDONTWRITEBYTECODE=1

export PYTHONWARNINGS="ignore::UserWarning:google.adk.features._feature_decorator"
export GOOGLE_GENAI_USE_VERTEXAI=True

export KC_ENRICH_SAMPLE_PROJECT=$(gcloud -q config get-value project)
if [ "$KC_ENRICH_SAMPLE_PROJECT" == "" ]; then
  echo "No sample project set. Please run 'gcloud config set project <project-id>'"
  exit 1
fi

export KC_ENRICH_SRC_DIR=$(cd -- "." && pwd)
export KC_ENRICH_SAMPLE_DOCS_DIR=$(cd -- "../sample/docs" && pwd)
