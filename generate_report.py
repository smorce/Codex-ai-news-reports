import json
import os

output = {
    "generated_on": "2025-09-29",
    "site": "ai-news.dev",
    "articles": [
        {
            "title": "Write the damn code",
            "url": "https://antonz.org/write-code/",
            "publication_date": "2025-09-26",
            "executive_summary": [
                "\u8457\u8005\u306f\u3001AI\u983c\u307f\u306e\u30d7\u30ed\u30f3\u30d7\u30c8\u8abf\u6574\u3088\u308a\u81ea\u5206\u3067\u30b3\u30fc\u30c9\u3092\u66f8\u304f\u3079\u304d\u3060\u3068\u8a34\u3048\u308b\u3002",
                "AI\u3068\u306e\u5354\u50cd\u30d1\u30bf\u30fc\u30f3\u3092\u4f7f\u3044\u5206\u3051\u308c\u3070\u54c1\u8cea\u3068\u901f\u5ea6\u3092\u4e21\u7acb\u3067\u304d\u308b\u3068\u6307\u6458\u3059\u308b\u3002",
                "\u958b\u767a\u8005\u304c\u4e3b\u4f53\u7684\u306b\u624b\u3092\u52d5\u304b\u3059\u307b\u3069\u6210\u679c\u3068\u6e80\u8db3\u5ea6\u304c\u9ad8\u307e\u308b\u3068\u5f37\u8abf\u3059\u308b\u3002"
            ],
            "key_findings": [
                {"text": "AI\u304c\u521d\u7a3f\u3092\u4f5c\u3063\u305f\u5f8c\u306f\u958b\u767a\u8005\u304c\u30ea\u30d5\u30a1\u30af\u30bf\u30ea\u30f3\u30b0\u3057\u3066\u95a2\u4e0e\u3092\u7dad\u6301\u3059\u3079\u304d\u3060\u3068\u8aac\u304f\u3002[1]", "footnote": "[1]"},
                {"text": "\u958b\u767a\u8005\u81ea\u8eab\u304c\u521d\u671f\u5b9f\u88c5\u3092\u66f8\u304d\u3001AI\u306b\u30ec\u30d3\u30e5\u30fc\u3092\u4efb\u305b\u308b\u6d41\u308c\u3092\u63a8\u5968\u3059\u308b\u3002[1]", "footnote": "[1]"},
                {"text": "\u91cd\u8981\u90e8\u5206\u3060\u3051\u4eba\u9593\u304c\u8a18\u8ff0\u3057\u6b8b\u308a\u3092AI\u306b\u88dc\u5b8c\u3055\u305b\u308b\u624b\u6cd5\u3082\u6319\u3052\u3066\u3044\u308b\u3002[1]", "footnote": "[1]"},
                {"text": "\u30b3\u30fc\u30c9\u306e\u30a2\u30a6\u30c8\u30e9\u30a4\u30f3\u3092\u4eba\u9593\u304c\u793a\u3057AI\u304c\u8a73\u7d30\u3092\u57cb\u3081\u308b\u5354\u50cd\u3092\u4f8b\u793a\u3059\u308b\u3002[1]", "footnote": "[1]"},
                {"text": "\u7d42\u308f\u308a\u306a\u304d\u30d7\u30ed\u30f3\u30d7\u30c8\u8abf\u6574\u3088\u308a\u5b9f\u88c5\u3078\u79fb\u308b\u65b9\u304c\u6210\u679c\u306f\u9ad8\u3044\u3068\u8b66\u9418\u3092\u9cf4\u3089\u3059\u3002[1]", "footnote": "[1]"}
            ],
            "references": [
                {
                    "id": "[1]",
                    "title": "Write the damn code",
                    "author": "Anton Zhiyanov",
                    "url": "https://antonz.org/write-code/",
                    "publisher": "Anton Zhiyanov",
                    "accessed": "2025-09-29"
                }
            ]
        },
        {
            "title": "Brave updates its AI-powered search with a detailed answers feature",
            "url": "https://techcrunch.com/2025/09/29/brave-updates-its-ai-powered-search-with-a-detailed-answers-feature/",
            "publication_date": "2025-09-29T09:00:00-07:00",
            "executive_summary": [
                "Brave\u306fAsk Brave\u306b\u8a73\u7d30\u56de\u7b54\u3092\u8fd4\u3059AI\u6a5f\u80fd\u3092\u5c0e\u5165\u3057\u3001\u6df1\u6398\u308a\u30cb\u30fc\u30ba\u306b\u5fdc\u3048\u3066\u3044\u308b\u3002",
                "\u30e6\u30fc\u30b6\u30fc\u306f\u901a\u5e38\u691c\u7d22\u304b\u3089\u5373\u5ea7\u306bAsk Brave\u3078\u5207\u308a\u66ff\u3048\u3001\u30ec\u30dd\u30fc\u30c8\u5f62\u5f0f\u3068\u5bfe\u8a71\u4f53\u9a13\u3092\u5f97\u3089\u308c\u308b\u3002",
                "\u81ea\u793eAPI\u3067\u691c\u7d22\u7d50\u679c\u3092\u30b0\u30e9\u30a6\u30f3\u30c7\u30a3\u30f3\u30b0\u3057\u3001\u6697\u53f7\u5316\u306824\u6642\u9593\u5f8c\u524a\u9664\u3067\u30d7\u30e9\u30a4\u30d0\u30b7\u30fc\u3092\u5b88\u308b\u3068\u5f37\u8abf\u3057\u305f\u3002"
            ],
            "key_findings": [
                {"text": "Ask Brave\u306f\u5f93\u6765\u306eAI Answers\u3068\u4e26\u5b58\u3057\u3001\u65e5\u6b21\u30671500\u4e07\u4ef6\u8d85\u306e\u56de\u7b54\u3092\u63d0\u4f9b\u3057\u3066\u3044\u308b\u3002[1]", "footnote": "[1]"},
                {"text": "\u30e6\u30fc\u30b6\u30fc\u306f\u691c\u7d22\u30d0\u30fc\u6a2a\u306e\u30dc\u30bf\u30f3\u3084\u300c??\u300d\u8ffd\u8a18\u3067Ask Brave\u3092\u547c\u3073\u51fa\u305b\u308b\u3002[1]", "footnote": "[1]"},
                {"text": "\u751f\u6210\u3055\u308c\u308b\u56de\u7b54\u306f\u30ea\u30f3\u30af\u3084\u52d5\u753b\u3001\u753b\u50cf\u30ab\u30eb\u30fc\u30bb\u30eb\u3092\u542b\u3080\u30ec\u30dd\u30fc\u30c8\u5f62\u5f0f\u3067\u63d0\u4f9b\u3055\u308c\u3001\u5f8c\u7d9a\u306e\u30d5\u30a9\u30ed\u30fc\u30a2\u30c3\u30d7\u3082\u53ef\u80fd\u3060\u3002[1]", "footnote": "[1]"},
                {"text": "Ask Brave\u306f\u30af\u30a8\u30ea\u306e\u7a2e\u985e\u3092\u81ea\u52d5\u3067\u5224\u65ad\u3057\u9069\u5207\u306a\u5fdc\u7b54\u5f62\u5f0f\u3092\u9078\u629e\u3059\u308b\u3002[1]", "footnote": "[1]"},
                {"text": "Brave\u306f\u30c1\u30e3\u30c3\u30c8\u6697\u53f7\u5316\u306824\u6642\u9593\u5f8c\u306e\u524a\u9664\u3067\u30d7\u30e9\u30a4\u30d0\u30b7\u30fc\u4fdd\u8b77\u3092\u8a34\u6c42\u3059\u308b\u3002[1]", "footnote": "[1]"}
            ],
            "references": [
                {
                    "id": "[1]",
                    "title": "Brave updates its AI-powered search with a detailed answers feature",
                    "author": "Ivan Mehta",
                    "url": "https://techcrunch.com/2025/09/29/brave-updates-its-ai-powered-search-with-a-detailed-answers-feature/",
                    "publisher": "TechCrunch",
                    "published": "2025-09-29T09:00:00-07:00",
                    "accessed": "2025-09-29"
                }
            ]
        }
    ]
}

os.makedirs("reports/2025-09-29", exist_ok=True)
with open(os.path.join("reports/2025-09-29", "report.json"), "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)
