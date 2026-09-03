import os
import sys
import requests
import json

def analyze_security(file_path, api_key):
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} not found.")
        return

    with open(file_path, 'r') as f:
        code_content = f.read()

    # هندسة موجهة للذكاء الاصطناعي لاستخراج الثغرات وتقديم التصحيح
    prompt = f"""
    You are an elite Cloud Security & DevSecOps Architect. Analyze the following configuration/code for severe security vulnerabilities, misconfigurations, or compliance risks. 
    Provide a concise technical report and the exact remediated code snippet.

    Target Code:
    {code_content}
    """

    # استخدام واجهة برمجية سحابية مجانية وسريعة للتحليل
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.1
    }

    print("[*] Analyzing code security via Cloud AI Agent...")
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        result = response.json()
        print("\n=== Security Audit & Remediation Report ===")
        print(result['choices'][0]['message']['content'])
    else:
        print(f"API Error: {response.status_code} - {response.text}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 scanner.py <path_to_config_file>")
        sys.exit(1)
    
    # جلب مفتاح الـ API مجاناً من متغيرات البيئة لتجنب تسريبه
    api_key = os.getenv("AI_API_KEY")
    if not api_key:
        print("Error: AI_API_KEY environment variable is not set.")
        sys.exit(1)

    analyze_security(sys.argv[1], api_key)
