# Upload this dataset to Hugging Face (manual)

## Create dataset

1. Open https://huggingface.co/new-dataset  
2. Owner: `anhmtk`  
3. Dataset name (gợi ý): **`agentshare-multi-chain-defi`** (khớp Space)  
4. License: MIT · Public  

## Upload files (drag & drop hoặc Add file)

Từ thư mục này:

- `README.md` (dataset card — **giữ nguyên** block YAML giữa `---` ở dòng đầu; đừng paste qua “Edit dataset card” rồi mất YAML)
- `meteora_brief.sample.json`
- `solana_dex_brief.sample.json`
- `dex_overview.sample.json`
- `service_meta.sample.json`

### Fix “YAML Metadata Warning”

Warning này **không làm hỏng dataset** — chỉ mất badge license/tags trên Hub. Nguyên nhân thường gặp: README trên HF **không còn** frontmatter YAML (upload qua UI đôi khi strip `---` block).

**Cách sửa:** Files and versions → `README.md` → Replace / Upload lại file `README.md` từ repo này (phải bắt đầu bằng `---\\nlicense: mit\\n...`). Refresh Dataset card → warning biến mất.

## After publish

Dataset URL sẽ dạng:

`https://huggingface.co/datasets/anhmtk/agentshare-multi-chain-defi`

Trong README Space (nếu muốn) thêm dòng link dataset đó.

**Không** đẩy lên repo `agentshare-openclaw`.
