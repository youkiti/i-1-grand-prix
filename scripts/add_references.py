import sys
import json
from pathlib import Path

def load_metadata(meta_dir: Path):
    file_info = {}
    if not meta_dir.exists():
        return file_info
    
    for meta_file in meta_dir.glob("metadata_*.json"):
        print(f"Loading meta: {meta_file.name}")
        try:
            with open(meta_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                files = data.get("files", {})
                for fname, info in files.items():
                    file_info[fname] = info
        except Exception as e:
            print(f"Error loading {meta_file}: {e}")
    return file_info

def parse_docs(hypo_path: Path):
    docs = []
    if not hypo_path.exists():
        print(f"Hypothesis file not found: {hypo_path}")
        return docs
    
    content = hypo_path.read_text(encoding='utf-8')
    current_doc = {}
    in_source_docs = False
    
    for line in content.splitlines():
        line_stripped = line.strip()
        if "source_documents:" in line:
            in_source_docs = True
            continue
        
        if not in_source_docs:
            continue
            
        # Fix: Check stripped line to handle indentation
        if line_stripped.startswith("generated_at:"): # End of metadata section
            break
            
        if line_stripped.startswith("- id:"):
             if current_doc.get("id"): docs.append(current_doc)
             clean_id = line_stripped.split(":", 1)[1].strip().strip('"').strip("'")
             current_doc = {"id": clean_id}
        elif line_stripped.startswith("filename:") and current_doc:
             clean_name = line_stripped.split(":", 1)[1].strip().strip('"').strip("'")
             current_doc["filename"] = clean_name
        elif line_stripped.startswith("url:") and current_doc:
             parts = line_stripped.split(":", 1)
             if len(parts) > 1:
                 clean_url = parts[1].strip().strip('"').strip("'")
                 current_doc["url"] = clean_url
        elif line_stripped.startswith("date:") and current_doc:
             parts = line_stripped.split(":", 1)
             if len(parts) > 1:
                 clean_date = parts[1].strip().strip('"').strip("'")
                 current_doc["date"] = clean_date
    
    if current_doc.get("id"): docs.append(current_doc)
    return docs

def write_references_to_new_file(report_path: Path, docs, file_info):
    if not report_path.exists():
        print(f"Report not found: {report_path}")
        return
    
    content = report_path.read_text(encoding='utf-8')
    
    # Check if reference section likely exists (simple check)
    if "# 出典一覧" in content or "# References" in content:
        print("Reference section might already exist. Appending to new file anyway.")
        
    lines = ["\n\n# 出典一覧 (References)\n"]
    lines.append("| ID | 資料名 | URL | 日付 |")
    lines.append("| :--- | :--- | :--- | :--- |")
    
    for doc in docs:
        doc_id = doc.get("id", "")
        fname = doc.get("filename", "")
        url = doc.get("url", "")
        date = doc.get("date", "") or ""
        if date == "null": date = ""
        
        # Resolve title from metadata
        title = fname
        if fname in file_info:
            info = file_info[fname]
            meta_title = info.get("link_text") or info.get("page_title")
            if meta_title:
                title = meta_title.replace("|", "\|")
        
        # Format URL
        link = f"[Link]({url})" if url and url != "null" else "-"
        
        lines.append(f"| {doc_id} | {title} | {link} | {date} |")
    
    new_content = content + "\n".join(lines)
    
    # Create new file path with _with_refs suffix
    output_path = report_path.with_name(f"{report_path.stem}_with_refs{report_path.suffix}")
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Created report with references: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python add_references.py <report> <hypothesis> [meta_dir]")
        sys.exit(1)
        
    report = Path(sys.argv[1])
    hypo = Path(sys.argv[2])
    meta_dir = Path(sys.argv[3]) if len(sys.argv) > 3 else Path(".")
    
    print("Parsing documents...")
    docs = parse_docs(hypo)
    print(f"Found {len(docs)} documents.")
    
    print("Loading metadata...")
    file_info = load_metadata(meta_dir)
    print(f"Found metadata for {len(file_info)} files.")
    
    print("Writing new report with references...")
    write_references_to_new_file(report, docs, file_info)
