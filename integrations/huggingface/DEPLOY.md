# Hugging Face presence (AgentShare)

Gradio Space source for **Solana DeFi** tools with MCP support.

## Deploy (anh làm trên HF UI — ~10 phút)

1. https://huggingface.co/new-space  
2. Owner: tài khoản HF của anh · Name gợi ý: `agentshare-solana-defi`  
3. SDK: **Gradio** · Visibility: **Public**  
4. Clone / upload 3 file trong thư mục này vào root Space:
   - `app.py`
   - `requirements.txt`
   - `README.md` (YAML frontmatter giữ nguyên)
5. **Settings → Secrets** → `AGENTSHARE_API_KEY` = key từ https://agentshare.dev/get-key  
6. Đợi build xong → kiểm tra tab Meteora / MCP badge  
7. Add Space vào https://huggingface.co/settings/mcp  

Hoặc push git:

```bash
git remote add hf https://huggingface.co/spaces/<USERNAME>/agentshare-solana-defi
git subtree push --prefix integrations/huggingface hf main
```

**Không** đụng repo `agentshare-openclaw` cho việc này.
