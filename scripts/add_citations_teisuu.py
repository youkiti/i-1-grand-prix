import json
import re
import sys
from pathlib import Path

# Add project root to sys.path
sys.path.append(str(Path(__file__).parent.parent))

from src.interview_analysis.diet_api import fetch_meeting_meta

def main():
    report_path = Path("doc/2025-12-16/run-095133/outputs/report.md")
    shingikai_registry_path = Path("doc/2025-12-16/run-074854/outputs/citation_registry.json")
    kokkai_registry_path = Path("doc/2025-12-16/run-090649/outputs/citation_registry.json")
    
    print(f"Reading report from {report_path}")
    
    # Load registries
    shingikai_data = {}
    if shingikai_registry_path.exists():
        shingikai_data = json.loads(shingikai_registry_path.read_text(encoding="utf-8"))
    
    kokkai_data = {}
    if kokkai_registry_path.exists():
        kokkai_data = json.loads(kokkai_registry_path.read_text(encoding="utf-8"))
    
    citation_map = {}
    
    # Processing Shingikai
    if "citations" in shingikai_data:
        for cid, c in shingikai_data["citations"].items():
            citation_map[cid] = c
            citation_map[c["file"]] = c
            if c.get("link_text"):
                citation_map[c["link_text"]] = c

    # Processing Kokkai
    if "citations" in kokkai_data:
        for cid, c in kokkai_data["citations"].items():
            citation_map[cid] = c
            citation_map[c["file"]] = c
            
            # Handle various filename formats
            filename = c["file"]
            no_ext = filename.replace(".txt", "")
            citation_map[no_ext] = c
            
            # Extract date_id format: YYYY-MM-DD_ID
            citation_map[filename] = c

    # --- New Logic: Scan merged_hypothesis.md for ID -> Filename mapping ---
    merged_hypo_path = Path("each_project/teisuu/merged_hypothesis.md")
    id_to_filename = {}
    if merged_hypo_path.exists():
        print(f"Scanning {merged_hypo_path} for ID mappings...")
        mh_content = merged_hypo_path.read_text(encoding="utf-8")
        matches = re.findall(r'source_doc_id:\s*"([^"]+)"\s*\n\s*source_filename:\s*"([^"]+)"', mh_content)
        for doc_id, filename in matches:
            id_to_filename[doc_id] = filename

    # Update citation_map with these new mappings
    for doc_id, filename in id_to_filename.items():
        if doc_id not in citation_map:
             # Try to find info for filename
             key_candidates = [filename, filename.replace(".txt", "")]
             found_info = None
             for k in key_candidates:
                 if k in citation_map:
                     found_info = citation_map[k]
                     break
             
             if found_info:
                 citation_map[doc_id] = found_info.copy()
                 citation_map[doc_id]["cite_id"] = doc_id # Override ID for lookup
             else:
                 # Create a dummy info if not in registry (fallback)
                 citation_map[doc_id] = {
                     "cite_id": doc_id,
                     "file": filename,
                     "cite_type": "kokkai" if "X" in filename else "shingikai",
                     "link_text": f"{filename} (ID: {doc_id})"
                 }

    content = report_path.read_text(encoding="utf-8")
    
    used_citations = {} # id -> info
    
    def fetch_kokkai_meta_cached(issue_id):
        # Allow caching within script run
        if not hasattr(fetch_kokkai_meta_cached, "cache"):
            fetch_kokkai_meta_cached.cache = {}
        if issue_id in fetch_kokkai_meta_cached.cache:
            return fetch_kokkai_meta_cached.cache[issue_id]
        
        print(f"Fetching meta for {issue_id}...")
        try:
            meta = fetch_meeting_meta(issue_id)
            fetch_kokkai_meta_cached.cache[issue_id] = meta
            return meta
        except Exception as e:
            print(f"Error fetching meta for {issue_id}: {e}")
            return None

    def replace_citation(match):
        full_text = match.group(0)
        content_inner = match.group(1).strip()
        
        # Direct match or Map lookup
        info = citation_map.get(content_inner)
        
        # Fuzzy / Filename match
        if not info:
             clean_inner = content_inner.replace(".txt", "")
             if clean_inner in citation_map:
                 info = citation_map[clean_inner]
             else:
                 for k, v in citation_map.items():
                     if len(k) > 10 and (k in content_inner or content_inner in k):
                         info = v
                         break
        
        # If still no info but looks like Kokkai file
        if not info and re.match(r'\d{4}-\d{2}-\d{2}_\d+X', content_inner):
            filename = content_inner if content_inner.endswith(".txt") else content_inner + ".txt"
            info = {
                "cite_id": content_inner,
                "file": filename,
                "cite_type": "kokkai",
                "url": f"https://kokkai.ndl.go.jp/txt/{filename.split('_')[-1].replace('.txt','')}" 
            }

        if info:
            used_citations[info.get("cite_id", content_inner)] = info
            

            page_title = info.get("page_title", "")
            link_text = info.get("link_text", "")
            filename = info.get("file", "")
            
            # Generic link texts that should be prefixed with page_title for clarity
            generic_terms = ["議事概要", "答申", "参考資料", "説明", "委員名簿", "協議員名簿", "設置要綱"]
            
            title = link_text or page_title or filename
            
            # Refine title if it's too generic
            if link_text and page_title:
                # If link_text is one of the generic terms, prepend page_title
                # e.g. "議事概要" -> "第６回　衆議院選挙制度に関する調査会 議事概要"
                if any(term == link_text.strip() for term in generic_terms): # Exact match or close
                    title = f"{page_title} {link_text}"
                # Also handle cases where link_text might be slightly longer but still generic-ish context
                elif len(link_text) < 10 and page_title not in link_text:
                    title = f"{page_title} {link_text}"
            
            # SAVE the title so it appears in the appendix table later!
            info["display_title"] = title

            url = info.get("url")
            
            # Enrich Kokkai Information
            if "kokkai" in info.get("cite_type", "") or "diet" in str(info.get("file", "")).lower() or re.search(r'\d+X\d+', str(info.get("file", ""))):
                
                file_val = info.get("file", "")
                issue_id = None
                
                match_id = re.search(r'_(\d+X\d+)', file_val)
                if match_id:
                    issue_id = match_id.group(1)
                elif "X" in file_val:
                     # fallback
                     issue_id = file_val.replace(".txt", "")
                
                if issue_id:
                     meta = fetch_kokkai_meta_cached(issue_id)
                     if meta:
                         date_str = meta.get('date', '')
                         house = meta.get('house', '')
                         meeting = meta.get('meeting_name', '')
                         
                         title = f"{house} {meeting} ({date_str})"
                         if meta.get('page_url'):
                             url = meta.get('page_url')
                         
                         info["display_title"] = title
                         info["display_url"] = url
            
            display_title = info.get("display_title", title)
            display_url = info.get("display_url", url)

            if display_url:
                return f"[{display_title}]({display_url})"
            else:
                return f"[{display_title}]"
        
        return full_text

    # Replace standard [出典: ...]
    new_content = re.sub(r'\[出典:\s*([^\]]+)\]', replace_citation, content)
    
    # Replace bare filenames [YYYY-MM-DD_...X...]
    def replace_bare_citation(match):
        content_inner = match.group(1).strip()
        class MockMatch:
            def group(self, i):
                return f"[出典: {content_inner}]" if i == 0 else content_inner
        return replace_citation(MockMatch())

    new_content = re.sub(r'\[(\d{4}-\d{2}-\d{2}_\d+X[^\]]+)\]', replace_bare_citation, new_content)

    
    # Collect Pubcoms
    used_pubcoms = set()
    def replace_pubcom(match):
        pid = match.group(1).strip()
        used_pubcoms.add(pid)
        return match.group(0) # Keep format
    
    new_content = re.sub(r'\[パブコメ:\s*([^\]]+)\]', replace_pubcom, new_content)
    
    # Generate Appendix
    appendix = "\n\n---\n\n# 出典一覧\n\n"
    
    # Documents / Kokkai
    if used_citations:
        appendix += "## 審議会・国会資料\n"
        appendix += "| ID | 資料名 / 会議名 | リンク |\n"
        appendix += "|----|-----------------|--------|\n"
        
        sorted_citations = sorted(used_citations.values(), key=lambda x: str(x.get("cite_id", "")))
        
        for info in sorted_citations:
            cid = info.get("cite_id")
            title = info.get("display_title") or info.get("link_text") or info.get("file")
            url = info.get("display_url") or info.get("url")
            
            url_str = f"[Link]({url})" if url else "-"
            appendix += f"| {cid} | {title} | {url_str} |\n"
            
    # Pubcoms
    if used_pubcoms:
        appendix += "\n## 引用されたパブリックコメント\n"
        appendix += "| コメントID |\n"
        appendix += "|------------|\n"
        for pid in sorted(used_pubcoms):
             appendix += f"| {pid} |\n"

    final_content = new_content + appendix
    
    output_path = report_path.with_name("report_with_references.md")
    output_path.write_text(final_content, encoding="utf-8")
    print(f"Saved report with references to {output_path}")

if __name__ == "__main__":
    main()
