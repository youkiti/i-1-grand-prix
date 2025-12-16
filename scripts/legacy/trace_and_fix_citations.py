import sys
import csv
import re
import json
from pathlib import Path

# Add project root to python path
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

from src.interview_analysis.diet_api import fetch_meeting_meta

def load_diet_speeches(csv_path: Path):
    """
    Load diet speeches/transcripts into a list of (session_id, message).
    Scans both the CSV and the 'transcripts' sibling directory.
    """
    speeches = []
    
    # 1. Load CSV if it exists
    if csv_path.exists():
        print(f"Loading CSV: {csv_path}")
        # Increase CSV field limit for large messages
        csv.field_size_limit(2**31 - 1)
        
        try:
            with open(csv_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if 'session_id' in row and 'message' in row:
                        speeches.append((row['session_id'], row['message']))
        except Exception as e:
            print(f"Error loading CSV: {e}")
            
    # 2. Load Transcripts from sibling directory
    transcripts_dir = csv_path.parent / "transcripts"
    if transcripts_dir.exists():
        print(f"Loading transcripts from: {transcripts_dir}")
        for txt_file in transcripts_dir.glob("*.txt"):
            # Filename format expected: Date_SessionID.txt or just SessionID.txt
            # e.g. 2025-04-16_121704889X01420250416.txt
            # Extract Session ID: look for the long alphanumeric string
            fname = txt_file.name
            match = re.search(r'([0-9]{10,}X[0-9]{10,})', fname)
            if match:
                session_id = match.group(1)
                try:
                    content = txt_file.read_text(encoding='utf-8')
                    speeches.append((session_id, content))
                except Exception as e:
                    print(f"Error reading {txt_file}: {e}")
            else:
                print(f"Skipping file (no session ID found): {fname}")

    print(f"Loaded total {len(speeches)} speech records.")
    return speeches

def find_session_id_for_text(text: str, speeches: list) -> str:
    """Find the session_id where the text appears in the message."""
    # Clean up text for better matching (remove newlines, extra spaces)
    clean_text = re.sub(r'\s+', '', text).strip()
    if len(clean_text) < 10: # Too short to be unique
        return None
        
    for session_id, message in speeches:
        clean_message = re.sub(r'\s+', '', message)
        if clean_text in clean_message:
            return session_id
    return None

def extract_contexts_from_report(report_content: str):
    """
    Extract citation contexts from the report.
    Returns a dict: {cite_id: context_text}
    
    Strategy:
    Look for citations like [出典: kokkai_XXX] or [出典: doc_XXX].
    Grab the preceding text chunk.
    """
    contexts = {}
    
    # 1. Try to find "verbatim_quote" or similar if the report has structured blocks (unlikely in pure MD body)
    # 2. Look for the citation tag and take the preceding sentence/paragraph.
    
    # Pattern: "...some text... [出典: ID]"
    # We'll take the 50-100 chars before the citation as the search query.
    
    img_pattern = r'([^\[\n]{30,})\[出典:\s*([^\]]+)\]'
    
    for match in re.finditer(img_pattern, report_content):
        text_chunk = match.group(1).strip()
        citation_label = match.group(2).strip()
        
        # citation_label might be "kokkai_001", "doc_001", "kokkai_001, p.5", etc.
        # Extract the ID part
        id_match = re.match(r'^(kokkai_\d+|doc_\d+|[a-zA-Z]+_\d+)', citation_label)
        if id_match:
            cite_id = id_match.group(1)
            # Use the last part of the text chunk for searching
            search_query = text_chunk[-100:] # Last 100 chars
            contexts[cite_id] = search_query
            
    return contexts

def update_report_references(report_path: Path, csv_path: Path):
    if not report_path.exists():
        print(f"Report not found: {report_path}")
        return

    content = report_path.read_text(encoding="utf-8")
    speeches = load_diet_speeches(csv_path)
    
    # Map cite_id -> session_id
    id_map = {}
    
    # Extract contexts
    contexts = extract_contexts_from_report(content)
    print(f"Found {len(contexts)} citations to trace: {list(contexts.keys())}")
    
    for cite_id, query in contexts.items():
        print(f"Tracing {cite_id}...")
        session_id = find_session_id_for_text(query, speeches)
        if session_id:
            print(f"  -> Found session_id: {session_id}")
            id_map[cite_id] = session_id
        else:
            print(f"  -> No match found in CSV.")
            
    if not id_map:
        print("No session IDs resolved. Exiting.")
        return

    # Generate new Reference Table
    new_rows = []
    
    # Also reuse existing "Reference" section parsing to keep other docs if needed?
    # For now, let's just focus on generating the Kokkai part or replacing lines.
    
    # Let's locate the table rows for these IDs and update them.
    lines = content.split('\n')
    new_lines = []
    inside_table = False
    
    # Pre-fetch metadata for resolved IDs
    meta_cache = {}
    for cite_id, sess_id in id_map.items():
        if sess_id not in meta_cache:
            meta = fetch_meeting_meta(sess_id)
            meta_cache[sess_id] = meta

    # Parse existing content to find where to insert or update
    lines = content.split('\n')
    new_lines = []
    
    # Track which IDs we have handled
    handled_ids = set()
    
    # Pre-fetch metadata
    meta_cache = {}
    for cite_id, sess_id in id_map.items():
        if sess_id not in meta_cache:
            meta = fetch_meeting_meta(sess_id)
            meta_cache[sess_id] = meta

    # We will look for an existing table to update
    # If we find a row with one of our IDs, we update it.
    
    for line in lines:
        match = re.match(r'\|\s*([^\|\s]+)\s*\|', line)
        if match:
            row_id = match.group(1).strip()
            if row_id in id_map:
                handled_ids.add(row_id)
                session_id = id_map[row_id]
                meta = meta_cache.get(session_id)
                if meta:
                     title = f"{meta.get('house', '')} {meta.get('meeting_name', '')} 第{meta.get('meeting_number', '')}号 (第{meta.get('session')}回国会)"
                     url = f"[会議録]({meta.get('page_url', '')})"
                     date = meta.get('date', '-')
                     # Format: | ID | Title | URL | Date |
                     new_row = f"| {row_id} | {title} | {url} | {date} |"
                     new_lines.append(new_row)
                     continue
        
        new_lines.append(line)

    # If there are unhandled IDs, we need to add them.
    # Look for the "# 出典一覧" section to append to.
    unhandled_ids = set(id_map.keys()) - handled_ids
    
    if unhandled_ids:
        print(f"Adding new rows for: {unhandled_ids}")
        # Construct the new table section
        appendix_lines = []
        appendix_lines.append("")
        appendix_lines.append("## 国会会議録 (National Diet Records)")
        appendix_lines.append("| ID | 資料名 | URL | 日付 |")
        appendix_lines.append("|----|--------|-----|------|")
        
        for cite_id in sorted(unhandled_ids):
            session_id = id_map[cite_id]
            meta = meta_cache.get(session_id)
            if meta:
                title = f"{meta.get('house', '')} {meta.get('meeting_name', '')} 第{meta.get('meeting_number', '')}号 (第{meta.get('session')}回国会)"
                url = f"[会議録]({meta.get('page_url', '')})"
                date = meta.get('date', '-')
                appendix_lines.append(f"| {cite_id} | {title} | {url} | {date} |")
        
        # Insert before the end or after "# 出典一覧"
        # Simplest: Append to the end of the file if "出典一覧" exists, 
        # or try to insert nicely if we can find the section header.
        
        # Check if we already have "Reference" header in `new_lines`
        has_ref_header = any("# 出典一覧" in l for l in new_lines)
        
        if has_ref_header:
            # Find the index of the header
            # Actually, just appending to the end is safe for Markdown, 
            # but better to put it *after* the header if possible.
            # But since we reconstructed `new_lines`, let's just append to end of file
            # or finding the main header and inserting after it is complicated if other sections exist.
            # Let's just append to the end.
            new_lines.extend(appendix_lines)
        else:
            # Create header if missing
            new_lines.append("\n# 出典一覧 (References)")
            new_lines.extend(appendix_lines)

    updated_content = '\n'.join(new_lines)
    
    # Write back
    report_path.write_text(updated_content, encoding='utf-8')
    print(f"Updated reference table in {report_path}")

if __name__ == "__main__":
    # Configure paths
    csv_path = project_root / "each_project/ai-plan-test/kokkai/diet_speeches.csv"
    
    # Expect report path as argument, or default to a search
    if len(sys.argv) > 1:
        report_path = Path(sys.argv[1])
    else:
        # Default search if not provided (placeholder)
        print("Please provide report path.")
        sys.exit(1)
        
    update_report_references(report_path, csv_path)
