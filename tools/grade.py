import os
import sys

def check_file_exists(filepath):
    if os.path.exists(filepath):
        print(f"✅ Found: {filepath}")
        return True
    else:
        print(f"❌ Missing: {filepath}")
        return False

def check_report_content(filepath):
    if not os.path.exists(filepath):
        return False
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check for empty table cells (represented by | | in the template)
    # The template has cells like | 10 | | | |
    # We want to see if the student added values.
    # A simple check: count the number of pipes and ensure content isn't just whitespace between them.
    
    # Check for placeholder markers like "[Record your answer here]" or "[]"
    placeholders = ["[Record your answer here]", "[MJPEG / H.264]"]
    for p in placeholders:
        if p in content:
            print(f"❌ Placeholder remaining in {filepath}: '{p}'")
            return False
            
    # Check if tables are filled (basic check for non-empty cells in the measurement rows)
    lines = content.split('\n')
    tables_filled = True
    for line in lines:
        if line.strip().startswith('| 10 |') or line.strip().startswith('| MJPEG |'):
            cells = [c.strip() for c in line.split('|') if c.strip()]
            if len(cells) < 3: # Should have Quality/Codec, FPS, Bandwidth, etc.
                tables_filled = False
                break
    
    if not tables_filled:
        print(f"❌ Tables in {filepath} seem incomplete.")
        return False

    print(f"✅ Report {filepath} appears to be completed.")
    return True

def main():
    print("--- Starting Artifact Audit ---")
    
    success = True
    
    # Check for proof image
    if not check_file_exists("reports/latency-proof.jpg"):
        success = False
        
    # Check for report completion
    if not check_report_content("reports/artifact_test.md"):
        success = False
        
    print("--- Audit Summary ---")
    if success:
        print("PASS: All required artifacts are present and completed.")
        sys.exit(0)
    else:
        print("FAIL: Some artifacts are missing or incomplete.")
        sys.exit(1)

if __name__ == "__main__":
    main()
