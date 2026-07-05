import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "Skills"
DATA_PATH = ROOT / "data" / "cognitive-core-skills.json"


def build_markdown(skill: dict) -> str:
    lines = []
    lines.append("---")
    lines.append(f"id: {skill['id']}")
    lines.append(f"name: {skill['name']}")
    lines.append(f"domain: {skill['domain']}")
    lines.append(f"skill_type: {skill['skill_type']}")
    lines.append(f"difficulty_level: {skill['difficulty_level']}")
    lines.append(f"human_review_required: {skill['human_review_required']}")
    lines.append("model_relevance:")
    lines.append(f"  llm: {skill['model_relevance']['llm']}")
    lines.append(f"  slm: {skill['model_relevance']['slm']}")
    lines.append(f"  agent: {skill['model_relevance']['agent']}")
    lines.append(f"  world_model: {skill['model_relevance']['world_model']}")
    lines.append("---")
    lines.append("")
    lines.append(f"# {skill['name']}")
    lines.append("")
    lines.append("## Summary")
    lines.append(skill["summary"])
    lines.append("")
    lines.append("## Definition")
    lines.append(skill["definition"])
    lines.append("")

    def section(title: str, items):
        lines.append(f"## {title}")
        for item in items:
            lines.append(f"- {item}")
        lines.append("")

    section("Inputs", skill["inputs"])
    section("Outputs", skill["outputs"])
    section("Required Capabilities", skill["required_capabilities"])
    section("Failure Modes", skill["failure_modes"])
    section("Evaluation Questions", skill["evaluation_questions"])
    section("Evaluation Signals", skill["evaluation_signals"])
    section("Example Tasks", skill["example_tasks"])
    section("Related Skills", skill["related_skills"])
    section("Source Patterns", skill["source_patterns"])

    return "\n".join(lines)


def main():
    payload = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    skills = payload["skills"]

    SKILLS_DIR.mkdir(parents=True, exist_ok=True)

    for md in SKILLS_DIR.glob("*.md"):
        md.unlink()

    for skill in skills:
        out = SKILLS_DIR / f"{skill['id']}.md"
        out.write_text(build_markdown(skill), encoding="utf-8")

    by_domain = {}
    for skill in skills:
        by_domain.setdefault(skill["domain"], []).append(skill)

    index_lines = [
        "# Skills Index",
        "",
        f"Generated from data/cognitive-core-skills.json. Total skills: {len(skills)}",
        "",
    ]

    for domain in sorted(by_domain.keys()):
        index_lines.append(f"## {domain}")
        for skill in sorted(by_domain[domain], key=lambda x: x["id"]):
            index_lines.append(f"- [{skill['name']}]({skill['id']}.md) (`{skill['id']}`)")
        index_lines.append("")

    (SKILLS_DIR / "index.md").write_text("\n".join(index_lines), encoding="utf-8")
    print(f"Generated {len(skills)} skill cards and Skills/index.md")


if __name__ == "__main__":
    main()
